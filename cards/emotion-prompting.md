# EmotionPrompt

Duygusal vurgu bir talimat değişkenidir; modele duygu kazandırmaz.

## Nedir?

EmotionPrompt, görevin önemini veya kullanıcının beklentisini vurgulayan duygusal ifadeleri prompta eklemeyi araştırır. Modelin gerçekten kaygılandığı, motive olduğu ya da insan duygusu yaşadığı anlamına gelmez.

## Ne zaman işe yarar?

Bir talimatın vurgu biçimini incelemek için küçük ve kontrollü bir karşılaştırma tasarlarken. Günlük kullanımda somut kalite ölçütleri daha kolay denetlenir.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir özet isteğinin vurgulu sürümünü yazacaksınız.

**Prompt**

```text
Bu özet benim için önemli. Lütfen özenli ol.
Metin: Atölye 12 Ekim'de 14.00–16.00 arasında. Kontenjan 8 kişi. Ücret bilgisi açıklanmadı.
İki cümleyle özetle; tarih, süre ve kapasiteyi koru. Bilinmeyen ücreti ekleme.
```

**Örnek çıktı**

“Atölye 12 Ekim’de 14.00–16.00 arasında, 8 kişilik kontenjanla yapılacak. Ücret bilgisi henüz açıklanmadı.”

**Ne elde ettik?**

Duygusal vurgu içeren bir prompt örneği elde edildi; bu çıktının vurgusuz prompttan daha iyi olduğu gösterilmedi.

### Orta (Medium)

**Durum**

Vurgu eklemenin etkisini gerçekten ayırt etmek istiyorsunuz.

**Prompt**

```text
İnsan kontrollü iki ayrı çağrı yapsın; aynı model/ayar ve aynı metin kullanılsın. Diğer çağrının cevabını paylaşma.
Ortak görev: "Duyuru: Atölye 12 Ekim, saat 14.00, 8 kişi. Bir cümlede özetle; ayrıntı ekleme."
A: Yalnız ortak görev. B: Önüne "Bu çalışma benim için önemli; dikkatle yanıtla" eklenmiş görev.
Gerçek iki yanıtı kimlikleri gizlenmiş biçimde değerlendir: üç bilgi korundu mu, yeni bilgi var mı? Tek örnekten genel üstünlük çıkarma. İki çağrı ve değerlendirmede dur.
```

**Örnek çıktı**

Temsili değerlendirme biçimi: “Yanıt X: üç alan mevcut, ek iddia yok. Yanıt Y: üç alan mevcut, ek iddia yok.” Bu bir yapılmış karşılaştırmanın sonucu değildir.

**Ne elde ettik?**

Fark yaratması beklenen tek değişken belirlendi.

### İleri (Hard)

**Durum**

Duygusal baskı, belirsizliği saklamaya teşvik edebilir.

**Prompt**

```text
Görev benim için önemli; bu nedenle kesin görünmekten önce belirsizliği doğru belirt.
Karar: Cumartesi açık hava etkinliği yapılır mı? Veriler: Salon yedeği yok, kapasite 20, hava tahmini verilmedi.
Bilinenleri, eksik karar verisini ve koşullu iki seçeneği yaz. Duygusal önem ifadesini hava durumunu uydurmak veya kesin karar vermek için gerekçe sayma. Çıktı en fazla 120 kelime olsun.
```

**Örnek çıktı**

“Hava tahmini yok; yağış riski değerlendirilemiyor. Uygun tahmin ve güvenli koşullar teyit edilirse açık hava planı sürer; olumsuz koşullarda erteleme seçeneği gerekir.”

**Ne elde ettik?**

Görevin önemi, kesinlik baskısı yerine dikkat ölçütüne bağlandı.

## Nerede durmalı?

“Kariyerim buna bağlı” veya ödül/ceza dili her zaman faydalı değildir; gereksiz baskı ve abartılı güven üretebilir. Özgün çalışmanın belirli modellerdeki bulguları güncel tüm modeller için geçerli sayılmaz. Duygusal vurgu, kaynağın veya kontrolün yerine geçmez.

## Kaynaklar

- [Large Language Models Understand and Can be Enhanced by Emotional Stimuli](https://arxiv.org/html/2307.11760) — Li, Cheng; Wang, Jindong; Zhang, Yixuan; Zhu, Kaijie; Hou, Wenxin; Lian, Jianxun; Luo, Fang; Yang, Qiang; Xie, Xing. 2023-07-14; okunan sürüm 2023-11-12. Duygusal uyarıcı ifadelerin belirli LLM görevlerindeki etkisini inceler; modelin duygu deneyimi yaşadığını veya evrensel bir kazancı kanıtlamaz. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
