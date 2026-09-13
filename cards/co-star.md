# CO-STAR

Bağlamı, amacı ve okuru aynı kısa brief içinde görünür kılın.

## Nedir?

CO-STAR altı alanı hatırlatır: Context (bağlam), Objective (amaç), Style (üslup), Tone (ton), Audience (okur) ve Response (çıktı). Bir yazı isteğinde eksik kalmış tercihleri bu alanlarla kontrol edebilirsiniz.

Üslup metnin nasıl kurulacağını, ton okurla kuracağı tavrı anlatır. Alanları doldurmak için bilmediğiniz ayrıntıları uydurmanız gerekmez. Bu bir brief düzenidir; arama, ajan veya otomatik değerlendirme algoritması kurmaz.

## Ne zaman işe yarar?

Duyuru, açıklama, düzenleme brief’i ve farklı okurlara yönelik yazılar için yararlıdır. Olgusal bilgiler ile yazım tercihlerini baştan ayırın.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir kütüphane çalışma odası duyurusu yazacaksınız.

**Prompt**

```text
Context: Kütüphanenin çalışma odası salı 14.00–16.00 bakımda kapalı.
Objective: Ziyaretçi kapalı saate gelmesin.
Style: Sade duyuru.
Tone: Sakin ve doğrudan.
Audience: Günlük ziyaretçiler.
Response: En fazla iki cümle; kapanış aralığı tam yazılsın. Başka hizmetler hakkında bilgi ekleme.
```

**Örnek çıktı**

Çalışma odası salı günü 14.00–16.00 arasında bakım nedeniyle kapalıdır. Ziyaretinizi bu saatlerin dışında planlayabilirsiniz.

**Ne elde ettik?**

Okur, saat ve amaç bir arada görülebiliyor. Duyuruyu yayımlamadan bakım bilgisini sorumlu kişi doğrular.

### Orta (Medium)

**Durum**

Aynı bakım bilgisi iki okura gidecek; çalışan notunda eylem gerekiyor.

**Prompt**

```text
Bağlam: Çalışma odası salı 14.00–16.00 bakımda. Anahtar sorumlusu Deniz.
Amaç: Ziyaretçiyi bilgilendir, görevliye hazırlığı hatırlat.
Üslup: Kısa, açıklayıcı. Ton: Nazik, telaşsız.
Okur: Bir sürüm ziyaretçiye, bir sürüm görevliye.
Çıktı: İki ayrı kısa metin. Görevli notunda Deniz’den anahtarı isteme adımı olsun. Ziyaretçi metnine personel adı ekleme. Ek kapanış uydurma.
```

**Örnek çıktı**

Ziyaretçi: Çalışma odası salı 14.00–16.00 arasında bakım nedeniyle kapalıdır.

Görevli: Salı 14.00–16.00 bakımı için çalışma odasının anahtarını Deniz’den isteyin.

**Ne elde ettik?**

Aynı olgu iki farklı işe hizmet ediyor. Okur alanı, metne hangi ayrıntının gireceğini değiştirdi.

### İleri (Hard)

**Durum**

Kısa olmak ile önemli koşulu açıklamak çatışıyor.

**Prompt**

```text
Context: Atölye ücretsiz; malzeme katılımcıdan. Kayıt formu başvuru topluyor; yer e-postayla onaylanıyor.
Objective: Ücret ve kayıt koşulları yanlış anlaşılmasın.
Style: Tek paragraf, günlük Türkçe. Tone: Davetkâr, abartısız.
Audience: İlk kez katılacak yetişkinler.
Response: En fazla 35 sözcük. Ücretsiz katılım, malzeme sorumluluğu ve e-posta onayı mutlaka bulunsun. Sözcük sınırı uğruna koşul silme; sığdıramazsan çelişkiyi bildir.
```

**Örnek çıktı**

Atölyeye katılım ücretsizdir; malzemelerinizi kendiniz getirmelisiniz. Formu doldurarak başvurabilirsiniz. Yeriniz, onay e-postası geldiğinde kesinleşir.

**Ne elde ettik?**

Kısa metinde üç karar bilgisi korunuyor. Gerçek malzeme listesi ayrı yerdeyse bağlantısını sonradan siz ekleyebilirsiniz; model onu uydurmadı.

## Nerede durmalı?

CO-STAR’ın her alanını her görevde uzatmak gerekmez. Teknik kod görevi, şiirsel ton tarifinden çok kabul ölçütüne ihtiyaç duyabilir. Sheila Teo çerçeveyi GovTech ekibine atfeder; burada tek mucit veya ölçülmüş evrensel üstünlük iddiası kurmuyoruz.

## Kaynaklar

- [Mastering the art of prompt engineering with Empower | Government Technology Agency of Singapore (GovTech Singapore)](https://www.tech.gov.sg/technews/mastering-the-art-of-prompt-engineering-with-empower/) — GovTech Singapore. 2025-04-03. GovTech’in CO-STAR alanlarını nasıl kullandığını açıklayan kurumsal kaynaktır. Kanıt düzeyi: sayfa gövdesi.
- [How I Won Singapore's GPT-4 Prompt Engineering Competition | Towards Data Science](https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41/) — Sheila Teo. 2023-12-29; okunan sürüm 2025-01-28. Teo’nun pratisyen anlatımı ve GovTech atfını destekler; yarışma deneyimi bütün işlere taşınan karşılaştırmalı kanıt değildir. Kanıt düzeyi: sayfa gövdesi.
