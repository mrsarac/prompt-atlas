# CRITIC

Eleştiriyi dış araç sonucuna bağla, sonra cevabı düzelt.

## Nedir?

CRITIC, ilk cevabı araçlarla kontrol ettirip gelen geri bildirime göre düzeltir. Araç; arama, kod yürütme veya göreve uygun başka bir dış kontrol olabilir. Yalnız “kendini eleştir” demek yöntemin araç destekli kısmını karşılamaz.

## Ne zaman işe yarar?

Bir cevabın doğruluğunu dışarıdan kontrol edebileceğiniz hesap, kod veya kaynaklı bilgi işlerinde.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

İlk cevapta bir toplama hatası var.

**Prompt**

```text
İnsan denetleyici olsun. Soru: 4 kutuda 5'er kalemden 3 kalem alındı; kaç kaldı? İlk cevap adayı: 18.
Kontrol çağrısı: Cevabı doğrulamak için hesaplayıcıya verilecek tek ifadeyi yaz; araç sonucunu tahmin edip gerçekmiş gibi sunma.
Uygulama calculator("4*5-3") çalıştırsın; gerçek dönüşü kontrol çağrısına eklesin.
Düzeltme çağrısı soruyu, ilk cevabı ve gerçek araç sonucunu alsın; yanlış alanı ve düzeltilmiş cevabı kısaca yazsın. Bir araç kontrolü ve bir revizyonda dur.
```

**Örnek çıktı**

Temsili araç sonucu 17; revizyon: “18 yanlıştı. 4 × 5 − 3 = 17 kalem.”

**Ne elde ettik?**

Düzeltme modelin ikinci tahminine değil, hesap kontrolüne bağlandı.

### Orta (Medium)

**Durum**

Bir kaynaklı cevap yanlış günü söylüyor.

**Prompt**

```text
Soru: Kurgusal Kent Müzesi pazartesi açık mı? İlk aday: "Evet, her gün açık."
Denetleyici yalnız resmi saat kaydını okuyan araca izin versin; en fazla 2 okuma. Temsili dönüş D1: "Pazartesi kapalı; salı-pazar 10.00–18.00", güncelleme 1 Eylül 2026.
Eleştiri çağrısı ilk iddiayı D1 ile karşılaştırsın; hangi kısmın çeliştiğini yazsın. Revizyon çağrısı bu eleştiriyi ve D1'i alıp cevabı düzeltsin.
Araç başarısızsa "kontrol edildi" deme; doğrulanamadığını söyle ve dur. Geçerli sonuçta bir revizyon yeterli.
```

**Örnek çıktı**

“Her gün açık ifadesi D1 ile çelişiyor. 1 Eylül tarihli kayda göre pazartesi kapalı.”

**Ne elde ettik?**

Kaynak kontrolü, eleştirinin somut dayanağı oldu.

### İleri (Hard)

**Durum**

Kod düzeltmesinin yeni bir sınır hatası üretip üretmediği kontrol edilecek.

**Prompt**

```text
Görev: 500 ve üzeri ücretsiz, altı 50 TL kargo. İlk kod total > 500 ? 0 : 50.
Denetleyici yalnız izole test aracı sunsun; dış dosyaya yazma yok. Test girdileri 499,500,501; beklenen 50,0,0. Gerçek test dönüşlerini sakla.
Eleştiri çağrısı başarısız girdiyi ve nedenini kısa yazsın. Revizyon çağrısı en küçük kod değişimini üretsin. Aynı testler yeni aday üzerinde gerçekten yeniden çalışsın.
En fazla 2 test turu/1 revizyon. İkinci tur başarısızsa yeni başarı iddiası yerine kalan hatayı raporla. Test yoksa sadece öneri de.
```

**Örnek çıktı**

Temsili ilk sonuç 50,50,0; `>=` revizyonu sonrası beklenen 50,0,0. Bunlar bu kartta çalıştırılmış model/araç kayıtları değildir.

**Ne elde ettik?**

Düzeltmenin işe yaradığı da ayrı araç kontrolüne bağlandı.

## Nerede durmalı?

Aracın kendisi, kaynak seçimi veya test kapsamı yanlış olabilir. CRITIC, Self-Refine’dan dış geri bildirim kullanımıyla ayrılır. Chain-of-Verification doğrulama soruları kurar; CRITIC araç destekli eleştiri ve revizyon döngüsünü öne çıkarır.

## Kaynaklar

- [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/html/2305.11738) — Gou, Zhibin; Shao, Zhihong; Gong, Yeyun; Shen, Yelong; Yang, Yujiu; Duan, Nan; Chen, Weizhu. 2023-05-19; okunan sürüm 2024-02-21. İlk model çıktısının araç etkileşimlerinden gelen geri bildirimle eleştirilip düzeltilmesini tanımlar; araçsız öz eleştiriyle eş tutulmaz. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
