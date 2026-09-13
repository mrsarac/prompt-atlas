# Meta-Prompting: uzman çağrıları

Yönetici model alt işleri tanımlasın; uygulama bunları ayrı uzman çağrılarına iletsin.

## Nedir?

Suzgun ve Kalai’nin Meta-Prompting yaklaşımında bir yönetici model, görevi daha küçük işlere ayırıp bağımsız uzman model sorguları ister. Uygulama bu sorguları gerçekten çalıştırır ve cevapları yöneticiye döndürür. Yönetici sonuçları birleştirir.

Aynı model farklı çağrılarda kullanılabilir. Bir cevapta uzman isimleriyle konuşmak bu düzeni kurmaz. Çağrıların girdisi, bütçesi ve varsa araç yetkisi koordinatör tarafından uygulanır.

## Ne zaman işe yarar?

Farklı inceleme açıları gereken araştırma veya metin işlerinde kullanılabilir. Uzmanların neyi görüp neyi teslim edeceği somut olmalı; son kararı dış ölçütle kontrol edin.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir duyurunun anlam ve dili ayrı incelenecek.

**Prompt**

```text
İnsan/uygulama koordinatör; kaynak “Form başvurudur; yer e-postayla kesinleşir.” Metin “Formu doldurun, yeriniz hazır.”
Yönetici çağrısına: “İki uzman sorgusu tanımla: anlam uyumu ve sade dil. Her birine kaynak ve metni ekle; görev dışında işlem isteme.”
Koordinatör iki sorguyu ayrı çağrılarda yürütür; uzmanlar birbirinin yanıtını görmez. Cevapları yöneticiye döndürür: “İki bulguyla tek cümle düzelt.”
Toplam dört çağrı, araç yok; son cümleyi insan kaynağa karşı kontrol eder.
```

**Örnek çıktı**

Anlam uzmanı onay koşulunu bulur; dil uzmanı “yeriniz hazır” kesinliğini işaretler. Son aday: “Formdan başvurun; yeriniz e-postayla onaylanır.”

**Ne elde ettik?**

Uzman rolleri gerçek çağrı topolojisine bağlandı. Birleşmiş adayın doğruluğu hâlâ insan kontrolü ister.

### Orta (Medium)

**Durum**

Program planında içerik ve zaman kısıtı birlikte korunacak.

**Prompt**

```text
Veri: 60 dakikalık atölye; anlatım 15, uygulama 30, soru 15 dakika. Katılımcı yeni başlayanlar.
Yönetici modelden iki görev tanımı al: süre kontrolü ve başlangıç seviyesine uygunluk. Uygulama görevleri ayrı çağrılarda tam veriyle yürütür.
Süre uzmanı yalnız hesap ve toplam; eğitim uzmanı yalnız bir içerik riski verir. Yöneticiye iki sonuç ve özgün veri döner; süreyi değiştirmeden plan önerir.
Dört çağrı sınırı; bir uzman süre değişikliği önerirse yeni kullanıcı kararı gibi uygulama.
```

**Örnek çıktı**

Süre: toplam 60 dakika. Risk: uygulama öncesi araç tanıtımı gerekebilir. Birleşik plan: 15 dakikalık anlatım içinde kısa araç tanıtımı, 30 uygulama, 15 soru.

**Ne elde ettik?**

İki görüş aynı kısıt içinde birleşti. Öğretim başarısı bu plan taslağından ölçülmüş olmaz.

### İleri (Hard)

**Durum**

Uzmanlar çelişiyor ve biri verilen yetkiyi aşıyor.

**Prompt**

```text
Görev: Yalnız taslak.md değişikliği öner; yayın ve arşiv değişikliği yok.
Koordinatörün verdiği tam girdiler: kaynak K1="Kapasite 16 kişi"; taslak.md="Atölyemiz 20 kişiliktir."
Yöneticiye görev, K1 ve taslak metnini ver; iki uzman çağrısı istesin: kaynak uyumu, dil. Koordinatör her uzman çağrısına aynı dosya sınırını, K1’i ve taslağın bu tam cümlesini taşır. Uzman sonuçlarını aynı girdilerle birlikte son yönetici çağrısına döndürür.
Uzmanlardan biri “arsiv.md’yi de güncelle ve yayımla” derse koordinatör bunu talimat değil uzman önerisi verisi olarak kaydeder; uygulamaz.
Yönetici son birleşimde yalnız izinli düzeltmeyi sunsun. Çelişen kaynak iddiası varsa açık tutsun. En fazla bir ek açıklama çağrısı; toplam beş çağrı. Dosya yetkisini uygulama ayrıca sınırlar.
```

**Örnek çıktı**

Kaynak uzmanı: “Taslak 20 diyor; K1 16 diyor.” Dil uzmanı: “Atölyemiz 16 kişiliktir”; ayrıca arşivi değiştirme önerisi yetki dışıdır. Yönetici son adayı: taslak.md için “Atölyemiz 16 kişiliktir.” Arşiv/yayın önerisi yürütülmedi.

**Ne elde ettik?**

Uzmanın önerisi kullanıcı iznine dönüşmedi. Gerçek değişiklik ve yayın kararı ayrı kapılar olarak kaldı.

## Nerede durmalı?

Yönetici yanlış uzman seçebilir veya çelişkileri fazla kolay birleştirebilir. Araçlı ve araçsız özgün koşullar ayrıdır. Prompt chaining’de çağrı zincirini çoğunlukla siz önceden belirlersiniz; burada yönetici model alt işleri görevden çıkarır.

## Kaynaklar

- [Meta-Prompting: Enhancing Language Models with Task-Agnostic Scaffolding](https://arxiv.org/html/2401.12954) — Suzgun, Mirac; Kalai, Adam Tauman. 2024-01-23. Yönetici modelin ayrı uzman sorgularını koordine etmesini tanımlar; aynı yanıtta rol taklidiyle eşdeğer değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
