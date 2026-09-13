# Self-Debug

Üretilen kodu açıklat, çalışmasını kontrol et, hatalı adımı düzelt.

## Nedir?

Self-Debug, modelin kendi ürettiği programı açıklama ve yürütme geri bildirimi gibi bilgilerle yeniden ele almasıdır. İnsan Rubber Duck’ta kendi kodunu anlatır; burada incelenen ve düzelten taraf modeldir.

## Ne zaman işe yarar?

Kod adayının davranışını örnek girdilerle sınayabileceğiniz, küçük revizyonları kontrol edebileceğiniz durumlarda.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Kod bir sınır değerde yanlış davranıyor.

**Prompt**

```text
Görev: 500 TL ve üzeri ücretsiz, altı 50 TL kargo. Modelin kod adayı: total > 500 ? 0 : 50.
İnsan denetleyici olsun. İlk inceleme çağrısı kodun 499/500/501 için ne yaptığını kısa açıklasın; gerçek test sonucu gibi sunmasın.
Sonra uygulama izole yürütücüde bu girdileri gerçekten çalıştırsın; stdout ve beklenen 50/0/0 değerlerini düzeltme çağrısına taşısın.
Model yalnız en küçük revizyonu versin. Bir tekrar testi sonrası dur; çalışma aracı yoksa öneri düzeyinde kal.
```

**Örnek çıktı**

Temsili ilk sonuç 50/50/0; revizyon `>=` olur. Beklenen yeni sonuç 50/0/0’dır.

**Ne elde ettik?**

Kod açıklaması gerçek davranış kontrolüne ve küçük revizyona bağlandı.

### Orta (Medium)

**Durum**

Program normal örnekte geçiyor, boş listede hata veriyor.

**Prompt**

```text
Görev: Boş listede None, diğer listelerde en büyük sayıyı döndür.
Kod adayı: def largest(xs): return max(xs)
Denetleyici testleri izole çalıştırsın: [2,5] -> 5; [-5,-2] -> -2; [] -> None. Gerçek hata mesajını modele ver.
İnceleme çağrısı hatayı kod davranışıyla bağlasın; genel yeniden yazım yapmasın. Revizyon çağrısı yalnız boş liste koşulunu eklesin. Aynı testleri yeniden çalıştır; en fazla iki test turu. Sonuçlar geçmeden doğru kod ilan etme.
```

**Örnek çıktı**

Temsili hata boş listede `ValueError`; aday düzeltme: `return max(xs) if xs else None`.

**Ne elde ettik?**

Başarılı sıradan örnek, boş girişin de doğru olduğu varsayımına dönüşmedi.

### İleri (Hard)

**Durum**

Açıklama doğru görünse de test kapsamı yetersiz olabilir.

**Prompt**

```text
Görev: Listedeki tekrarları ilk görünüm sırasıyla kaldır. Kod adayı: return list(set(xs)).
Model kodun sıralama garantisini kısa biçimde açıklasın. Denetleyici yalnız bir çıktının tesadüfen doğru olmasına güvenmesin; görev sözleşmesini de kontrol etsin.
Test verileri: ["B","A","B","C"] -> ["B","A","C"]; [] -> []; ["A","A"] -> ["A"]. İzole yürütme sonuçlarını ve sıra gereksinimini revizyon çağrısına taşı.
Model sıralamayı açıkça koruyan bir çözüm önersin; iki test turu sonunda kalan belirsizliği bildir. Yalnız kendi açıklamasını kanıt diye kullanma.
```

**Örnek çıktı**

Aday revizyon: hashable öğeler için `list(dict.fromkeys(xs))`. Sıra ve hashable girdi sınırı ayrıca belirtilir.

**Ne elde ettik?**

Hata ayıklama, tesadüfi test geçişinin ötesinde sözleşmeyi de kontrol etti.

## Nerede durmalı?

Özgün Self-Debug çalışmasında göreve göre açıklama ve yürütme geri bildirimi düzenleri bulunur; her görev insan doğruluk etiketi gerektirir denemez. Bu kart açık test oracle’lı bir uyarlama gösterir. Modelin kendi eleştirisi her zaman düzeltmez; gerçek test ve doğru gereksinim hâlâ gerekir.

## Kaynaklar

- [Teaching Large Language Models to Self-Debug](https://arxiv.org/html/2304.05128) — Chen, Xinyun; Lin, Maxwell; Schärli, Nathanael; Zhou, Denny. 2023-04-11; okunan sürüm 2023-10-05. Modelin ürettiği programı doğal dil açıklaması ve yürütme sonuçları üzerinden inceleyip düzeltmesini araştırır; insanın Rubber Duck öğrenme etkisi değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
- [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/html/2310.01798) — Huang, Jie; Chen, Xinyun; Mishra, Swaroop; Zheng, Huaixiu Steven; Yu, Adams Wei; Song, Xinying; Zhou, Denny. 2023-10-03; okunan sürüm 2024-03-14. Dış geri bildirim olmadan öz düzeltmenin sınırlarını gösteren görev/model bulguları sunar; her öz düzeltme düzeninin başarısız olduğu anlamına gelmez. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
