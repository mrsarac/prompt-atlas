# Generated Knowledge

Cevaptan önce ilgili bilgi adaylarını üret; bunları kaynak sanma.

## Nedir?

Generated Knowledge Prompting, modelden önce soruyla ilgili bilgi üretmesini, sonra bu bilgiyi soruyu yanıtlarken kullanmasını ister. Üretilen bilgi model kaynaklıdır; dış belge getirme veya doğrulama yapılmış olmaz.

## Ne zaman işe yarar?

Gündelik bilgi gerektiren bir soruda ilgili kavramları ortaya çıkarmak ve ardından cevabı kurmak için. Güncel, hassas veya kaynak zorunlu konularda tek başına yetmez.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

“Buz neden suda yüzer?” sorusunu iki aşamada ele alacaksınız.

**Prompt**

```text
İnsan iki ayrı çağrı yapsın.
1. Soruya yardımcı olabilecek en fazla iki kısa bilgi adayı yaz: Buz neden suda yüzer? Bunlar model üretimi; kaynak doğrulaması yaptığını söyleme.
2. Gerçek ilk çıktıyı ve soruyu yeni çağrıya ver. Bu bilgi adaylarından yararlanarak iki cümlelik cevap yaz. Bir aday belirsizse kesin bilgi diye kullanma. İkinci cevapta dur.
```

**Örnek çıktı**

Bilgi adayları: “Buzun yoğunluğu sıvı sudan düşüktür. Daha düşük yoğunluk yüzmeyi açıklayabilir.” Cevap: “Buz, sıvı sudan daha düşük yoğunluklu olduğu için yüzer.”

**Ne elde ettik?**

Cevapta kullanılacak ilişki ayrı bir aşamada görünür oldu.

### Orta (Medium)

**Durum**

Bir gündelik çıkarım sorusuna iki farklı bilgi desteği üretilecek.

**Prompt**

```text
Soru: Kapağı açık bırakılan çay neden daha çabuk soğuyabilir?
Denetleyici iki ayrı bilgi üretim çağrısı çalıştırsın; her biri soruyla ilgili en fazla iki açıklama adayı versin. Gerçek çıktıları K1/K2 olarak sakla.
Son çağrı soruyu, K1 ve K2'yi birlikte alsın. Buharlaşma ve çevreyle ısı alışverişini ayır; ortam koşulları verilmediği için kesin dakika söyleme. Çelişkili bilgi varsa belirt. Üç çağrı sonunda insan temel fizik kaynağıyla kontrol etmeden metni doğrulanmış ilan etmesin.
```

**Örnek çıktı**

“Açık yüzey buharlaşmaya ve çevreyle ısı alışverişine izin verir. Soğuma hızı sıcaklık, hava akımı ve kabın yapısına da bağlıdır.”

**Ne elde ettik?**

Bilgi adayları cevapta birleştirildi; koşullar yok sayılmadı.

### İleri (Hard)

**Durum**

Üretilen bilgiyle sağlanan belge çelişirse hangisinin ne olduğunu koruyacaksınız.

**Prompt**

```text
Görev: Kurgusal müze pazartesi neden kapalı olabilir?
1. Bilgi üretim çağrısı genel müze kapanış nedenlerine iki ihtimal yazsın; kurum hakkında gerçek bilgi iddia etmesin.
2. Son çağrı bu adayları ve D1="Kent Müzesi pazartesi özel bakım nedeniyle kapalı" belgesini alsın.
Önce D1'in desteklediği kurum bilgisine cevap ver; genel ihtimalleri bu kuruma mal etme. Denetleyici model adaylarını generated, D1'i provided_source etiketiyle taşısın. İki çağrıda dur; arama yapılmadığını gizleme.
```

**Örnek çıktı**

“D1’e göre kapanışın nedeni özel bakım. Genel olarak önerilen personel planlaması gibi ihtimaller bu belgeyle doğrulanmıyor.”

**Ne elde ettik?**

Modelden gelen olası bilgilerle kuruma ait kanıt birbirinden ayrıldı.

## Nerede durmalı?

RAG dış koleksiyondan ilgili belge getirir; bu yöntem ilgili bilgiyi modelden üretir. Bir modelin iki çağrıda aynı yanlış bilgiyi söylemesi doğrulama değildir. Özgün çalışmada bilgi örnekleme ve cevapların kullanımı için belirli stratejiler vardır; burada başarı oranı vaat edilmez.

## Kaynaklar

- [Generated Knowledge Prompting for Commonsense Reasoning](https://arxiv.org/html/2110.08387) — Liu, Jiacheng; Liu, Alisa; Lu, Ximing; Welleck, Sean; West, Peter; Bras, Ronan Le; Choi, Yejin; Hajishirzi, Hannaneh. 2021-10-15; okunan sürüm 2022-09-28. Önce ilgili bilgi üretip daha sonra bu bilgiyi soru yanıtlama girdisi olarak kullanma yöntemini tanımlar. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
