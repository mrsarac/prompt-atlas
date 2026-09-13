# Self-Ask

Ana soruya dönmeden önce eksik alt soruyu yanıtla.

## Nedir?

Self-Ask, bir sorunun takip sorusu gerektirip gerektirmediğini belirler; gerekli alt soruyu ve ara cevabı görünür kılar. Özgün çalışma arama motoruyla birleşen bir sürüm de gösterir. Dış arama varsa ara cevabı gerçekten araç sağlamalıdır.

## Ne zaman işe yarar?

İki bilgi arasında bağlantı kurmadan yanıtlanamayan sorularda; özellikle bir sonraki sorgu önceki cevaba bağlıysa.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Verilen iki kayıttan bir kişinin doğum şehrini bulacaksınız.

**Prompt**

```text
Soru: Kurgusal Gölgeler kitabının yazarının doğum şehri nedir?
Verilen kayıtlar: D1="Gölgeler'in yazarı Deniz Arı." D2="Deniz Arı Eskişehir'de doğdu."
Önce takip sorusu gerekiyor mu belirt. Gerekiyorsa tek alt soru ve bu kayıtlardan ara cevabını yaz; sonra ana soruya dön. Dış arama yok. Kaynakta olmayan ayrıntı ekleme.
```

**Örnek çıktı**

“Takip sorusu: Gölgeler’in yazarı kim? Ara cevap: Deniz Arı [D1]. Son cevap: Eskişehir [D2].”

**Ne elde ettik?**

Ana sorunun bağımlı olduğu ara bilgi ayrıldı.

### Orta (Medium)

**Durum**

Aynı soruda kayıtlar baştan verilmemiş.

**Prompt**

```text
Denetleyici salt okunur lookup(query) aracı sunsun; en fazla 2 sorgu. Başlangıç sorusu: Gölgeler'in yazarının doğum şehri nedir?
Model ilk alt soruyu üretsin. Uygulama sorguyu çalıştırıp gerçek sonucu geçmişe eklesin.
Temsili 1. sonuç: "Gölgeler — yazar Deniz Arı" [D1]. Sonraki alt soru bu ada bağlı olsun.
Temsili 2. sonuç: "Deniz Arı — doğum şehri Eskişehir" [D2].
Model gerçek iki ara cevabı kaynak kimliğiyle birleştirsin. Sonuç yoksa tahmin etmesin; bütçe sonunda dur.
```

**Örnek çıktı**

Sorgular: “Gölgeler yazarı” → “Deniz Arı doğum şehri”. Cevap: “Kayıtlardaki yazar eşleşmesine göre Eskişehir [D1, D2].”

**Ne elde ettik?**

Alt soru, önceki araç sonucundan üretildi.

### İleri (Hard)

**Durum**

Aynı adlı iki kişi aramayı belirsiz hâle getiriyor.

**Prompt**

```text
Görev: Gölgeler'in yazarının doğum şehrini bul. lookup aracı var; toplam 3 sorgu sınırı.
1. gerçek dönüş: "Gölgeler (2018), yazar Deniz Arı, çevirmen." 2. gerçek dönüş: "Deniz Arı: sporcu, İzmir; Deniz Arı: çevirmen, şehir bilgisi yok."
Model yalnız isim benzerliğiyle İzmir sonucuna atlamasın. Son alt soru çevirmen ve 2018 eserini birlikte kullanarak kimlik eşleştirmesi arasın.
3. dönüşte şehir yoksa son yanıtta çözülen ara bilgi ve çözülemeyen bilgiyi ayır. Denetleyici tüm soru/ara cevap/kaynak kayıtlarını taşısın; üç sorguda dur.
```

**Örnek çıktı**

“Yazarın çevirmen Deniz Arı olduğu eşleşiyor; doğum şehri mevcut kayıtlarda yok. Sporcuya ait İzmir bilgisini kullanmadım.”

**Ne elde ettik?**

Alt sorular, yanlış kişi eşleşmesini de görünür kıldı.

## Nerede durmalı?

Self-Ask kullanıcıya mülakat yapmak değildir; modelin ana soru için alt bilgi sorularını düzenlemesidir. Ara cevabın modelden mi, verilen belgeden mi, aramadan mı geldiği belirtilmeli. Arama sonucu da kaynak ve kimlik kontrolü gerektirir.

## Kaynaklar

- [Measuring and Narrowing the Compositionality Gap in Language Models](https://arxiv.org/html/2210.03350) — Press, Ofir; Zhang, Muru; Min, Sewon; Schmidt, Ludwig; Smith, Noah A.; Lewis, Mike. 2022-10-07; okunan sürüm 2023-10-17. Takip sorusu, ara cevap ve son cevap yapısını; ayrıca arama motoruyla birleştirilmiş Self-Ask sürümünü tanımlar. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
