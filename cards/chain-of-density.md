# Chain-of-Density

Özetin boyunu büyütmeden, kaynakta kalan önemli bilgileri içeri al.

## Nedir?

Chain-of-Density, önce daha seyrek bir özet yazar; sonra eksik önemli varlık ve ayrıntıları aynı sözcük bütçesi içinde ekleyerek özeti yoğunlaştırır. Eklenen her unsur kaynakta bulunmalı, eski önemli bilgi korunmalıdır.

## Ne zaman işe yarar?

Kısa özetlerin giderek daha fazla bilgi taşımasını istediğinizde. Okunabilirlik ve doğruluk yoğunluktan daha önceliklidir.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

On sözcüklük bir etkinlik özeti geliştireceksiniz.

**Prompt**

```text
Kaynak: Suluboya atölyesi 12 Ekim'de. Kontenjan sekiz. Yer ve ücret henüz açıklanmadı.
İlk özet: "Atölye ekimde yapılacak; katılım sınırlı, yer ve ücret sonra açıklanacak."
Aynı çağrıda bir yoğunlaştırma turu yap: eksik üç unsuru listele, sonra özeti tam 10 sözcükle yeniden yaz. Sayım boşlukla ayrılan sözcüklerdir. Önceki yer/ücret belirsizliğini koru; yeni bilgi ekleme.
İnsan sayımı ve kaynak eşleşmesini kontrol edip bir turda dursun.
```

**Örnek çıktı**

“Eksik: suluboya, 12 Ekim, sekiz kişi. Yeni özet: Suluboya atölyesi 12 Ekim’de; kontenjan sekiz, yer ve ücret belirsiz.”

**Ne elde ettik?**

Uzunluk sabit kalırken konu, tarih ve kapasite belirginleşti.

### Orta (Medium)

**Durum**

İki turda yoğunluk artacak ama eski bilgiler düşmemeli.

**Prompt**

```text
Kaynak: Suluboya atölyesi 12 Ekim'de yapılacak. Kontenjan sekiz kişi. Malzemeler dahil. Yer ve ücret açıklanmadı.
Önce tam 15 sözcüklük seyrek bir özet yaz. Ardından iki tur uygula: o an eksik olan 1–3 kaynak unsurunu adlandır; bunları ekleyerek yine 15 sözcük yaz. Önceki önemli olguları koru. Her turda sözcük sayısını dışarıda belirt.
İnsan kaynak, eski bilgi korunumu ve 15 sözcük koşulunu denetlesin. Yeni unsur kalmadığında ikinci turu zorla doldurma; en fazla iki turda dur.
```

**Örnek çıktı**

Son özet örneği: “Suluboya atölyesi 12 Ekim’de yapılacak; kontenjan sekiz kişi, malzemeler dahil, yer ve ücret henüz açıklanmadı.”

**Ne elde ettik?**

Yalnız kısaltma değil, aynı uzunlukta daha fazla kaynak bilgisi hedeflendi.

### İleri (Hard)

**Durum**

Yoğunlaştırma, bir istisnayı ortadan kaldırabilir.

**Prompt**

```text
Kaynak: Başvurular 20 Ekim'de kapanır. Öğrenciler ücretsiz katılır. Diğer katılımcılar 200 TL öder. Kontenjan 16 kişidir. Erişim desteği önceden talep edilmelidir.
Tam 20 sözcüklük özet yaz; sonra eksik unsurları bulup en fazla iki yoğunlaştırma turu yap. Ücretsizliği herkese yayma; erişim desteğini otomatik hazır sayma.
Her turda insan şu alanları denetlesin: kapanış tarihi, ücretin kime bağlı olduğu, kapasite, önceden talep koşulu. Bunlar 20 sözcüğe sığmazsa ayrıntı uydurma veya koşulu silme; bütçenin yetersizliğini bildir.
```

**Örnek çıktı**

“Başvurular 20 Ekim’de kapanır; öğrenciler ücretsiz, diğerleri 200 TL öder. Kontenjan 16 kişidir; erişim desteği için önceden talep iletilmesi gereklidir.”

**Ne elde ettik?**

Daha yoğun özet, farklı grupların koşullarını birbirine karıştırmadı.

## Nerede durmalı?

Yoğunluk tek başına kalite ölçüsü değildir; okunmaz bir cümle veya kaybolan istisna başarısızlıktır. Kaynakta bulunmayan ayrıntıyı eklemek bu yöntem değildir. Özgün çalışmanın özetleme bağlamı bütün yazı türlerine doğrudan genellenmez.

## Kaynaklar

- [From Sparse to Dense: GPT-4 Summarization with Chain of Density Prompting](https://arxiv.org/html/2309.04269) — Adams, Griffin; Fabbri, Alexander; Ladhak, Faisal; Lehman, Eric; Elhadad, Noémie. 2023-09-08. Sabit uzunlukta özete eksik, kaynak destekli varlıklar ekleyerek ardışık yoğunlaştırmayı tarif eder; senaryolar özgün haber deneyinin tekrarı değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
