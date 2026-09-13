# Least-to-Most

Kolay alt problemi çözün; onun sonucunu bir sonraki problemin girdisi yapın.

## Nedir?

Least-to-Most önce zor soruyu daha basit alt sorulara ayırır, sonra bunları sırayla çözer. Önceki cevaplar sonraki çağrıya aktarılır. Bu yüzden yalnız bir yapılacaklar listesi yazmak yöntemin tamamı değildir.

Koordinatör insan da olabilir, program da. Ayrıştırmayı denetler, çözüm için gereken önceki sonuçları taşır ve yanlış bir ara sonucu devam ettirmeden kontrol eder.

## Ne zaman işe yarar?

Bir sonraki adımın önceki cevaba bağlı olduğu metin veya hesap işlerinde uygundur. Alt soruların sırasını ve başarı ölçütünü belirleyebilmelisiniz.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Üç kutudaki kalemlerden kalanları bulacaksınız.

**Prompt**

```text
İnsan koordinatör; en fazla üç çağrı.
1. Ayrıştır: “Üç kutuda dörder kalem var, beşi veriliyor. Önce çözülmesi gereken alt soruları sırala.”
2. İlk alt soru için: “Üç kutuda dörder kalem varsa toplam kaçtır? Kısa eşitlik ver.”
3. Önceki cevabı ve özgün soruyu taşı: “Toplamdan verilen beşi çıkar.”
Ara sonuç negatif veya verilerle uyumsuzsa dur; yeni veri uydurma.
```

**Örnek çıktı**

Alt sorular: başlangıç toplamı, kalan. İlk çözüm: 12. Son çözüm: 12−5=7 kalem.

**Ne elde ettik?**

Önceki sonuç sonraki soruda kullanıldı. Aynı hesabı doğrudan yapmak mümkün; bu küçük örnek bağımlılığı göstermek içindir.

### Orta (Medium)

**Durum**

Toplantıdan önce iki iş var ve biri ötekine bağlı.

**Prompt**

```text
Görev: A işi 20 dakika. B işi A bitince başlıyor ve 15 dakika sürüyor. Toplantı 11.00’de. Hazırlık ne zaman başlamalı?
Koordinatör önce modelden “Bitirme saatinden önce hangi alt zamanı bulmalıyız?” sorusuyla ayrıştırma alır.
Sonra ayrı çağrıda B’nin başlangıcını 11.00 ve 15 dakika ile buldurur.
Bu sonucu yeni çağrıya aktarır; A için 20 dakika geri gider.
Son kontrolde süreleri ileri topla; toplantıyı geçiyorsa planı kabul etme. Bütçe üç çağrı.
```

**Örnek çıktı**

B 10.45’te, A 10.25’te başlamalı. İleri kontrol: 10.25+20 dakika=10.45; +15 dakika=11.00.

**Ne elde ettik?**

Bağımlı iki başlangıç saati çıktı. Gerçek iş süreleri tahminse bu planın da tahmine dayandığını ayrıca belirtin.

### İleri (Hard)

**Durum**

Bir duyuru kararında önce geçerli kural, sonra kişi sayısı, sonra metin gerekiyor.

**Prompt**

```text
Veriler: V1 eski kapasite 20, yürürlükten kaldırılmış. V2 onaylı kapasite 16. Başvuran 18 kişi; henüz kimseye onay gönderilmemiş.
İnsan koordinatör dört çağrıyı sırayla yapar:
1. Alt problemleri çıkar: geçerli kapasite → boşluk/fazlalık → kayıt duyurusu.
2. V1/V2’den geçerli kapasiteyi seçtir; kaynak kodunu sakla.
3. Yalnız bu kapasite ve 18 başvuruyla farkı hesaplat.
4. Önceki cevapları taşı: “Form başvuru toplar; yer e-postayla kesinleşir. İki cümlelik duyuru yaz; tüm başvuranlara yer sözü verme.”
Sürüm doğrulanamazsa üçüncü aşamaya geçme. Son metni insan onaylar.
```

**Örnek çıktı**

V2: 16 yer. Başvuru kapasiteyi 2 kişi aşıyor. Duyuru: “Atölye 16 kişiliktir. Başvurunuz, onay e-postası geldiğinde kesin kayda dönüşür.”

**Ne elde ettik?**

Belge seçimi hesaplamayı, hesaplama da duyuruyu sınırladı. Son metin onay kararını kendiliğinden vermiyor.

## Nerede durmalı?

Yanlış ayrıştırma bütün zinciri etkiler. Bağımsız bölümleri sırayla çözmek gereksiz gecikme yaratabilir. Skeleton-of-Thought bağımsız bölümleri paralel genişletir; Decomposed Prompting alt işleri farklı işlevlere yönlendirir.

## Kaynaklar

- [Least-to-Most Prompting Enables Complex Reasoning in Large Language Models](https://arxiv.org/html/2205.10625) — Zhou, Denny; Schärli, Nathanael; Hou, Le; Wei, Jason; Scales, Nathan; Wang, Xuezhi; Schuurmans, Dale; Cui, Claire; Bousquet, Olivier; Le, Quoc; Chi, Ed. 2022-05-21; okunan sürüm 2023-04-16. Ayrıştırma ve önceki çözümleri bağlama ekleyerek sıralı çözme mekanizmasını destekler; kolaydan zora genelleme deneylerinin kapsamı sınırlıdır. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
