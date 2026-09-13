# Program of Thoughts

Sayısal hesabı dil modelinden yürütücüye aktar.

## Nedir?

Program of Thoughts, sayısal akıl yürütmenin gerekli bölümünü program olarak üretip sonucu bir yorumlayıcıya hesaplatır. Model problemdeki nicelikleri programa taşır; gerçek sayısal sonucu dış yürütücü sağlar.

## Ne zaman işe yarar?

Sayısal soru yanıtlama, tekrar eden hesap ve işlem hatalarının denetlenebildiği görevlerde. Kod üretimi ve yürütme ayrı aşamalardır.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Kutulardaki kalem hesabını Python’a yaptıracaksınız.

**Prompt**

```text
Denetleyici: Kod yalnız izole Python yürütücüsünde; ağ/dosya erişimi yok, 1 saniye sınırı. Tek üretim ve tek çalıştırma.
Model görevi: 4 kutuda 5'er kalem, 3 kalem dağıtıldı. Sadece şu nicelikleri adlandıran ve sonucu print eden Python kodu üret: kutu, kutu başına kalem, dağıtılan, kalan. Gizli düşünce dökümü verme.
Uygulama kodun izinli aritmetik dışında işlem içermediğini kontrol etsin, çalıştırsın. Gerçek stdout sonraki yanıt çağrısına aktarılsın; araç yoksa hesap çalıştırıldı deme. Sonucu birimiyle bildirip dur.
```

**Örnek çıktı**

Kod adayı: `boxes=4; per_box=5; given=3; print(boxes*per_box-given)`. Temsili stdout: `17`. Son cevap: “17 kalem.”

**Ne elde ettik?**

Sayısal sonuç, kodun yazılmasıyla değil gerçekten yürütülmesiyle elde edilecek biçimde kuruldu.

### Orta (Medium)

**Durum**

Para hesabında kuruş kullanarak belirsiz yuvarlamayı azaltacaksınız.

**Prompt**

```text
Girdi: 3 ürün, birim fiyat 80 TL; ürünlere %25 indirim; kargo 20 TL.
Model yalnız hesap bölümünü Python olarak yazsın. Birim kuruş: fiyat 8000, kargo 2000; indirimli ara toplamın bu örnekte tam kuruş olduğunu kontrol et. Sonucu kuruş olarak print et.
Denetleyici izole yürütücüde kodu çalıştırsın; gerçek çıktıyı görevle birlikte son çağrıya taşısın. Son çağrı TL'ye çevirip kısa yanıtlasın. İzin dışı kod veya yürütme hatasında dur; en fazla bir hesap çalıştırma.
```

**Örnek çıktı**

Kod adayı: `subtotal=3*8000*75//100; print(subtotal+2000)`. Temsili çıktı: `20000`, yani 200 TL.

**Ne elde ettik?**

Dil modeli kuralları programa çevirdi; aritmetik ve birim dönüşümü denetlenebilir kaldı.

### İleri (Hard)

**Durum**

Tam kesir gerektiren bir ifadede ondalık hata istemiyorsunuz.

**Prompt**

```text
Görev: 8 / (3 - 8/3) ifadesini tam kesirle hesapla.
Denetleyici Python'da yalnız fractions.Fraction ve temel aritmetiğe izin versin; ağ/dosya yok. Model pay/payda yapısını aynen taşıyan kod üretsin; sıfıra bölme ve yürütme hataları ayrı sonuç olsun.
Uygulama kodu ve gerçek stdout/stderr'i saklasın. Son çağrı yalnız başarılı yürütme sonucundan cevaplasın. Ardından insan ifadenin kodla aynı parantez yapısında olduğunu kontrol etsin; farklıysa doğru stdout bile görevin cevabı sayılmasın. Bir çalışma sonunda dur.
```

**Örnek çıktı**

Kod adayı: `from fractions import Fraction; print(Fraction(8)/(3-Fraction(8,3)))`. Temsili stdout: `24`.

**Ne elde ettik?**

Hesap doğruluğunun yanında sorunun programa doğru aktarılması da kontrol edildi.

## Nerede durmalı?

Yürütücü doğru yazılmış yanlış problemi kusursuz hesaplayabilir. PAL de program yürütmeden yararlanır; Program of Thoughts özellikle sayısal hesabı dilsel görevden ayırmayı öne çıkarır. Kod yazdırmak tek başına iki yöntemin de gerçek yürütme kısmı değildir. Güvenli çalıştırma ortamı uygulamanın sorumluluğudur.

## Kaynaklar

- [Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks](https://arxiv.org/html/2211.12588) — Chen, Wenhu; Ma, Xueguang; Wang, Xinyi; Cohen, William W.. 2022-11-22; okunan sürüm 2023-10-23. Sayısal hesaplamayı üretilen program ve dış yürütücüye devreden yaklaşımı tanımlar; örnek kodlar burada öğretim amaçlıdır. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
