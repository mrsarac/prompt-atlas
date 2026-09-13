# Chain-of-Verification

Taslağı küçük kontrol sorularına ayırın; cevapları taslaktan etkilenmeden yeniden alın.

## Nedir?

Chain-of-Verification önce bir taslak cevap üretir, ardından taslaktaki iddialar için kontrol soruları hazırlar. Ayrı cevaplama aşaması bu soruları yanıtlar; son aşama taslağı kontrol cevaplarına göre düzenler. Factored biçimde kontrol çağrıları taslağın önerdiği cevabı görmez.

Bu bağlam ayrımı dış kaynak sağlamaz. Aşağıdaki belge örneklerinde kaynağı kontrol çağrısına ayrıca veren biziz; bu, kaynak denetimini görünür kılan öğretici uyarlamadır.

## Ne zaman işe yarar?

Bir taslakta birkaç doğrulanabilir olgu bulunduğunda işe yarayabilir. Kontrol sorularının hangi bilgiyi sınadığını ve cevaplayıcının hangi verilere eriştiğini belirleyin.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir duyuru onay koşulunu atlamış.

**Prompt**

```text
Koordinatör:
1. Taslak çağrısı: “K1: Form başvuru toplar; yer onay e-postasıyla kesinleşir. Kısa duyuru yaz.”
2. Taslağı ayrı çağrıya ver: “Kayıt iddiasını kontrol edecek tek soru üret; cevap verme.”
3. Yeni çağrıya yalnız soru ve K1’i ver; taslağı taşıma.
4. İlk taslak, K1 ve kontrol cevabını birleştir: “Yanlış kesinlik varsa düzelt.”
En fazla dört çağrı; kontrol cevabı K1’de yoksa insan denetimi iste.
```

**Örnek çıktı**

Temsili taslak: “Formu doldurun, yeriniz hazır.” Kontrol sorusu: “Yer ne zaman kesinleşir?” Cevap: “Onay e-postasıyla.” Son metin bu koşulu içerir.

**Ne elde ettik?**

Taslağın eksik koşulu ayrı soruyla görünür oldu. Örnek, otomatik model başarısının ölçümü değildir.

### Orta (Medium)

**Durum**

Duyuruda iki olgu ayrı kontrol edilecek.

**Prompt**

```text
Kaynak: K1 “Atölye 16 kişilik”; K2 “Kalem sağlanır; defter katılımcıdan”.
1. Modelden bu kaynaklarla duyuru taslağı al.
2. Taslak üzerinden kapasite ve malzeme için iki kontrol sorusu al.
3. Her soruyu ayrı yeni çağrıda ilgili kaynakla cevaplat; diğer kontrolün yanıtını ve ilk taslağı gösterme.
4. Taslak ve iki cevabı birleştirerek son metni yazdır.
Koordinatör toplam beş çağrıyı aşmaz. Kaynak dışı iddiayı çıkarır veya bilinmiyor diye işaretler.
```

**Örnek çıktı**

Temsili kontroller: kapasite 16 [K1]; sağlanan malzeme kalem, getirilecek defter [K2]. Son metin “bütün malzemeler sağlanır” diyemez.

**Ne elde ettik?**

Birbirinden farklı iddialar tek genel “kontrol ettim” mesajına gömülmedi. Kaynakların gerçekliği yine ayrıca denetlenir.

### İleri (Hard)

**Durum**

Kontrol sorularının birine kaynak cevap vermiyor.

**Prompt**

```text
Taslak hedefi: Atölyenin kapasitesi, malzemesi ve video erişimini anlat.
Kaynaklar: K1 “Kapasite 16”; K2 “Kalem sağlanır”. Video bilgisi yok.
Koordinatör taslak→kontrol soruları→her soruya ayrı cevap→son düzenleme akışını yürütür. Kontrol çağrılarına yalnız soru ve K1/K2 gider; tahmin yapmaları yasaktır.
En fazla altı çağrı. Eksik videoyu başka kontrol cevabından türetme. Son düzenlemede destekli iki bilgi ile açık video sorusunu ayır; kaynak bulunmadıkça kesin erişim sözü verme.
```

**Örnek çıktı**

Temsili video kontrolü: “K1/K2’de bu bilgi yok.” Son metin: “Atölye 16 kişilik; kalem sağlanır. Video erişimi hakkında bu kaynaklarda bilgi bulunmuyor.”

**Ne elde ettik?**

Kontrol zinciri eksik bilgiyi sonuçtan silmedi. Yeni kaynak için ayrıca araştırma gerekir.

## Nerede durmalı?

Ayrı bağlamdaki aynı model aynı yanlışı tekrarlayabilir. Özgün CoVe’nin modelden alınan kontrollerini bağımsız olgusal kanıt gibi sunmayın. CRITIC dış araç gözlemi kullanır; Self-Refine daha genel üret–eleştir–düzelt döngüsüdür.

## Kaynaklar

- [Chain-of-Verification Reduces Hallucination in Large Language Models](https://arxiv.org/html/2309.11495) — Dhuliawala, Shehzaad; Komeili, Mojtaba; Xu, Jing; Raileanu, Roberta; Li, Xian; Celikyilmaz, Asli; Weston, Jason. 2023-09-20; okunan sürüm 2023-09-25. Taslak, kontrol sorusu, ayrı cevaplama ve son düzenleme sırasını tanımlar; Llama 65B ve seçilmiş olgusal görevler tüm kullanım alanlarını kanıtlamaz. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
