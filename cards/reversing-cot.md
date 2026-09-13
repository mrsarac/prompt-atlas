# Reversing Chain-of-Thought

Çözümün hangi soruyu varsaydığını geriye doğru kur ve asıl soruyla karşılaştır.

## Nedir?

Reversing Chain-of-Thought, üretilen çözümden bir problem yeniden kurar; bunu özgün problemle karşılaştırarak olgu uyuşmazlıklarını bulmaya çalışır. RCOT adıyla sunulan yöntem, dış kaynak doğrulaması değildir.

## Ne zaman işe yarar?

Bir çözümde sayı, ilişki veya koşulun yanlış okunmuş olabileceği durumlarda. Özellikle çözüm akıcı olduğu için girişteki farkın gözden kaçtığı hesaplarda.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Çözüm doğru hesaplıyor ama yanlış sayıyı kullanıyor.

**Prompt**

```text
İnsan denetleyici olsun. Özgün soru: 4 kutuda 5'er kalem var; 3 kalem dağıtıldı. Kaç kaldı?
Çözüm adayı: "4×5=20; 20−2=18".
1. Ayrı çağrıya yalnız çözüm adayını ver: Bu işlemlerin varsaydığı soruyu kısa biçimde yeniden kur. Asıl soruyu bu çağrıya gösterme.
2. Karşılaştırma çağrısına özgün soru ve gerçek yeniden kurulan soruyu ver; değişen olguyu bul.
3. Düzeltme çağrısına özgün soru ve bulunan farkı aktar. Bir düzeltme sonunda dur; kısa işlem yeterli.
```

**Örnek çıktı**

Yeniden kurulan soru 2 kalemin dağıtıldığını varsayar. Fark: özgün sayı 3. Revizyon: “20 − 3 = 17.”

**Ne elde ettik?**

İşlem hatası olmayan bir çözümdeki yanlış girdi ortaya çıktı.

### Orta (Medium)

**Durum**

İndirim ve kargo eşikleri farklı sırada uygulanmış.

**Prompt**

```text
Özgün soru: 600 TL sepetten 100 TL düşülür; indirimli tutar 550 altındaysa 40 TL kargo.
Çözüm adayı: "600≥550, kargo yok; 600−100=500."
Denetleyici üç ayrı çağrı kullansın: yalnız çözümden varsayılan problemi kur; bu sonucu özgün soruyla karşılaştır; saptanan farkla çözümü düzelt.
Her aşamanın gerçek çıktısını kimlikle sakla. Yeniden kurma çağrısı bilinmeyen koşulu uydurmasın; yalnız çözümde görünen eşik uygulamasını tarif et. En fazla 3 çağrıda dur.
```

**Örnek çıktı**

“Çözüm, kargo eşiğini indirim öncesi tutara uyguluyor. Özgün koşul indirim sonrası. Düzeltme: 500 + 40 = 540 TL.”

**Ne elde ettik?**

Yanlışlık yalnız sonuç sayısında değil, varsayılan kuralda bulundu.

### İleri (Hard)

**Durum**

Geriye kurulan problem tek olmayabilir.

**Prompt**

```text
Özgün soru: 23 kişi, her masada en fazla 6 kişi; gereken en az masa sayısı?
Çözüm adayı yalnız "4" yazıyor; işlem veya kısıt yok.
1. Ters kurma çağrısına yalnız bu cevabı ver. Prompt: Bu cevaptan özgün problemi tekil olarak çıkarabilir misin? Kanıtlanmayan sayı veya ilişki üretme.
2. Denetleyici yetersiz bilgi sonucunu özgün soruyla bir kontrol çağrısına taşısın. Cevabı doğrulamak için gerekli görünür ilişkiyi ayrıca iste: 3 masa kapasitesi ve 4 masa kapasitesi.
Ters kurma başarısızlığını çözüm doğruluğunun kanıtı sayma. En fazla iki çağrı; açık kontrol sonucu yoksa belirsiz de.
```

**Örnek çıktı**

“Yalnız 4’ten problem yeniden kurulamaz. Ayrı kontrol: 3×6=18 < 23; 4×6=24 ≥ 23, dolayısıyla 4 masa gerekir.”

**Ne elde ettik?**

Yöntemin bilgi yetersizliğinde çalışmadığı sınır açıkça görüldü.

## Nerede durmalı?

Yeniden kurulan sorunun aslına benzemesi çözümün doğru olduğuna yetmez. Aynı model iki aşamada aynı yanlışı koruyabilir. Yöntem yeni bağımsız kanıt getirmez; CRITIC gibi araçlı doğrulama veya gerçek hesap kontrolüyle aynı değildir.

## Kaynaklar

- [RCOT: Detecting and Rectifying Factual Inconsistency in Reasoning by Reversing Chain-of-Thought](https://arxiv.org/html/2305.11499) — Xue, Tianci; Wang, Ziqi; Wang, Zhenhailong; Han, Chi; Yu, Pengfei; Ji, Heng. 2023-05-19; okunan sürüm 2023-10-02. Çözümden problemi yeniden kurup özgün problemle olgusal tutarlılığı karşılaştıran RCOT düzenini tanımlar; aritmetik veri kümelerindeki sonuçlar tüm doğrulama işlerine genellenmez. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
