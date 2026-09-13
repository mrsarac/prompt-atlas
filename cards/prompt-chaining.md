# Prompt chaining

Bir işi, çıktısı kontrol edilen küçük çağrılara böl.

## Nedir?

Prompt chaining, önceden belirlenmiş görevleri sırayla ayrı model çağrılarına verir. Bir adımın çıktısı sonraki adıma girdi olur. Geçişteki kontrol, yanlış bir ara sonucun bütün zincire taşınmasını önler.

## Ne zaman işe yarar?

Ayıklama, taslak ve biçimleme gibi aşamaları açıkça ayrılan tekrarlı işlerde.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir atölye duyurusunu iki adımda hazırlıyorsunuz.

**Prompt**

```text
Başlatıcı: İnsan; iki ayrı sohbet çağrısı ve arada insan kontrolü.
Çağrı 1: Şu nottan yalnız kesin bilgileri ayıkla: "Çizim atölyesi, 12 Ekim, 14.00, 8 kişi. Yer sonra açıklanacak." Tarih, saat, kapasite, yer alanlarını yaz.
Kontrol: Dört alanın kaynakla eşleştiğini doğrula; yer bilinmiyorsa boş bilgi olarak koru.
Çağrı 2: Kontrol edilen alanları kullanarak iki cümlelik duyuru yaz. Yeni yer, ücret veya kayıt bağlantısı ekleme. Son metin dört alanı koruyorsa bitir.
```

**Örnek çıktı**

Ara çıktı: “12 Ekim; 14.00; 8 kişi; yer açıklanmadı.” Son çıktı: “Çizim atölyesi 12 Ekim saat 14.00’te, 8 kişilik kontenjanla düzenlenecek. Yer daha sonra açıklanacak.”

**Ne elde ettik?**

Yazı üslubu değişirken bilgi sabit kaldı.

### Orta (Medium)

**Durum**

Üç müşteri yorumunu anonim bir özete dönüştürüyorsunuz.

**Prompt**

```text
Uygulama 3 ayrı çağrı çalıştırsın; yalnız önceki onaylı çıktıyı taşısın.
Girdi: "Ada: Kurulum kolay." "Bora: Kurulum kolay ama yazı küçük." "Cem: Yazı küçük."
1. Adları kaldır; her yoruma y1, y2, y3 kimliği ver. İnsan kontrolü: isim kalırsa dur.
2. Anonim yorumlardan tema ve destekleyen yorum kimliklerini çıkar. Her kimlik mevcut olmalı; değilse bir düzeltme dene, sonra dur.
3. Tema listesinden iki maddelik ürün özeti yaz. Sıklık dışında neden veya tüm müşterilere genelleme ekleme.
```

**Örnek çıktı**

“Kurulum kolay: y1, y2. Yazı küçük: y2, y3.” Ardından: “Üç yorumun ikisi kurulum kolaylığını, ikisi küçük yazıyı belirtiyor.”

**Ne elde ettik?**

Her aşama farklı bir iş yaptı; kişisel veri son yazım çağrısına gitmedi.

### İleri (Hard)

**Durum**

Belge değişikliklerinden yayın taslağı çıkacak, fakat çelişki varsa zincir durmalı.

**Prompt**

```text
Denetleyici durum nesnesi: belgeler, ayiklanan_degisimler, celiskiler, taslak. En fazla 4 model çağrısı; yayınlama aracı yok.
Girdi A: "v2: Dışa aktarma CSV ve JSON." Girdi B: "v2: Yalnız CSV desteklenir."
1. Her iddiayı A/B kimliğiyle çıkar.
2. Aynı özellik için uyuşmazlık denetle. Kaynaklardan birini yetkili varsayma.
Geçiş kapısı: celiskiler boş değilse yazım çağrısını çalıştırma. İnsana sadece hangi bilginin seçilmesi gerektiğini göster.
İnsan kaynak B'nin geçerli olduğunu ayrıca bildirirse bu kararı durum kaydına ekle; 3. çağrıda yalnız onaylı bilgiden yayın taslağı yaz. Taslak üretiminde dur.
```

**Örnek çıktı**

“JSON desteği çelişkili: A var, B yok diyor. Yetkili kayıt belirlenmeden taslak aşamasına geçilmedi.”

**Ne elde ettik?**

Hızlı bir zincir yerine denetlenebilir bir geçiş elde edildi.

## Nerede durmalı?

Her paragraf için ayrı çağrı açmak gereksiz olabilir. Zincirin değeri iş ayrımında ve geçiş kontrolündedir. ReAct gözleme göre yol seçer; bu yöntemde yol baştan bellidir. Çağrıları ayrı tutmak tek başına bağımsız doğrulama sağlamaz.

## Kaynaklar

- [Building Effective AI Agents \ Anthropic](https://www.anthropic.com/engineering/building-effective-agents) — Anthropic. 2024-12-19. Önceden tanımlanmış alt görevlere ayırma ve ara kapılarla kontrol edilen prompt chaining örüntüsünü açıklar; sağlayıcı mühendislik rehberidir. Kanıt düzeyi: sayfa gövdesi.
