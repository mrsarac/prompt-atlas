# Teach-back

Anladığını kendi sözlerinle geri anlat; açıklamanın nerede eksik kaldığını kontrol et.

## Nedir?

Teach-back, anlatılan bilgiyi karşıdaki kişinin kendi sözleriyle geri anlatmasını istemektir. Amaç kişiyi sınavda yakalamak değil, anlatımın anlaşılır olup olmadığını görmektir. Buradaki LLM kullanımı insan iletişimi yönteminin öğretim uyarlamasıdır.

## Ne zaman işe yarar?

Bir kullanım kuralı veya adım dizisini okuduktan sonra gerçekten uygulayabilir durumda olup olmadığınızı görmek için.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir dosya kaydetme kuralını öğreniyorsunuz.

**Prompt**

```text
Kural: Çalışmayı önce taslak klasörüne kaydet. Kontrol edilince son klasörüne kopyala; taslağı silme.
Bana kuralı kısaca açıkla, sonra kendi sözlerimle geri anlatmamı iste. Cevabımı bekle; eksik bir adım varsa anlatımını düzeltip yeniden geri anlatmamı rica et. Bunu benim zekâmı ölçen bir sınav gibi sunma.
```

**Örnek çıktı**

İnsan: “Son klasörüne kaydedip taslağı silerim.” Model: “Ben yeterince açık anlatmamış olabilirim: önce taslağa kaydetmek ve onu korumak gerekiyor. Sırayı yeniden nasıl anlatırsın?”

**Ne elde ettik?**

Yanlış anlama, yargılama olmadan görünür oldu.

### Orta (Medium)

**Durum**

Bir iade kuralının istisnası var.

**Prompt**

```text
Kural metni: Kullanılmamış ürün 14 gün içinde iade edilebilir. Kişiye özel üretim kapsam dışıdır. Bu yalnız kurgusal mağaza kuralıdır.
Önce kısa açıklama yap. Ardından "Bir arkadaşına hangi ürünleri hangi süre içinde iade edebileceğini nasıl anlatırsın?" diye sor. Yanıtımı bekle. Süreyi veya istisnayı atladıysam yalnız o kısmı yeniden açıkla; en fazla iki geri anlatım turu.
```

**Örnek çıktı**

İnsan: “Her şeyi 14 günde iade ederiz.” Model: “Süreyi doğru aldın. Kural yalnız kullanılmamış ürünlere uygulanıyor; kişiye özel üretim hariç. Bunu kendi cümlenle yeniden anlatır mısın?”

**Ne elde ettik?**

Genel cümlede kaybolan kapsam ve istisna kontrol edildi.

### İleri (Hard)

**Durum**

Bir iş akışında farklı hata durumları farklı adım gerektiriyor.

**Prompt**

```text
Kurgusal süreç: Dosya yüklemede "biçim hatası" varsa PDF olarak yeniden dışa aktar; "bağlantı hatası" varsa bir kez tekrar dene. İkinci bağlantı hatasında destek kaydı aç. Aynı dosyayı art arda tekrar gönderme.
Önce süreci açıkla; sonra benden iki durumu kendi sözlerimle anlatmamı iste: biçim hatası ve ikinci bağlantı hatası. Ben cevap vermeden çözümü gösterme.
Yanıtları kurala göre kontrol et; eksik dalları kısaca yeniden anlat ve farklı bir sırayla tekrar geri anlatım iste. En fazla üç tur; gerçek yükleme veya destek mesajı gönderme.
```

**Örnek çıktı**

İnsan biçim hatasında tekrar denemeyi söylerse model PDF adımını yeniden açıklar. İkinci bağlantı hatasında durup destek kaydı hazırlama koşulu ayrıca kontrol edilir.

**Ne elde ettik?**

Yalnız ezberlenen sıra değil, koşula göre değişen eylem anlaşıldı.

## Nerede durmalı?

Kaynak AHRQ’nun insan sağlık iletişimi rehberidir; bu kart tıbbi öneri vermez ve LLM ile öğrenme artışı kanıtı sunmaz. Kendine açıklama “neden?” bağlantılarını açar; teach-back anlatılanı kişinin nasıl anladığını kontrol eder. Modelin kaynak kuralı yanlış yorumlama ihtimali ayrıca denetlenmelidir.

## Kaynaklar

- [Use the Teach-Back Method: Tool #5](https://www.ahrq.gov/health-literacy/improve/precautions/tool5.html) — Agency for Healthcare Research and Quality. yayın tarihi doğrulanmadı. Kişinin ne bilmesi/yapması gerektiğini kendi sözleriyle geri anlatmasıyla anlayışı kontrol etme yöntemini tanımlar; LLM etkisi deneyi değildir. Kanıt düzeyi: sayfa gövdesi.
