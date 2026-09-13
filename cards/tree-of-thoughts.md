# Tree of Thoughts

Birden fazla çözüm yolunu açın; ara durumları değerlendirip gerektiğinde geri dönün.

## Nedir?

Tree of Thoughts, çözümü bir arama problemi olarak düzenler. Koordinatör aday adımlar üretir, her adayın ulaştığı durumu değerlendirir ve umut veren dalları sürdürür. Çıkmaza girince önceki duruma dönmek mümkündür.

Aşağıdaki taslaklarda aday üreten model ile durumları saklayan ve seçen koordinatör ayrı işler yapar. Tek yanıtta bir ağaç çizmek, bu aramayı yürütmek değildir.

## Ne zaman işe yarar?

Sıralama, kısıtlı tasarım veya bulmaca gibi ara adayların sınanabildiği işlerde yararlıdır. Önce durumun nasıl saklanacağını, değerlendirme kuralını ve çağrı sınırını belirleyin.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

A ve B işleri yapılacak; A, B’den önce gelmeli.

**Prompt**

```text
İnsan koordinatör başlangıç durumunu [] tutar. Aday çağrısı: “Kalan işler A,B. İlk adım için iki aday ver.”
Her adayı ayrı değerlendir: B önceyse önkoşul ihlaliyle ele; A önceyse durum [A], kalan [B].
Yeni çağrı: “Durum [A], kalan B. Önkoşulları koruyan sonraki adımı ver.”
Tam sırayı A’nın B’den önce gelmesiyle denetle. En fazla iki üretim çağrısı; geçerli dal kalmazsa dur.
```

**Örnek çıktı**

Adaylar [A] ve [B]. [B] elenir; [A] → [A,B]. Son sıra geçerli.

**Ne elde ettik?**

Aday üretme, eleme ve devam etme ayrı adımlar oldu. Böylesi küçük bir işi elle çözmek daha kolaydır; örnek arama mekanizmasını gösterir.

### Orta (Medium)

**Durum**

Üç görev tek kişiyle bitecek; son teslim saatleri farklı.

**Prompt**

```text
Başlangıç 09.00. A 30 dakika, B 20 dakika, C 10 dakika. B en geç 09.30’da bitmeli. C ancak A’dan sonra yapılabilir.
Koordinatör durum olarak tamamlanan sıra, saat ve kalan işleri saklar. Her model çağrısından en fazla iki uygun sonraki adım ister.
Değerlendirici süreyi toplar; önkoşul veya teslim ihlalinde dalı eler. En fazla iki dalı açık tutar; çıkmazda önceki duruma döner. En fazla altı üretim çağrısı. Tam sırayı zaman çizelgesiyle denetler.
```

**Örnek çıktı**

[A] sonrası saat 09.30; B artık 09.30’da bitemez, dal elenir. [B] 09.20 → [B,A] 09.50 → [B,A,C] 10.00.

**Ne elde ettik?**

Erken kararın sonraki işi olanaksızlaştırdığı görüldü. Seçilen sıra süreler ve önkoşullarla kontrol edilebilir.

### İleri (Hard)

**Durum**

3,3,8,8 sayılarının her birini bir kez kullanarak 24 elde edeceksiniz.

**Prompt**

```text
Koordinatör sayısal ifadeleri ve kullanılan sayı kimliklerini durum olarak tutar. Başlangıç [3a,3b,8a,8b].
Model her çağrıda iki sayıyı bir işlemle birleştiren en fazla üç aday önerir. Değerlendirici kesin kesir hesabı yapar; sıfıra bölmeyi ve sayı tekrarını eler. İyi görünen en fazla üç dalı tut; başarısız dalda geri dön.
En fazla 20 aday genişletme; aday kalmazsa bulunamadı de. Yalnız tüm sayıları bir kez kullanan ve tam 24 veren ifadeyi kabul et. Hesaplayıcı gerekir; modelin “24” demesi yetmez.
```

**Örnek çıktı**

Temsili başarılı dal: 8b/3b → 3a−8b/3b → 8a/(3a−8b/3b)=24. Kullanılan sayılar: iki 3 ve iki 8.

**Ne elde ettik?**

Bir çözüm adayı ve kesin doğrulama ölçütü var. Bu anlatımda arama koşusu yapılmadı; yalnız verilen ifadenin hesabı ayrıca kontrol edilebilir.

## Nerede durmalı?

Değerlendirici yanlış dalı iyi bulabilir; arama maliyeti hızla büyür. Bütçe bitmesi çözüm olmadığı anlamına gelmez. Graph of Thoughts dalların birleşmesine de izin verir. Self-Consistency ise tamamlanmış bağımsız cevapları sayar; ara dalları aramaz.

## Kaynaklar

- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/html/2305.10601) — Yao, Shunyu; Yu, Dian; Zhao, Jeffrey; Shafran, Izhak; Griffiths, Thomas L.; Cao, Yuan; Narasimhan, Karthik. 2023-05-17; okunan sürüm 2023-12-03. Aday üretimi, değerlendirme ve BFS/DFS gibi aramayla ilerleme düzenini tanımlar; Game of 24, yazı ve bulmaca koşulları genel planlama garantisi değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
