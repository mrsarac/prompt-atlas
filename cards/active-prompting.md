# Active Prompting

Modelin en çok kararsız kaldığı örnekleri insana etiketlet.

## Nedir?

Active Prompting, bir soru havuzunda birden fazla ayrı yanıt üretip belirsizliği ölçer; seçilen sorulara insanın açıklamalı doğru örnekler hazırlamasını sağlar. Bu örnekler daha sonra few-shot girdisi olur. Bu bir örnek seçme sürecidir; otomatik model eğitimi değildir.

## Ne zaman işe yarar?

İnsan etiketleme zamanı sınırlıysa ve hangi sorulara iyi örnek hazırlanacağını sistemli seçmek istiyorsanız.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

İki oyuncak hesap sorusundan hangisini açıklamalı örnek yapacağınızı seçeceksiniz.

**Prompt**

```text
Denetleyici havuzu: Q1="2+2?", Q2="500 TL dahil eşikte ücretsiz kargo kuralında 500 TL kargo ücreti?" Kural: altı 50, eşik ve üzeri 0.
Her soruya 3 bağımsız çağrı yap; önceki cevapları diğerine gösterme. Gerçek cevapları sayısal biçime normalize et.
Belirsizlik ölçütünü baştan sabitle: 1 - en sık cevabın oranı. En yüksek belirsizlikteki bir soruyu insana seçtir.
İnsan doğru cevabı ve kısa kontrolü yazsın. Sonraki yeni soruya bu onaylı örneği few-shot olarak ekle. Bütçe 6 örnekleme + 1 çıkarım çağrısı; sonra dur.
```

**Örnek çıktı**

Temsili örnekleme: Q1=[4,4,4], belirsizlik 0; Q2=[0,50,0], belirsizlik 1/3. İnsan Q2 için “500 ≥ 500, kargo 0” örneğini hazırlar.

**Ne elde ettik?**

Etiketleme emeği, gerçekten ölçülecek kararsızlığa göre yönlendirildi.

### Orta (Medium)

**Durum**

Yanıt biçimleri sahte anlaşmazlık yaratabilir.

**Prompt**

```text
Sonlu havuz: Q1="23 kişi, masa başına en fazla 6 kişi; kaç masa?"; Q2="500 TL dahil eşikte ücretsiz kargo; altı 50 TL. 500 TL sepetin kargosu?"; Q3="2+2?"
Denetleyici her soru için birbirinin yanıtını görmeyen 4 çağrı alsın. Temsili yanıtlar: Q1=["4","dört masa","4 masa","3"], Q2=["0","50","0 TL","50 TL"], Q3=["4","dört","4","4"]. Önce sayı/birim anlamını normalize et.
Belirsizlik = 1 − en sık cevabın payı. En yüksek iki soruyu seç; eşitlikte küçük Q kimliği öne gelsin. İnsan yalnız bu iki soruya doğru cevap ve kısa gerekçe yazsın; onaysız örneği kullanma.
İki etiket onaylanamazsa yeni çıkarıma geçmeden dur. Bu iki onaylı örneği ayrı yeni soruya taşı: "25 kişi, masa başına en fazla 6 kişi; kaç masa?" Bu sorunun cevabı seçim aşamasına girmez. Bütçe 3×4=12 örnekleme, 2 insan etiketi, 1 yeni çıkarım; toplam 13 model çağrısı, sonra dur.
```

**Örnek çıktı**

Normalizasyon sonrası Q1=[4,4,4,3], Q2=[0,50,0,50], Q3=[4,4,4,4]; belirsizlikler sırasıyla 1/4, 1/2, 0. Seçim Q2 ve Q1. İnsan etiketleri: “500 ≥ 500, kargo 0”; “3 masa 18 kişi alır; 4 masa 24, bu yüzden 4 gerekir.” Yeni soruya temsili cevap: “4 masa 24 kişi alır; 25 kişi için 5 masa gerekir.”

**Ne elde ettik?**

Farklı yazım biçimleri farklı görüş sayılmadı.

### İleri (Hard)

**Durum**

Kararsızlık düşük ama ortak yanlış cevap mümkün.

**Prompt**

```text
Sonlu havuz: Q1="Sepet 600 TL, kupon 100 TL; indirim sonrası 550 altı kargo 40 TL, diğer durumda 0. Ödeme toplamı?"; Q2="23 kişi, masa başına en fazla 6 kişi; kaç masa?"; Q3="2+2?"
Her soruya 3 bağımsız çağrı yap. Temsili sayısal yanıtlar Q1=[500,500,500], Q2=[4,3,4], Q3=[4,4,4]. Belirsizlik = 1 − modal pay. En kararsız bir soruyu seç; eşitlikte küçük kimlik öne gelsin. İnsan doğru cevap ve kısa gerekçe hazırlasın.
Ek insan denetimi kuralını sonuçlardan önce sabitle: seçilmeyen sıfır-belirsizlikli sorular arasından kimliği en küçük bir soruyu denetle. Bu, belirsizlik seçimine ek öğretim uyarlamasıdır. İki insan etiketi üst sınırdır; doğrulanamayan etiketi havuza katma.
İki etiket onaylanamazsa değerlendirmeye geçmeden dur. İki onaylı örnekle tek ayrı değerlendirme sorusunu yanıtlat: "Sepet 620 TL, kupon 100 TL; indirim sonrası 550 altı kargo 40 TL, diğer durumda 0. Ödeme toplamı?" Değerlendirme cevabı seçim/güncelleme için kullanılmaz. Bütçe 9 örnekleme + 1 değerlendirme çağrısı ve en fazla 2 insan etiketi; sonra dur.
```

**Örnek çıktı**

Belirsizlikler Q1=0, Q2=1/3, Q3=0. İlk seçim Q2; insan “4 masa gerekir” etiketini hesapla doğrular. Ek denetim Q1’i seçer; insan “600−100=500; 500<550, bu yüzden 500+40=540” etiketini ekler. Temsili son değerlendirme: 620−100+40=560 TL. Sıfır belirsizlikli ortak yanlış cevap, ayrı insan kontrolüyle görünür oldu.

**Ne elde ettik?**

Model kararsızlığı ile insanın doğruluk kontrolü ayrı ölçütler olarak kaldı.

## Nerede durmalı?

Self-consistency ayrı cevapları birleştirerek o soruyu yanıtlar; Active Prompting belirsizliği insanın etiketleyeceği örnekleri seçmek için kullanır. Özgün çalışmada insan yazımı açıklamalar vardır. Buradaki kısa gerekçeler öğretim uyarlamasıdır; yöntemin kazancını garanti etmez.

## Kaynaklar

- [Active Prompting with Chain-of-Thought for Large Language Models](https://arxiv.org/html/2302.12246) — Diao, Shizhe; Wang, Pengcheng; Lin, Yong; Pan, Rui; Liu, Xiang; Zhang, Tong. 2023-02-23; okunan sürüm 2024-07-21. Çoklu örnekle belirsizlik tahmini, buna göre soru seçimi ve insan açıklamalı örneklerinin few-shot kullanımını tanımlar. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
