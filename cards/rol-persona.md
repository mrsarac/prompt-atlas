# Rol ve persona

Modelin hangi ayrıntıya, hangi okur için bakacağını belirtin.

## Nedir?

Rol vermek, bir metne bakılacak açı seçmektir. “Yeni başlayan okurun editörü” dediğinizde belirsiz terimlere; “test gözden geçiren geliştirici” dediğinizde sınır koşullarına odaklanmasını isteyebilirsiniz. Rolün işini somut fiillerle açıklamak, yalnız unvan yazmaktan daha denetlenebilirdir.

Bir uzman personası modele yeni bilgi, diploma veya araç erişimi kazandırmaz. Bir yanıt içinde üç karakter konuşturmak da üç bağımsız ajan çağrısı değildir.

## Ne zaman işe yarar?

Aynı metni farklı okurlar için düzenlerken veya belirli bir inceleme amacı seçerken kullanın. Rolün bakacağı nesneyi ve teslim edeceği değişikliği de verin.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Yeni katılımcılar “kayıt teyidi” ifadesini anlamıyor.

**Prompt**

```text
Başlangıç seviyesindeki okurun editörü gibi incele. Cümle: “Kayıt teyidi akabinde katılımınız aktive edilir.” Anlam: yer, onay e-postası gelince kesinleşir. Resmî sözcükleri sadeleştir; yeni koşul eklemeden tek cümle yaz.
```

**Örnek çıktı**

Yeriniz, onay e-postası geldiğinde kesinleşir.

**Ne elde ettik?**

Rol, hangi dil sorununa bakılacağını daralttı. Cümlenin kayıt sürecini doğru anlattığını ayrıca denetleyin.

### Orta (Medium)

**Durum**

Kargo fonksiyonunu arayüz metni açısından ve test açısından ayrı okumak istiyorsunuz.

**Prompt**

```text
Tek yanıt içinde iki inceleme açısı kullan; bunlar bağımsız ajanlar değil.
Bilgi: “500 TL ve üzeri ücretsiz kargo.” Kod: total > 500 ? 0 : 50.
Editör: metnin vaat ettiği sınırı bir cümlede belirt.
Test inceleyicisi: bu vaat için bir sınır testi ve beklenen sonucu öner.
Kod çalıştırdığını iddia etme.
```

**Örnek çıktı**

Editör: Tam 500 TL ücretsiz aralıkta. Test inceleyicisi: total=500 için beklenen kargo 0; mevcut ifade 50 üretir.

**Ne elde ettik?**

İki rol farklı denetim soruları üretti. İkisi aynı yanıtın parçalarıdır; gerçek test geliştiricinin işidir.

### İleri (Hard)

**Durum**

Bir karar notunda maliyet ile erişim çatışıyor. Rolün kararı ele geçirmesini istemiyorsunuz.

**Prompt**

```text
Karar notu editörüsün; seçimi benim yerime yapma.
A salonu: 800 TL, basamaksız giriş doğrulandı. B: 600 TL, girişte üç basamak var. 18 kişilik ekipte basamaksız erişim zorunlu. Bütçe üst sınırı 700 TL.
Önce zorunlu koşulları ayır. Ardından seçeneklerin hangi koşulu karşılamadığını belirt. Bana ait bütçe değişikliğini varsayma. En fazla bir sonraki karar sorusunu yaz.
```

**Örnek çıktı**

A bütçeyi 100 TL aşıyor; B erişim koşulunu karşılamıyor. Mevcut bilgilerle uygun seçenek yok. Basamaksız ve en fazla 700 TL olan üçüncü bir salon aransın mı?

**Ne elde ettik?**

Rol, notu düzenledi; yeni bütçe yetkisi üretmedi. Aramayı başlatma veya kapsamı değiştirme kararı sizde kaldı.

## Nerede durmalı?

“Dünyanın en iyi uzmanı” gibi sıfatları olgusal doğruluk garantisi saymayın. Persona çalışmalarının sonuçları görev ve modellere bağlıdır. CO-STAR rol yerine bağlam, amaç ve okur gibi brief alanlarını birlikte düzenler; çok ajanlı yöntemler ayrıca gerçek çağrı altyapısı ister.

## Kaynaklar

- [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT](https://arxiv.org/html/2302.11382) — White, Jules; Fu, Quchen; Hays, Sam; Sandborn, Michael; Olea, Carlos; Gilbert, Henry; Elnashar, Ashraf; Spencer-Smith, Jesse; Schmidt, Douglas C.. 2023-02-21. Persona desenini bir etkileşim biçimi olarak tanımlar; mesleki yetkinlik sertifikası değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
- [When “A Helpful Assistant” Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models](https://arxiv.org/html/2311.10054v3) — Zheng, Mingqian; Pei, Jiaxin; Logeswaran, Lajanugen; Lee, Moontae; Jurgens, David. 2023-11-16; okunan sürüm 2024-10-09. İncelenen modellerde persona eklemenin olgusal görevlerde tutarlı iyileşme sağlamadığını inceler. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
- [[2512.05858] Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy](https://arxiv.org/abs/2512.05858) — Basil, Savir; Shapiro, Ina; Shapiro, Dan; Mollick, Ethan; Mollick, Lilach; Meincke, Lennart. 2025-12-05. Uzman personası ile doğruluk ilişkisine dair özet düzeyinde sınır sağlar; tam deney gövdesi bu kayıtta okunmadı. Kanıt düzeyi: yalnız özet.
