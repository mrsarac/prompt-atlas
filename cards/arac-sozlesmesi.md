# Araç ve sonuç sözleşmesi

Araca ne verileceği kadar, geri ne geleceğini de tanımla.

## Nedir?

Araç sözleşmesi; işlevin ne yaptığı, kabul ettiği girdiler, yan etkileri ve sonuç biçimidir. Model uygun çağrıyı seçer; uygulama girdiyi denetler ve aracı çalıştırır. İyi yazılmış bir araç açıklaması, olmayan bir yetkiyi var etmez.

## Ne zaman işe yarar?

Aynı görünen araçların karıştığı, hataların başarı gibi okunduğu veya bir işlem sonucunun teyit edilmesi gereken uygulamalarda.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir ajanın ürün stok bilgisini okumasını istiyorsunuz.

**Prompt**

```text
Uygulama sözleşmesi: stock_read(sku: string), salt okunur. Çıktı: {status:"ok", sku, available: integer, checked_at} veya {status:"not_found", sku}. Negatif stok ve boş sku reddedilir.
Kullanıcı: Mavi defter D7 var mı?
Model: Yalnız stock_read("D7") çağrısı öner. Uygulama şemayı denetleyip çalıştırsın.
Temsili dönüş: {status:"ok", sku:"D7", available:3, checked_at:"10:00"}
Sonraki çağrıya bu dönüşü aynen ver. Model bir cümleyle durumu bildirsin; ayırma veya satın alma yapmasın. Bir okuma sonunda dur.
```

**Örnek çıktı**

“D7 için saat 10.00 kontrolünde 3 adet stok görünüyor.”

**Ne elde ettik?**

Stok sorgusuyla rezervasyonun farklı işler olduğu korundu.

### Orta (Medium)

**Durum**

Arama sonucu boş olabilir; ağ hatasıyla karışmamalı.

**Prompt**

```text
Denetleyici: search_docs(query, limit), limit 1..5. Yanıt ya {status:"ok", hits:[{id,title,excerpt}]} ya {status:"error", code, retryable}.
Görev: İade süresi hakkında belge bul. İlk çağrı search_docs("iade süresi", 3).
Temsili dönüş: {status:"error", code:"timeout", retryable:true}.
Model: "Belge yok" deme. Denetleyici aynı çağrıyı en fazla bir kez tekrar etsin; ikinci sonuç {status:"ok",hits:[]} ise yalnız bu aramada eşleşme olmadığını söyle. Durum ve çağrı sayısını sonraki modele aktar; 2 çağrıda dur.
```

**Örnek çıktı**

“İlk istek zaman aşımına uğradı. Tekrar edilen arama tamamlandı, bu sorguda eşleşme bulunmadı.”

**Ne elde ettik?**

Veri yokluğu ile teknik hata ayrı tutuldu.

### İleri (Hard)

**Durum**

Yan etkili bir taslak kaydı, tekrar çağrıda iki kez oluşmamalı.

**Prompt**

```text
Bu bir uygulama tasarım örneğidir; gerçek kayıt gönderme.
İzin: Yalnız taslak oluşturma; yayınlama yok. create_draft(title, body, idempotency_key) anahtarı uygulama üretir ve kalıcı saklar.
Girdi: title="Atölye", body="12 Ekim, saat 14.00", key="job-42".
Denetleyici: İnsan bu içeriği onayladıktan sonra şemayı doğrula, tek çağrı çalıştır. Bağlantı kesilirse yeni anahtar üretme; aynı anahtarla sonuç sorgula/sağlayıcının belgelenmiş tekrar davranışını kullan.
Beklenen dönüş: {status:"created" veya "existing", draft_id:"D42", published:false}.
Model: draft_id ile yalnız taslak durumunu bildir. Sonuç belirsizse başarı deme; insan incelemesine bırak ve dur.
```

**Örnek çıktı**

“D42 taslağı mevcut; yayımlanmadı.” Bağlantı belirsizliğinde: “Kayıt durumu doğrulanamadı; ikinci taslak oluşturulmadı.”

**Ne elde ettik?**

Sözleşme, biçimin yanında tekrar ve yan etki davranışını da kapsadı.

## Nerede durmalı?

Idempotency gibi garantiler prompttan değil gerçek sunucu uygulamasından gelir. JSON istemek katı şema uygulamak değildir. Araç adı, izin denetimi, hata türleri ve ölçülebilir testler birlikte düşünülmelidir.

## Kaynaklar

- [Writing effective tools for AI agents—using AI agents \ Anthropic](https://www.anthropic.com/engineering/writing-tools-for-agents) — Anthropic. 2025-09-11. Araç açıklaması, anlamlı yanıt ve değerlendirme tasarımını destekler; örnekteki idempotency sözleşmesi uygulama tasarımı uyarlamasıdır, kaynağın hazır API’si değildir. Kanıt düzeyi: sayfa gövdesi.
