# OPRO

Önceki adayları gerçek skorlarıyla birlikte göstererek yeni adaylar üretin.

## Nedir?

OPRO’da model, önceki çözüm veya prompt adaylarını ve ölçülen değerlerini görür. Yeni aday önerir; dış değerlendirici bu adayı çalıştırıp puanlar. Aday ve skor geçmişe eklenir, sonraki tur bu geçmişi kullanır.

Optimizasyon hedefi ve ölçüm yordamı dışarıda tanımlıdır. “Bu prompta 95 puan verdim” biçimindeki model beyanı ölçüm değildir. Burada OPRO’nun prompt optimizasyonu kullanımını küçük bir etiketleme görevinde gösteriyoruz.

## Ne zaman işe yarar?

Ölçütü belli, tekrarlanabilir işlerde kullanın. Gerçek çağrı kayıtlarını tutan bir koordinatör ve aday aramasından ayrılmış kontrol verisi gerekir.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

İki kayıt üzerinde etiketleme talimatı geliştirilecek.

**Prompt**

```text
Geliştirme: “Giremiyorum”→erisim; “Fatura yanlış”→fatura. Başlangıç promptu: “Konuyu yaz.”
Koordinatör başlangıç promptunu iki hedef çağrısında çalıştırır, exact-match skorunu hesaplar.
Optimizatör çağrısına şu paketi verir: görev “Destek iletisini konuya göre etiketle”; izinli etiketler erisim (giriş sorunu), fatura (fatura sorunu); yukarıdaki iki geliştirme girdi/etiket çifti; başlangıç promptunun tam metni ve az önce ölçülmüş skoru. İstek: “Bu görev ve örnekler için geçmişteki aday/skor çiftini kullanarak tek yeni tam talimat öner; skor uydurma.”
Yeni adayı aynı iki girdide yürütür; ölçülen skoru geçmişe ekler. Bir iyileştirme turu; toplam beş çağrı. Henüz gözlenmeyen skoru boş bırak.
```

**Örnek çıktı**

Temsili geçmiş: “Konuyu yaz” → 1/2; “Yalnız erisim veya fatura etiketi yaz” → 2/2. Bu sayılar akışı göstermek için uydurulmuş öğretim verisidir.

**Ne elde ettik?**

Skorun hangi aşamada oluştuğu belli. Modelin aday önerirken skoru kendi üretmesi engelleniyor.

### Orta (Medium)

**Durum**

İlk iyileştirme biçimi düzeltmiş, belirsiz sınıfı hâlâ kaçırıyor.

**Prompt**

```text
Veri: “Giremiyorum”→erisim; “Fatura yanlış”→fatura; “Yardım”→belirsiz.
Görev: destek iletisini etiketle; giriş sorunu erisim, fatura sorunu fatura, açık konu yoksa belirsiz. Başlangıç adayı “Yalnız erisim veya fatura etiketi yaz.” Koordinatör bunu üç geliştirme kaydında ölçer.
Her optimizatör çağrısına görev, üç izinli etiketin anlamı, bu üç geliştirme çifti ve tüm önceki tam aday/ölçülmüş skor çiftleri birlikte gider. Tek yeni aday üretir; hedef model üç kaydı işler, yazılım exact-match skorunu hesaplayıp geçmişe ekler. Kontrol girdisi ve etiketi bu pakete girmez.
En fazla iki iyileştirme turu; iyileşme yoksa erken dur. En iyi prompt dondurulur. Bütçe: başlangıç için 3 hedef çağrısı + iki tur için 2 optimizatör ve 6 hedef çağrısı + 1 ayrı kontrol; toplam en fazla 12.
Ayrı kontrol: “Hesabım açılmıyor”→erisim. Bu örneği arama geçmişine sokma; dondurulmuş adayla bir kez kontrol et.
```

**Örnek çıktı**

Temsili yeni aday: “İletide açık konu yoksa belirsiz; aksi halde erisim veya fatura.” Kontrol için beklenen etiket erisimdir.

**Ne elde ettik?**

Geçmiş, yeni adayın hangi sorunu hedeflediğini gösterir. Tek kontrol örneği güvenilir başarı oranı vermez.

### İleri (Hard)

**Durum**

Optimizatörün talimatı hedefi değiştirebilir.

**Prompt**

```text
Görev: destek konusunu erisim/fatura/belirsiz diye sınıflandır. Geliştirme: “Giremiyorum”→erisim; “Fatura yok”→fatura; “Selam”→belirsiz.
Sözleşme: giriş sorunu erisim, fatura sorunu fatura, açık konu yoksa belirsiz; etiket dışında işlem yok. Koordinatör başlangıç adayı “Her girdiye fatura yaz”ı üç geliştirme örneğinde ölçüp aday/skor geçmişine kaydeder.
İki iyileştirme turunun her optimizatör çağrısına görev/sözleşme, üç geliştirme çifti ve o ana kadarki tam aday/ölçülmüş skor geçmişi gider. Son testin girdisi ve etiketi yalnız değerlendirme tarafında kalır.
Her yeni aday çalıştırılmadan önce sınıf kümesi ve kaynak dışı işlem yasağı kontrol edilir. “Etiketleri değiştirelim” önerisini reddet ve turu durdur; geçerli adayı üç geliştirme kaydında ölçüp geçmişe ekle. En iyi geçerli adayı geliştirme skoruna göre dondur.
Test: “Parolam reddediliyor”→erisim, aramadan ayrı. Bütçe: 3 başlangıç + 2 optimizatör + 6 geliştirme + 1 test çağrısı; toplam en fazla 12. Testte hata varsa yeni başarı etiketi üretme veya aynı teste göre aramayı yeniden açma.
```

**Örnek çıktı**

Temsili sabit-fatura adayı 1/3 eşleşir. Etiket kümesini değiştiren aday çalıştırma öncesi reddedilir.

**Ne elde ettik?**

Daha yüksek görünen skor uğruna görevin tanımı değişmedi. Son seçim gerçek ölçümlere ve sabit hedefe bağlı kaldı.

## Nerede durmalı?

Ölçüt dar ise model o ölçüte uygun ama işin asıl amacına uymayan promptlar bulabilir. OPRO’nun sayısal optimizasyon ve prompt optimizasyon deneyleri aynı kullanım değildir. Veri ayrımı ve çağrı maliyeti ayrıca denetlenmelidir.

## Kaynaklar

- [Large Language Models as Optimizers](https://arxiv.org/html/2309.03409) — Yang, Chengrun; Wang, Xuezhi; Lu, Yifeng; Liu, Hanxiao; Le, Quoc V.; Zhou, Denny; Chen, Xinyun. 2023-09-07; okunan sürüm 2024-04-15. Önceki aday/değer çiftlerini yeni çözüm üretimine taşıyan optimizasyon döngüsünü tanımlar; skorun dış değerlendirmeden gelmesi gerekir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
