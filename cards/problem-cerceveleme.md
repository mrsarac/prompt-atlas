# Problem çerçeveleme

Çözümü seçmeden önce hangi sorunu çözdüğünü netleştir.

## Nedir?

Problem çerçeveleme; belirti, hedef, kısıt ve başarı ölçütünü ayırır. Model alternatif çerçeveler önerebilir, fakat hangi sorunun değerli olduğuna tek başına karar vermez. Burada pratik bir düşünme düzeni olarak kullanılıyor.

## Ne zaman işe yarar?

Bir araç veya özellik seçmişsiniz ama bunun hangi kullanıcı ihtiyacını karşılayacağı belirsizse.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

“Bir chatbot yapalım” fikrinden başlayacaksınız.

**Prompt**

```text
Fikrim: Siteme chatbot ekleyelim. Gözlem: İnsanlar açılış saatlerini bulamıyor. Kısıt: Küçük site, bakım için haftada 1 saat.
Çözüm fikrini, gözlenen sorunu ve bilinmeyeni ayır. Başarıyı araç kuruldu diye değil, okurun saat bilgisini bulabilmesiyle tanımla. Bir netleştirme sorusu sor; yeni ürünü tasarlamaya başlama.
```

**Örnek çıktı**

“Çözüm adayı: chatbot. Sorun: saat bilgisine erişim. Bilinmeyen: insanlar hangi sayfada arıyor? Başarı: saat bilgisini bulma görevinin tamamlanması.”

**Ne elde ettik?**

Araç adı, problem tanımının yerine geçmedi.

### Orta (Medium)

**Durum**

Aynı belirti iki farklı soruna işaret edebilir.

**Prompt**

```text
Gözlem: Beş yeni kullanıcının üçü ilk notunu kaydetmedi. Görüşme veya ekran kaydı yok. Önerilen çözüm: Daha büyük kaydet düğmesi.
En fazla üç problem çerçevesi yaz: düğmeyi bulamama, kayıt mantığını anlamama, not girmek istememe. Her biri için ayırt edici tek gözlem öner. Bunları doğrulanmış neden diye yazma.
Sonunda en küçük bilgi toplama adımını öner; kullanıcı araştırması veya mesaj gönderme işlemi yapma.
```

**Örnek çıktı**

“Kaydet düğmesini fark ediyor ama sonuçtan emin olamıyorsa sorun görünürlükten çok geri bildirim olabilir. Kısa görev gözlemi bu ayrımı açabilir.”

**Ne elde ettik?**

Aynı çözümün her açıklamaya uymadığı görüldü.

### İleri (Hard)

**Durum**

Hedefler çatışırken optimizasyonu erken başlatmamak gerekiyor.

**Prompt**

```text
Ekip hedefleri: Destek süresini azaltmak; yanıt doğruluğunu korumak. Veri: 20 örnek talep, ortalama işlem süresi biliniyor ama doğruluk ölçümü yok. Kısıt: Müşteri verisi dışarı aktarılamaz.
Problem briefi yaz: karar, hedefler, ölçülebilenler, henüz ölçülemeyenler, sert kısıtlar. Süreyi tek başarı ölçütü yapma. Bir doğruluk ölçütünün kim tarafından tanımlanacağını açık soru olarak bırak.
İki alternatif çerçeve öner: taslak hazırlama yardımı; tam otomatik yanıtlama. İkincisini mevcut yetki veya veriyle yapılabilir varsayma.
```

**Örnek çıktı**

“Önce taslak desteğinin süre ve insan onaylı doğruluk üzerindeki etkisi değerlendirilebilir. Tam otomatik yanıtlama için ayrı doğruluk ve yetki kararı gerekir.”

**Ne elde ettik?**

Optimizasyon, henüz tanımlanmamış bir başarı anlayışına bağlanmadı.

## Nerede durmalı?

Question Refinement sorunun cümlesini geliştirir; problem çerçeveleme kararın ve başarı ölçütünün ne olduğunu sorgular. Optimizasyon öncesi netleştirme araştırması bu yaklaşımın komşusudur; hangi insan probleminin değerli olduğunu otomatik belirlediği söylenemez.

## Kaynaklar

- [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT](https://arxiv.org/html/2302.11382) — White, Jules; Fu, Quchen; Hays, Sam; Sandborn, Michael; Olea, Carlos; Gilbert, Henry; Elnashar, Ashraf; Spencer-Smith, Jesse; Schmidt, Douglas C.. 2023-02-21. Etkileşimli soru ve alternatif üretme örüntüleri için kaynak sağlar; geniş problem çerçeveleme yaklaşımının deneysel etkinlik kanıtı değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
- [Ask Before You Optimize: Dynamic Pre-Formulation Clarification for Interactive Optimization](https://arxiv.org/html/2609.05258) — Ge, Sihan; Lin, Yichen; Zhou, Chenyu; Lin, Jianghao; Yao, Tao; Ge, Dongdong. 2026-09-04; okunan sürüm 2026-09-08. Optimizasyon formülasyonundan önce hedef/kısıt netleştirmeyi simüle kullanıcıyla inceler; gerçek insanların bütün problem seçme sürecini temsil etmez. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
