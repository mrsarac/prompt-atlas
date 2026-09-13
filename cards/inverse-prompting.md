# Inverse Prompting

Üretilen metnin başlangıç istemini ne kadar öngördüğünü olasılıkla ölçerek adayları sıralayın.

## Nedir?

Inverse Prompting’in bu akademik kullanımı, üretilen metinden özgün istemin olasılığını hesaplar. Beam search sırasında aday devamlar bu ters olasılık sinyaliyle değerlendirilir. Böylece başlangıç konusu ile metin arasındaki ilişkiyi korumaya çalışır.

Bu iş token olasılıklarına ve üretim aramasına erişen bir model/yürütücü gerektirir. Sohbette “hangi promptu kullanmış olabilirim?” diye sormak ya da kullanıcıya soru sordurmak aynı yöntem değildir.

## Ne zaman işe yarar?

Kontrollü uzun metin veya şiir üretimi araştırmalarında kullanılabilir. Olasılık hesaplayan model arayüzü olmadan yalnız kavramsal taslak olarak kalır.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Kütüphaneyle ilgili tek cümle üretiminde konudan sapmayı sıralayacaksınız.

**Prompt**

```text
İstem x: “Sessiz bir kütüphaneyi anlat.”
Koordinatör aynı modelin üretim aramasında iki aday devam tutar: A “Rafların arasında sayfa sesleri duyulur.”; B “Stadyum kalabalığı bağırıyor.”
Her aday için aynı modelde ters bağlamı kurup logP(x|aday) hesapla; aynı ters istem şablonu ve aynı başlangıç istemi kullanılsın. Ters şablon: "Metin: [gerçek aday]. Bu metnin isteği:"; bu önekten sonra x tokenlarının gerçek log olasılığını oku, modelden puan tahmin etmesini isteme. Bunlar modelden gerçek olasılık okumaları olmalı.
Yüksek ters skorlu adayı sürdür; tek cümle sonlandırıcısında dur. Olasılık erişimi yoksa akışı çalıştı diye sunma.
```

**Örnek çıktı**

Yalnız öğretici skorlar: A −4, B −11; daha yüksek olan −4 nedeniyle A seçilir. Bu değerler ölçülmüş model olasılıkları değildir.

**Ne elde ettik?**

Hangi sayının nereden gelmesi gerektiği açık. Sohbetin öznel puanı bu olasılıkların yerine geçmez.

### Orta (Medium)

**Durum**

Bir paragrafın ikinci cümlesinde konu kayıyor.

**Prompt**

```text
İstem: “Kütüphane çalışma odasının sessizliğini iki cümlede anlat.” İlk cümle: “Masalarda açık kitaplar bekliyor.”
Ters puanlama şablonu bu düzeyde de aynıdır: önek = "Metin: [ilk cümle dahil bütün aday metin]. Bu metnin isteği:"; hedef tokenlar = yukarıdaki “Kütüphane çalışma odasının sessizliğini iki cümlede anlat.” isteminin tamamı. Öneği puanlama; yalnız önekten sonraki hedef tokenların gerçek log olasılıklarını topla ve hedef token sayısına bölerek ortalama ters logP’yi bul.
Koordinatör beam genişliğini 2 tutar; her tur modelden aday devamlar alır. Her tamamlanan cümle için ters istem olasılığını ve bütün adayın ileri üretim log olasılığını gerçekten okur. Bu öğretim uyarlamasında skor = 0,5 × ortalama ters logP + 0,5 × (ileri logP / üretilen token sayısı). Katsayılar baştan sabittir; makalenin özgün ayarları olduğu iddia edilmez. Bu skorla adayları yeniden sıralar.
İki cümle veya 60 token sınırında bitir. Her dalda metin, kullanılan ters şablon ve gerçek skor korunur. Dosya veya ağ aracı gerekmez; olasılık destekleyen yerel/model arayüzü gerekir.
```

**Örnek çıktı**

Temsili kalan dal: “Masalarda açık kitaplar bekliyor. Yalnız çevrilen sayfaların sesi duyuluyor.”

**Ne elde ettik?**

İlk cümleden sonraki aday seçimi de başlangıç istemine bağlandı. Metnin güzel olması skorun gerçekten hesaplandığını göstermez.

### İleri (Hard)

**Durum**

Ters skor yüksek olsa da metin verilen gerçeği bozabilir.

**Prompt**

```text
İstem: “Salonun kapanışını anlat. Doğru kayıt K1: 17.00.”
Koordinatör en fazla 2 beam, 3 genişletme turu uygular. Ters şablon: önek = "Metin: [gerçek adayın tamamı]. Bu metnin isteği:"; hedef = “Salonun kapanışını anlat. Doğru kayıt K1: 17.00.” isteminin bütün tokenları. Her aday için aynı modelde yalnız bu önekten sonraki hedef tokenların gerçek log olasılıkları toplamını okur; aynı hedefi kullanarak skorla sıralar. Önek, hedef ve ölçülen skoru dal kaydında saklar.
Ek uygulama denetimi: Son adayda K1’e aykırı saat varsa reddet. Ters olasılık kaynağa uygunluk testi değildir.
“Salon 18.00’de kapanır” yüksek skor alsa bile yayımlama. Üç turda kaynak uyumlu aday yoksa bulunamadı de; olasılık değerini modelden tahmin ettirme.
```

**Örnek çıktı**

Temsili sonuç: 18.00 adayı kaynak kontrolünde elenir; 17.00 adayı varsa ayrı kontrolü geçebilir.

**Ne elde ettik?**

Kontrol edilebilir konu ilişkisi ile olgusal doğruluk aynı puana sıkıştırılmadı.

## Nerede durmalı?

Özgün çalışma Çince şiir ve uzun cevap üretimi üzerindedir. Uygulamaya göre ters skor, uzunlukla normalize edilmiş ileri olasılık ve şiir biçimi gibi ek terimlerle birleşir; basit senaryo yalnız ters skor çekirdeğini gösterir. Türkçe örnekler yöntemin ölçülmüş uyarlaması değildir. Flipped Interaction modelin kullanıcıya soru sormasıdır; Reversing CoT çözümden problemi yeniden kurar. Buradaki “inverse” gerçek olasılık ve decoding mekanizmasına bağlıdır.

## Kaynaklar

- [Controllable Generation from Pre-trained Language Models via Inverse Prompting](https://arxiv.org/html/2103.10685) — Zou, Xu; Yin, Da; Zhong, Qingyang; Ding, Ming; Yang, Hongxia; Yang, Zhilin; Tang, Jie. 2021-03-19; okunan sürüm 2021-11-09. Aynı modelle üretilen metinden özgün istemin olasılığını hesaplayıp beam adaylarını seçmeyi tanımlar; normal sohbet arayüzünün bu erişimi sunduğunu göstermez. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
