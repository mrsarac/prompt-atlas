# Question Refinement

Soruyu yanıtlamadan önce daha işe yarar hâlini öner.

## Nedir?

Question Refinement, kullanıcının sorusunu daha belirli ve yanıtlanabilir biçime dönüştürür. Model yeni soruyu önerir; kullanıcının amacı değişiyorsa bunu açık eder ve onay bekler.

## Ne zaman işe yarar?

“En iyisi hangisi?” veya “Bunu nasıl düzeltirim?” gibi ölçütü ve kapsamı belirsiz sorularda.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

“Hangi bilgisayar iyi?” sorusundan başlayacaksınız.

**Prompt**

```text
Sorumu hemen yanıtlamak yerine daha iyi bir sürüm öner. Bilinmeyen tercihleri ekleme. Bir kısa açıklama ve tek netleştirme sorusu yaz.
Sorum: Hangi bilgisayar iyi?
Bildiğin: Metin yazıyorum, sık taşıyorum. Bütçemi henüz söylemedim.
```

**Örnek çıktı**

“Öneri: Metin yazmak ve sık taşımak için hangi bilgisayar özelliklerine öncelik vermeliyim? Model önerisine geçmek için bütçe aralığın nedir?”

**Ne elde ettik?**

“İyi” sözcüğü görünür kullanım ölçütlerine ayrıldı.

### Orta (Medium)

**Durum**

“Sitem yavaş” yakınmasını incelenebilir bir soruya çevireceksiniz.

**Prompt**

```text
Şu soruyu teknik inceleme için daralt, ama bir neden uydurma: Sitem neden yavaş?
Veriler: Ürün sayfası mobilde 6 saniyede açılıyor. Masaüstü ölçümü yok. Son değişiklik ürün görselleri; bunun neden olduğu henüz test edilmedi.
Daha iyi soruyu, bilinenleri ve eksik tek karşılaştırmayı yaz. Kullanıcı yeni soruyu kabul etmeden çözüm uygulama.
```

**Örnek çıktı**

“Mobil ürün sayfasındaki 6 saniyelik açılışta hangi kaynak en çok süre alıyor? Görsel değişikliği bir hipotez; ağ/işlem zamanlaması henüz ölçülmedi.”

**Ne elde ettik?**

Belirti, doğrulanmamış nedenin içine kilitlenmedi.

### İleri (Hard)

**Durum**

Bir politika sorusu içinde iki farklı karar gizli.

**Prompt**

```text
Soru: Ekibimiz yapay zekâyı tamamen kullanmalı mı?
Bağlam: 6 kişilik tasarım ekibi. Kullanım adayları: kamuya açık metin özeti ve müşteriye ait gizli çizimler. Amaç süre kazanmak; veri aktarımı için izin yok.
Soruyu iki karar sorusuna ayır. Yetki sınırını koru. Her soruya gereken kanıtı ve kullanıcının seçmesi gereken önceliği ekle. İki soru aynı sonuca çıkmak zorunda değil. Kullanıcı seçim yapana kadar uygulama veya politika önerisini kesinleştirme.
```

**Örnek çıktı**

“1. Kamuya açık metin özetinde doğruluk ve süre nasıl ölçülür? 2. Gizli çizimleri dış hizmete aktarmadan hangi yerel seçenekler değerlendirilebilir? İkinci iş için mevcut aktarım izni yok.”

**Ne elde ettik?**

Tek bir evet/hayır sorusu, farklı veri ve karar sınırlarına ayrıldı.

## Nerede durmalı?

Daha süslü bir soru daha iyi soru olmayabilir. Yeni sürüm kullanıcının niyetini değiştirmemeli. Problem çerçeveleme sorunun kendisini ve başarı ölçütünü tartışır; bu örüntü daha dar biçimde sorunun ifadesini iyileştirir.

## Kaynaklar

- [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT](https://arxiv.org/html/2302.11382) — White, Jules; Fu, Quchen; Hays, Sam; Sandborn, Michael; Olea, Carlos; Gilbert, Henry; Elnashar, Ashraf; Spencer-Smith, Jesse; Schmidt, Douglas C.. 2023-02-21. Question Refinement örüntüsünde modelin daha iyi soru önermesini ve kullanıcının bunu kullanma kararını korumasını açıklar. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
