# Self-Consistency

Aynı soruya ayrı örneklemeler alın; son cevapları ortak biçimde sayın.

## Nedir?

Self-Consistency, bir modelin tek cevabını tekrar okutmak yerine aynı problem için farklı örneklenmiş çözümler üretir. Son cevaplar ortak biçime getirilir ve en sık görülen cevap seçilir. Özgün yöntem, çeşitlilik üreten örnekleme ve toplulaştırma gerektirir.

Çağrılar birbirlerinin cevaplarını görmeden başlamalıdır. Aynı modelden gelebilirler; bu onları bağımsız bilgi kaynakları yapmaz. Bir sohbet içinde “üç uzman gibi düşün” yazmak bu işlemi kurmaz.

## Ne zaman işe yarar?

Son cevapların karşılaştırılabilir olduğu sayı, seçenek veya kısa etiket görevlerinde kullanın. İnsan ayrı sohbetler açabilir; otomasyonda örnekleme ayarlarına ve çağrı bütçesine erişen bir koordinatör gerekir.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Aynı kalem hesabı için üç ayrı cevap alacaksınız.

**Prompt**

```text
Koordinatör üç ayrı örnekleme çağrısına aynı girdiyi verir; yanıtları aralarında paylaşmaz:
“Dört kutuda beşer kalem var; üçü veriliyor. Kısa kontrol eşitliği ve son kalem sayısını yaz.”
Örnekleme destekleniyorsa farklı örnekler üretmeye izin veren ayar kullan; kopyalanmış tek yanıtı çoğaltma.
Son cevapları tam sayı olarak oku, en sık olanı say. Eşitlikte sonuç seçme. Üç çağrı sonunda hesabı dışarıda kontrol et.
```

**Örnek çıktı**

Temsili ayrı sonuçlar: 17, 17, 23. Sayım: 17 iki kez, 23 bir kez. Seçilen aday: 17.

**Ne elde ettik?**

Bir aday oy sıklığıyla seçildi. Doğruluğunu 4×5−3 hesabı gösterir; oy tek başına ispat değildir.

### Orta (Medium)

**Durum**

Aynı para tutarı farklı biçimlerde yazılabiliyor.

**Prompt**

```text
Beş ayrı çağrıya şu soruyu ver: “3 ürünün tanesi 80 TL. Ürünlere %25 indirim, sonra 20 TL kargo. Toplam nedir? Para birimiyle yaz.”
Koordinatör yalnız son tutarı normalize eder: 200 TL ve 200,00 TL aynı değerdir. Birimi farklı veya ayrıştırılamayan yanıtı geçersiz işaretle; sessizce dönüştürme.
En sık tutarı, geçerli/geçersiz yanıt sayısıyla raporla. En fazla beş çağrı; beraberlikte insan kontrolü.
```

**Örnek çıktı**

Temsili sonuçlar: 200 TL, 200,00 TL, 200 TL, 195 TL, “bilmiyorum”. Geçerli 4, geçersiz 1; 200 TL üç kez görülüyor.

**Ne elde ettik?**

Biçim farkının oyları bölmesi önlendi. Geçersiz örneklerin saklanması, seçimin neye dayandığını gösteriyor.

### İleri (Hard)

**Durum**

Eksik bir kuralda çoğunluk aynı varsayımı yapabilir.

**Prompt**

```text
Koordinatör beş ayrı çağrı yapar:
“Ürün 600 TL, indirim 100 TL, ücretsiz kargo eşiği 550 TL; ücretli kargo 40 TL. Eşiğin indirim öncesi/sonrası uygulandığı belirtilmiyor. Sonuç ve zorunlu varsayımı yaz.”
Cevap sınıfları: 500, 540, eksik-kural. Sayımı sakla. Çoğunluk kesin tutar söylese bile özgün sorudaki kural boşluğunu insan ayrıca denetler.
Beş çağrıdan sonra dur; eksik kural çözülmeden ödeme hesabını kesinleştirme.
```

**Örnek çıktı**

Temsili sonuçlar: 500, 500, 500, 540, eksik-kural. En sık cevap 500; kabul kararı yine beklemede, çünkü eşik tabanı verilmemiş.

**Ne elde ettik?**

Örnekleme ile kabul kontrolü ayrıldı. Ortak varsayım hatasının çoğunlukla güçlenebileceği görünür oldu.

## Nerede durmalı?

En sık cevabın payı kalibre güven olasılığı değildir; mutlaka yüzde 50 üstü oy da özgün yöntemin genel şartı değildir. Beraberlik ve geçersiz yanıt politikası uygulamanıza aittir. Multiagent Debate ilk bağımsız yanıtlardan sonra karşılıklı geri bildirim ekler.

## Kaynaklar

- [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/html/2203.11171) — Wang, Xuezhi; Wei, Jason; Schuurmans, Dale; Le, Quoc; Chi, Ed; Narang, Sharan; Chowdhery, Aakanksha; Zhou, Denny. 2022-03-21; okunan sürüm 2023-03-07. Çeşitli çözüm örneklemelerinin son cevap üzerinden birleştirilmesini destekler; model ve görev koşullarına bağlı bulgular sunar. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
