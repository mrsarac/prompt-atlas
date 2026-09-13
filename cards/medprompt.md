# Medprompt

Yakın örnekleri seç, seçenekleri karıştır, ayrı cevapları eşleştirerek birleştir.

## Nedir?

Medprompt; dinamik few-shot örnek seçimi, örnekler için üretilip kontrol edilen gerekçeler ve seçenekleri karıştırarak ayrı cevapları birleştiren bir düzeni bir araya getirir. Özgün çalışma tıbbi soru yanıtlamadan hareket eder; burada güvenli oyuncak hesap soruları kullanılıyor.

## Ne zaman işe yarar?

Etiketli örnek havuzu, benzerlik araması, çoklu model çağrısı ve doğru cevabı bilinen değerlendirme soruları olan çoktan seçmeli görevlerde.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Küçük bir hesap sorusu için bütün akışın en sade hâlini kuracaksınız.

**Prompt**

```text
Denetleyici ve embedding modeli gerekir. Havuz örneği Q1="2 kutuda 3'er kalem: 6"; doğru etiket insan tarafından bilinir. Ayrı test sorusu Q2="3 kutuda 4'er kalem?" seçenekler 7,12,16.
Hazırlık: Q1 için kısa işlem gerekçesi üret; son cevap bilinen 6 ile eşleşmezse örneği at. Havuz sorularının embeddinglerini kaydet.
Çıkarım: Q2'ye en yakın örneği gerçek embedding benzerliğiyle seç. Bu örnek ve Q2 ile iki bağımsız çağrı yap; seçenek sırasını ikinci çağrıda değiştir. Kısa kontrol edilebilir hesap ve seçenek iste.
Denetleyici harfleri asıl cevap değerlerine geri eşlesin, oyları birleştirsin. İki oy çatışırsa çekimser kal; bütçe iki çıkarım çağrısıdır.
```

**Örnek çıktı**

Birinci çağrı B=12, karıştırılmış ikinci çağrı A=12 diyebilir. Eşleme sonrası iki cevap da 12 olur; B ve A doğrudan sayılmaz.

**Ne elde ettik?**

Yalnız seçenek harfleri değil, aynı asıl cevap için oy toplandı.

### Orta (Medium)

**Durum**

Havuzdaki gerekçe doğru etikete rağmen yanlış işlem içerebilir.

**Prompt**

```text
Havuz: Q1="600−100+40?", doğru cevap 540. Modelin temsili gerekçesi: "600−100=510; 510+40=540".
İkinci sentetik havuz kaydı Q2="400 TL’ye %25 indirim, sonra 20 TL kargo?", doğru cevap 320. Temsili gerekçe: "400 × 0,75 = 300; 300 + 20 = 320". İki gerekçe bu örnekte hazır verilmiştir; yeni hazırlık çağrısı yok.
Hazırlık denetleyicisi önce son cevapları etiketlere göre süzsün; ardından bu uyarlamada insan/arithmetic kontrolü ara işlemleri de denetlesin. Q1’in gerekçesini reddet, Q2’yi ancak işlem kontrolünden geçerse kabul et. Kabul edilmiş kayıt kalmazsa çıkarım yapmadan dur.
Test sorusu: 625 TL'ye %20 indirim; indirim sonrası 500 ve üzeri kargo 0, altı 50. Seçenekler 500,550,625.
Yalnız kabul edilmiş Q2 ile embedding indeksini kur; test sorusuyla gerçek benzerlik sorgusu yapıp top-1 Q2’yi getir. Bu örneği ve test sorusunu 3 ayrı çağrıya taşı; seçenek sıraları sırasıyla [500,550,625], [550,625,500], [625,500,550] olsun. Gerçek cevapları özgün değerlerine eşleştir ve çoğunluk yoksa belirsiz bildir. Bir embedding araması ve üç çıkarım çağrısından sonra dur.
```

**Örnek çıktı**

Q1 reddedilir; Q2’nin 300 + 20 = 320 gerekçesi kontrolü geçer ve örnek olarak seçilir. Test için temsili kontrol: “625 × 0,8 = 500; kargo 0; cevap 500.” Temsili oylar A, C, B; üçü de kendi seçenek sıralarında 500 değerine eşlenir.

**Ne elde ettik?**

Son etiketin doğru olması, açıklamanın bütün işlemlerini doğrulamadı.

### İleri (Hard)

**Durum**

Dinamik seçimde test cevabının örnek havuzuna sızmasını engelleyeceksiniz.

**Prompt**

```text
Veri yöneticisi eğitim/örnek havuzu, geliştirme ve son test sorularını ayırsın. Aynı sorunun yeniden yazılmış kopyaları da aynı bölüme gitsin.
Denetleyici: Hazırlık gerekçelerini yalnız etiketli örnek havuzunda üret ve kontrol et; embedding indeksini bu havuzdan kur. Her testte seçilen örnek kimliklerini, seçenek permütasyonunu ve gerçek cevapları sakla.
Örnek test: 18 biletin 7'si satıldı, 4 yeni bilet eklendi; seçenekler 11,15,22. Üç çıkarım çağrısında seçenekleri karıştır; değerleri geri eşleştir.
Son test sonucuna bakıp aynı test için örnek seçme kuralını ayarlama. Üç oy sonunda sonucu veya çözülemeyen uyuşmazlığı raporla; gerçek klinik karar verme.
```

**Örnek çıktı**

Temsili hesap 18 − 7 + 4 = 15. Denetim kaydı, seçilen örneklerin test sorusunu içermediğini ayrıca göstermelidir.

**Ne elde ettik?**

Birleşik yöntemin başarısı veri sızıntısıyla karıştırılmadı.

## Nerede durmalı?

Dinamik örnek seçimi ve ensemble gerçek çağrı/arama düzeni gerektirir. Aynı sohbet içinde üç doktor rolü oynatmak Medprompt değildir. Oy birliği tıbbi güvenilirlik garantisi vermez; bu kart klinik karar protokolü sunmaz. Kısa gerekçeli örnekler özgün uzun açıklama biçiminin öğretim uyarlamasıdır.

## Kaynaklar

- [Can Generalist Foundation Models Outcompete Special-Purpose Tuning? Case Study in Medicine](https://arxiv.org/html/2311.16452) — Nori, Harsha; Lee, Yin Tat; Zhang, Sheng; Carignan, Dean; Edgar, Richard; Fusi, Nicolo; King, Nicholas; Larson, Jonathan; Li, Yuanzhi; Liu, Weishung; Luo, Renqian; McKinney, Scott Mayer; Ness, Robert Osazuwa; Poon, Hoifung; Qin, Tao; Usuyama, Naoto; White, Chris; Horvitz, Eric. 2023-11-28. Dinamik few-shot seçimi, modelin ürettiği gerekçeleri doğru cevapla süzme ve choice-shuffle ensembling bileşenlerini tanımlar; buradaki aritmetik ara işlem kontrolü ek bir açık uyarlamadır. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
