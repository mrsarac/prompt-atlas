# Automatic Prompt Engineer

Aday talimatlar üretin; hangisinin işe yaradığını hedef modelin gerçek çıktılarıyla seçin.

## Nedir?

Automatic Prompt Engineer, örnek girdi–çıktılardan talimat adayları üretir ve bunları hedef görevde değerlendirir. Adayı yazan model ile adayı uygulayan model aynı işi yapmaz. Skor, adayın kendisini övmesinden değil, alınan çıktının doğru cevapla karşılaştırılmasından gelir.

İnsan veri setini, ölçütü ve çağrı bütçesini belirler. Otomasyonda bu işleri yürüten bir program gerekir. Aşağıdaki küçük veri kümeleri mekanizmayı öğretir; sağlam performans tahmini için yeterli değildir.

## Ne zaman işe yarar?

Tekrarlı sınıflandırma ve veri dönüşümleri için uygundur. Doğru cevapları bilinen geliştirme örnekleri ve aday seçiminde kullanılmayacak ayrı kontrol örnekleri gerekir.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Destek etiketleme promptu seçilecek.

**Prompt**

```text
Koordinatör geliştirme çiftlerini verir: “Giremiyorum”→erisim; “Fatura yanlış”→fatura.
Üretici çağrısı: “Bu dönüşümü yapacak iki farklı tam talimat öner. Yalnız erisim/fatura çıktı alanı var.”
Her adayı hedef modelde iki girdiyle ayrı çalıştır. Dört gerçek çıktıyı doğru etiketle eşleştir; eşleşme sayısını skor yap.
En iyi adayı seç; eşitlikte daha kısa olanı al. En fazla bir üretici + dört hedef çağrısı. Çalıştırılmayan adaya skor verme.
```

**Örnek çıktı**

Temsili aday: “İletinin açık konusunu erisim veya fatura olarak yaz; başka metin ekleme.” Temsili sonuçlar doğruysa 2/2 olur; bu puan burada ölçülmedi.

**Ne elde ettik?**

Talimat seçiminin hangi gözleme dayanacağı belli. İki örnekten genel başarı sonucu çıkarılmaz.

### Orta (Medium)

**Durum**

Belirsiz iletiler yanlış etiketleniyor.

**Prompt**

```text
Geliştirme: “Giremiyorum”→erisim; “Fatura iki kez geldi”→fatura; “Yardım edin”→belirsiz.
Üreticiden iki aday iste; belirsiz sınıfı ve tek etiket çıktısı zorunlu.
Her adayı üç geliştirme girdisinde çalıştır; exact-match skorunu gerçek sonuçlardan hesapla. Seçimden sonra promptu dondur.
Ayrı kontrol: “Parolam kabul edilmiyor”→erisim; “Ne yapacağımı bilmiyorum”→belirsiz. Bu iki girdiyi aday üreticisine gösterme.
Bütçe 1+6+2 çağrı. Kontrol sonucu düşükse başarı ilan etme; test örneklerini prompta kopyalama.
```

**Örnek çıktı**

Temsili iyi aday: “Konu açık değilse belirsiz seç.” Kontrol çıktıları erisim/belirsiz olmalıdır; gerçek doğruluk ancak yürütmeden sonra hesaplanır.

**Ne elde ettik?**

Aday seçme ve seçimi sınama verisi ayrıldı. Belirsiz sınıfı yalnız sonradan eklenmiş etiket olmaktan çıktı.

### İleri (Hard)

**Durum**

Kısa çıktı ile kaynak dayanağı iki ayrı kabul koşulu.

**Prompt**

```text
Geliştirme girdileri: “Fatura yanlış”→fatura|Fatura; “Giremiyorum”→erisim|Giremiyorum; “Yardım”→belirsiz|Yardım.
Üretici üç talimat adayı önerir. Hedef model her adayla üç örneği işler. Yazılım önce etiket|alıntı biçimini, sonra etiket doğruluğunu ve alıntının girdide bulunmasını denetler.
Biçimi bozan aday elenir; kalanlar doğru kayıt sayısıyla sıralanır. Bağımsız kontrol girdisi: “Hesabıma giremiyorum”→erisim; dayanak girdideki kısa alıntı olmalı.
Bir üretici, dokuz geliştirme, bir kontrol çağrısı sınırı. Kontrolü geçmeyen prompt otomatik kullanıma alınmaz.
```

**Örnek çıktı**

Temsili `erisim|Hesabıma giremiyorum` kabul edilebilir. `erisim|şifre yanlış` kaynakta olmayan alıntı nedeniyle kalır.

**Ne elde ettik?**

Tek başarı sayısının gizleyebileceği biçim ve kanıt hataları ayrı denetleniyor. Kullanıma alma kararı hâlâ koordinatörde.

## Nerede durmalı?

Geliştirme verisine aşırı uyum ve test verisinin aday üretimine sızması kolaydır. Genel meta prompt yalnız talimat yazabilir; APE gerçek aday değerlendirmesi ekler. OPRO ise geçmiş aday ve skorları sonraki üretime açıkça taşır.

## Kaynaklar

- [Large Language Models are Human-Level Prompt Engineers](https://arxiv.org/html/2211.01910) — Zhou, Yongchao; Muresanu, Andrei Ioan; Han, Ziwen; Paster, Keiran; Pitis, Silviu; Chan, Harris; Ba, Jimmy. 2022-11-03; okunan sürüm 2023-03-10. Talimat adaylarının üretimi, hedef modelde değerlendirilmesi ve seçimini tanımlar; Instruction Induction/BIG-Bench bulguları her görev için üstünlük değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
