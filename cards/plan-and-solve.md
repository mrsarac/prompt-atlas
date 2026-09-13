# Plan-and-Solve

Önce çözüm planını kur, sonra aynı planın adımlarını uygula.

## Nedir?

Plan-and-Solve, problemi doğrudan çözmek yerine önce gerekli adımları belirlemeyi, ardından planı uygulamayı önerir. PS+ sürümü değişkenler ve hesap ayrıntıları için ek yönlendirmeler içerir. Görünür planda kısa, kontrol edilebilir işlemler yeterlidir.

## Ne zaman işe yarar?

Atlanan adımların veya yanlış işlem sırasının sonuca etki ettiği küçük planlama ve hesap işlerinde.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Kutulardaki kalem sayısını hesaplayacaksınız.

**Prompt**

```text
4 kutuda 6'şar kalem var; 7 kalem dağıtılıyor. Kaç kalem kalır?
Önce iki maddelik çözüm planı yaz. Sonra planı kısa işlem satırlarıyla uygula ve tek sonuç ver. Gizli düşünce dökümü istemiyorum; yalnız plan ve denetlenebilir hesap.
```

**Örnek çıktı**

Plan: “Toplamı bul; dağıtılanı çıkar.” Uygulama: “4 × 6 = 24; 24 − 7 = 17. Sonuç: 17 kalem.”

**Ne elde ettik?**

İşlem sırası sonuçtan önce görünür oldu.

### Orta (Medium)

**Durum**

İndirim ve kargonun sırası yanlış okunabilir.

**Prompt**

```text
Sepet 625 TL. Önce %20 indirim uygulanır. İndirim sonrası tutar 500 TL ve üzeriyse kargo ücretsiz, altındaysa 50 TL.
PS+ yaklaşımıyla önce değişkenleri ve sayıları listele, sonra planı yaz, ardından uygula. Para birimini koru; eşiğin dahil olduğunu kontrol et. Son cevap bir cümle olsun.
```

**Örnek çıktı**

“Plan: indirimi uygula, indirimli tutarı eşikle karşılaştır, kargoyu ekle. 625 × 0,8 = 500; 500 ≥ 500; kargo 0. Ödenecek tutar 500 TL.”

**Ne elde ettik?**

Sınırın eşitlik durumunu kontrol eden bir plan oluştu.

### İleri (Hard)

**Durum**

Bir iş takvimi kısıtları karşılamıyorsa plan revize edilmeli.

**Prompt**

```text
Saat 09.00'da başlıyoruz. A 30 dakika; B 20 dakika ve en geç 09.30'da bitmeli; C 10 dakika ve A'dan sonra. İşler tek kişiyle, çakışmadan yapılacak.
Önce kısıtları çıkar ve bir sıra planla. Sonra başlangıç/bitiş saatlerini hesapla. Son kontrol her kuralı plana karşı denetlesin. Plan bir kuralı bozarsa tek revizyon yap; hâlâ uygun değilse çözülemedi de. İç düşünce anlatma, görünür plan ve kontrol tablosu yeterli.
```

**Örnek çıktı**

“B 09.00–09.20; A 09.20–09.50; C 09.50–10.00. B son saat koşulu sağlanıyor; C, A’dan sonra; çakışma yok.”

**Ne elde ettik?**

Plan yalnız listelenmedi; uygulanıp kısıtlarla karşılaştırıldı.

## Nerede durmalı?

Plan yazmak planın doğru olduğunu garanti etmez. Least-to-Most alt soruları çözüp sonuçlarını taşımaya odaklanır; Plan-and-Solve önce bütün çözüm için bir yol çıkarır. Özgün promptların uzun düşünme isteği yerine burada kısa plan ve kontrol kullanılıyor; birebir deney tekrarı değil.

## Kaynaklar

- [Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](https://arxiv.org/html/2305.04091) — Wang, Lei; Xu, Wanyu; Lan, Yihuai; Hu, Zhiqiang; Lan, Yunshi; Lee, Roy Ka-Wei; Lim, Ee-Peng. 2023-05-06; okunan sürüm 2023-05-26. Önce planlama, sonra çözme ve PS+ ek talimatlarını açıklar; her modelde aynı etkiyi göstereceği sonucu çıkarılmaz. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
