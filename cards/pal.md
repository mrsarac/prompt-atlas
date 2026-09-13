# PAL

Model programı kursun; sayısal cevabı gerçek yorumlayıcı hesaplasın.

## Nedir?

PAL, doğal dildeki problemi program olarak ifade ettirir ve o programı bir yorumlayıcıda çalıştırır. Model doğru değişkenleri ve işlemleri seçmelidir; gerçek hesaplamayı Python gibi dış bir yürütücü yapar.

Kod bloğunun sohbet içinde görünmesi çalıştırıldığı anlamına gelmez. Başlatıcı, üretilen kodu inceleyen kişi veya uygulamadır. İzinli bir çalışma ortamı ve hata çıktısının korunması gerekir.

## Ne zaman işe yarar?

Çok adımlı hesap, sayma ve sembolik işlemlerde kullanılabilir. Çalıştırılacak kodun ağ, dosya veya başka yan etki gerektirmediğini kontrol ederek başlayın.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Kalem sayısını programla hesaplayacaksınız.

**Prompt**

```text
Model çağrısı: “Dört kutuda beşer kalem var; üçü veriliyor. Python’da yalnız sabit sayılar ve aritmetik kullan; sonucu print et. Dosya/ağ erişimi isteme.”
İnsan kodu inceler, izinli Python yorumlayıcısında bir kez çalıştırır. Hata varsa sonucu kabul etmez. Temsili üretilen program:
print(4 * 5 - 3)
Gerçek stdout okunmadan model çıktısı hesap sonucu diye sunulmaz.
```

**Örnek çıktı**

Temsili program çıktısı: `17`. Birim: kalem.

**Ne elde ettik?**

Hesaplanacak program açık. Kendi çalıştırmanızın stdout kaydı, programın gerçekten yürütüldüğünü gösterir.

### Orta (Medium)

**Durum**

İndirimli ürün ve kargo toplamını kuruşla hesaplamak istiyorsunuz.

**Prompt**

```text
Modelden şu iş için Python programı iste: “Tanesi 80 TL üç ürün, ürün toplamına %25 indirim, ardından 20 TL kargo. Hesabı kuruş tamsayılarıyla yap. Yalnız print çıktısı üret.”
İnsan kodu inceleyip yorumlayıcıda çalıştırır; bir çağrı ve bir çalıştırma sınırı.
Temsili program:
subtotal = 3 * 8000
payable = subtotal * 75 // 100 + 2000
print(payable)
Sonucun kuruş olduğunu koru; hata çıktısını ücret sanma.
```

**Örnek çıktı**

Temsili stdout: `20000`; karşılığı 200 TL.

**Ne elde ettik?**

Birim ve hesap sırası programda görülebiliyor. Kesirli kuruş oluşan başka tutarlarda yuvarlama kuralını ayrıca belirlemek gerekir.

### İleri (Hard)

**Durum**

Bir listede mükerrer başvuruları ayırıp kapasiteyi kontrol edeceksiniz.

**Prompt**

```text
Model çağrısı: “Başvurular ['A','B','A','C','D','B']; kapasite 3. Kimlikler harf duyarlı. İlk görünme sırasını koruyarak tekilleştir; ilk üçü aday, kalanı bekleme listesi. Python kodu yaz; dosya/ağ yok.”
İnsan yalnız bu veri üzerinde kodu çalıştırır. Temsili program:
ids = ['A','B','A','C','D','B']
unique = list(dict.fromkeys(ids))
print({'aday': unique[:3], 'bekleme': unique[3:]})
Kontrol: hiçbir kimlik iki listede olamaz, toplam 4 benzersiz kimlik olmalı. Hata varsa onay e-postası üretme. Bir üretim ve bir yürütme sonunda dur.
```

**Örnek çıktı**

Temsili çıktı: `{'aday': ['A', 'B', 'C'], 'bekleme': ['D']}`.

**Ne elde ettik?**

Hesap ile gerçek kayıt onayı ayrıldı. Kimliklerin aynı kişiyi temsil edip etmediğini ve seçim kuralının yetkili olup olmadığını insan doğrular.

## Nerede durmalı?

Yorumlayıcı yanlış kurulmuş problemi doğru hesaplayabilir. Kod incelemesi ve beklenen davranış kontrolü bu yüzden önemlidir. Program of Thoughts yakın bir programla hesaplama yaklaşımıdır; PAL adı altında bütün kod üreten yöntemlerin aynı deney olduğu söylenmez.

## Kaynaklar

- [PAL: Program-aided Language Models](https://arxiv.org/html/2211.10435) — Gao, Luyu; Madaan, Aman; Zhou, Shuyan; Alon, Uri; Liu, Pengfei; Yang, Yiming; Callan, Jamie; Neubig, Graham. 2022-11-18; okunan sürüm 2023-01-27. Problemi programla ifade edip dış yorumlayıcıyla yürütme mekanizmasını destekler; özgün dil/arithmetic görevleri bu Türkçe programların çalıştırma makbuzu değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
