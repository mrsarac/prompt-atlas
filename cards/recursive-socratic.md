# Recursive Socratic Questioning

Alt soruyu gerektiğinde yeniden böl; cevapları yukarı doğru birleştir.

## Nedir?

Recursive Socratic Questioning, modelin ana problemi alt sorulara bölüp gerektiğinde aynı işlemi alt sorulara da uyguladığı bir algoritmadır. Denetleyici çözülmüş alt cevapları birleştirir. İnsan öğrenciyi soruyla eğitme yöntemiyle aynı şey değildir.

## Ne zaman işe yarar?

Bir alt sorunun da kendi içinde parçalanması gereken, bağımlılıkları izlenebilir görevlerde.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

İki bölümden oluşan bir sayısal soruyu çözeceksiniz.

**Prompt**

```text
Denetleyici bir soru ağacı tutsun. Ana soru: 3 kutunun her birinde 8 defter var, toplamdan 5'i dağıtıldı; kaç kaldı? En fazla derinlik 2 ve toplam 4 model çağrısı.
Kök çağrı gerekli alt soruları belirlesin: toplam defter; dağıtım sonrası kalan.
İlk alt soru çözüldükten sonra gerçek 24 cevabını ikinciye aktar. Her düğüm yalnız kısa işlem ve cevap versin; çözülebilir yaprakları yeniden bölme.
Birleştirme çağrısı ana soru ve alt cevaplardan sonucu kontrol etsin. Bütçe biterse eksik düğümü belirt; sonuç uydurma.
```

**Örnek çıktı**

Yaprak: “3×8=24”. Üst birleşim: “24−5=19”. Sonuç 19 defterdir.

**Ne elde ettik?**

Alt cevapların nereye taşındığı açık kaldı.

### Orta (Medium)

**Durum**

Kargo sorusunun alt sorusu da iki işlem gerektiriyor.

**Prompt**

```text
Ana soru: 3 ürünün her biri 80 TL, ürün toplamına %25 indirim, kargo 20 TL; ödeme ne?
Denetleyici: derinlik en fazla 3, toplam 6 çağrı. Model kökü "indirimli ürün toplamı" ve "kargoyla toplam" diye bölsün. İlk alt soru gerekirse ham toplam ve indirim olarak yeniden bölünsün.
Yaprak çıktıları kimlikleriyle saklansın: ham toplam 240; indirimli 180; ödeme 200. Bunlar temsili beklenen değerlerdir; gerçek çağrı çıktısı ayrı kaydedilsin.
Birleşim her sayının birimini korusun. Düğüm çözüldüyse aynı girdiyi yeniden sorma; kök kontrolünden sonra dur.
```

**Örnek çıktı**

Ağaç: 3×80 → 240; 240×0,75 → 180; 180+20 → 200 TL.

**Ne elde ettik?**

Alt problem de gerektiği kadar bölündü; bütün dallar tek kök cevaba bağlandı.

### İleri (Hard)

**Durum**

Bir yaprakta veri yoksa özyineleme bunu yaratamaz.

**Prompt**

```text
Ana soru: Atölyenin toplam maliyeti kaç TL? Bilinen: 8 kişi, malzeme kişi başı 30 TL. Salon ücreti belirtilmedi.
Denetleyici derinlik 3, toplam 5 çağrı sınırı koysun; her düğüm solved/missing_data/failed durumlarından birini döndürsün.
Model malzeme ve salon alt sorularını ayırsın. Malzeme 8×30 olarak çözülebilir. Salon verisi yoksa yeni alt soru uydurarak sayı üretmesin; missing_data durumunu üst düğüme taşısın.
Birleşim yalnız "240 TL + salon ücreti" koşullu sonucunu yazsın. Eksik veri veya bütçe sınırında dur; kesin toplam verme.
```

**Örnek çıktı**

“Malzeme 240 TL. Salon ücreti bilinmediğinden toplam maliyet kesinleşmiyor.”

**Ne elde ettik?**

Daha fazla alt soru, eksik olguyu sahte bir cevaba dönüştürmedi.

## Nerede durmalı?

Bu yöntem için gerçek çağrı ağacı, durum kaydı ve durma sınırı gerekir. Sokratik öğretimde öğrenen insandır; burada modelin problem çözme akışı düzenlenir. Görünür kısa alt cevaplar özgün yöntemin sade uyarlamasıdır; insan öğrenme etkisi çıkarılamaz.

## Kaynaklar

- [The Art of SOCRATIC QUESTIONING: Recursive Thinking with Large Language Models](https://arxiv.org/html/2305.14999) — Qi, Jingyuan; Xu, Zhiyang; Shen, Ying; Liu, Minqian; Jin, Di; Wang, Qifan; Huang, Lifu. 2023-05-24; okunan sürüm 2023-11-02. Alt soruları özyinelemeli üretip cevaplarını birleştiren divide-and-conquer algoritmasını tanımlar; insan tutor konuşması veya öğrenme deneyi değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
