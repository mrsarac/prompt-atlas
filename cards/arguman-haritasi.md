# Argüman haritası

İddiayı, dayanağını ve itirazını ayrı düğümler olarak gör.

## Nedir?

Argüman haritası, bir görüşü destekleyen gerekçeleri ve ona yönelen itirazları bağlantılarıyla düzenler. Model metni haritalayabilir; bir bağlantı çizmek dayanağın doğru olduğunu kanıtlamaz.

## Ne zaman işe yarar?

Uzun tartışmada herkes farklı bir iddiaya cevap veriyorsa veya görüş ile kanıt birbirine karışıyorsa.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Kısa bir karar gerekçesini ayıracaksınız.

**Prompt**

```text
Metin: "Atölyeyi sabah yapmalıyız çünkü üç katılımcı sabahı tercih etti. Ama diğer beş kişinin tercihini bilmiyoruz."
İddia, destek, itiraz/bilgi boşluğu alanlarını çıkar. Her alıntıyı metindeki ifadeyle eşleştir. Sonra bağlantıları düz metinle yaz: destek -> iddia; itiraz -> hangi destek veya çıkarım? Yeni katılımcı tercihi ekleme.
```

**Örnek çıktı**

“İddia: sabah yapalım. Destek: üç kişi sabahı tercih etti. Boşluk: diğer beş kişi bilinmiyor. Boşluk, tercihin tüm gruba genellenmesine itiraz ediyor.”

**Ne elde ettik?**

Tartışmanın asıl zayıf bağlantısı görüldü.

### Orta (Medium)

**Durum**

Aynı dayanak iki farklı sonuca bağlanmış.

**Prompt**

```text
A: "Üç kişi notunu bulamadı; etiket sistemi ekleyelim." B: "Aynı gözlem arama kutusunun görünürlüğünü artırmayı da destekleyebilir."
Düğümler üret: ortak gözlem, A'nın çözüm iddiası, B'nin çözüm iddiası, her bağlantının varsayımı. Kimlikleri D1, I1, I2, V1, V2 olarak ver. Varsayımları gözlenmiş kanıt sayma.
Sonunda iki yol arasında ayrım yapacak tek gözlem sorusu yaz; çözümü kesinleştirme.
```

**Örnek çıktı**

“D1→I1 bağlantısı sınıflama sorunu varsayıyor; D1→I2 bağlantısı arama görünürlüğü sorunu varsayıyor. Kullanıcı not ararken ne yapıyor?”

**Ne elde ettik?**

Ortak veri, zorunlu tek sonuç gibi sunulmadı.

### İleri (Hard)

**Durum**

Bir grup tartışmasında normatif tercih ile ampirik iddia ayrılmalı.

**Prompt**

```text
Metinler: A="Toplantı kaydı sonradan erişimi kolaylaştırır." B="Mahremiyet benim için erişim kolaylığından önemli." C="Herkes kayda razı olur." Eldeki veri: Katılımcılara henüz sorulmadı.
İddia, değer tercihi, kanıt ihtiyacı ve itiraz haritası çıkar. B'yi yanlış bilgi diye sınıflama; C'yi doğrulanmış uzlaşı sayma. Her düğüme konuşmacı ve metin dayanağı ekle.
Sonuç harita ve açık sorular olsun. Oy veya kayıt izni üretme. Haritadaki bir bağ belirsizse kesin ok yerine "olası ilişki" yaz.
```

**Örnek çıktı**

“B değer tercihi; C kanıt gerektiren genelleme. C’nin dayanağı yok. A’nın olası faydası B’nin tercihini mantıken geçersiz kılmıyor.”

**Ne elde ettik?**

Tartışmanın olgu, değer ve izin boyutları ayrı kaldı.

## Nerede durmalı?

Kaynak setindeki LLM destekli argüman haritalama yayınının yalnız özeti ve künyesi okunabildi; ayrıntılı deney veya etkinlik sonucu ileri sürülmüyor. Harita güzel görünse de eksik veya yanlış bağlantı içerebilir; özgün konuşmacı metniyle denetlenmelidir.

Steelman, devil’s advocate ve counterfactual gibi adlar tartışmada farklı hamlelere işaret edebilir. Bu seçkide ayrı yöntem kökenleri veya LLM etkileri doğrulanmadığından argüman haritasının ya da premortem’in eşanlamlısı sayılmıyor.

## Kaynaklar

- [A Hybrid Human-AI Approach for Argument Map Creation From Transcripts](https://aclanthology.org/2024.delite-1.6/) — Lucas Anastasiou; Anna De Liddo. 2024-05. LLM destekli argüman haritalama çalışmasının kapsamını özet düzeyinde destekler; PDF gövdesi okunmadığından yöntem ayrıntısı veya etki iddiası kurulmaz. Kanıt düzeyi: özet ve künye.
