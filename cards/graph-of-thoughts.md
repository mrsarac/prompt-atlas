# Graph of Thoughts

Tek bir yol yerine, birleşebilen çözüm parçalarıyla çalış.

## Nedir?

Graph of Thoughts, üretilen çözüm parçalarını bir grafın düğümleri, aralarındaki bağımlılıkları da kenarlar olarak ele alır. Bir denetleyici üretme, birleştirme, puanlama ve iyileştirme işlemlerini yürütür. Sohbete “graf gibi düşün” yazmak bu yürütmeyi kurmaz.

## Ne zaman işe yarar?

Birden çok parçanın ayrı işlenip sonra birleştirilmesi veya aynı ara sonucun farklı dallarda kullanılabilmesi gereken işlerde.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

İki kısa listeden tekrar etmeyen tek bir liste çıkarılacak.

**Prompt**

```text
İnsan denetleyici olsun; her düğüm ayrı çağrı, çıktılar bir kayıt tablosunda tutulsun. En fazla 3 çağrı.
N1 girdisi: "elma, armut, elma". Prompt: Tekrarları kaldır, ilk görünüm sırasını koru.
N2 girdisi: "armut, kiraz". Aynı prompt; N1 çıktısını bu çağrıya verme.
N3 girdisi: Gerçek N1 ve N2 çıktıları. Prompt: N1 ardından N2 sırasıyla birleştir; tekrarları kaldır.
İnsan sonucu ham listelerle karşılaştırsın. Yeni sözcük veya eksik öğe varsa başarısız say; bütçe sonunda dur.
```

**Örnek çıktı**

N1: “elma, armut”; N2: “armut, kiraz”; N3: “elma, armut, kiraz”. Kenarlar N1→N3 ve N2→N3 olur.

**Ne elde ettik?**

Ayrı işlenen iki parça tek birleşim noktasında buluştu.

### Orta (Medium)

**Durum**

Bir etkinlik briefinde erişim ve program bilgisi ortak özete bağlanacak.

**Prompt**

```text
Denetleyici durumunda her düğümün girdisi, çıktısı, kaynak kimliği saklansın. Kaynak: D1="Başlangıç 14.00, bitiş 16.00"; D2="Giriş rampalı; asansör arızalı".
N1 çağrısı D1'den programı çıkarır. N2 çağrısı D2'den erişim bilgilerini çıkarır. N3 gerçek N1+N2 ile 3 maddelik katılımcı notu üretir.
N4 denetim çağrısı ham D1/D2 ve N3'ü alır: her iddia için kaynak göster; arızalı asansörü erişilebilir diye sunma.
Uygulama kaynaksız iddiada yayını engellesin. 4 çağrıda dur; yayın aracı yok.
```

**Örnek çıktı**

“14.00–16.00 [D1]. Girişte rampa var [D2]. Asansör arızalı [D2].” N4, N3’ün yalnız kaynaklı alanları taşıdığını denetler.

**Ne elde ettik?**

Grafın birleşim düğümü yanında ayrı bir kontrol düğümü de oluştu.

### İleri (Hard)

**Durum**

Birleştirilen taslakta çelişki çıktığında yalnız ilgili dal yeniden işlenecek.

**Prompt**

```text
Kaynak A: "Salon 20 kişi". Kaynak B: "Yangın düzeni kapasitesi 16 kişi". Kaynak C: "Atölye 90 dakika".
Denetleyici: A/B/C için ayrı çıkarım düğümleri; birleşim düğümü; kısıt kontrol düğümü. Her kayda kaynak ve ebeveyn düğüm kimliği ekle. Toplam en fazla 6 model çağrısı.
Kontrol, kapasite farkını bulunca A/B dalını insan kararına bırak; C'nin onaylı süresini yeniden üretme. İnsan "operasyonel üst sınır 16" derse bu kararı yeni düğüm olarak birleştir.
Bütçe dolarsa mevcut doğrulanmış süreyi ve açık kapasite sorununu raporla. Karar olmadan kapasiteyi ortalama veya yüksek olanı seçme.
```

**Örnek çıktı**

“Süre 90 dakika doğrulandı [C]. Kapasite için 20/16 ayrımı var; yetkili karar bekleniyor.” Karar sonrası yeni birleşim 16 kişi / 90 dakika olur.

**Ne elde ettik?**

Ortak durum korundu; sorunlu dal bütün çalışmayı yeniden başlatmadı.

## Nerede durmalı?

Tree of Thoughts dallanan adayları arar; Graph of Thoughts ayrıca düğümlerin birleşmesine ve yeniden kullanılmasına izin verir. Grafın varlığı doğruluğu kanıtlamaz. Denetleyici, değerlendirme ölçütü, çağrı bütçesi ve saklanan gerçek çıktılar gerekir.

## Kaynaklar

- [Graph of Thoughts: Solving Elaborate Problems with Large Language Models](https://arxiv.org/html/2308.09687) — Besta, Maciej; Blach, Nils; Kubicek, Ales; Gerstenberger, Robert; Podstawski, Michal; Gianinazzi, Lukas; Gajda, Joanna; Lehmann, Tomasz; Niewiadomski, Hubert; Nyczyk, Piotr; Hoefler, Torsten. 2023-08-18; okunan sürüm 2024-02-06. Çözüm parçalarının graf üzerinden üretim, birleştirme ve iyileştirme işlemleriyle düzenlenmesini tanımlar; örnek denetleyiciler yöntemin sade öğretim uyarlamalarıdır. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
