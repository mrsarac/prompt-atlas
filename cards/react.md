# ReAct

Bir sonraki adımı, gerçekten gelen araç sonucuna göre seç.

## Nedir?

ReAct, kısa bir karar gerekçesini eylem ve gözlemle dönüşümlü kullanır. Model araç çağrısı önerir; uygulama aracı çalıştırır, gerçek sonucu sonraki çağrıya taşır. Sohbette hayal edilen bir arama sonucu gözlem sayılmaz.

## Ne zaman işe yarar?

Başta bütün adımları belirleyemediğiniz, bir belge veya ortamdan gelecek sonuca göre yön değiştiren işlerde.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir müzenin pazartesi açık olup olmadığını öğrenmek istiyorsunuz.

**Prompt**

```text
Kullanıcı görevi: Kurgusal Kent Müzesi pazartesi açık mı?
Uygulama: Yalnız salt okunur museum_hours(name) aracı var. En fazla 2 çağrı; araç yoksa bunu söyle ve dur.
Model: Gerekli eylemi ve bir cümlelik nedenini yaz. Uygulama sonucu gelmeden açık/kapalı deme.
Temsili araç sonucu: {name:"Kent Müzesi", monday:"closed", source:"resmi saat kaydı", updated:"2026-09-01"}
Sonraki model çağrısı: Görevi ve bu gerçek araç sonucunu al; kaydın tarihini belirterek yanıtla, yeterliyse bitir.
```

**Örnek çıktı**

Eylem: `museum_hours("Kent Müzesi")`. Gözlem geldikten sonra: “1 Eylül tarihli resmi saat kaydında pazartesi kapalı görünüyor.”

**Ne elde ettik?**

Karar, araç çağrısından önce uydurulmuş bir gözleme dayanmadı.

### Orta (Medium)

**Durum**

İlk belgede başvuru tarihi yok; ikinci bir kaynağa ihtiyaç doğuyor.

**Prompt**

```text
Görev: Kurgusal serginin son başvuru gününü bul.
Denetleyici en fazla 3 salt okunur belge okuma çağrısı çalıştırsın. Her tur görevi, okunan URL kimliklerini ve alıntıları modele taşısın.
1. read_document("sergi-duyuru") -> "Tarih için koşullar belgesine bakın: sergi-kosullar."
Modelden tek sonraki eylemi iste; aynı belgeye sebepsiz dönme.
2. read_document("sergi-kosullar") -> "Başvurular 20 Ekim 2026 saat 17.00'de kapanır."
Model: Sonucu belge kimliğiyle yaz. Tarih çelişirse kesin tarih verme; bütçe biterse eksikliği bildir.
```

**Örnek çıktı**

İkinci eylem `read_document("sergi-kosullar")` olur. Sonuç: “20 Ekim 2026, 17.00 — sergi-kosullar.”

**Ne elde ettik?**

İkinci adımı ilk gözlem belirledi.

### İleri (Hard)

**Durum**

Bir destek tanısı, başarılı ve başarısız sorguları ayırt etmeli.

**Prompt**

```text
Görev: Sipariş K42 neden görünmüyor? Yazma ve yeniden gönderme yetkisi yok.
Denetleyici: En fazla 3 araç çağrısı. İzinli araçlar order_read(id), sync_status(id). Durum: çağrı kimliği, yanıt durumu, bulgu, kalan bütçe.
order_read("K42") -> {status:"not_found"}
Model: Yok kaydını silinmiş sipariş diye yorumlama. Bir sonraki salt okunur kontrolü seç.
sync_status("K42") -> {status:"pending", next_retry:"14:30"}
Model: Bu sonucu önceki gözlemle birlikte değerlendir; müşteriye teşhis sınırını ve takip zamanını yaz. Aracı yeniden çalıştırma; bir durum açıklaması üretince dur.
```

**Örnek çıktı**

“Sipariş aramasında kayıt bulunmadı; eşitleme kuyruğunda bekliyor. Sonraki otomatik deneme 14.30. Silindiğine dair kanıt yok.”

**Ne elde ettik?**

Başarısız sorgu ile asıl neden birbirine karıştırılmadı.

## Nerede durmalı?

ReAct araç erişimi yaratmaz. Denetleyici izinleri ve çağrı bütçesini uygulamalıdır. Sabit adımlı prompt zincirinden farklı olarak sonraki eylem gözleme göre seçilir. İç düşünce dökümü istemek yerine karar, eylem, kaynak ve sonuç kaydı yeterlidir.

## Kaynaklar

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/html/2210.03629) — Yao, Shunyu; Zhao, Jeffrey; Yu, Dian; Du, Nan; Shafran, Izhak; Narasimhan, Karthik; Cao, Yuan. 2022-10-06; okunan sürüm 2023-03-10. Karar, eylem ve dış gözlemin dönüşümlü kullanıldığı ReAct mekanizmasını tanımlar; örnekler buraya ait sade uyarlamalardır. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
