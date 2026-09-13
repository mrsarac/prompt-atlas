# RUNE

Dağınık bir isteği, sürümü belli katmanlı bir talimat yapısına dönüştür.

## Nedir?

RUNE, Mustafa Saraç / NeuraByte Labs imzalı açık kaynak bir prompt yapılandırma projesi. Kamuya açık README’de istekleri sekiz katmanda düzenleyen bir yaklaşım ve bunu kullanan araçlar anlatılıyor. Buradaki örnekler katman fikrini elle uygular; araç kurulumu veya sağlayıcı çağrısı yapıldığını varsaymaz.

## Ne zaman işe yarar?

Aynı işte amaç, bağlam, sınırlar ve çıktı biçimi sık sık birbirine karışıyorsa. Tek cümlelik net bir soru için sekiz bölüm açmak gerekmeyebilir.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

“Bu notu duyuru yap” isteğini açık bir talimata çevireceksiniz.

**Prompt**

```text
Aşağıdaki görevi RUNE README/RUNE.md L0–L7 adlarıyla düzenle; görevi henüz yerine getirme. Eksik gerçekleri ekleme. Bu, elle şablonlama örneğidir.
Ham istek: Suluboya atölyesi 12 Ekim 14.00, 8 kişi; iki cümlelik duyuru yap.
L0 System Core: görev rolü. L1 Context: verilen bilgiler. L2 Intent: hedef.
L3 Governance: sınırlar. L4 Cognitive Engine: kısa çalışma yöntemi, gizli düşünce dökümü değil.
L5 Capabilities: kullanılabilen araçlar. L6 Quality Assurance: kontrol.
L7 Output & Meta: çıktı biçimi.
İnsan sekiz alanı ham istekle karşılaştırsın. Onaylı talimatı ikinci çağrıya verip duyuruyu üretsin; bir yapılandırma ve bir uygulama çağrısında dur.
```

**Örnek çıktı**

“L0: Duyuru editörü. L1: Suluboya, 12 Ekim 14.00, 8 kişi. L2: Katılımı anlat. L3: Yer/ücret uydurma. L4: Bilgiyi ayıkla, iki cümlede yaz. L5: Araç yok. L6: Tarih/saat/kapasiteyi kontrol et. L7: İki cümle.”

**Ne elde ettik?**

Yeni bilgi üretmeden tekrar kullanılabilir bir görev çerçevesi oluştu.

### Orta (Medium)

**Durum**

Bir inceleme promptunu çalışma alanına göre uyarlayacaksınız.

**Prompt**

```text
Başlatıcı insan; L0–L7 yapısını kullan. Görev: Verilen kargo kuralını incelemek.
Bağlam: Kod total > 500 ? 0 : 50; kural 500 ve üzeri ücretsiz. İzin: yalnız öneri, dosyaya yazma yok. Araç: yok.
Katmanlı talimatta bu bilgileri uygun yerlere yerleştir. Kontrol alanı 499/500/501 girdileri için 50/0/0 beklenen değerlerini içersin. Çıktı: sorun, en küçük yama önerisi, nasıl kontrol edileceği.
İnsan izin alanını doğrulasın; ikinci çağrıya çerçeveyi ve kodu birlikte versin. İnceleme çıktısından sonra dur. Test çalıştırılmadıysa çalıştırılmış gibi yazma.
```

**Örnek çıktı**

İnceleme: “500 sınırı dışarıda kalıyor; `>=` önerilir. Beklenen sınır değerleri 50/0/0. Bu yanıtta gerçek test çalıştırılmadı.”

**Ne elde ettik?**

Katmanlar, rol kadar yetki ve kontrol beklentisini de taşıdı.

### İleri (Hard)

**Durum**

Birden fazla şablonu olan ekip sürüm karışıklığını önlemek istiyor.

**Prompt**

```text
İnsan denetimli yerel tasarım: Araç çalıştırmadan şablon seçimini belgele.
Seçenek A: RUNE README/RUNE.md L0–L7: System Core, Context, Intent, Governance, Cognitive Engine, Capabilities, Quality Assurance, Output & Meta.
Seçenek B: prompts/README.md MP v4.3 L1–L8: Identity, Mission, Constraints, Methodology, Output, Error Taxonomy, Personalization, Context.
Görev: Haftalık üç nottan kaynaklı özet. Notlar N1="Kurulum tamam", N2="Test bekliyor", N3="Yayın izni yok".
A'yı seç; şablon adı/sürüm ailesini kayda yaz. B'nin numaralarını A'ya yapıştırma. Üretim çağrısı yalnız onaylı çerçeve ve N1-N3'ü alsın. Ayrı kontrol çağrısı her iddiayı not kimliğiyle eşlesin. En fazla 3 çağrı; yayın aracı yok. Kanıtsız tamamlanma ifadesi varsa insan düzeltmesine bırak.
```

**Örnek çıktı**

“Kurulum tamam [N1]. Test bekliyor [N2]. Yayın izni yok [N3].” Şablon kaydı: “README/RUNE.md L0–L7 ailesi; MP v4.3 L1–L8 ile karıştırılmadı.”

**Ne elde ettik?**

Benzer sekizli yapıların aynı sürüm veya aynı bölüm eşlemesi olduğu varsayılmadı.

## Nerede durmalı?

RUNE bir evrensel başarı garantisi veya tek başına model eğitimi değildir. Projenin kendi değerlendirme puanı bağımsız doğruluk kanıtı sayılmaz. Master prompt süreklilik sağlayan ana çalışma talimatıdır; meta prompting görev veya prompt yapısı üzerinde çalışır; RUNE bunun belirli katmanları ve araçları olan bir uygulamasıdır. Kamuya açık belgelerdeki sürüm ve katman adları birbirinden farklı olabilir.

## Kaynaklar

- [RUNE: proje tanımı ve sekiz katman](https://github.com/neurabytelabs/rune/blob/main/README.md) — Mustafa Saraç / NeuraByte Labs. yayın tarihi doğrulanmadı. Projenin sekiz katmanlı istek dönüştürme yaklaşımını ve araç kapsamını tanımlar; burada etkinlik ya da model üstünlüğü iddiası kurulmaz. Kanıt düzeyi: kamuya açık projenin yerel özgün belgesi; yeni uzak sürüm teyidi yok.
- [RUNE.md: L0–L7 talimat yapısı](https://github.com/neurabytelabs/rune/blob/main/RUNE.md) — Mustafa Saraç / NeuraByte Labs. yayın tarihi doğrulanmadı. L0–L7 katmanlarının adları ve görevlerini verir; README’nin sürüm etiketiyle bu dosyanın sürüm etiketi eşit varsayılmaz. Kanıt düzeyi: kamuya açık projenin yerel özgün belgesi; yeni uzak sürüm teyidi yok.
- [MP v4.3 Prompt Library: L1–L8 şablonları](https://github.com/neurabytelabs/rune/blob/main/prompts/README.md) — Mustafa Saraç / NeuraByte Labs. yayın tarihi doğrulanmadı. MP v4.3 kütüphanesindeki ayrı L1–L8 şemasını tanımlar; L0–L7 ile birebir numara eşlemesi yapılmaz. Kanıt düzeyi: kamuya açık projenin yerel özgün belgesi; yeni uzak sürüm teyidi yok.
