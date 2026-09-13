# Sokratik öğretici diyalog

Cevabı hemen vermeden, öğrenenin bir sonraki adımı bulmasına yardım et.

## Nedir?

Sokratik öğretim, öğrenenin mevcut anlayışına göre soru ve ipucu vermeyi amaçlar. Bu kartta işi yapan insan, model ise rehberdir. Modelin kendi kendine alt sorular üretmesi ayrı bir yöntemdir.

## Ne zaman işe yarar?

Çözümün hazır gelmesinden çok, insanın kendi başına çözebilmesi önemliyse.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Basit bir denklemde ilk adımı bulacaksınız.

**Prompt**

```text
Öğrenen benim. Soru: x + 3 = 8. Son cevabı verme.
Önce eşitliği koruyarak 3'ü nasıl kaldırabileceğimi tek soruyla sor ve yanıtımı bekle. Doğru adımı söylersem sonucu benim hesaplamamı iste. Yanlışsa daha küçük bir ipucu ver. En fazla üç tur; sonunda aynı yapıda yeni bir soru sor.
```

**Örnek çıktı**

Model: “İki taraftan hangi sayıyı çıkarırsan x yalnız kalır?” İnsan: “3.” Model: “Bunu uyguladığında sağ taraf kaç olur?”

**Ne elde ettik?**

Öğrenen, son sayıyı kopyalamadan işlemi kurdu.

### Orta (Medium)

**Durum**

Kod hatasında model düzeltmeyi söylemeden sınır durumunu düşündürecek.

**Prompt**

```text
Kural: 500 TL ve üzeri ücretsiz, altı 50 TL. Kod: total > 500 ? 0 : 50.
Bana doğru kodu veya değişecek operatörü hemen söyleme. Önce hangi girdinin kuralı sınayacağını sor. Yanıtımdan sonra o girdinin mevcut kodda ne döndürdüğünü benim tahmin etmemi iste.
En fazla üç ipucu; takılırsam önce genel karşılaştırma kavramını açıkla, sonra aynı örneğe dön. Gerçek test çalıştırma erişimin yok; tahminle testi ayır.
```

**Örnek çıktı**

İnsan 500’ü seçer; kodun 50 verdiğini fark eder. Model: “Kural bu sınır değeri hangi gruba koyuyor?”

**Ne elde ettik?**

Doğrudan yama yerine hataya götüren kontrol alışkanlığı çalışıldı.

### İleri (Hard)

**Durum**

Öğrenen cevabı istiyor; yardım düzeyi açıkça ayarlanmalı.

**Prompt**

```text
Öğrenme hedefi: Ortalama hızın toplam yol/toplam süre olduğunu uygulamak. Soru: 60 km'yi 30 km/saat, sonraki 60 km'yi 60 km/saat ile gitmek.
Önce benim denememi iste. "Direkt cevabı söyle" dersem öğrenme modunda olduğumuzu hatırlatıp süreleri bulmaya yönelik tek ipucu sun; sonsuz sorgulama yapma.
Yardım sırası: kavram sorusu -> ilk bölümün süresi için ipucu -> benzer, sayıları farklı çözülmüş örnek. Asıl sorunun cevabını ancak öğrenme modunu açıkça değiştirmemi takiben göster.
En fazla üç turdan sonra nerede takıldığımı ve bağımsız denenecek yeni soruyu özetle.
```

**Örnek çıktı**

Model: “İlk 60 km’lik bölüm kaç saat sürer?” İnsan süreleri bulduktan sonra toplamları kurar. Yardım düzeyi ve mod değişimi görünür kalır.

**Ne elde ettik?**

Rehberlik, cevabı sızdırmadan ilerlemeyi ve tıkanınca durmayı birlikte ele aldı.

## Nerede durmalı?

Yalnız soru işareti eklemek Sokratik öğretim değildir. Fazla ipucu cevabı dolaylı biçimde verebilir; yetersiz ipucu da öğreneni oyalayabilir. Pisan’ın otomatik davranış denetimi insan öğrenme deneyi değildir. Bastani ve arkadaşlarının okul matematiği bulguları da her kullanıcı veya ders için garanti değildir.

## Kaynaklar

- [Teaching a Large Language Model Tutor to Withhold the Answer: A Supervisor Architecture and an Evidence-Driven Method for Tuning Socratic Behavior](https://arxiv.org/html/2608.12292) — Pisan, Yusuf. 2026-08-12. Yardım düzeyi ve cevap sızdırmama davranışını denetleyen bir tutor mimarisi sunar; değerlendirmesi insan katılımcı içermez. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
- [Generative AI without guardrails can harm learning: Evidence from high school mathematics](https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/) — Hamsa Bastani; Osbert Bastani; Alp Sungu; Haosen Ge; Özge Kabakcı; Rei Mariman. 2025 Jun 25. İpuçlarıyla korunan ve korunmayan AI yardımını okul matematiğinde, yardım kaldırıldıktan sonraki performans dahil inceler; kaynakta düzeltme kaydı da vardır. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
