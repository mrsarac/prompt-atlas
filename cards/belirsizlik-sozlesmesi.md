# Belirsizlik ve yanıt vermeme

Cevabın nerede bittiğini ve hangi bilginin eksik olduğunu açık bırakın.

## Nedir?

Belirsizlik sözleşmesi, modelin hangi durumda cevap verebileceğini, hangi durumda koşullu konuşacağını ve ne zaman duracağını tarif eder. “Bilmiyorsan söyle” cümlesini somut bir veri eşiğine bağlamak işe yarar: örneğin tarih ve onay kaydı yoksa kesin program yazmamak.

Amaç bütün cevapları çekingen yapmak değildir. Kaynakta açık olanı söyleyip açık olmayanı ayrı tutmaktır. Modelin kendi güven yüzdesi bağımsız doğruluk ölçümü sayılmaz.

## Ne zaman işe yarar?

Eksik belge, çelişen sürüm veya karar için zorunlu bilgilerin eksik olduğu işlerde kullanın. Hangi eksikliğin sonucu değiştireceğini belirtin.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir etkinlik notunda saat var, ücret yok.

**Prompt**

```text
Not: Çizim atölyesi 15.00’te başlar.
Soru: Ne zaman başlar ve ücretli mi?
Yalnız nottaki bilgiyle cevapla. Ücret bilgisi yoksa “Bu notta ücret belirtilmiyor” yaz. Ücretsiz veya ücretli diye tahmin etme.
```

**Örnek çıktı**

15.00’te başlar. Bu notta ücret belirtilmiyor.

**Ne elde ettik?**

Bilinen saat ile bilinmeyen ücret ayrıldı. Notta yazmaması etkinliğin ücretsiz olduğunu göstermez.

### Orta (Medium)

**Durum**

İki belge aynı gün için farklı saat söylüyor.

**Prompt**

```text
A: “Atölye 14.00’te.” B: “Atölye 15.00’te.” İkisinin de onay ve güncelleme bilgisi yok.
Tek bir saati doğru diye seçme. Çelişen iki bilgiyi kaynak kodlarıyla ver. Kararı değiştirecek tek eksik bilgiyi sor; güven yüzdesi uydurma.
```

**Örnek çıktı**

A 14.00, B 15.00 diyor. Hangi kayıt organizatörün onaylı son duyurusu?

**Ne elde ettik?**

Karar için gereken kaynak otoritesi sorusu çıktı. Çoğunluk veya daha akıcı cümleyle saat seçilmedi.

### İleri (Hard)

**Durum**

Bir ajan, kaynağı eksik bir takvimi ilerletmeye çalışıyor.

**Prompt**

```text
Görev: Yalnız taslak program öner; gerçek davet gönderme.
Veriler: Salon 10.00–12.00 uygun. Eğitmenin notu “sabah olabilir”; kesin uygunluk yok. Ders 90 dakika.
Salona göre mümkün aralığı hesapla; eğitmen uygunluğunu varsayma. Davet metnini kesinleşmiş gibi yazma. Eğitmen cevabı gelmeden durulacak koşulu belirt. Bilgi beklerken tamamlanabilecek tek bağımsız hazırlığı öner.
```

**Örnek çıktı**

Salon açısından 10.00–11.30 mümkündür. Eğitmenin bu aralığa onayı eksik; program kesinleşmez. Bağımsız hazırlık: 90 dakikalık içerik akışının taslağı.

**Ne elde ettik?**

Eksik bilgi bütün düşünmeyi durdurmadı; fakat bağımlı karar da verilmedi. Gerçek davet yetkisi bu promptta yok.

## Nerede durmalı?

Model belirsizliği yanlış değerlendirebilir: doğru cevabı gereksiz yere reddedebilir veya eksik bilgiyi fark etmeyebilir. Kaynak kapsamını insan denetlemelidir. Atıf sözleşmesi dayanağı gösterir; bu kart dayanak yetmediğinde verilecek davranışı belirler.

## Kaynaklar

- [Prompt design strategies  |  Gemini API  |  Google AI for Developers](https://ai.google.dev/gemini-api/docs/prompting-strategies) — Google. yayın tarihi doğrulanmadı. Açık görev ve eksik bağlam durumunda talimat tasarımına dayanak sağlar; kalibrasyon garantisi vermez. Kanıt düzeyi: sayfa gövdesi.
- [Enabling Large Language Models to Generate Text with Citations](https://arxiv.org/html/2305.14627) — Gao, Tianyu; Yen, Howard; Yu, Jiatong; Chen, Danqi. 2023-05-24; okunan sürüm 2023-10-31. Kaynak desteği ile doğru cevabın ayrı değerlendirilmesi gerektiğini gösterir; bu çekimserlik sözleşmesinin tek başına etki testi değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
