# Structured Outputs

Çıktı şemasını destekleyen API’ye verin; gelen verinin anlamını ayrıca kontrol edin.

## Nedir?

Structured Outputs, destekleyen bir model/API yolunda çıktı üretimini JSON Schema ile sınırlar. Şema, alanların türünü ve izin verilen değerleri tanımlar. “JSON yaz” istemi ve yalnız geçerli JSON üreten JSON mode, aynı şema sözleşmesini sağlamaz.

Uygulama API isteğini kurar, ret veya tamamlanmamış yanıtı ayırır, sonra sonucu işler. Şemaya uygun bir sayı yanlış olabilir. Aşağıdaki parçalar gerçek çağrı değil, uygulamaya yerleştirilecek somut istek ve kontrol taslaklarıdır.

## Ne zaman işe yarar?

Model cevabını programla okuyacaksanız kullanın. Desteklenen şema alt kümesini, model uyumluluğunu ve ret/hata yolunu önce kontrol edin; sohbet arayüzü her zaman bu ayarı sunmaz.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Destek iletisini tek etikete ayıracak API uygulaması hazırlıyorsunuz.

**Prompt**

```text
Uygulama, Structured Outputs destekleyen modelle Responses API isteğinde input ve text.format alanlarını gönderir:
input: “İleti: Hesabıma giriş yapamıyorum. Konuyu etiketle.”
text.format:
{"type":"json_schema","name":"ticket","strict":true,"schema":{"type":"object","properties":{"etiket":{"type":"string","enum":["erisim","fatura","belirsiz"]}},"required":["etiket"],"additionalProperties":false}}
İstemci model kimliğini kendi doğrulanmış yapılandırmasından alır. Bir çağrı yapar; önce API hatası, refusal ve incomplete durumunu kontrol eder. Yalnız tamamlanmış şema çıktısını ayrıştırır. Ret varsa etiket uydurmaz.
```

**Örnek çıktı**

Temsili kabul edilebilir gövde: `{"etiket":"erisim"}`. `{"etiket":"diger"}` bu şemaya uymaz.

**Ne elde ettik?**

Programın beklediği değerler belli. Gerçek API çağrısı yapılmadan şema zorlamasının çalıştığı iddia edilemez.

### Orta (Medium)

**Durum**

Bir saat metninde kapanış bilinmiyor; alanın kaybolmasını istemiyorsunuz.

**Prompt**

```text
Input: “Not: Salon saat 10.00’da açılır. Kapanış belirtilmemiş. Bilinmeyen kapanışı null yaz.”
Desteklenen API’nin text.format ayarı:
{"type":"json_schema","name":"hours","strict":true,"schema":{"type":"object","properties":{"acilis":{"type":"string"},"kapanis":{"type":["string","null"]}},"required":["acilis","kapanis"],"additionalProperties":false}}
Uygulama tek çağrı yapar; ret/kesilmede kaydı kaydetmez. Şemayı okuduktan sonra saat dizgesinin geçerli HH.MM biçiminde olduğunu kendi koduyla denetler. Kaynakta olmayan saati kabul etmez.
```

**Örnek çıktı**

Temsili gövde: `{"acilis":"10.00","kapanis":null}`.

**Ne elde ettik?**

Eksik bilgi ile eksik alan ayrıldı. Şema string türünü sınırlasa da saat anlamının doğruluğu uygulamanın kontrolüdür.

### İleri (Hard)

**Durum**

Şemaya uygun sayı kaynağa aykırı olabilir.

**Prompt**

```text
Input: “Kaynak K1: Kapasite 16 kişi. Yalnız kaynak kodunu ve kapasiteyi çıkar.”
text.format:
{"type":"json_schema","name":"capacity","strict":true,"schema":{"type":"object","properties":{"kaynak":{"type":"string","enum":["K1"]},"kapasite":{"type":"integer"}},"required":["kaynak","kapasite"],"additionalProperties":false}}
Koordinatör en fazla iki deneme yapar. İlk tamamlanmış yanıtın kapasitesini K1 ile karşılaştırır. Uyuşmazsa aynı kaynak ve somut farkla bir düzeltme çağrısı yapar; ikinci uyuşmazlıkta insan incelemesine ayırır. Hata/ret veya kesilmeyi başarı nesnesine dönüştürmez.
```

**Örnek çıktı**

Temsili ilk yanıt `{"kaynak":"K1","kapasite":60}` biçimce uygun, anlamca yanlış. Temsili düzeltme `{"kaynak":"K1","kapasite":16}`; kabul için K1 eşlemesi gerekir.

**Ne elde ettik?**

Şema denetimi ile kaynak denetimi iki ayrı kapı oldu. Otomatik yeniden deneme için de somut bütçe var.

## Nerede durmalı?

Strict ayarını prompt metninin içine yazmak API’de etkinleştirmez. Sağlayıcının desteklediği şema özellikleri ve yanıt hata biçimleri değişebilir. Tool calling eylem seçimi için, yapılandırılmış metin ise veri cevabı için kullanılır; hiçbiri eylem yetkisini kendiliğinden vermez.

## Kaynaklar

- [Structured model outputs | OpenAI API](https://developers.openai.com/api/docs/guides/structured-outputs) — OpenAI. yayın tarihi doğrulanmadı. Desteklenen JSON Schema ile Structured Outputs, JSON mode, ret ve tamamlanmamış yanıt ayrımlarını açıklar; içerik doğruluğunu garanti etmez. Kanıt düzeyi: sayfa gövdesi.
