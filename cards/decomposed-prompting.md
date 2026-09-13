# Decomposed Prompting

Alt işleri isimli işleyicilere yönlendir, sonuçlarını bir program gibi taşı.

## Nedir?

Decomposed Prompting, bir problemi alt görevlere ayıran bir ayrıştırıcı ile bu görevleri çözen yeniden kullanılabilir işleyiciler kurar. Denetleyici, üretilen çağrı sırasını gerçekten yürütür ve ara cevapları sonraki adıma bağlar.

## Ne zaman işe yarar?

Aynı alt görevlerin farklı sorularda tekrarlandığı, görev türüne göre farklı prompt veya araç gerektiği durumlarda.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

İsim listesini alfabetik düzenleyeceksiniz.

**Prompt**

```text
Denetleyici iki işleyici tanımlasın: split_names metni isim listesine çevirir; sort_names listeyi verilen basit Latin harf sırasına göre sıralar. İkisi ayrı prompt çağrısıdır.
Girdi: "Cem, Ada, Bora".
Ayrıştırıcı çağrısı yalnız izinli işleyicilerden program üretsin: v1=split_names(girdi); v2=sort_names(v1); return v2.
Uygulama işleyici adlarını denetlesin, gerçek v1/v2 çıktısını saklasın. Ad eklenmesi veya kaybolması durumunda dur. En fazla 1 ayrıştırma + 2 işleyici çağrısı.
```

**Örnek çıktı**

v1: [Cem, Ada, Bora]. v2: [Ada, Bora, Cem]. Denetleyici return v2 ile biter.

**Ne elde ettik?**

Alt görev isimleri ve aralarındaki veri aktarımı açık hâle geldi.

### Orta (Medium)

**Durum**

Belge okuma ve hesaplama farklı yetenekler gerektiriyor.

**Prompt**

```text
Girdi D1="3 paket, pakette 8 defter; 5 defter dağıtıldı". Soru: kalan defter?
İzinli işleyiciler: extract_quantities(D1) ayrı model çağrısı; calculate(expression) izole aritmetik aracı.
Ayrıştırıcı önce sayıları ve ilişkileri ayıklayan, sonra gerçek ara sonuçtan ifade kurup hesaplayan program üretsin. Denetleyici araç adlarını ve şemayı doğrulasın; yalnız mevcut değişkenlere başvuruya izin versin.
extract dönüşü: {packs:3,per_pack:8,given:5}; calculate girdisi 3*8-5. Gerçek hesap sonucunu son cevaba taşı. Her işleyici bir kez; hata veya eksik alan varsa dur.
```

**Örnek çıktı**

Program akışı ayıklama → hesap → cevap olur. Temsili sonuç 19 defterdir.

**Ne elde ettik?**

Metin anlama ile aritmetik farklı işleyicilere verildi.

### İleri (Hard)

**Durum**

Bir alt görev tekrar kullanılacak; denetleyici döngüyü sınırlandırmalı.

**Prompt**

```text
Soru: A ve B etkinliklerinin toplam kapasitesi nedir?
Kaynak: D1="A kapasite 8"; D2="B kapasite 12". İşleyiciler lookup_capacity(event,document), add_numbers(values).
Ayrıştırıcı iki lookup ve bir add programı üretsin. Denetleyici her çağrıyı kimlik, girdi, çıktı, kaynakla saklasın; A'nın sonucu B'nin kaynağı yerine geçmesin. Aynı girdi/kaynak çifti tekrar istenirse doğrulanmış ara sonucu kullanabilir.
Bilinmeyen işleyici, ileriye referans veya toplam 4 adımı aşan program reddedilsin. Kaynakta kapasite yoksa toplama çağrısı çalışmasın. Başarılı toplamda kaynak kimlikleriyle bitir.
```

**Örnek çıktı**

“A: 8 [D1]; B: 12 [D2]; toplam 20.” Eksik B kaydında toplam yerine eksik veri bildirimi gelir.

**Ne elde ettik?**

Modülerlik, kontrolsüz araç çağrıları yerine denetlenebilir bir program yapısına bağlandı.

## Nerede durmalı?

Prompt chaining baştan belirlenen aşamaları yürütür; Decomposed Prompting ayrıştırıcı ve tekrar kullanılabilir görev işleyicilerini öne çıkarır. Ayrı roller yazmak işleyici yürütmek değildir. Gerçek çağrı düzeni, değişken aktarımı ve izin kontrolü gerekir.

## Kaynaklar

- [Decomposed Prompting: A Modular Approach for Solving Complex Tasks](https://arxiv.org/html/2210.02406) — Khot, Tushar; Trivedi, Harsh; Finlayson, Matthew; Fu, Yao; Richardson, Kyle; Clark, Peter; Sabharwal, Ashish. 2022-10-05; okunan sürüm 2023-04-11. Ayrıştırıcının alt görev/işleyici çağrılarından oluşan prompting programları üretmesini ve denetleyicinin bunları yürütmesini tanımlar. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
