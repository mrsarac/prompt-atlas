# Metacognitive Prompting

Görevi anlama, ilk çözüm ve son kontrolü ayrı görünür adımlar yap.

## Nedir?

Metacognitive Prompting, modelin görevi yorumlama, ilk yargı, değerlendirme ve son yanıt aşamalarını düzenler. Buradaki “metabiliş” modelin bilinçli öz farkındalığı olduğu iddiası değildir; bir prompt yapısının adıdır.

## Ne zaman işe yarar?

Bir cevapta görev yanlış okunmuş mu, koşul atlanmış mı, güven düzeyi dayanakla uyumlu mu görmek istediğinizde.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Kısa bir kuralı doğru okuyup okumadığını kontrol edeceksiniz.

**Prompt**

```text
Kural: 500 TL ve üzeri kargo ücretsiz, altı 50 TL. Soru: 500 TL sepetin kargosu?
Dört kısa alanla yanıtla: görevi anlama; ilk cevap; kurala karşı kontrol; son cevap ve dayanak sınırı. Her alan bir cümle olsun. Gizli düşünce dökümü veya bilinç iddiası istemiyorum.
```

**Örnek çıktı**

“Görev: eşik değerini değerlendirmek. İlk cevap: 0 TL. Kontrol: ‘ve üzeri’ 500’ü içeriyor. Son cevap: verilen kurala göre 0 TL.”

**Ne elde ettik?**

Cevabın hangi yorum ve kontrole dayandığı görünür oldu.

### Orta (Medium)

**Durum**

Modelin ilk yorumuna karşı bir alternatif var.

**Prompt**

```text
Veri: Beş kişiden üçü kaydet düğmesini kullanmadı. Görüşme yok. Soru: Düğme küçük olduğu için mi?
Önce görevi ve mevcut kanıtı özetle. İlk yargını kesin neden olarak kurma. Sonra aynı gözlemi açıklayabilecek bir alternatif ve ikisini ayıracak kontrol öner. Son cevapta bildiğin ile tahmin ettiğini ayır; yüzdelik güven uydurma.
```

**Örnek çıktı**

“Küçük düğme bir ihtimal; kayıt ihtiyacı duymamış olmaları da mümkün. Görev gözlemi olmadan neden belirlenemiyor.”

**Ne elde ettik?**

İlk açıklama, kanıtın desteklediğinden daha kesin hâle gelmedi.

### İleri (Hard)

**Durum**

Öz değerlendirme, dış kanıtın eksikliğini kapatmamalı.

**Prompt**

```text
Görev: Kurgusal hizmetin bugün çalışıp çalışmadığını söyle. Verilen tek kayıt: "Dün 18.00'de çalışıyordu." Canlı durum aracı yok.
Aşamalar: sorunun zamanını anla; mevcut veriden ilk değerlendirmeyi yap; zaman farkı ve araç eksikliğini kontrol et; son cevabı revize et. Her aşama kısa, gözlenebilir bir kontrol olsun.
Öz güven puanı vererek bugünü doğrulanmış sayma. Son cevap neyin eksik olduğunu ve hangi gerçek kontrolün gerekli olduğunu içersin; yeni araç varmış gibi davranma.
```

**Örnek çıktı**

“Dünkü kayıt bugünkü durumu doğrulamıyor. Canlı durum kaydı veya güncel kontrol gerekli.”

**Ne elde ettik?**

Daha dikkatli öz değerlendirme, olmayan gözlemi yaratmadı.

## Nerede durmalı?

Bu yöntem insanın öğrenmesini ölçen metabiliş çalışmasıyla aynı iddia değildir. Self-Refine ürünün taslağını eleştirip yeniler; burada görevi anlama ve yargıyı değerlendirme aşamaları öne çıkar. Öz değerlendirme dış doğrulamanın yerine geçmez.

## Kaynaklar

- [Metacognitive Prompting Improves Understanding in Large Language Models](https://arxiv.org/html/2308.05342) — Wang, Yuqing; Zhao, Yun. 2023-08-10; okunan sürüm 2024-03-20. Model yanıtını görev anlayışı, yargı ve değerlendirme aşamalarıyla düzenleyen Metacognitive Prompting yaklaşımını tanımlar. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
- [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/html/2310.01798) — Huang, Jie; Chen, Xinyun; Mishra, Swaroop; Zheng, Huaixiu Steven; Yu, Adams Wei; Song, Xinying; Zhou, Denny. 2023-10-03; okunan sürüm 2024-03-14. İç geri bildirimin doğru düzeltme sağlamadığı durumları gösterir; bu kart için evrensel üstünlük iddiasını sınırlar. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
