# Sınırlı yürütme ve yetki

Yetkiyi, bütçeyi ve durma koşulunu işin başında görünür yap.

## Nedir?

Sınırlı ajan çalışması, modelin hangi adımı seçebileceği kadar hangi adımı seçemeyeceğini de belirler. Prompt sınırları anlatır; uygulama izin listesi, işlem bütçesi ve onay kapısıyla bunları uygular.

## Ne zaman işe yarar?

Dosya, dış hizmet veya araç kullanan işlerde; özellikle okuma, yerel değişiklik ve dışarıya yayın birbirinden ayrılmalıysa.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir asistanın üç metin dosyasını özetlemesini istiyorsunuz.

**Prompt**

```text
Görev: a.txt="Kurulum 5 dakika", b.txt="İptal ücretsiz", c.txt="Destek hafta içi" içeriklerini özetle.
Denetleyici yalnız bu üç dosyaya salt okunur erişim versin. Araç bütçesi 3; ağ ve yazma araçları kapalı.
Her çağrının dosya adını ve dönen metnini durum kaydına ekle. Model en fazla üç maddelik özet üretsin.
Eksik dosya varsa adını söyle, arama alanını genişletme. Üç dosya okunduğunda veya bütçe bittiğinde dur.
```

**Örnek çıktı**

“Kurulum 5 dakika. İptal ücretsiz. Destek hafta içi.” Eksik bir dosya için ayrıca “b.txt okunamadı” denir.

**Ne elde ettik?**

Küçük görev için erişim alanı da küçük kaldı.

### Orta (Medium)

**Durum**

Kodda yalnız kargo eşiği değiştirilecek.

**Prompt**

```text
Başlatıcı: Geliştirici. İzinli dosya shipping.js; kural: 500 TL ve üzeri ücretsiz, altı 50 TL. Mevcut kod total > 500 ? 0 : 50.
Denetleyici: Sadece bu dosyaya yerel yama; başka dosya, bağımlılık, commit ve dış hizmet araçları kapalı. En fazla 1 yama ve 1 ilgili test komutu.
Model yama önerisini versin; uygulama dosya yolunu ve diff kapsamını denetlesin. Kontrol girdileri 499,500,501; beklenen 50,0,0.
Test sonucu durum kaydına aktarılır. Başarısızsa sonucu raporla; yeni kapsam açma. Başarıda diff ve kontrol sonucuyla dur.
```

**Örnek çıktı**

Öneri: `>` yerine `>=`. “İlgili üç sınır kontrolü beklenen değerleri verirse yerel değişiklik tamamdır.” Bu cümle gerçek test çalıştırıldığı iddiası değildir.

**Ne elde ettik?**

Bitiş, modelin “biraz daha iyileştireyim” kararına bırakılmadı.

### İleri (Hard)

**Durum**

Ajan bir duyuru taslağı oluşturabilir ama yayımlayamaz.

**Prompt**

```text
Görev: "Atölye 12 Ekim, 14.00; yer henüz belli değil" notundan duyuru taslağı hazırlamak.
Uygulama yetkileri: read_note ve save_local_draft. publish ve send_message yok. En fazla 4 araç çağrısı, 2 düzeltme.
Durum: kullanıcı kapsamı, kaynak not, taslak yolu, doğrulanmış alanlar, açık eksikler, kalan çağrılar.
Ajan bilgi boşluğunu uydurmasın. Yer bilgisini eksik olarak işaretleyip taslağı yerel kaydetsin. Kullanıcı "devam" derse bunu yayın izni sayma; zaten izinli eksik işleri tamamla.
Dur: taslak ve eksik bilgi listesi hazır olduğunda. Yayın için ayrı, somut içerik ve hedefe yönelik yetki gerekir.
```

**Örnek çıktı**

“Yerel taslak hazır. Yer bilgisi henüz yok; metin bunu açıkça belirtiyor. Dışarıya gönderim yapılmadı.”

**Ne elde ettik?**

İşi sürdürmek ile yetki alanını büyütmek ayrı kararlar olarak kaldı.

## Nerede durmalı?

Onay sorularını her küçük adıma yaymak da iş akışını bozabilir. Zaten verilmiş yetki içinde devam edilir; yeni yan etki için ayrı sınır gerekir. Prompt tek başına güvenlik duvarı değildir.

## Kaynaklar

- [Building Effective AI Agents \ Anthropic](https://www.anthropic.com/engineering/building-effective-agents) — Anthropic. 2024-12-19. Ajanlarda durma koşulları, geri bildirim ve insan kontrol noktalarının önemini açıklar. Kanıt düzeyi: sayfa gövdesi.
- [Safety in building agents | OpenAI API](https://developers.openai.com/api/docs/guides/agent-builder-safety) — OpenAI. yayın tarihi doğrulanmadı. Güvenilmeyen girdiyi ayırma ve araç onayları gibi uygulama katmanı önlemlerini anlatır; ürün rehberindeki öneriler evrensel garanti değildir. Kanıt düzeyi: sayfa gövdesi.
