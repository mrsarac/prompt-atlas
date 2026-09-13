# Hatırlama alıştırması

Cevabı görmeden hatırla, sonra kaynakla karşılaştır.

## Nedir?

Hatırlama alıştırması, bilgiyi yeniden okumadan önce zihinden geri çağırmaktır. Model soru hazırlayabilir ve yanıtı kaynakla karşılaştırabilir; hatırlayan insan olmalıdır. Modelin kendi sorusunu kendi yanıtlaması aynı öğrenme etkinliği değildir.

## Ne zaman işe yarar?

Bir konuyu okurken tanıdık buluyor ama kitaba bakmadan anlatamıyorsanız.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

HTTP durum kodlarını çalışacaksınız.

**Prompt**

```text
Kaynak not: 200 istek başarılı; 404 istenen kaynak bulunamadı; 500 sunucuda hata.
Bana bu nottan tek açık uçlu soru sor. Cevabı aynı mesajda gösterme; yanıtımı bekle. Sonra notla karşılaştır, yalnız eksik veya yanlış kısmı düzelt. İki soruda dur. Ben yanıtlarken kaynak notunu kapatacağım.
```

**Örnek çıktı**

Model: “İstenen kaynak bulunamadığında hangi kodu beklersin?” İnsan: “404.” Model: “Notla eşleşiyor.”

**Ne elde ettik?**

Tanıma yerine cevabı kaynaksız geri çağırma denendi.

### Orta (Medium)

**Durum**

Ezberlenen tanımı yeni örneğe uygulayacaksınız.

**Prompt**

```text
Kaynak: Ortalama hız toplam yolun toplam süreye bölümüdür; hızların basit ortalaması her zaman doğru değildir.
Önce tanımı kaynağa bakmadan söylememi iste. Sonra farklı bir uygulama sorusu sor: 90 km yol 3 saatte alınırsa ortalama hız?
Her soruda cevabımı bekle; ipucu verirsen yardım verildiğini not et. Son geri bildirim tanım, işlem ve birimi ayrı kontrol etsin. Doğru cevabı önümde tutarak tekrar ettirme.
```

**Örnek çıktı**

İnsan: “Toplam yol / toplam süre; 90/3=30 km/saat.” Geri bildirim üç alanın da uygun olduğunu söyler.

**Ne elde ettik?**

Tanım hatırlama ile basit uygulama ayrı ayrı kontrol edildi.

### İleri (Hard)

**Durum**

Yanlış sorular yanlış bilgiyi pekiştirebilir.

**Prompt**

```text
Öğretmen için soru hazırlama düzeni. Kaynak kural: 500 TL ve üzeri kargo ücretsiz, altı 50 TL.
Model üç soru ve ayrı cevap anahtarı üretsin: kuralı hatırlama, 500 sınırı, 499 uygulaması. Öğretmen anahtarı kaynakla kontrol etmeden öğrenciye sunulmasın.
Öğrenci sürümünde cevap anahtarı gizli kalsın. Her yanıtın yardımsız mı ipuçlu mu olduğunu kaydet; yanlışta kısa kaynaklı düzeltme ver. Sonunda aynı sayıları tekrar ettirmek yerine 501 için yeni soru sor.
En fazla dört soru; bu oturumu uzun dönem öğrenme ölçümü diye sunma.
```

**Örnek çıktı**

Öğretmen anahtarı: “eşik dahil; 500→0; 499→50; 501→0.” Öğrenci yalnız soruları sırayla görür.

**Ne elde ettik?**

Soru kalitesi, cevap sızıntısı ve yardım düzeyi denetlenen bir alıştırma oluştu.

## Nerede durmalı?

Geri bildirim önemli olabilir ama kaynağı yanlışsa hata pekişir. İnsan hatırlama araştırması LLM üretimi her sorunun kaliteli olduğunu kanıtlamaz. Ders içi kısa başarı, günler sonra yardımsız hatırlamayla aynı ölçüm değildir.

## Kaynaklar

- [Test-enhanced learning: taking memory tests improves long-term retention](https://pubmed.ncbi.nlm.nih.gov/16507066/) — Henry L. Roediger III; Jeffrey D. Karpicke. 2006-03. İnsanlarda test yoluyla geri çağırma ile sonraki hatırlama ilişkisini inceler; burada yalnız özet ve künye okunmuştur. Kanıt düzeyi: özet ve künye.
- [Enhancing Student Learning with LLM-Generated Retrieval Practice Questions: An Empirical Study in Data Science Courses](https://arxiv.org/html/2507.05629) — An, Yuan; Liu, John; Acharya, Niyam; Hashmi, Ruhma. 2025-07-08; okunan sürüm 2025-07-29. LLM tarafından hazırlanan hatırlama sorularını ders bağlamında inceleyen yarı deneysel çalışmadır; öğretmen doğrulaması ihtiyacını açıkça belirtir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
