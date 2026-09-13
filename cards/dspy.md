# DSPy

Model çağrılarını giriş–çıkış modülleri olarak tanımlayın; optimizasyonu ölçüte bağlayın.

## Nedir?

DSPy, dil modeli programlarını modüller ve veri akışlarıyla yazmak için bir çerçevedir. Hangi girdiden hangi çıktının üretileceğini tanımlarsınız; modülleri birleştirirsiniz. Seçilen optimizer, eğitim/geliştirme örnekleri ve ölçütle prompt veya gösterimleri düzenleyebilir.

DSPy tek bir prompt veya tek bir optimizer değildir. Bir imza yazmak sistemi optimize etmez; model bağlantısı, gerçek modül çağrıları, veri ve değerlendirme gerekir. Aşağıdaki taslaklar sürüme bağlı API kodu yerine uygulanacak modül sözleşmeleridir.

## Ne zaman işe yarar?

Aynı bileşenleri farklı işlerde birleştirmek veya ölçülebilir bir model akışı kurmak istediğinizde kullanın. Python ortamı ve kurulu, sürümü bilinen DSPy gerekir; kart bunları kurmaz.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Tek bir sınıflandırıcı modülü tanımlanacak.

**Prompt**

```text
Geliştirici DSPy programında şu imzayı kurar: ileti:string → etiket:string.
Modül talimatı: “Yalnız erisim/fatura/belirsiz; açık konu yoksa belirsiz.”
Tam girdi: “Giremiyorum”. Beklenen etiket: erisim.
Program, yapılandırılmış model bağdaştırıcısıyla modülü bir kez çağırır. Çıktı izinli etiket kümesinde mi ve beklenenle eşleşiyor mu kontrol eder. Bu adımda optimizer yok.
API hatasında sonuç üretme; çıktı sözleşmesini geçmeden kaydetme.
```

**Örnek çıktı**

Temsili modül sonucu: etiket=erisim. Bu yalnız programın çalıştıracağı örnek girdidir.

**Ne elde ettik?**

İmza, görev ve kontrol ölçütü belli. Tek modül çağrısı henüz derleme/optimizasyon sayılmaz.

### Orta (Medium)

**Durum**

Bulma ve cevaplama iki modül olarak bağlanacak.

**Prompt**

```text
Depo: K1 “Salon A 16 kişilik”; K2 “Salon B 30 kişilik”. Soru: Salon A kaç kişilik?
DSPy uygulaması: retrieve(soru) → pasajlar; answer(soru,pasajlar) → cevap,kaynak_kodlari.
Gerçek arama bileşeni K1/K2 üzerinde çalışır. Cevap modülü yalnız getirilen pasajı kullanır. İmzalarla birlikte “pasaj yoksa cevap yok” kuralı uygulanır.
Koordinatör arama sonucu ile cevap alanlarının bağını denetler. Bir arama, bir cevap çağrısı; eksik kayıtta dur.
```

**Örnek çıktı**

Temsili akış: retrieve → K1; answer → “16 kişi”, [K1].

**Ne elde ettik?**

Modüller arasındaki veri sözleşmesi açık. Programın kurulması ve çalıştırılması ayrı mühendislik adımıdır.

### İleri (Hard)

**Durum**

Aynı program için örnek seçimi optimize edilecek.

**Prompt**

```text
Program: ileti → etiket. Geliştirme: “Giremiyorum”→erisim; “Fatura yok”→fatura; “Selam”→belirsiz.
Geliştirici kurulu DSPy sürümündeki örnek destekli optimizer’ı seçer; metric=exact-match, en fazla 12 hedef çağrısı ayarlar. Optimizatör aday gösterimleri üretip gerçek modül çıktılarıyla değerlendirir.
Son programı dondur. Ayrı kontrol “Hesap açılmıyor”→erisim; bu örneği optimizer’a verme.
Derlenen programın talimat/gösterimlerini ve kontrol sonucunu kaydet. Bütçede geçerli aday yoksa başlangıç programını otomatik başarılı sayma.
```

**Örnek çıktı**

Temsili teslim: dondurulmuş imza, seçilen gösterimler, ölçüm kayıtları. Ayrı kontrolün çıktısı çalıştırmadan bilinmez.

**Ne elde ettik?**

Çerçeve kullanımıyla gerçek optimize edilmiş program birbirinden ayrıldı. Metrik ve veri olmadan başarı iddiası kalmadı.

## Nerede durmalı?

Kurulu sürümün API’si ve optimizer davranışı özgün makaleyle birebir aynı olmayabilir. Değerlendirme ölçütünü yanlış seçerseniz düzgün derlenmiş bir program yanlış işi daha tutarlı yapabilir. APE, OPRO ve GEPA belirli arama yaklaşımlarıdır; DSPy bunlarla aynı tek yöntem değildir.

## Kaynaklar

- [DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines](https://arxiv.org/html/2310.03714) — Khattab, Omar; Singhvi, Arnav; Maheshwari, Paridhi; Zhang, Zhiyuan; Santhanam, Keshav; Vardhamanan, Sri; Haq, Saiful; Sharma, Ashutosh; Joshi, Thomas T.; Moazam, Hanna; Miller, Heather; Zaharia, Matei; Potts, Christopher. 2023-10-05. Bildirime dayalı modüller, dil modeli çağrı grafikleri ve ölçütle derlemeyi tanımlar. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
- [stanfordnlp/dspy: DSPy: The framework for programming—not prompting—language models](https://github.com/stanfordnlp/dspy) — DSPy contributors. yayın tarihi doğrulanmadı. Çerçevenin kamu deposunu ve uygulama kapsamını gösterir; depo ile makalenin sürümleri aynı sayılmaz. Kanıt düzeyi: sayfa gövdesi.
