# Step-Back

Ayrıntılı soruya dönmeden önce hangi genel ilkenin geçerli olduğunu bulun.

## Nedir?

Step-Back, sorudan bir adım uzaklaşıp gerekli kavramı veya genel kuralı belirler. Sonraki cevap bu ilkeyi özgün durumun koşullarıyla birleştirir. Amaç soruyu unutmak değil, ayrıntılar arasında kaybolan ilişkiyi görünür kılmaktır.

Buradaki iki çağrılı uyarlamada ilk çıktı bir ilke notudur. İkinci çağrıya özgün problemle birlikte taşınır; ilkeyi duruma uydurmak için olmayan bilgi eklenmez.

## Ne zaman işe yarar?

Bir sınır koşulu, oran veya genellenebilir kuralın belirleyici olduğu durumlarda kullanılabilir. Genel ilkenin sorunuzun koşullarında gerçekten geçerli olduğunu kontrol edin.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Kargo kodundaki tam eşik davranışını inceliyorsunuz.

**Prompt**

```text
İnsan iki çağrı yapar.
1: “En az 500 ifadesi tam 500’ü kapsar mı? Yalnız genel karşılaştırma kuralını yaz.”
2: Bu ilkeyi ve şu soruyu ekle: “500 TL ve üstü ücretsiz kargo için total > 500 doğru mu? Doğru ifadeyi ve tek sınır kontrolünü ver.”
İkinci çağrıdan sonra insan koşulu değerlendirir; kod çalıştırılmış sayılmaz.
```

**Örnek çıktı**

İlke: “en az” eşitliği kapsar. Uygulama: `total >= 500`; total=500 için ücretsiz.

**Ne elde ettik?**

Dilsel eşik ile kod karşılaştırması bağlandı. Diğer fiyat kuralları hakkında sonuç çıkmadı.

### Orta (Medium)

**Durum**

Aynı mesafeyi iki farklı hızla giderken ortalama soruluyor.

**Prompt**

```text
Çağrı 1: “Bir yolculukta ortalama hızın genel tanımını ve hangi toplamların gerektiğini tek cümlede yaz.”
Çağrı 2’ye bu yanıtı aktar: “60 km’yi 30 km/saat, sonraki 60 km’yi 60 km/saat ile gidiyorum. Mola yok. Genel tanımı kullanarak ortalama hızı kısa eşitlikle bul.”
Koordinatör toplam mesafe ve zamanı ayrı kontrol eder. İki çağrı sınırı.
```

**Örnek çıktı**

İlke: toplam mesafe / toplam süre. Süreler 2 ve 1 saat; 120/3=40 km/saat.

**Ne elde ettik?**

Hızları doğrudan ortalama hatası yerine süre hesabı görünür oldu. İlkenin uygulandığı varsayım, molanın olmamasıdır.

### İleri (Hard)

**Durum**

Duyuruda en yeni belgenin otomatik geçerli sayılmasını sorguluyorsunuz.

**Prompt**

```text
Koordinatör iki çağrı yapar.
1: “Bir yönergenin uygulanabilirliğinde tarih, kapsam ve onay durumunun rolünü kısa kontrol listesi olarak yaz. Belirli hukuk kuralı uydurma.”
2: İlkeyi şu kayıtlarla kullan: “A: 1 Eylül, onaylı, mağaza iadesi 30 gün. B: 10 Eylül, taslak, mağaza iadesi 60 gün. Soru: 12 Eylül mağaza alışverişine hangi kayıt esas alınmalı?”
Taslağı onaylı sayma. Kaynak sahibinin onay kaydı yoksa kesin uygulamayı durdur. Son cevapta kayıt kodu ve kontrol ihtiyacı olsun.
```

**Örnek çıktı**

Kapsam eşleşiyor; B’nin yeni tarihi taslak durumunu kaldırmıyor. Verilen kayıtlarda A, 30 gün. A’nın güncel onay durumu belge sahibinden teyit edilmeli.

**Ne elde ettik?**

Genel sürüm kontrolü somut kayıt seçimine uygulandı. Bu, gerçek bir mağazanın iade taahhüdü değildir.

## Nerede durmalı?

Yanlış genel ilke doğru ayrıntıları bile bozabilir. Problem çerçeveleme kartı hangi sorunu çözeceğinizi seçtirir; Step-Back aynı soruya uygun soyutlamayı arar. Ortaya çıkan ilke yeni bir kaynak veya dış doğrulama değildir.

## Kaynaklar

- [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://arxiv.org/html/2310.06117) — Zheng, Huaixiu Steven; Mishra, Swaroop; Chen, Xinyun; Cheng, Heng-Tze; Chi, Ed H.; Le, Quoc V; Zhou, Denny. 2023-10-09; okunan sürüm 2024-03-12. Soyut kavram/ilke çıkarıp özgün soruya dönme yaklaşımını inceler; PaLM-2L, GPT-4 ve Llama2-70B görev sonuçları evrensel değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
