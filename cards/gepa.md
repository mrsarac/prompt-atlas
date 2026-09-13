# GEPA

Hata izlerinden prompt değişikliği çıkarın; farklı örneklerde güçlü adayları birlikte koruyun.

## Nedir?

GEPA, prompt adaylarını çalıştırırken oluşan izleri ve geri bildirimleri okuyarak yeni adaylar üretir. Yalnız tek ortalama puana bakmak yerine farklı örneklerde güçlü adayları Pareto yaklaşımıyla koruyabilir; tamamlayıcı dersleri birleştirmeyi dener.

Gerçek yürütme, değerlendirme ve aday geçmişini yöneten bir optimizasyon sistemi gerekir. Bir modele “promptumu evrimleştir” demek bu düzeni çalıştırmaz. Burada küçük, öğretici bir kontrol taslağı kullanıyoruz.

## Ne zaman işe yarar?

Bir veya birkaç prompt içeren sistemde hata nedenleri kaydedilebiliyorsa yararlıdır. Doğru cevapları bilinen veri ve izlerin hassas bilgiden arındırılması gerekir.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

İki destek örneğinde farklı hatalar görülüyor.

**Prompt**

```text
Geliştirme: “Fatura yanlış”→fatura; “Giremiyorum”→erisim.
Koordinatör mevcut adayı iki çağrıda çalıştırır; prompt, girdi, çıktı ve exact-match sonucunu iz olarak saklar.
Reflection çağrısı: “Yalnız bu izdeki etiket/biçim hatasına yönelik bir prompt değişikliği öner.”
Yeni adayı aynı iki örnekte yürüt. Her örnek için başarı vektörünü sakla; eskisinden hiçbir örnekte kötüleşmeyen ve birinde iyileşen adayı üstün say.
Bir değişiklik turu; beş çağrı. Gerçek iz yoksa skor yazma.
```

**Örnek çıktı**

Temsili eski vektör [1,0], yeni [1,1]. Yeni aday iki örnekte de en az aynı, birinde daha iyi.

**Ne elde ettik?**

Değişikliğin dayandığı hata ve seçim kuralı görülebiliyor. Bu iki kayıt gerçek performans deneyi değildir.

### Orta (Medium)

**Durum**

İki aday farklı örneklerde iyi; ortalama aynı.

**Prompt**

```text
Veri: “Fatura yanlış”→fatura; “Giremiyorum”→erisim; “Yardım”→belirsiz.
Koordinatör A ve B’yi gerçek hedef çağrılarıyla değerlendirir. Temsili vektörler A=[1,1,0], B=[0,1,1]. İkisini de koru; biri ötekine her örnekte üstün değil.
Reflection’a iki prompt ve hata izlerini ver: “Belirsiz sınıfı korurken fatura ayrımını kaybetmeyen bir aday öner.”
Bir birleşik adayı üç kayıtta dene; yalnız gerçek sonuçla karşılaştır. Aday üretimi bir çağrı; bu tur en fazla dört çağrı.
```

**Örnek çıktı**

Temsili birleşik aday: “Açık konu varsa fatura/erisim; konu yoksa belirsiz. Tek etiket yaz.” Sonuç vektörü ancak çalıştırılınca bilinir.

**Ne elde ettik?**

Tamamlayıcı adayları koruma gerekçesi açık. Birleşimin ikisinden iyi olacağı varsayılmadı.

### İleri (Hard)

**Durum**

İzlerden türeyen prompt test örneğini ezberleyebilir.

**Prompt**

```text
Geliştirme kayıtları: “Fatura yanlış”→fatura; “Giremiyorum”→erisim; “Yardım”→belirsiz. Ayrı kontrol: “Ödeme belgem iki kez kesildi”→fatura.
Koordinatör en fazla iki GEPA revizyon turu yapar. Reflection yalnız geliştirme izlerini görür; kontrol girdisi ve etiketi aday üretimine girmez.
Her değişiklikte eski/yeni başarı vektörünü tut; tamamlayıcı adayları koru. Seçilen promptu dondur, ayrı kontrolü bir kez uygula.
Adaya tek tek geliştirme cümleleri eklenmişse genelleme riskini insan inceler. Bütçe biterse en iyi gözlenen aday ve çözülmemiş hatayla dur.
```

**Örnek çıktı**

Temsili riskli kural: “Yardım sözcüğüne belirsiz de.” Daha genel aday: “Açık konu yoksa belirsiz.” Ayrı kontrolün sonucu yeni gözlem olarak raporlanır.

**Ne elde ettik?**

Adayın ölçüm kaydı ile son kontrolün bağımsızlığı korunuyor. Genel kural yazılmış olması tek başına genelleme kanıtı değil.

## Nerede durmalı?

Pareto kümesi tek bir mutlak kazanan vaat etmez. Yanlış değerlendirme veya eksik iz yanlış revizyon doğurabilir. Özgün GEPA bulgularının görev/model sınırlarını koruyun; kendi Türkçe örneğinize aynı kazanım yüzdesini taşımayın.

## Kaynaklar

- [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://arxiv.org/html/2507.19457) — Agrawal, Lakshya A; Tan, Shangyin; Soylu, Dilara; Ziems, Noah; Khare, Rishi; Opsahl-Ong, Krista; Singhvi, Arnav; Shandilya, Herumb; Ryan, Michael J; Jiang, Meng; Potts, Christopher; Sen, Koushik; Dimakis, Alexandros G.; Stoica, Ion; Klein, Dan; Zaharia, Matei; Khattab, Omar. 2025-07-25; okunan sürüm 2026-02-14. Yürütme izlerinden reflection, aday güncelleme ve Pareto tabanlı seçim/birleştirmeyi destekler; seçilmiş altı görevdeki sonuçlar evrensel üstünlük değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
