# Reflexion

Bir denemenin geri bildirimini kısa ders notuna çevirip sonraki denemeye taşıyın.

## Nedir?

Reflexion’da ajan bir işi dener, sonucu değerlendirilir ve bu sonuca dair kısa bir not oluşturur. Not, sonraki denemenin bağlamına eklenir. Değişen model ağırlıkları değil, denemeler arasında taşınan bilgidir.

Geri bildirim gerçek ortamdan veya belirli düzenlerde iç simülasyondan gelebilir. Bunları eşdeğer saymamak gerekir. Burada dış kontrolün ne olduğu açıkça belirtilir; temsili sonuçlar gerçek yürütme kaydı gibi sunulmaz.

## Ne zaman işe yarar?

Tekrarlanabilir görevlerde aynı hatayı yeniden yapmamak için kullanılır. Deneme ortamı, değerlendirme kuralı ve notu gerçekten yeniden yükleyen koordinatör gerekir.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Ajanın duyurusu onay koşulunu unutmuş.

**Prompt**

```text
İnsan koordinatör ilk görev ve kaynakla metin çağrısı yapar: “Form başvuru toplar; kayıt e-postayla onaylanır.”
İnsan değerlendirici, onay koşulu metinde yoksa “başvuru ile onay karışmış” geri bildirimini kaydeder.
Ayrı reflection çağrısı: “Bu geri bildirimi sonraki denemede kullanılacak tek somut ders yap; başarı iddia etme.”
Yeni denemeye kaynak, görev ve ders notu birlikte gider. İki deneme sınırı; insan yeniden kontrol eder.
```

**Örnek çıktı**

Temsili not: “Duyuruda form ve e-posta onayını ayrı söyle.” Sonraki temsili cümle: “Formdan başvurun; yeriniz e-postayla onaylanır.”

**Ne elde ettik?**

Geri bildirim yalnız mevcut metinde kalmadı, yeni denemenin girdisine dönüştü.

### Orta (Medium)

**Durum**

Bir program tam eşikte yanlış sonuç veriyor.

**Prompt**

```text
Görev: 500 TL ve üzeri ücretsiz, altı 50 TL kargo. İlk program total > 500 koşulunu kullanıyor.
Koordinatör gerçek test yürütücüsünden 499,500,501 sonuçlarını alır. Beklentiler 50,0,0. Test çalışmadıysa reflection’a hayali sonuç verme.
Gerçek farkı modelin kısa notuna dönüştür: “Eşitlik sınırını sonraki denemede koru.”
Yeni kod çağrısına görev, başarısız test ve notu ver; ardından aynı testleri yeniden çalıştır. En fazla iki kod denemesi; kalan başarısızlıkta dur.
```

**Örnek çıktı**

Temsili ilk gözlem: 50,50,0. Ders: eşik eşitliği eksik. Temsili yeni koşul `total >= 500`; beklenen sonuçlar 50,0,0.

**Ne elde ettik?**

Notun neye dayandığı belli. Gerçek başarı ancak ikinci test yürütmesinin kaydıyla söylenebilir.

### İleri (Hard)

**Durum**

Eski bir ders yeni kural değişince yanlış hale geliyor.

**Prompt**

```text
Önceki not: “Kargoda eşik her zaman 500 TL.” Yeni görev v2: “İndirim sonrası 600 TL ve üstü ücretsiz; altı 50 TL.”
Koordinatör yeni denemeye notu tarih/sürümüyle taşır. Modelden eski dersin yeni kuralla uyumunu denetlemesini ister. Çelişen sabit sayıyı otorite saymaz; yeni kaynak v2 üstün gelir.
Ajan kod önerir; gerçek testler 599,600,601 için 50,0,0 beklentisiyle yürütülür. Reflection notu kural v2 ve gözlem kimliğiyle güncellenir.
İki deneme bütçesi; gerçek test yoksa notta doğrulanmadı yazılır.
```

**Örnek çıktı**

Temsili güncel ders: “v2 eşiği 600; eşitliği kapsa. Eski 500 bilgisi geçersiz.”

**Ne elde ettik?**

Bellekteki dersin güncelliği de işin parçası oldu. Önceki deneyim, yeni talimatın yerine geçmedi.

## Nerede durmalı?

Yanlış reflection notu hatayı kalıcı bağlama taşıyabilir. Yapılandırılmış harici notlar daha genel bir saklama pratiğidir; Reflexion özellikle deneme geri bildiriminin sonraki denemeyi yönlendirmesidir. Self-Refine aynı çıktı üzerinde revizyon yapar.

## Kaynaklar

- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/html/2303.11366) — Shinn, Noah; Cassano, Federico; Berman, Edward; Gopinath, Ashwin; Narasimhan, Karthik; Yao, Shunyu. 2023-03-20; okunan sürüm 2023-10-10. Deneme geri bildiriminin episodik metin belleğiyle sonraki denemeye aktarılmasını destekler; ağırlık güncellemesi yapılmaz. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
- [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/html/2310.01798) — Huang, Jie; Chen, Xinyun; Mishra, Swaroop; Zheng, Huaixiu Steven; Yu, Adams Wei; Song, Xinying; Zhou, Denny. 2023-10-03; okunan sürüm 2024-03-14. Öz değerlendirme ile gerçek dış geri bildirimi ayırmanın önemini sınırlar. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
