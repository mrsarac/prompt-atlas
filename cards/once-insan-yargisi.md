# Önce insanın yargısı

Önce kendi yargını kaydet, sonra modelin önerisiyle karşılaştır.

## Nedir?

Önce insan yargısı, model önerisini görmeden bir ilk cevap veya karar gerekçesi yazma düzenidir. Amaç otomatik kabule ara vermektir. Bu, insanın ilk cevabını değişmez doğru ilan etmek değildir.

## Ne zaman işe yarar?

Modelin akıcı cevabına kolayca uyduğunuzu fark ettiğiniz, kendi kontrolünüzü korumak istediğiniz işlerde.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir sınır hesabını modelden önce yapacaksınız.

**Prompt**

```text
Kural: 500 TL ve üzeri kargo ücretsiz, altı 50 TL. Soru: 500 TL'de kargo?
Önce cevabı söyleme; benim kendi yanıtımı ve kısa dayanağımı yazmamı iste. Ben yanıtlayınca ayrı olarak kendi cevabını ver ve fark varsa kurala bağla. İlk yargımı sonradan değiştirilmiş gibi yeniden yazma.
```

**Örnek çıktı**

İnsan: “50, çünkü 500’den büyük değil.” Model: “Kural ‘ve üzeri’ diyor; 500 dahil, kargo 0. İlk yanıtındaki sınır yorumu değişmeli.”

**Ne elde ettik?**

İlk düşünce görünür kaldı; düzeltme kaynağa bağlandı.

### Orta (Medium)

**Durum**

Bir metindeki iddianın desteklenip desteklenmediğini kontrol edeceksiniz.

**Prompt**

```text
Kaynak: "Beş katılımcının üçü sabahı tercih etti." İddia: "Bütün katılımcılar sabah istiyor."
Önce benim destekleniyor/desteklenmiyor yargımı ve alıntımı bekle. Sonra model değerlendirmesini göster. Anlaşmazlık varsa çoğunluk veya model güveniyle değil, kaynak kapsamıyla çöz.
Bir karşılaştırma turu sonunda ilk yargı, model yargısı ve kaynakla son karar alanlarını ayrı yaz.
```

**Örnek çıktı**

“İlk yargı: destekleniyor. Model: desteklenmiyor. Kaynakla son karar: üç kişinin tercihi bütün gruba genellenemez.”

**Ne elde ettik?**

Karar değişiminin nedeni model otoritesi değil, kapsam kontrolü oldu.

### İleri (Hard)

**Durum**

İnsan da model de aynı yanlış varsayımı paylaşabilir.

**Prompt**

```text
Karar: Kurgusal hizmet bugün çalışıyor mu? Veri: Dün 18.00'de çalışıyordu; canlı kayıt yok.
Önce insan ilk yargısını yerel notuna yazsın; model yanıtını sonra alsın. Model görevi: mevcut verinin zaman sınırını ve gereken kontrolü belirt.
Denetleyici ilk insan ve model cevabını ayrı saklasın. İkisi de "çalışıyor" dese bile uzlaşıyı dış kanıt sayma; bugüne ait gözlem gerektiğini kontrol listesine koy.
Canlı araç yoksa son karar doğrulanamadı olsun. Tek karşılaştırma turunda dur; yapılmayan kontrolü tamamlanmış sayma.
```

**Örnek çıktı**

“İnsan-model anlaşması olabilir; bugünkü durum yine doğrulanmış değildir.”

**Ne elde ettik?**

İlk yargı düzeni, ortak hataya karşı ayrıca kaynak kontrolüyle tamamlandı.

## Nerede durmalı?

İnsan önce düşününce her zaman daha doğru karar verir denemez. Bu tasarım ek zihinsel yük getirebilir. Buçinca ve arkadaşlarının çalışması belirli bir AI destekli karar görevidir, LLM prompting deneyi değildir; daha az aşırı güven ile genel ekip performansı aynı sonuç değildir.

## Kaynaklar

- [To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making](https://arxiv.org/html/2102.09692) — Buçinca, Zana; Malaya, Maja Barbara; Gajos, Krzysztof Z.. 2021-02-19. Cognitive forcing düzenlerinin AI önerisine aşırı güven ve kullanılabilirlik üzerindeki etkilerini inceler; LLM olmayan, belirli karar bağlamındaki bulgular bu uyarlamaya doğrudan başarı garantisi vermez. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
