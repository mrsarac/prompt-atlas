# Zero-shot CoT

Çözülmüş örnek vermeden kısa ara sonuçlar isteyin; son cevabı ayrı çıkarın.

## Nedir?

Zero-shot CoT, örnek çözüm sağlamadan modeli aşamalı çözüm üretmeye yönlendirir. Kojima ve arkadaşlarının özgün düzeni iki aşamalıdır: önce çözüm üretimi, ardından bu çıktıdan cevap çıkarımı. İki aşamayı tek bir sloganla eşitlememek gerekir.

Aşağıdaki uyarlamalarda ara çıktı yalnız kısa eşitlik veya kontrol noktalarıdır. Çağrıları siz başlatabilir, ilk cevabı ikinci çağrıya taşıyabilirsiniz. Bu işlem gizli düşünce kaydı istemeyi gerektirmez.

## Ne zaman işe yarar?

Örnek hazırlamadığınız küçük problemler veya nihai cevabın belirli bir biçimde alınması gereken durumlarda kullanılabilir. Aynı yanlışı ikinci aşama da taşıyabilir.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir kitaplıkta kalan kitapları hesaplayacaksınız.

**Prompt**

```text
İnsan başlatır; iki ayrı model çağrısı kullanır.
Çağrı 1: “Rafta 18 kitap var. 7 kitap alınıyor, 4 kitap ekleniyor. Kısa eşitlik ve kalan kitap sayısını yaz.”
Çağrı 2: İlk çıktıyı aynen ekle ve “Bu çözümden yalnız kalan kitap sayısını çıkar; yeni hesap veya bilgi ekleme” de.
İkinci yanıt tek sayı değilse kabul etme; en fazla bu iki çağrı. Hesabı ayrıca kontrol et.
```

**Örnek çıktı**

Birinci çağrı: 18−7+4=15 kitap. İkinci çağrı: 15.

**Ne elde ettik?**

Çözüm üretimi ve cevap biçimleme ayrı oldu. İkinci çağrı ilk hesabı bağımsız doğrulamış sayılmaz.

### Orta (Medium)

**Durum**

Bir rezervasyonda kişi ve masa sayısı ayrılıyor.

**Prompt**

```text
Koordinatör iki çağrı yapar.
1: “23 kişi geliyor. Her masada en fazla 6 kişi oturabilir. Gereken masa sayısını kısa bölme ve kapasite kontrolüyle ver. Kısmi masayı da tam masa say.”
2: İlk çıktıyı taşı: “Yalnız masa sayısını ve son masadaki kişi sayısını yaz.”
Kontrol: bütün insanlar bir masaya yerleşmiş olmalı. İki çağrı sonunda kapasite tutmuyorsa kesin plan verme.
```

**Örnek çıktı**

İlk çıktı: 3 masa 18 kişiyi alır; kalan 5 kişi için bir masa gerekir. Son çıktı: 4 masa; son masada 5 kişi.

**Ne elde ettik?**

Yuvarlama gereği görünür. Gerçek mekândaki masa düzeni bu sayısal örneğin dışında kalır.

### İleri (Hard)

**Durum**

Kargoyu belirlemek için indirim tabanı eksik; iki çağrı kesin sayı üretmemeli.

**Prompt**

```text
İnsan iki çağrı başlatır.
1: “Ürün 600 TL; indirim 100 TL. Kargo eşiği 550 TL; eşik altında kargo 40 TL. Eşiğin indirim öncesi mi sonrası mı uygulandığı belirtilmiyor. Olası iki hesabı kısa yaz; kesin toplam seçme.”
2: İlk çıktı ve özgün soruyu ekle: “Son cevapta olası toplamları ve tek eksik kuralı koru. Bilinmeyeni tahminle kapatma.”
Durma: ikinci yanıt sonrası mağaza kuralı kullanıcıdan beklenir; üçüncü bir tahmin çağrısı yapma.
```

**Örnek çıktı**

Önceki tutara göre eşik: 600≥550, toplam 500 TL. Sonraki tutara göre: 500<550, toplam 540 TL. Eksik bilgi: kargo eşiğinin hangi tutara uygulandığı.

**Ne elde ettik?**

Yanıt çıkarımı belirsizliği silmedi. Kesin sonuç için gerekli tek kural açık kaldı.

## Nerede durmalı?

“Adım adım düşün” cümlesi doğru hesap garantisi değildir. Özgün deneyler belirli eski model ve görevlerle yapılmıştır. Örnekli CoT farklı bir girdi düzeni kullanır; PAL hesaplamayı gerçek yorumlayıcıya devreder.

## Kaynaklar

- [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/html/2205.11916) — Kojima, Takeshi; Gu, Shixiang Shane; Reid, Machel; Matsuo, Yutaka; Iwasawa, Yusuke. 2022-05-24; okunan sürüm 2023-01-29. Örneksiz çözüm üretimi ve cevap çıkarımı düzenini tanımlar; InstructGPT/PaLM koşulları güncel her modele genellenmez. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
- [Reasoning best practices | OpenAI API](https://developers.openai.com/api/docs/guides/reasoning-best-practices) — OpenAI. yayın tarihi doğrulanmadı. Belirli reasoning modellerinde ayrıca CoT istemenin gerekmeyebileceğini açıklar. Kanıt düzeyi: sayfa gövdesi.
