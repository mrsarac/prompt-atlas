# Kendine açıklama

Açıklamayı sen kur; model, atladığın bağlantıyı görünür kılsın.

## Nedir?

Kendine açıklama, bir örneğin neden çalıştığını kendi sözlerinizle anlatmaktır. Model açıklamayı sizin yerinize üretirse insanın yaptığı öğrenme işi değişir. Bu kartta model kısa sorular ve kaynakla sınırlı geri bildirim verir.

## Ne zaman işe yarar?

Bir çözümü okuduğunuzda tanıdık geliyor ama aynı fikri yeni örneğe uygularken zorlanıyorsanız.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Yüzde indirim hesabını kendi cümlenizle anlatacaksınız.

**Prompt**

```text
Öğrenen benim. Kural: %20 indirim, fiyatın %80'ini ödemektir. Örnek: 100 TL -> 80 TL.
Önce bana "Neden 100 ile 0,8'i çarpıyoruz?" diye sor ve cevabımı bekle. Açıklamayı benim yerime yazma. Yanıtımdaki doğru bağlantıyı belirt; eksikse tek takip sorusu sor. En fazla iki soru.
```

**Örnek çıktı**

Model: “Neden 0,8 ile çarpıyoruz?” İnsan: “Yüzde 20 gidince yüzde 80 kalıyor.” Model: “Kalan payı doğru bağladın. Peki 200 TL’de aynı oran neyi değiştirir?”

**Ne elde ettik?**

Sonucu tekrar etmek yerine kalan payın anlamı açıklandı.

### Orta (Medium)

**Durum**

Bir kod satırının neden sınır durumunu kapsadığını anlatacaksınız.

**Prompt**

```text
Kod: total >= 500 ? 0 : 50. Kural: 500 ve üzeri ücretsiz, altı 50 TL.
Benim açıklamam: "500'den büyükse kargo ücretsiz."
Açıklamamı kural ve kodla karşılaştır. Doğru bölümü belirt; eksik olan tek sınır için soru sor. Bana düzeltmeyi hemen söyleme. Ben yeniden açıklayınca 499/500/501 için tahmin istemen yeterli; gerçek kod testi yaptığını iddia etme.
```

**Örnek çıktı**

Model: “Büyük tutarları anlattın. Tam 500 olduğunda `=` işareti neyi değiştiriyor?” İnsan: “500 de ücretsiz; 499 için 50, 500 ve 501 için 0.”

**Ne elde ettik?**

Sözel açıklamadaki eksik eşitlik, yeni sınır örneğine taşındı.

### İleri (Hard)

**Durum**

Doğru görünen açıklamanız yeni durumda işlemiyor.

**Prompt**

```text
Kaynak kural: Ortalama hız toplam yol / toplam süredir.
Benim açıklamam: "60 km'yi 30 km/saat, sonra 60 km'yi 60 km/saat ile gidince ortalama 45 km/saat olur; iki hızı ortaladım."
Önce açıklamamın hangi varsayımını kontrol etmem gerektiğini tek soruyla göster. Cevabı vermeden süreleri benim hesaplamamı bekle. Sonra toplam yol ve toplam süreyi kendi sözlerimle bağlamamı iste.
En fazla üç soru; sonunda yeni görev ver: iki eşit süre boyunca bu hızlarla gidilse neden farklı olur? Açıklama kalitesini, yardımsız doğru cevapla aynı ölçüt sayma.
```

**Örnek çıktı**

Model: “İki bölümde eşit süre mi geçiriyorsun?” İnsan: “İlk bölüm 2, ikinci 1 saat; 120/3=40.” Model, eşit yol ile eşit süre ayrımını yeniden açıklamasını ister.

**Ne elde ettik?**

Yanlış genelleme, başka bir koşulla karşılaştırılarak açığa çıktı.

## Nerede durmalı?

Self-explanation insanın yaptığı açıklamadır; modelin kendi cevabını açıklamasıyla aynı öğrenme iddiası kurulamaz. Feynman adıyla anılan sade anlatım yaklaşımları bu kartla ilişkili, fakat tek bir özgün dört adımlı akademik protokol diye sunulmuyor. Açıklamanın güzelleşmesi doğru cevap veya uzun süreli öğrenme artışı demek değildir.

## Kaynaklar

- [Self-explanations: How students study and use examples in learning to solve problems](https://education.asu.edu/lcl/publications/chi-m-t-h-bassok-m-lewis-m-reimann-p-glaser-r-1989-self-explanations-how-students) — Michelene T. H. Chi; Miriam Bassok; Matthew W. Lewis; Peter Reimann; Robert Glaser. 1989. İnsan self-explanation çalışmasının başlık, yazar ve 1989 künyesini doğrular; bu kayıttan deney ayrıntısı veya etki büyüklüğü çıkarılmaz. Kanıt düzeyi: yalnız bibliyografik kayıt.
- [Practice Less, Explain More: LLM-Supported Self-Explanation Improves Explanation Quality on Transfer Problems in Calculus](https://arxiv.org/html/2604.00142) — Chen, Eason; Tang, Xinyi; Zhao, Yvonne; Chen, Meiyi; Elmir, Meryam; McLaughlin, Elizabeth; Yuan, Mingyu; Wang, Yumo; Agarwal, Shyam; Cochrane, Jared; Lin, Jionghao; Wu, Tongshuang; Koedinger, Ken. 2026-03-31; okunan sürüm 2026-05-30. LLM geri bildirimli self-explanation koşulunu inceler; açıklama kalitesi ile son-test performansı ayrı ölçütlerdir ve koşullar arasında anlamlı son-test farkı bildirilmez. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
- [Learn Faster with the Feynman Technique](https://www.scotthyoung.com/blog/2011/09/01/learn-faster/) — Scott H. Young. 2011-09. Feynman Technique adının pratisyen kullanımını doğrular; okunmayan videodan özgün adım veya etki iddiası kurulmaz. Kanıt düzeyi: sayfa yazısı; gömülü video incelenmedi.
