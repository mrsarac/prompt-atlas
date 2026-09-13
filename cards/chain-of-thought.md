# Chain-of-Thought

Çözülmüş örnekteki kısa, denetlenebilir ara sonuçları yeni probleme taşıyın.

## Nedir?

Chain-of-Thought prompting’in özgün örnekli biçiminde, yalnız soru ve cevap değil, aradaki çözüm adımları da gösterilir. Amaç modele çözüm biçimini örneklemektir. Burada uzun iç düşünce dökümleri yerine eşitlikler, varsayımlar ve kontrol edilebilir kısa açıklamalar kullanıyoruz.

Bu görünür açıklamalar modelin gerçekten nasıl düşündüğünün kaydı değildir. Akıcı ama hatalı bir çözüm de aynı biçimde yazılabilir; sonucun kontrolü ayrı kalır.

## Ne zaman işe yarar?

Aritmetik, sıralama ve birkaç bağlantının birlikte tutulduğu problemler için deneyebilirsiniz. Örnek çözümünüzün doğru ve hedef soruyla yapısal olarak ilgili olması gerekir.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Kutulardaki kalemleri sayacaksınız; örnek, çarpma ve çıkarmanın sırasını gösteriyor.

**Prompt**

```text
Örnek: İki kutuda üçer kalem var, biri veriliyor. Hesap: 2×3=6; 6−1=5. Cevap: 5 kalem.
Örnek: Üç kutuda ikişer kalem var, ikisi veriliyor. Hesap: 3×2=6; 6−2=4. Cevap: 4 kalem.
Yeni soru: Dört kutuda beşer kalem var, üçü veriliyor. Aynı biçimde kısa eşitlikler ve son cevap yaz.
```

**Örnek çıktı**

4×5=20; 20−3=17. Cevap: 17 kalem.

**Ne elde ettik?**

Ara hesabı ve sonucun birimini görebiliyoruz. Aritmetiği ayrı bir hesapla siz kontrol edebilirsiniz.

### Orta (Medium)

**Durum**

İndirim ve sabit ücret birlikte uygulanıyor.

**Prompt**

```text
Örnek: 100 TL ürüne %10 indirim, sonra 5 TL hizmet ücreti. İndirimli ürün: 100×0,90=90; toplam: 90+5=95 TL.
Örnek: 200 TL ürüne %25 indirim, sonra 10 TL ücret. 200×0,75=150; 150+10=160 TL.
Soru: Tanesi 80 TL olan üç ürüne ürün toplamı üzerinden %25 indirim uygulanıyor; sonra 20 TL kargo ekleniyor. İndirimin kargoya uygulanmadığını koru. Kısa eşitlikler ve toplamı ver.
```

**Örnek çıktı**

Ürünler: 3×80=240 TL. İndirim sonrası: 240×0,75=180 TL. Toplam: 180+20=200 TL.

**Ne elde ettik?**

İndirim tabanı açık kaldı. Başka bir mağazanın kuralını bu örnekten çıkaramayız.

### İleri (Hard)

**Durum**

Ücretsiz kargo eşiği indirimden sonraki tutara bağlı.

**Prompt**

```text
Örnek: Ürün 600 TL, %10 indirim → 540 TL. Kural indirim sonrası en az 500 TL ise ücretsiz kargo: toplam 540 TL.
Örnek: Ürün 400 TL, %10 indirim → 360 TL. Eşik altına 50 TL kargo: toplam 410 TL.
Yeni soru: Ürün toplamı 625 TL; %20 indirim var. Kargo, indirim sonrası tutar 500 TL veya üzeriyse 0, altındaysa 50 TL. Vergi ayrıca eklenmiyor. Kullanılan eşik karşılaştırmasını ve toplamı yaz; ayrıca ürün toplamı 620 TL olsaydı ne değişirdi?
```

**Örnek çıktı**

625×0,80=500; 500≥500, kargo 0; toplam 500 TL. 620×0,80=496; kargo 50; toplam 546 TL.

**Ne elde ettik?**

Sınırın iki yanındaki beklenen davranış görünüyor. Gerçek kodda sayı türü ve para yuvarlaması ayrıca denetlenmelidir.

## Nerede durmalı?

Örnekli CoT ile örneksiz yönlendirmeyi aynı işlem saymayın. Bazı reasoning modelleri doğrudan talimatla çalışmak üzere tasarlanmıştır; fazladan çözüm anlatımı her durumda yararlı olmayabilir. İnsan self-explanation kartında açıklayan ve öğrenen sizsiniz; bu kart model çıktısının düzeniyle ilgilidir.

## Kaynaklar

- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/html/2201.11903) — Wei, Jason; Wang, Xuezhi; Schuurmans, Dale; Bosma, Maarten; Ichter, Brian; Xia, Fei; Chi, Ed; Le, Quoc; Zhou, Denny. 2022-01-28; okunan sürüm 2023-01-10. Örnek çözüm adımlarıyla aritmetik, sağduyu ve sembolik görevlerde prompting’i inceler; burada verilen Türkçe senaryolar makalenin deneyleri değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
- [Reasoning best practices | OpenAI API](https://developers.openai.com/api/docs/guides/reasoning-best-practices) — OpenAI. yayın tarihi doğrulanmadı. Belirli reasoning modellerinde kısa, doğrudan talimat tavsiyesini sağlar; eski CoT bulgularının bütün modellere aktarılmasını sınırlar. Kanıt düzeyi: sayfa gövdesi.
