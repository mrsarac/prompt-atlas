# Tercihleri açığa çıkarma

Tercihi tek etiketle sorma; ödünleşimler üzerinden açığa çıkar.

## Nedir?

Tercihleri açığa çıkarma, kişinin neye öncelik verdiğini somut seçenekler ve karşılaştırmalarla anlamaya çalışır. Model tercihlerinizi tahmin etmek yerine soru sorar; çelişki varsa bunu görünür bırakır.

## Ne zaman işe yarar?

“Kaliteli”, “rahat” veya “bana uygun” gibi ifadelerin farklı seçeneklerde farklı anlamlara geldiği kararlarda.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Yazı çalışma ortamınızı seçeceksiniz.

**Prompt**

```text
Seçenekler: A kütüphane, sessiz ve 20 dakika uzakta; B ev, yol yok ama ara sıra gürültü var. Amacım 90 dakika yazmak.
Tercihimi benim yerime çıkarma. Sessizlik ile yol süresi arasında seçimimi açacak tek soru sor ve yanıtımı bekle. Sonra söylediğim önceliği bir cümleyle özetle; kararımı teyit et.
```

**Örnek çıktı**

Model: “90 dakikalık çalışmada kesintisizlik için toplam 40 dakika yol ayırmayı kabul eder misin?” İnsan: “Bugün hayır.” Özet: “Bugün zaman kaybını azaltmak daha öncelikli.”

**Ne elde ettik?**

Tercih, kalıcı kişilik etiketi yerine bu günün koşuluna bağlandı.

### Orta (Medium)

**Durum**

İki öncelik birbirine ters düşüyor.

**Prompt**

```text
Laptop tercihleri: Hafiflik çok önemli; büyük ekran da çok önemli. Seçenek A 1,2 kg/13 inç; B 1,8 kg/16 inç. Diğer özellikler aynı varsayılsın.
Önce bu iki önceliğin hangi kullanım durumunda baskın olduğunu sor. Yanıt: Haftada dört gün taşıyorum, uzun yazıyı çoğunlukla evde yazıyorum.
Sonra harici ekran kullanabilme durumunu sor; varsayma. En fazla iki soru sonrası koşullu tercih özeti yaz, ürün tavsiyesini kesinleştirme.
```

**Örnek çıktı**

“Taşıma sık; uzun yazım evde. Evde ekran imkânı varsa hafiflik tercihi güçlenebilir; yoksa küçük ekranın bedeli ayrıca değerlendirilmeli.”

**Ne elde ettik?**

Çatışan tercihler kullanım bağlamıyla açıldı.

### İleri (Hard)

**Durum**

Aynı kişi farklı koşullarda farklı seçim yapıyor.

**Prompt**

```text
Karar: Haftalık ekip buluşması. Önceki yanıtım: Yüz yüze iletişim önemli. Yeni yanıtım: Ulaşım 1 saati aşarsa çevrim içi olsun. Katılım zorunlu değil.
Tercih kaydını sabit hüküm yerine koşullu kural olarak yaz. En fazla iki sınır örneği sor: 40 dakika ulaşım; 75 dakika ulaşım. Yanıtlarımı bekle, çelişkiyi sessizce düzeltme.
Son özette sert kısıt, tercih ve açık belirsizliği ayır. Diğer ekip üyelerinin benimle aynı tercihi olduğunu varsayma; toplantı oluşturma.
```

**Örnek çıktı**

“Tercih: ulaşım makulse yüz yüze. Koşul: 1 saati aşınca çevrim içi. Diğer üyelerin tercihleri bilinmiyor.”

**Ne elde ettik?**

İnsan tercihi, bağlamdan bağımsız tek puana indirgenmedi.

## Nerede durmalı?

Bu düzen tercihleri ölçmeye yardımcı olabilir; “gerçek arzunu senden iyi biliyorum” iddiası taşımaz. COPE kaynağındaki insan tercih değerlendirmesi ile offline çıkarım başarısı farklı ölçütlerdir. Modelin verdiği özet, insanın açık teyidine ihtiyaç duyabilir.

## Kaynaklar

- [When and How to Ask: Dynamic Preference Elicitation Strategies for Conversational Recommendation](https://arxiv.org/html/2607.06765v1) — Xia, Feng; Zhang, Shuo; Wang, Xi. 2026-07-07. Konuşma yoluyla tercih elicitation yaklaşımını ve değerlendirmesini inceler; insan tercih bulgusu ile offline model ölçümleri birbirine karıştırılmaz. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
