# Prompt üreten meta prompt

Modelden işi çözmesini değil, o işte kullanılacak talimatı yazmasını isteyin.

## Nedir?

Genel kullanımda meta prompt, başka bir prompt üreten veya düzenleyen istektir. Siz hedefi ve sınırları verirsiniz; model kullanılabilir talimat taslağını çıkarır. Bu taslağın kalitesini hedef görev üzerinde ayrıca denetlersiniz.

Bir kere prompt yazdırmak APE veya OPRO gibi ölçümle aday seçen optimizasyon süreçlerinin tamamı değildir. Burada otomatik başarı puanı icat etmiyoruz.

## Ne zaman işe yarar?

Aynı işi tekrar edecekseniz veya dağınık isteği açık bir görev metnine çevirmek istiyorsanız kullanın. Eksik gereksinimi modelin sizin adınıza kararlaştırmasına izin vermeyin.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Atölye duyuruları için tekrar kullanılacak kısa talimat istiyorsunuz.

**Prompt**

```text
Duyurunun kendisini yazma; duyuru yazdıracak promptu oluştur.
Gereksinimler: Türkçe, iki cümle, yalnız verilen bilgiler, form başvuru; yer onay e-postasıyla kesinleşir. Eksik tarih eklenmez.
Örnek kullanım verisi: Çizim atölyesi, 20 kişi, tarih henüz belli değil.
Çıktıda prompt ve bu örnek verisini birlikte ver; sonra dur.
```

**Örnek çıktı**

Temsili prompt: “20 kişilik çizim atölyesi için iki Türkçe cümle yaz. Formun başvuru olduğunu, yerin onay e-postasıyla kesinleştiğini belirt. Tarih belli değil; ekleme.”

**Ne elde ettik?**

Doğrudan kullanılacak bir talimat var. Henüz bu talimatla modelin nasıl cevap vereceği test edilmedi.

### Orta (Medium)

**Durum**

Eski prompt, kaynakta olmayan ayrıntılar ekletiyor.

**Prompt**

```text
Eski prompt: “Bu etkinliği heyecanlı ve ayrıntılı tanıt.”
Sorun: “Atölye ücretsiz” kaynağından tarih ve malzeme desteği uyduruluyor.
Promptu yeniden yaz. Amaç tanıtım kalsın; yalnız kaynak bilgisini kullanma ve eksik alanı belirtme koşulu eklensin. Örnek kaynak “Atölye ücretsizdir.” olsun. Çıktı: yeni tam prompt ve değişikliğin tek gerekçesi. Tanıtım metnini şimdi üretme.
```

**Örnek çıktı**

Yeni prompt: “Kaynak: Atölye ücretsizdir. Bu bilgiyle kısa tanıtım yaz. Tarih, yer ve malzeme desteği verilmemiş; bunları ekleme. Gerekirse bu alanların henüz belirtilmediğini söyle.”

**Ne elde ettik?**

Talimatın hedeflediği hata belli. Sonradan aynı kaynak üzerinde çıktı alınarak düzeltmenin etkisi kontrol edilmelidir.

### İleri (Hard)

**Durum**

İki prompt sürümünün kapsamı farklı; birleşimde yetki artmamalı.

**Prompt**

```text
Prompt tasarımcısı olarak şu iki metni birleştir; görevi yürütme.
A: “Yalnız taslak.md dilini düzelt; kaynak.md salt okunur.”
B: “Bütün dokümanları düzenle; iş bitince yayımla.”
Geçerli kullanıcı sınırı: yalnız taslak.md, yayın yok. Amaç: kaynak anlamını koruyan dil düzeltmesi.
Yeni promptu tam yaz; kaldırılan çelişkileri iki kısa maddeyle belirt. Dosya okuma/yazma veya araç çağrısı yapma.
```

**Örnek çıktı**

Yeni prompt: “Kaynak anlamını koruyarak yalnız taslak.md için dil düzeltmesi öner. kaynak.md salt okunurdur. Diğer dokümanları değiştirme; yayın yapma. Sonuçta değişen ifadeleri ve kalan belirsizlikleri bildir.”

**Ne elde ettik?**

Birleştirme yetki genişletmedi. Talimat metni yine gerçek dosya izinleri ve çıktı kontrolüyle desteklenmelidir.

## Nerede durmalı?

Meta sözcüğü farklı araştırmalarda farklı anlam taşır. Uzman çağrılı Meta-Prompting bir orkestrasyon mimarisidir; yapısal Meta Prompting görev biçimini düzenler. Prompt üretmek bunlarla otomatik olarak aynı yöntem olmaz.

## Kaynaklar

- [The Prompt Report: A Systematic Survey of Prompt Engineering Techniques](https://arxiv.org/html/2406.06608v6) — Schulhoff, Sander; Ilie, Michael; Balepur, Nishant; Kahadze, Konstantine; Liu, Amanda; Si, Chenglei; Li, Yinheng; Gupta, Aayush; Han, HyoJung; Schulhoff, Sevien; Dulepet, Pranav Sandeep; Vidyadhara, Saurav; Ki, Dayeon; Agrawal, Sweta; Pham, Chau; Kroiz, Gerson; Li, Feileen; Tao, Hudson; Srivastava, Ashay; Da Costa, Hevander; Gupta, Saloni; Rogers, Megan L.; Goncearenco, Inna; Sarli, Giuseppe; Galynker, Igor; Peskoff, Denis; Carpuat, Marine; White, Jules; Anadkat, Shyamal; Hoyle, Alexander; Resnik, Philip. 2024-06-06; okunan sürüm 2025-02-26. Meta prompting ve prompt engineering terimlerinin kapsamını sınıflayan ikincil derlemedir; tek başına özgün etki kanıtı değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
- [Large Language Models are Human-Level Prompt Engineers](https://arxiv.org/html/2211.01910) — Zhou, Yongchao; Muresanu, Andrei Ioan; Han, Ziwen; Paster, Keiran; Pitis, Silviu; Chan, Harris; Ba, Jimmy. 2022-11-03; okunan sürüm 2023-03-10. Modelin aday talimat üretmesi için birincil örnek sağlar; APE ayrıca gerçek değerlendirme ve seçim yapar. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
- [Master Prompts and System Prompts: The ChatGPT-5 Growth Blueprint](https://www.danmartell.com/master-prompts-system-prompts-and-custom-gpts/) — Dan Martell. 2026-02-23; okunan sürüm 2026-02-23. Tekrar kullanılan master/system promptların pratisyen dilindeki kullanımını gösterir. Kanıt düzeyi: sayfa gövdesi.
