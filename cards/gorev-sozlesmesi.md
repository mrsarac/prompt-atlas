# Görev ve çıktı sözleşmesi

İsteği, neyin teslim edileceği ve nasıl kontrol edileceği belli bir işe çevirin.

## Nedir?

“Duyuruyu iyileştir” dediğinizde model hem sorunu hem çözümü seçebilir. Görev sözleşmesinde amacı, kullanılacak bilgiyi, çıktı biçimini ve bitiş ölçütünü siz yazarsınız. Modelin eksik bilgi karşısında ne yapacağı da bu sözleşmenin parçasıdır.

Çözülmüş örnek vermeden talimat yazmak zero-shot kullanımdır. RTF, CRISPE, RISEN, CARE, CRAFT ve RACE gibi kısaltmaların açılımları farklı kaynaklarda değişebilir; burada onları bağımsız algoritmalar saymadan ortak brief alanlarını açık yazıyoruz.

## Ne zaman işe yarar?

Duyuru, karşılaştırma veya küçük kod işi için başlayabilirsiniz. Önce doğru kabul edeceğiniz çıktıyı ve modelin kullanabileceği girdileri belirleyin.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir atölyede form başvuruyu topluyor; yer ancak e-postayla kesinleşiyor. Duyuruyu iki cümlede yazacaksınız.

**Prompt**

```text
Başvuru duyurusu yaz. Bilgi: Çizim atölyesi 20 kişilik. Form başvuru içindir; yer onay e-postası gelince kesinleşir. İki cümle kullan. Tarih ve ücret verilmedi; ekleme. Formu göndermenin kesin kayıt olmadığını anlaşılır söyle.
```

**Örnek çıktı**

Çizim atölyesine formu doldurarak başvurabilirsiniz. 20 kişilik atölyede yeriniz, onay e-postası geldiğinde kesinleşir.

**Ne elde ettik?**

Kontrol edilebilir iki cümle var: kapasite korunmuş, başvuru ve onay ayrılmış. Duyurunun gerçek koşullarla uyumunu siz denetlersiniz.

### Orta (Medium)

**Durum**

İki salonu karşılaştırıyorsunuz; birinin erişilebilirlik bilgisi eksik.

**Prompt**

```text
A: 800 TL, 25 kişilik, asansör var. B: 600 TL, 20 kişilik, erişim bilgisi yok. 18 kişilik atölye için yalnız maliyet, kapasite ve basamaksız erişimi karşılaştır. Her satırda A, B ve bilinmeyeni yaz. Asansör bilgisini tek başına basamaksız giriş kanıtı sayma. Kesin salon seçmeden sorulacak tek bilgiyi belirt.
```

**Örnek çıktı**

Maliyet: A 800 TL; B 600 TL. Kapasite: ikisi de 18 kişiyi alır. Basamaksız erişim: A’da asansör var, giriş doğrulanmadı; B’de bilgi yok. Soru: Her iki salona sokaktan basamaksız ulaşılabiliyor mu?

**Ne elde ettik?**

Eksik veri, olumlu özellik diye doldurulmadı. Erişimi salon sahipleri doğrulamadan seçim tamamlanmaz.

### İleri (Hard)

**Durum**

Bir geliştiriciye kargo hesabı değişikliği vereceksiniz. Kapsam ve kabul koşulu birlikte gerekiyor.

**Prompt**

```text
Yalnız shipping.js içindeki kargo koşulu için değişiklik öner. Mevcut ifade: total > 500 ? 0 : 50. Kural: sayısal ve indirimsiz total 500 veya üstüyse ücretsiz; altındaysa 50 TL. Çıktı: yeni ifade, beklenen üç sınır sonucu ve değişmemesi gereken davranış. Başka dosya, para birimi veya indirim sistemi ekleme. Kod çalıştırma erişimin yoksa sonuçları beklenti diye etiketle.
```

**Örnek çıktı**

Yeni ifade: `total >= 500 ? 0 : 50`. Beklenti: 499 → 50; 500 → 0; 501 → 0. Alt eşikteki 50 TL ücreti değişmez. Bu yanıt test çalıştırıldığını göstermez.

**Ne elde ettik?**

Hem dar değişiklik hem kabul örnekleri belli. Geliştirici ifadeyi gerçek dosyada ve testlerde kontrol eder; prompt dosya erişimini teknik olarak sınırlandırmaz.

## Nerede durmalı?

Çıktı sözleşmesi kaynak getirmez, hesap yürütmez ve JSON şemasını API düzeyinde zorlamaz. “ELI5” gibi sade anlatım isteği de okur seviyesini belirler; sizin kavramı öğrendiğinizi ölçmez. Öğrenme kontrolü için Teach-back kartındaki geri anlatma sırası gerekir.

## Kaynaklar

- [Prompt engineering | OpenAI API](https://developers.openai.com/api/docs/guides/prompt-engineering?api-mode=responses) — OpenAI. yayın tarihi doğrulanmadı. Görev, bağlam, örnek ve çıktı talimatlarını düzenleme rehberidir; sağlayıcı kapsamındaki tavsiyeler evrensel başarı garantisi değildir. Kanıt düzeyi: sayfa gövdesi.
- [Prompt design strategies  |  Gemini API  |  Google AI for Developers](https://ai.google.dev/gemini-api/docs/prompting-strategies) — Google. yayın tarihi doğrulanmadı. Açık talimat ve çıktı biçimi önerilerini destekler; bu Türkçe örneklerin başarı testi değildir. Kanıt düzeyi: sayfa gövdesi.
