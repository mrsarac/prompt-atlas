# Yapılandırılmış harici notlar

Hatırlanması gereken durumu sohbetin dışında, kaynaklı bir notta tut.

## Nedir?

Yapılandırılmış dış notlar, bir ajanın veya insanın sonraki oturumda okuyabileceği kalıcı çalışma kaydıdır. Modelin ağırlıklarını değiştirmez. Notun yazılması, saklanması ve geri okunması uygulama veya insan tarafından gerçekten yapılmalıdır.

## Ne zaman işe yarar?

Günlere yayılan araştırma, içerik veya kod işlerinde; karar, açık soru ve kanıtın oturumdan uzun yaşaması gerekiyorsa.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir sonraki yazım oturumuna kısa not bırakacaksınız.

**Prompt**

```text
İnsan başlatır. Bugünkü durum: konu bisiklet bakımı; hedef yeni başlayanlar; zincir temizliği bölümü yazıldı; fren bölümü eksik.
Model şu alanlarla bir Markdown notu üret: hedef, tamamlanan, açık iş, doğrulanmamış bilgi.
İnsan notu proje-notu.md olarak gerçekten kaydetsin ve tekrar açıp kontrol etsin. Sonraki oturumda dosyanın içeriğini yeni çağrıya eklesin.
Yeni çağrı: Yalnız açık işi öner; dosyayı görmediysen gördüm deme. Not ve bir sonraki adım hazır olunca dur.
```

**Örnek çıktı**

“Tamamlanan: zincir temizliği taslağı. Açık: fren bölümü. Sonraki adım: bu bölüm için kapsam ve kaynak belirlemek.”

**Ne elde ettik?**

“Bunu hatırla” demenin yerine yeniden okunabilir bir kayıt oluştu.

### Orta (Medium)

**Durum**

Araştırma notunda kaynakla yorumun karışmasını istemiyorsunuz.

**Prompt**

```text
Uygulama: notes_read ve notes_write yalnız bu projede; en fazla bir okuma ve bir yazma.
Mevcut kayıt: claim C1="Müze pazartesi kapalı", source D1="Resmi saat çizelgesi, 1 Eylül", status=verified_against_D1.
Yeni bilgi: Kullanıcı "Bayramda farklı olabilir" dedi; kaynak vermedi.
Model: C1'i silme. Yeni satırı assumption A1 olarak, kaynağı kullanıcı ifadesi ve durumu unverified olacak şekilde ekle. Uygulama kayıt şemasını denetlesin, kaydetsin ve yazma sonucunu geri versin. Yalnız başarılı kayıt yanıtından sonra kaydedildi de; sonra dur.
```

**Örnek çıktı**

“A1: Bayramda saatler değişebilir; doğrulanmadı. C1 olağan pazartesi saatine ilişkin kayıt olarak korundu.”

**Ne elde ettik?**

Yeni ihtimal, kaynaklı bulgunun üstüne yazılmadı.

### İleri (Hard)

**Durum**

İki oturum aynı karar kaydını güncelleyebilir.

**Prompt**

```text
Denetleyici sürümlü not saklasın. v3: hedef 400 kelime; açık iş kaynak kontrolü.
Ajan v3'ü okudu. İnsan bu arada v4'te hedefi 600 yaptı. Ajanın önerisi: kaynak kontrolü tamamlandı; dayanak D7.
Yazma kuralı: expected_version=3 ile güncelleme reddedilsin; v4 tekrar okunsun. Model yalnız kendi kanıtlı değişikliğini v4'e birleştirsin, 600 hedefini korusun. D7 erişilemiyorsa "tamamlandı" eklenmesin.
En fazla bir yeniden okuma/birleşim; tekrar çatışırsa insan incelemesine bırak. Uygulama onaylı v5'i döndürürse bitir.
```

**Örnek çıktı**

“v5: hedef 600 kelime; kaynak kontrolü D7’ye göre tamamlandı.” Kaynak erişimi yoksa açık iş olarak kalır.

**Ne elde ettik?**

Not, son yazanın bütün geçmişi ezdiği bir hafıza yerine denetlenen bir kayıt oldu.

## Nerede durmalı?

Kalıcı not, kalıcı doğruluk demek değildir. Tarih, kaynak, kapsam ve geçersiz kalan kararlar görünür olmalı. Compaction mevcut bağlamı küçültür; dış not sonraki oturumlarda geri alınacak durumu saklar. Hassas verileri gereksiz yere kalıcılaştırmayın.

## Kaynaklar

- [Effective context engineering for AI agents \ Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Anthropic. 2025-09-29. Structured note-taking ile oturum dışında tutulan notların tekrar bağlama alınmasını anlatır; sürüm çakışması örneği bu ilkenin uygulama tasarımıdır. Kanıt düzeyi: sayfa gövdesi.
