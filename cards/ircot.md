# IRCoT

Bulduğunuz ara bilgiyle bir sonraki aramanın yönünü değiştirin.

## Nedir?

IRCoT, arama ile kısa ara sonuçları sırayla birleştirir. İlk belgeler yeni bir ipucu verir; bu ipucu sonraki sorguyu oluşturur. Önceki pasajlar ve soru bağlamda tutulur, cevap yeterli kanıt oluşunca birleştirilir.

Aşağıdaki öğretici düzen, uzun düşünce dökümleri yerine kaynak kodlu ara olgular taşır. Gerçek arama aracı ve bu döngüyü yöneten bir koordinatör gerekir; modelin hayal ettiği arama sonuçları gözlem değildir.

## Ne zaman işe yarar?

Cevap için birbirine bağlı iki veya daha fazla belgenin bulunması gereken sorularda uygundur. Sorgu sayısını ve kaynak yetersizken durma koşulunu baştan koyun.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Kurgusal bir kitabın yayınevinin hangi şehirde olduğunu iki kayıttan bulacaksınız.

**Prompt**

```text
Soru: “Kıyı Defteri kitabının yayınevi hangi şehirde?”
Depo: B1 “Kıyı Defteri, Ada Yayınları tarafından basıldı.” B2 “Ada Yayınları’nın merkezi İzmir.”
Koordinatör ilk aramayı kitap adıyla yapar. Gelen B1 ile modelden tek ara olgu ister: yayınevi adı.
Bu ara olguyla “Ada Yayınları merkez şehir” aramasını yapar. B1 ve B2’yi son çağrıya taşır: “Kaynak kodlarıyla tek cümlede cevapla.”
En fazla iki arama; ara ilişki yoksa sonuca atlama.
```

**Örnek çıktı**

Ara olgu: yayınevi Ada Yayınları. [B1] Son cevap: Yayınevi İzmir’dedir. [B1, B2]

**Ne elde ettik?**

İkinci sorgu ilk belgenin sonucundan doğdu. İki ayrı kurumun aynı adı taşıma ihtimalini gerçek araştırmada ayrıca kontrol edin.

### Orta (Medium)

**Durum**

Aynı isimde iki atölye var; doğru mekânın kapasitesini arıyorsunuz.

**Prompt**

```text
Soru: Eylül çizim atölyesinin salonu kaç kişilik?
Depo sonuçları: E1 “Eylül çizim atölyesi Salon A’da”; E2 “Ağustos çizim atölyesi Salon B’de”; S1 “Salon A kapasitesi 16”; S2 “Salon B kapasitesi 30”.
Koordinatör ilk aramada ay ve atölyeyi birlikte kullanır. Modelden uygun olay ve salon kodunu kısa çıkarır. Yanlış ayın kaydını ayırır.
Sonraki aramayı bulunan salonla yapar; olay kaydı ve kapasite pasajını cevap çağrısına verir. En fazla iki arama, üç model çağrısı; ay uyuşmazsa dur.
```

**Örnek çıktı**

Eylül → Salon A [E1]. Salon A → 16 kişi [S1]. Cevap: Eylül atölyesinin salonu 16 kişilik. [E1, S1]

**Ne elde ettik?**

Ara kimlik korunarak yanlış etkinliğin kapasitesi elendi. Benzer sözcükler tek başına belge eşlemesi için yeterli olmadı.

### İleri (Hard)

**Durum**

İki bağlantı kuruluyor ama son bilgi bulunamıyor.

**Prompt**

```text
Soru: Kıyı Defteri’nin editörünün vereceği sonraki seminer ne zaman?
Depo: K1 “Kıyı Defteri editörü Derya Ak”; K2 “Derya Ak’ın bahar semineri 3 Mayıs 2026”; K3 “Sonbahar semineri duyurulacaktır.” Bugün 13 Eylül 2026.
Koordinatör kitap→editör ara olgusuyla ikinci aramayı yapar. Ara sonuçlarda tarih ve gelecekte/geride olma ayrımını korur. En fazla üç arama; yinelenen sonuç veya tarih bulunmaması halinde dur.
Son çağrı: “Kaynakların söylediğini ve cevapsız kalan kısmı ayır. Geçmiş tarihi sonraki seminer diye sunma.”
```

**Örnek çıktı**

Editör Derya Ak. [K1] 3 Mayıs semineri geçmişte. [K2] Sonbahar seminerinin tarihi bu kayıtlarda yok. [K3]

**Ne elde ettik?**

Arama zinciri bir isim buldu, fakat istenen tarihi bulmuş olmadı. Eksikliği gizleyen bir son cevap üretilmedi.

## Nerede durmalı?

Yanlış ara olgu sonraki aramayı da yanlış yönlendirir. Döngü aynı belgeleri getirerek uzayabilir. Tek sefer RAG’dan farkı sorgunun ara bilgiyle yenilenmesidir; Self-Ask’ta alt sorular arama olmadan da model tarafından cevaplanabilir.

## Kaynaklar

- [Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions](https://arxiv.org/html/2212.10509) — Trivedi, Harsh; Balasubramanian, Niranjan; Khot, Tushar; Sabharwal, Ashish. 2022-12-20; okunan sürüm 2023-06-23. Ara çıkarım ve retrieval adımlarının birbirini yönlendirmesini inceler; GPT-3/Flan-T5 ile çok adımlı QA sonuçları genel araştırma doğruluğu değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
