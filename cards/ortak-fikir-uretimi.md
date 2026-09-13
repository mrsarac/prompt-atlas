# Ortak fikir üretimi

Fikir üretimini, insanın kendi fikirleri ve açık kısıtlarla birlikte yürüt.

## Nedir?

Ortak fikir üretiminde insan ve model yeni seçenekler önerir, dönüştürür ve eler. Aynı modelin önerileri benzer noktalarda toplanabilir; bu yüzden insanın ilk fikirlerini ve seçme ölçütlerini görünür tutmak yararlıdır.

## Ne zaman işe yarar?

Yazı konusu, etkinlik biçimi veya ürün fikri ararken seçenek alanını genişletmek için.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir kitap kulübü buluşmasına fikir arıyorsunuz.

**Prompt**

```text
Benim ilk fikirlerim: kısa alıntı turu; herkesin bir soru getirmesi. Kısıt: 8 kişi, 45 dakika, ek malzeme yok.
Önce benim iki fikrimi koru. Sonra bunlardan işleyiş olarak farklı üç fikir üret; her birini iki cümlede anlat. Aynı fikre yeni isim vermekle yetinme. Sonunda hangi fikrin hangi kısıtı zorladığını belirt.
```

**Örnek çıktı**

Adaylar: “Bir karakterin kararını iki farklı açıdan tartışma; sessizce soru yazıp sırayla seçme; kitabın bir bölümünü farklı sonla yeniden kurma.”

**Ne elde ettik?**

İnsan fikirleri model önerileri arasında kaybolmadan seçenekler genişledi.

### Orta (Medium)

**Durum**

Modelin ilk fikirleri birbirine çok benziyor.

**Prompt**

```text
Görev: 30 dakikalık ekip öğrenme etkinliği. İlk öneriler: mini sunum, kısa sunum, hızlı sunum. Bunların aynı mekanizmayı tekrar ettiğini kabul et.
Yeni turda üç farklı katılım düzeni üret: herkesin tek başına denemesi; ikili karşılıklı açıklama; bütün grubun ortak ürün çıkarması. Her birinde süre, katılımcı eylemi ve ortaya çıkacak ürün net olsun. Uydurma verimlilik puanı verme.
```

**Örnek çıktı**

“10 dakika bireysel problem + 10 dakika karşılaştırma + 10 dakika ders çıkarma” ile “ikili teach-back” farklı eylem düzenleri olarak ayrılır.

**Ne elde ettik?**

Çeşitlilik, başlık değişiminden davranış değişimine taşındı.

### İleri (Hard)

**Durum**

Fikir seçerken yenilik ve uygulanabilirlik çatışıyor.

**Prompt**

```text
Amaç: Kütüphaneye ilk kez gelenlerin yön bulmasını kolaylaştırmak. Kısıtlar: Bir haftalık hazırlık, yeni yazılım yok, bütçe 500 TL. İnsan fikirleri: girişte harita; gönüllü karşılama saati.
Önce beş farklı fikir üret; sonra insanın fikirleri dahil hepsini mevcut kısıtlara göre ele. Ölçülmemiş etki tahmini yazma. Her kalan fikir için tek küçük deneme ve gözlenebilir başarı ölçütü öner.
İnsan seçim yapmadan uygulama, satın alma veya mesaj gönderme. Yenilik uğruna kısıtları kaldırma.
```

**Örnek çıktı**

“Giriş haritası için gözlem: yeni ziyaretçi hedef bölümü yardım almadan bulabiliyor mu? Gönüllü saatinin sınırı: yalnız belirli zamanlarda destek.”

**Ne elde ettik?**

Fikir listesi, uygulanabilir seçenek ve ölçülebilir deneme önerisine dönüştü.

## Nerede durmalı?

AI yardımı bazı bağlamlarda bireysel yaratıcı çıktıyı desteklerken toplu çeşitliliği azaltabilir; bu bütün yaratıcı işler için tek sonuç değildir. Modelin ürettiği fikrin yeni, özgün veya daha önce hiç yapılmamış olduğunu araştırmadan söylemeyin.

## Kaynaklar

- [Generative AI enhances individual creativity but reduces the collective diversity of novel content](https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532/) — Anil R Doshi; Oliver P Hauser. 2024 Jul 12. Kısa hikâye yazımı deneyinde bireysel yaratıcı değerlendirme ile kolektif çeşitliliğin farklı yönde değişebildiğini inceler; tüm yaratıcı alanlara genellenmez. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
- [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT](https://arxiv.org/html/2302.11382) — White, Jules; Fu, Quchen; Hays, Sam; Sandborn, Michael; Olea, Carlos; Gilbert, Henry; Elnashar, Ashraf; Spencer-Smith, Jesse; Schmidt, Douglas C.. 2023-02-21. Alternatif üretme örüntüsüne kaynak sağlar; özgünlük veya ticari başarı garantisi değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
