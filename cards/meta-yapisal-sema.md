# Meta Prompting: yapısal şema

Çözülmüş içerik örnekleri yerine görevin yapısını gösteren bir şema verin.

## Nedir?

Zhang ve arkadaşlarının Meta Prompting yaklaşımı, görevin biçimini ve dönüşümlerini öne çıkarır. Hangi tür girdinin hangi tür ara sonuca, oradan hangi çıktıya dönüşeceğini yazarsınız. Şema belirli bir çözülmüş örneğin içeriğine bağımlı olmak zorunda değildir.

Burada bu yaklaşımı kısa görev şemalarıyla uyarlıyoruz. Makaledeki biçimsel yapının korunması, anlamsal doğruluk veya her revizyonda iyileşme garantisi değildir. Okunan sürümdeki recursive düzen ayrıca önerici, şema doğrulayıcı ve yürütücü içerir.

## Ne zaman işe yarar?

Benzer yapıda farklı girdileri işleyen görevlerde kullanın. Girdi ve çıktı türlerini, izinli dönüşümleri ve kontrol koşullarını açıkça yazabilmelisiniz.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir aritmetik problemi örnek çözüm göstermeden düzenleyeceksiniz.

**Prompt**

```text
Görev şeması:
Girdi → başlangıç miktarı, eklenen, çıkarılan, birim.
Dönüşüm → başlangıç + eklenen − çıkarılan.
Kontrol → birimler aynı mı, sonuç anlamlı mı?
Çıktı → kısa eşitlik ve birimli sonuç.
Girdi: 18 kitap vardı, 4 eklendi, 7 alındı. Şemayı uygula; gizli düşünce dökümü istemiyorum.
```

**Örnek çıktı**

18+4−7=15 kitap; miktarların birimi aynı.

**Ne elde ettik?**

İçerik örneği olmadan hesap yapısı verildi. Sayısal sonuç ayrıca kontrol edilebilir.

### Orta (Medium)

**Durum**

Bir metinden koşullu işlem bilgisi çıkaracaksınız.

**Prompt**

```text
Şema: olay → önkoşul → izinli sonuç → eksik bilgi.
Kural: önkoşul gerçekleştiği açık değilse sonucu olmuş gibi yazma.
Girdi: “Başvuru formu gönderildi. Yer ancak onay e-postası gelince kesinleşir. E-posta henüz gelmedi.”
Şema alanlarını doldur ve tek cümlelik sonuç ver. Kaynakta olmayan süre ekleme.
```

**Örnek çıktı**

Olay: form gönderildi. Önkoşul: onay e-postası. İzinli sonuç: başvuru alındı, kesin kayıt henüz yok. Eksik bilgi: onayın ne zaman geleceği.

**Ne elde ettik?**

İşlem yapısı tamamlanmış sonuçtan ayrıldı. Şemadaki alanın dolu olması kaynak iddiasını doğrulamaz.

### İleri (Hard)

**Durum**

Şema sürümü otomatik değiştirilecek; her öneri uygulanmamalı.

**Prompt**

```text
Koordinatör için sade recursive şema uyarlaması:
Başlangıç şeması: girdi, kaynak, sonuç. Görev: “K1 kapasite 16; K2 kapasite bilinmiyor” notlarını özetlemek.
Önerici çağrısı: yalnız “belirsizlik” alanını ekleyen bir değişiklik öner.
Yazılım doğrulayıcı: yalnız izinli alan eklenebilir; kaynak alanı silinemez. Geçersiz değişiklik reddedilir.
Yürütücü ayrı çağrıda onaylı şema ve özgün notlarla cevap verir. İnsan K2’nin boşluğunun korunmasını denetler.
Bir öneri ve bir yürütme; doğrulayıcı yoksa otomatik şema uygulama. Bu taslak özgün bütün MP-CR deneyini yeniden kurmaz.
```

**Örnek çıktı**

Kabul edilebilir şema: girdi, kaynak, sonuç, belirsizlik. K2 için kapasite belirtilmemiş. “kaynak alanını sil” değişikliği doğrulayıcıdan geçmemeli.

**Ne elde ettik?**

Şema revizyonu ile görevi çözme ayrı aşamalar oldu. Biçim doğrulayıcı, cevabın anlamını insan yerine denetlemiş sayılmaz.

## Nerede durmalı?

Bu “meta” kullanımı uzman çağrılı Meta-Prompting’den farklıdır. RUNE’un katman adlarıyla da aynı formalizasyon değildir. Şema mantıklı görünse bile yanlış ilişki kurabilir; özgün veriye dönüş kontrolünü koruyun.

## Kaynaklar

- [Meta Prompting for AI Systems](https://arxiv.org/html/2311.11482) — Zhang, Yifan; Yuan, Yang; Yao, Andrew Chi-Chih. 2023-11-20; okunan sürüm 2026-08-03. Görev yapısını içerik örneklerinden ayıran Meta Prompting ve okunan 3 Ağustos 2026 sürümündeki recursive şema düzenini destekler; formalizasyon doğruluk/yakınsama garantisi değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
