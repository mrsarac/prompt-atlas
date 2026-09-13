# Atıf sözleşmesi

Her iddiayı onu gerçekten destekleyen pasajla eşleyin.

## Nedir?

Atıf sözleşmesi, cevabın hangi belgeye dayandığını görünür kılan çıktı kuralıdır. Model iddianın yanına kaynak kodu ekler; okur o pasajı açıp ilişkiyi kontrol edebilir. Kaynakta bulunmayan bir iddiaya kod iliştirmek, onu desteklenmiş yapmaz.

Belgeler zaten elinizdeyse bu görev yalnız kaynakla cevap yazmadır. RAG ayrıca ilgili belgeyi bulup getiren aşamayı içerir. Burada arama yapmış gibi davranmıyoruz.

## Ne zaman işe yarar?

Belge özeti, araştırma notu ve koşulları kaynaklarıyla açıklama işlerinde kullanın. Her belgenin kısa kodu ve okunabilir gövdesi olmalı.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Çalışma odasının kapanışını kısa nottan çıkaracaksınız.

**Prompt**

```text
Soru: Okuma odası kaçta kapanır?
[K1] Okuma odası hafta içi 09.00–17.00 açıktır.
Yalnız K1’i kullan. Yanıtın yanına kaynak kodunu koy ve destekleyen cümleyi kısa alıntıla. Hafta sonu hakkında bilgi ekleme.
```

**Örnek çıktı**

Hafta içi 17.00’de kapanır. [K1] Dayanak: “hafta içi 09.00–17.00 açıktır.”

**Ne elde ettik?**

Saatin hangi pasajdan geldiği belli. Kaynak kodu, odanın gerçek güncel saatini bağımsız doğrulamaz.

### Orta (Medium)

**Durum**

İki belge, kayıt ve malzemeyi ayrı açıklıyor.

**Prompt**

```text
Soru: Atölyeye nasıl kaydolurum; defter ve kalem gerekir mi?
[K1] Formu doldurun. Yeriniz onay e-postasıyla kesinleşir.
[K2] Defterinizi getirin; kalemler atölyede sağlanır.
Her bağımsız bilgiye doğru kodu ekle. Tek kodu bütün paragrafın kanıtı gibi kullanma. Belgede olmayan süre veya ücret bilgisi ekleme.
```

**Örnek çıktı**

Formla başvurun; yeriniz onay e-postasıyla kesinleşir. [K1] Defterinizi getirin; kalemler sağlanır. [K2]

**Ne elde ettik?**

Her cümlenin dayanağı ayrı izlenebiliyor. K1’in malzeme koşulunu desteklediği izlenimi oluşmuyor.

### İleri (Hard)

**Durum**

Taslak bir cümle, iki kaynaktan daha güçlü sonuç çıkarıyor.

**Prompt**

```text
Taslak: “Atölye bütün katılımcılara ücretsiz malzeme ve sonradan video kaydı sağlar.”
[K1] Katılım ücretsizdir.
[K2] Katılımcılar kendi defterini getirir; kalemler sağlanır.
Her iddiayı destekli / çelişkili / kaynakta yok diye ayır. Sonra yalnız desteklenen bilgilerle yeni metin yaz. Video kaydı yok diye kesin hüküm kurma; bilgi bulunmadığını söyle.
```

**Örnek çıktı**

Katılımın ücretsizliği destekli [K1]. Bütün malzemenin sağlanması çelişkili [K2]. Video kaydı kaynakta yok. Yeni metin: “Katılım ücretsizdir. [K1] Defterinizi getirin; kalemler sağlanır. [K2] Video kaydı hakkında bu belgelerde bilgi bulunmuyor.”

**Ne elde ettik?**

İddia gücü kaynakla sınırlandı. Eksik bilgi ile olumsuz bilgi birbirine karışmadı.

## Nerede durmalı?

Atıf kalitesi, cevap doğruluğu ve kaynağın kendi güvenilirliği ayrı şeylerdir. Model doğru kaynağı yanlış iddiaya bağlayabilir. ALCE bunları değerlendiren bir araştırma düzenidir; burada yazdığımız kısa sözleşme onun bütün sistemini yeniden kurmaz.

## Kaynaklar

- [Enabling Large Language Models to Generate Text with Citations](https://arxiv.org/html/2305.14627) — Gao, Tianyu; Yen, Howard; Yu, Jiatong; Chen, Danqi. 2023-05-24; okunan sürüm 2023-10-31. ALCE akıcılık, doğruluk ve atıf kalitesini ayrı değerlendirir; kaynak kodunun tek başına yeterli olmadığını destekler. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
- [Prompt engineering | OpenAI API](https://developers.openai.com/api/docs/guides/prompt-engineering?api-mode=responses) — OpenAI. yayın tarihi doğrulanmadı. Verilen bağlam ve çıktı talimatlarını açık belirtmeye dayanak sağlar. Kanıt düzeyi: sayfa gövdesi.
