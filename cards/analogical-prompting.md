# Analogical Prompting

Benzer çözümler üret, sonra hedef soruda hangi yapının taşındığını göster.

## Nedir?

Analogical Prompting, modelden hedefe yardımcı olacak benzer problem ve çözümler üretmesini, sonra bunlardan yararlanmasını ister. Üretilen benzerlikler gerçek geçmiş vaka veya dış kaynak değildir; yanlış örnekler cevabı da bozabilir.

## Ne zaman işe yarar?

Bir problemin yapısını tanımak ve uygun çözüm fikrini benzer örnekten taşımak istediğinizde.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir oran problemini benzer örnekle açacaksınız.

**Prompt**

```text
Hedef: 3 kutuda 8'er defter var, 5'i dağıtıldı; kaç kaldı?
Önce aynı işlem yapısını taşıyan, sayıları farklı bir kısa problem üret ve çöz. Sonra hangi ilişkinin ortak olduğunu tek cümleyle yaz. Ardından hedefi çöz. Örnekleri gerçek yaşanmış olay gibi anlatma; kısa işlem yeterli.
```

**Örnek çıktı**

Benzer örnek: “2 paketin her birinde 6 kalem var, toplamdan 4’ü verildi: 2×6−4=8.” Ortak yapı toplamdan çıkan miktarı düşürmek. Hedef: 3×8−5=19.

**Ne elde ettik?**

Yüzeydeki nesneden çok işlem ilişkisi taşındı.

### Orta (Medium)

**Durum**

Yanlış benzerlik ortalama hesabını bozabilir.

**Prompt**

```text
Hedef: 60 km 30 km/saat, sonra 60 km 60 km/saat; ortalama hız?
İki benzer görünen örnek üret: eşit süreli iki bölüm ve eşit mesafeli iki bölüm. Her birinde toplam yol/toplam süreyi kullanarak kısa kontrol yap.
Sonra hedefin hangisiyle yapısal olarak eşleştiğini belirt ve çöz. Sayıları sadece ortalamak yerine zaman ağırlığını kontrol et. Hatalı örnek bulursan onu kullanma.
```

**Örnek çıktı**

“Hedef eşit mesafe düzeninde: süreler 2 ve 1 saat; 120/3=40 km/saat. Eşit süre örneğindeki 45 sonucu buraya taşınamaz.”

**Ne elde ettik?**

Benzerlik kadar benzerliğin kırıldığı koşul da görüldü.

### İleri (Hard)

**Durum**

Bir kod tasarımına analoji aktarırken sınırları koruyacaksınız.

**Prompt**

```text
Hedef: Dosya yükleme tekrarında aynı taslağın iki kez oluşmasını önleyen tasarım. Koşul: Ağ yanıtı kaybolabilir; sunucu işlemi tamamlamış olabilir.
Önce iki kurgusal benzer problem üret ve çözüm fikrini yaz: aynı biletin iki kez kesilmesi; aynı sipariş numarasıyla tekrar başvuru. Her analojide ortak kimlik ve sonuç kaydının rolünü belirt.
Sonra hedefe aktarılabilen bileşenleri ve aktarılamayan varsayımları ayır. Gerçek API'nin idempotency garantisi belgelenmeden var sayma. Çıktı tasarım önerisi ve gerekli kontrol olsun; işlem çalıştırma.
```

**Örnek çıktı**

“Ortak istek kimliği ve kaydedilmiş sonuç tekrarları ayırt edebilir. Bu ancak sunucu aynı anahtar için tanımlı davranış sağlıyorsa garanti olur.”

**Ne elde ettik?**

Analoji fikir verdi; uygulama garantisinin yerine geçmedi.

## Nerede durmalı?

Few-shot örnekleri kullanıcı veya veri havuzu sağlayabilir; burada model hedefe uygun örnekleri kendisi üretir. Kurgusal örnekleri gerçek vaka kanıtı diye kullanmayın. İnsan benzetmeyle öğrenir iddiası ile modelin analogical prompting görev başarısı ayrı konulardır.

## Kaynaklar

- [Large Language Models as Analogical Reasoners](https://arxiv.org/html/2310.01714) — Yasunaga, Michihiro; Chen, Xinyun; Li, Yujia; Pasupat, Panupong; Leskovec, Jure; Liang, Percy; Chi, Ed H.; Zhou, Denny. 2023-10-03; okunan sürüm 2024-03-09. Hedef problem için ilgili örnekleri modelin üretip çözümde kullanmasını araştırır; üretilen örneklerin tarihsel doğruluk veya insan öğrenme kanıtı olduğu söylenmez. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
