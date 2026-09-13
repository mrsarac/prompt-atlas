# Directional Stimulus Prompting

Küçük bir politika modeli, büyük modele göreve özgü ipucu üretsin.

## Nedir?

Directional Stimulus Prompting, donmuş bir büyük dil modelini yönlendirmek için küçük bir politika modelinin ürettiği ipuçlarını kullanır. Özgün yöntem, bu küçük modeli gözetimli öğrenme ve ödüle dayalı iyileştirmeyle eğitir. Elle anahtar sözcük eklemek aynı sistemin tamamı değildir.

## Ne zaman işe yarar?

Tekrarlanan görevler, eğitim örnekleri, uygun değerlendirme ve model/API altyapısı varsa. Tek seferlik sohbet için eğitim düzeni kurmak ağırdır.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir cümlelik duyuru özetlerinde önemli alanların atlanmasını azaltmak istiyorsunuz.

**Prompt**

```text
Bu, gerçek eğitim gerektiren düzenin yalnız bir gözetimli güncelleme ve bir ödüllü güncelleme kesitidir; tam eğitim reçetesi değildir. Sohbet komutu eğitim başlatmaz.
Başlatıcı: Uygulama geliştiricisi. Eğitim örneği x="Suluboya 12 Ekim, 8 kişi", hedef özet y="Suluboya atölyesi 12 Ekim'de, 8 kişilik." Ayrı eğitim ve değerlendirme kümeleri gerekir; tek örnek yeterli değildir.
1. Küçük politikaya yalnız bu eğitim çiftiyle bir gözetimli güncelleme uygula: x -> "12 Ekim; 8 kişi". Ardından bu x için bir ipucu örnekle.
2. Bu tek örneklemenin temsili ipucu: "12 Ekim; 8 kişi". Donmuş büyük modele x+ipucunu ver: Bu bilgileri koruyarak tek cümle yaz, yeni olgu ekleme.
3. Gerçek çıktıyı puanla: doğru tarih +1, doğru kapasite +1, kaynak dışı iddia varsa −1. Bu tek yanıtın ödülüyle küçük politikaya en fazla bir güncelleme uygula; büyük modeli eğitme.
Sınır: 1 gözetimli adım, 1 ipucu örneklemesi, 1 büyük-model çağrısı, 1 ödül hesabı ve 1 ödüllü güncelleme; sonra dur. Bu kesitte değerlendirme çağrısı yok; ayrılmış veride ölçmeden iyileşti deme.
```

**Örnek çıktı**

Temsili ipucu: “12 Ekim; 8 kişi”. Temsili son çıktı: “Suluboya atölyesi 12 Ekim’de, 8 kişilik kontenjanla yapılacak.” Eğitim veya puan çalıştırılmış değildir.

**Ne elde ettik?**

İpucunun nereden geldiği ve neyin eğitildiği açık kaldı.

### Orta (Medium)

**Durum**

İpuçları, özette yanlış ayrıntıya ağırlık verebilir.

**Prompt**

```text
Gözetimli eğitimi daha önce tamamlanmış küçük politika ve donmuş büyük model önkoşuldur. Burada yalnız iki ipucundan tek ödüllü güncellemeye giden kesit gösterilir; yeni gözetimli eğitim yok. Girdi: "Atölye 14.00'te başlar; sekiz kişi; duvarlar mavi." Hedef: saat ve kapasiteyi koruyan özet.
Denetleyici x, üretilen ipucu z, gerçek büyük model yanıtı, alan doğruluğu ve ödülü saklasın. Ölçüt: doğru saat +1, doğru kapasite +1, kaynak dışı iddia varsa −1; yalnız anahtar sözcük sayma.
İki ipucu adayı örneği: z1="mavi duvar"; z2="14.00; sekiz kişi". Ayrı büyük model çağrılarıyla gerçek çıktıları al, aynı ölçütle değerlendir; küçük politikayı yalnız eğitim bölümünde güncelle.
Bütçe: bu tek eğitim girdisinden 2 politika örneklemesi, 2 büyük-model çağrısı, 2 ödül hesabı; ikisini içeren tek küçük-politika güncellemesi, sonra dur. Ayrı değerlendirme verisini bu güncellemeye katma; bu kesitte değerlendirme çağrısı veya başarı ölçümü yok.
```

**Örnek çıktı**

Temsili z1 yanıtı: “Atölyenin duvarları mavi.” Saat/kapasite yok, yeni iddia yok: bu metin için ölçüt 0 verir. Temsili z2 yanıtı: “Atölye 14.00’te başlar, sekiz kişiliktir.” İki alan da korunur: 2. Bu metinler modelden alınmış sonuçlar değildir; gerçek çalıştırmada yanıt ve ödül kayıtları yeniden oluşur.

**Ne elde ettik?**

Ödülün yanlış bir kısayolu teşvik etmesi önceden düşünülmüş oldu.

### İleri (Hard)

**Durum**

Eğitim alanı dışındaki duyurulara geçiliyor.

**Prompt**

```text
Eğitimde yalnız yüz yüze etkinlikler var. Yeni girdi: "Çevrim içi oturum, 16.00, bağlantı sonra gönderilecek; kapasite açıklanmadı."
Denetleyici eğitilmiş politikadan ipucu alsın, donmuş büyük modele kaynak+ipucu versin. Kaynakta kapasite yoksa politika alıştığı "8 kişi" bilgisini ekleyemez; çıktı doğrulayıcı bunu reddetsin.
Uyarlama gerekiyorsa yeni etiketli eğitim verisi ve ayrı test bölümü hazırlansın; test örneği üzerinde politika güncelleme yapılmasın. En fazla bir çıkarım ve bir doğrulama; hata varsa insan incelemesine bırak.
Gerçek eğitim altyapısı yoksa bunu elle ipucu denemesi olarak adlandır, tam DSP uygulaması deme.
```

**Örnek çıktı**

“Çevrim içi oturum 16.00’da; bağlantı daha sonra gönderilecek. Kapasite belirtilmemiş.”

**Ne elde ettik?**

Politikanın öğrenilmiş alışkanlığı, yeni girdide bulunmayan olguya dönüşmedi.

## Nerede durmalı?

Bu yöntem yalnız prompt cümlesi değildir: küçük model eğitimi, büyük modele çağrılar, ödül tasarımı ve bütçe ister. İpuçları anahtar sözcük veya başka kısa yönlendirmeler olabilir. Eğitimli düzen olmadan yapılan benzerlik, açıkça sade bir uyarlama olarak adlandırılmalıdır.

## Kaynaklar

- [Guiding Large Language Models via Directional Stimulus Prompting](https://arxiv.org/html/2302.11520) — Li, Zekun; Peng, Baolin; He, Pengcheng; Galley, Michel; Gao, Jianfeng; Yan, Xifeng. 2023-02-22; okunan sürüm 2023-10-09. Küçük politika modelinin gözetimli öğrenme ve reinforcement learning ile, donmuş black-box LLM için yönlendirici uyarıcı üretmesini tanımlar. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
