# Self-Refine

İlk metni ayrı bir eleştiri çağrısından geçirip somut geri bildirimle düzeltin.

## Nedir?

Self-Refine üretim, geri bildirim ve revizyon çağrılarını birbirine bağlar. Aynı model farklı çağrılarda bu işleri yapabilir. Koordinatör özgün görevi, son metni ve geri bildirimi taşır; belirlenen ölçüt sağlanınca veya bütçe bitince durur.

Bu döngü model eğitimi değildir. Modelin kendi eleştirisi yanlış olabilir; özellikle yeni kanıt gelmeyen olgusal sorularda tekrar düşünmek doğruluğu garanti etmez.

## Ne zaman işe yarar?

Yazı açıklığı, biçim koşulu veya test edilebilir küçük bir değişiklik için kullanabilirsiniz. Önce “daha iyi” yerine denetlenebilir bir ölçüt seçin.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir duyuru, başvuruyla kesin kaydı karıştırıyor.

**Prompt**

```text
Koordinatör üç ayrı çağrı yapar.
1. Üret: “Form başvuru toplar; yer e-postayla kesinleşir. Bir duyuru cümlesi yaz.”
2. Görev ve ilk metni taşı: “Başvuru/onay ayrımını denetle. Yalnız somut kusuru ve düzeltme yönünü yaz.”
3. Görev, metin ve eleştiriyi taşı: “Bu kusuru gidererek tek cümle yaz.”
İnsan son cümlede onay koşulunu kontrol eder. Üç çağrı sonunda yeni tur açma.
```

**Örnek çıktı**

Temsili ilk metin: “Formu doldurun, yeriniz hazır.” Eleştiri: form kesin kayıt gibi görünüyor. Revizyon: “Formdan başvurun; yeriniz onay e-postasıyla kesinleşir.”

**Ne elde ettik?**

Eleştiri, değişen cümleye bağlandı. Kaynaktaki koşulun gerçekten doğru olduğunu insan denetler.

### Orta (Medium)

**Durum**

Metin kısalırken zorunlu bilgi kayboluyor.

**Prompt**

```text
Kaynak: Atölye ücretsiz; defter katılımcıdan, kalem sağlanıyor. Hedef: en fazla 25 sözcük.
Üretim çağrısından sonra ayrı eleştiri çağrısına kaynak, hedef ve metni ver. Ücret/defter/kalem bilgilerinin her birini var-yok diye denetlet.
Revizyon çağrısına aynı paket ve denetim sonucunu ekle. Yalnız eksik bilgiyi tamamlat; yeni ayrıntı isteme.
İnsan sözcük sayısını ve üç koşulu kontrol eder. Bir revizyonla bitir; sığmıyorsa kısıt çelişkisini bildir.
```

**Örnek çıktı**

Temsili revizyon: “Atölye ücretsizdir. Defterinizi getirin; kalemler atölyede sağlanır.”

**Ne elde ettik?**

Kısaltma ölçütü doğruluk koşulunun önüne geçmedi. Gerçek metnin sözcük sayısı ayrıca sayılabilir.

### İleri (Hard)

**Durum**

İlk revizyon yeni bir hata ekliyor; döngü sınırlı kalmalı.

**Prompt**

```text
Kaynak: Kayıt e-postayla onaylanır; saat henüz belli değil. İlk taslak “Kayıt formu yeterlidir.”
Eleştiri çağrısı yalnız kaynak uyuşmazlığını bulsun. Revizyon çağrısı kaynak ve eleştiriyle düzeltme yapsın.
Koordinatör revizyonu yeniden kaynağa karşı kontrol ettirsin. Revizyonda “Cumartesi 10.00” gibi yeni tarih görülürse bir son düzeltme istesin: “Kaynakta olmayan zamanı çıkar.”
En fazla iki revizyon; ikinci denetimde de kusur varsa insan incelemesine bırak. Geçmiş kusur ve kaynak her revizyona taşınsın.
```

**Örnek çıktı**

Temsili ara revizyon: “Cumartesi 10.00 için kaydınız e-postayla onaylanır.” Yeni kusur: saat uydurulmuş. Son metin: “Kaydınız e-postayla onaylanır; saat henüz belli değildir.”

**Ne elde ettik?**

Revizyonun yeni hata üretmesi de denetlendi. Sonsuz düzeltme döngüsü yerine belirli bir durma sınırı var.

## Nerede durmalı?

Self-Debug program davranışını inceler; Rubber Duck’ta açıklayan insandır. Constitutional AI kaynağındaki ilkeye göre eleştiri/revizyon benzer görünebilir, fakat özgün Constitutional AI ayrıca supervised fine-tuning ve RLAIF içerir; bu üç çağrı o eğitimi yapmaz.

## Kaynaklar

- [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/html/2303.17651) — Madaan, Aman; Tandon, Niket; Gupta, Prakhar; Hallinan, Skyler; Gao, Luyu; Wiegreffe, Sarah; Alon, Uri; Dziri, Nouha; Prabhumoye, Shrimai; Yang, Yiming; Gupta, Shashank; Majumder, Bodhisattwa Prasad; Hermann, Katherine; Welleck, Sean; Yazdanbakhsh, Amir; Clark, Peter. 2023-03-30; okunan sürüm 2023-05-25. Üret–geri bildirim–revize et çağrılarını ve geçmiş aktarımını tanımlar; yedi görevdeki sonuçlar bütün öz eleştiri biçimlerinin başarısı değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
- [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/html/2310.01798) — Huang, Jie; Chen, Xinyun; Mishra, Swaroop; Zheng, Huaixiu Steven; Yu, Adams Wei; Song, Xinying; Zhou, Denny. 2023-10-03; okunan sürüm 2024-03-14. Yeni dış geri bildirim olmadan öz düzeltmenin sınırlı ve başlangıç düzenine bağlı olabileceğini gösterir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
- [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/html/2212.08073) — Bai, Yuntao; Kadavath, Saurav; Kundu, Sandipan; Askell, Amanda; Kernion, Jackson; Jones, Andy; Chen, Anna; Goldie, Anna; Mirhoseini, Azalia; McKinnon, Cameron; Chen, Carol; Olsson, Catherine; Olah, Christopher; Hernandez, Danny; Drain, Dawn; Ganguli, Deep; Li, Dustin; Tran-Johnson, Eli; Perez, Ethan; Kerr, Jamie; Mueller, Jared; Ladish, Jeffrey; Landau, Joshua; Ndousse, Kamal; Lukosuite, Kamile; Lovitt, Liane; Sellitto, Michael; Elhage, Nelson; Schiefer, Nicholas; Mercado, Noemi; DasSarma, Nova; Lasenby, Robert; Larson, Robin; Ringer, Sam; Johnston, Scott; Kravec, Shauna; Showk, Sheer El; Fort, Stanislav; Lanham, Tamera; Telleen-Lawton, Timothy; Conerly, Tom; Henighan, Tom; Hume, Tristan; Bowman, Samuel R.; Hatfield-Dodds, Zac; Mann, Ben; Amodei, Dario; Joseph, Nicholas; McCandlish, Sam; Brown, Tom; Kaplan, Jared. 2022-12-15. İlkeye bağlı eleştiri/revizyon ile model eğitimi aşamalarını birlikte tanımlar; yalnız sohbet döngüsüne indirgenemez. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
