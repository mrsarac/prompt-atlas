# Chain of Draft

Ara adımları uzun anlatmak yerine kısa, denetlenebilir notlarla sınırla.

## Nedir?

Chain of Draft, ara akıl yürütme metnini kısa taslaklarla tutmayı önerir. Özgün çalışmada adım başına çok az sözcük kullanma yönlendirmesi vardır. Okur için uygulanabilir karşılığı; değişken, işlem ve kontrolü kısa yazmak, gizli düşünce dökümü istememektir.

## Ne zaman işe yarar?

Basit hesap veya kısıt kontrolünde uzun açıklamalar sonucu gölgeliyorsa. Gereken açıklama derinliği her işte aynı değildir.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Üç kutudaki defterlerden bir kısmı dağıtılıyor.

**Prompt**

```text
3 kutuda 8'er defter var. 5 defter dağıtıldı. Kaç defter kaldı?
Kısa taslak biçimi kullan: yalnız gerekli işlem satırları ve son cevap. Her ara notu en fazla 5 sözcük tut. Gizli düşünce sürecini anlatma; görünen işlemler kontrol edilebilsin.
```

**Örnek çıktı**

“Toplam: 3 × 8 = 24. Kalan: 24 − 5 = 19. Cevap: 19 defter.”

**Ne elde ettik?**

Açıklama yerine hesabı denetlemek için yeterli iz kaldı.

### Orta (Medium)

**Durum**

İndirim ve kargo sırasını kısa notlarla koruyacaksınız.

**Prompt**

```text
Sepet 600 TL. Önce 100 TL kupon düşülür. İndirimli tutar 550 TL altındaysa kargo 40 TL, değilse 0 TL.
Gerekli değişkenleri kısa notlarla göster; her not en fazla 5 sözcük. Kargo eşiğini hangi tutara uyguladığını açık et. Sonunda ödenecek tutarı yaz.
```

**Örnek çıktı**

“İndirimli: 600 − 100 = 500. Eşik: 500 < 550. Kargo: 40. Ödeme: 500 + 40 = 540 TL.”

**Ne elde ettik?**

Kısalık, işlemlerin sırasını silmedi.

### İleri (Hard)

**Durum**

Bir toplantı planının koşullara uyup uymadığını denetleyeceksiniz.

**Prompt**

```text
Plan: A 09.00–09.20, B 09.20–09.35, C 09.35–09.45. Kurallar: A 20 dakika; B 15 dakika ve A'dan sonra; C 10 dakika; B en geç 09.30'da bitmeli. Çakışma olmamalı.
Her kural için en fazla 5 sözcüklük kısa kontrol notu ve geçti/kaldı etiketi ver. Hatalı koşul varsa planı uygun diye özetleme. Koşullar çelişiyorsa kısa taslağı uzatmak yerine eksikliği açıkça belirt.
```

**Örnek çıktı**

“A süre: geçti. B süre/sıra: geçti. C süre: geçti. Çakışma: yok. B son saat: kaldı, 09.35. Sonuç: uygun değil.”

**Ne elde ettik?**

Bir koşulun başarısızlığı kısa biçimde de görünür kaldı.

## Nerede durmalı?

Sözcük kısıtı, zor bir problemin gerekli ayrıntılarını kesebilir. Özgün makaledeki belirli model ve görev bulguları her modele maliyet veya doğruluk garantisi vermez. Bu yöntem CoT’nin görünür açıklamasını kısaltma fikridir; modelin erişilemeyen iç hesaplamasını denetlediğiniz anlamına gelmez.

## Kaynaklar

- [Chain of Draft: Thinking Faster by Writing Less](https://arxiv.org/html/2502.18600) — Xu, Silei; Xie, Wenhao; Zhao, Lingxiao; He, Pengcheng. 2025-02-25; okunan sürüm 2025-03-03. Kısa ara taslaklar kullanarak görünür akıl yürütme metnini sınırlama yaklaşımını tanımlar; buradaki kontroller özgün deneyin tekrarı değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
