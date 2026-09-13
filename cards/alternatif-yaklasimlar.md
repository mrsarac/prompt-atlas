# Alternatif yaklaşımlar

İlk çözümün yanına başka yollar koy; aynı ölçütlerle karşılaştır.

## Nedir?

Alternative Approaches, bir işi yapmanın farklı yollarını üretip artılarını ve eksilerini karşılaştıran bir örüntüdür. Seçeneklerin farklı isimler değil, farklı eylem yolları olması gerekir. Tercih, kullanıcının hedef ve kısıtlarına bağlıdır.

## Ne zaman işe yarar?

İlk akla gelen araca veya çözüme erken bağlanmak istemediğinizde.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Atölye saatini okurlara duyuracaksınız.

**Prompt**

```text
Görev: Site ziyaretçisi atölye saatini kolay bulsun. Bilgi: 12 Ekim 14.00. Site küçük; bakım süresi haftada 1 saat.
Üç farklı yol öner: mevcut sayfada belirgin alan, ayrı etkinlik sayfası, soru-cevap aracı. Her biri için kurulum yükü, bakım yükü ve okurun adım sayısını nitel olarak karşılaştır. Ölçülmemiş süre/sayı uydurma. Mevcut kısıta göre koşullu öneri ver.
```

**Örnek çıktı**

“Mevcut sayfada belirgin saat alanı en az yeni bakım gerektiren aday. Ayrı sayfa paylaşım için yararlı olabilir. Soru-cevap aracı bu tek bilgi için ek bakım getirir.”

**Ne elde ettik?**

Bir özellik isteği farklı eylem yollarıyla karşılaştırıldı.

### Orta (Medium)

**Durum**

Veriyi paylaşmadan bir metin özeti hazırlanmalı.

**Prompt**

```text
Hedef: Müşteri notlarının iç özetini hazırlamak. Sert kısıt: Veri dış hizmete aktarılamaz. Seçenekleri önce bu kısıta göre süz, sonra emek ve kontrol imkânıyla karşılaştır.
En az üç farklı yol düşün: insanın yerel özeti, kurumca onaylı yerel araç, dış API. Yerel aracın gerçekten kurulu veya onaylı olduğunu varsayma.
Uygun olmayanı neden elendiğiyle yaz; kalanlar için eksik bilgi belirt. Araç kurma, veri aktarma veya hizmet açma.
```

**Örnek çıktı**

“Dış API mevcut veri kısıtını karşılamıyor. İnsan özeti uygulanabilir; yerel araç için varlık ve kurum onayı teyidi gerekiyor.”

**Ne elde ettik?**

Alternatif üretmek, izin dışı seçeneği uygulamak anlamına gelmedi.

### İleri (Hard)

**Durum**

Bir seçenek hızda, diğeri doğruluk kontrolünde güçlü.

**Prompt**

```text
İş: 100 ürün açıklamasını güncellemek. Veriler: Kaynak alanlar düzenli CSV'de; bazı ürünlerde ölçü eksik. Öncelik sırası kullanıcı tarafından henüz seçilmedi.
Seçenekler üret ve karşılaştır: tamamen elle; şablonla otomatik taslak + insan kontrolü; model taslağı + alan doğrulayıcı + insan kontrolü.
Her yol için eksik ölçü, kaynak dışı iddia ve tekrar eden iş yükünün nasıl ele alınacağını açıkla. Ölçülmemiş başarı puanı verme. Sonunda hız/doğruluk/bakım arasında seçimi değiştirecek tek soru sor; toplu güncellemeye başlama.
```

**Örnek çıktı**

“Düzenli alanlarda şablon güçlü aday; model anlatım çeşitliliği ekleyebilir ama alan doğrulaması gerekir. Eksik ölçü her yolda açık kalmalı.”

**Ne elde ettik?**

Karşılaştırma yalnız araç isimleriyle değil, hata ve bakım davranışıyla yapıldı.

## Nerede durmalı?

Alternatif sayısını büyütmek tek başına iyi karar getirmez. Aynı yaklaşımın üç yeniden yazımı çeşitlilik değildir. Cognitive Verifier ek bilgi toplar; bu örüntü mevcut hedefe giden farklı yolları karşılaştırır. Kaynak, desen tanımıdır; üstünlük ölçümü değildir.

## Kaynaklar

- [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT](https://arxiv.org/html/2302.11382) — White, Jules; Fu, Quchen; Hays, Sam; Sandborn, Michael; Olea, Carlos; Gilbert, Henry; Elnashar, Ashraf; Spencer-Smith, Jesse; Schmidt, Douglas C.. 2023-02-21. Alternative Approaches örüntüsünde alternatif yolları ve artı/eksilerini sunmayı tanımlar; hangi seçeneğin her durumda daha iyi olduğunu belirlemez. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
