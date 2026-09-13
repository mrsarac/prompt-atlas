# Aralıklı tekrar

Tekrarı zamana yay; neyi unuttuğunu kaydet.

## Nedir?

Aralıklı tekrar, aynı bilgiyi tek oturumda sürekli görmek yerine farklı zamanlarda yeniden hatırlamayı denemektir. Model içerik ve kayıt şablonu hazırlayabilir; gerçek zaman geçişi ve hatırlama denemeleri insan veya uygulama tarafından yürütülür.

## Ne zaman işe yarar?

Öğrendiğiniz bilgiyi sonraki günlerde de kullanmak istiyorsanız. Tek bir sohbet mesajında “bir hafta sonra” yazmak aralıklı tekrar yapmak değildir.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Üç durum kodunu birkaç güne yayacaksınız.

**Prompt**

```text
Konu notu: 200 başarı, 404 kaynak bulunamadı, 500 sunucu hatası.
Bana kaynakla eşleşen üç kısa soru hazırla; cevap anahtarını ayrı bölümde tut. Örnek çalışma takvimi: bugün, 2 gün sonra, 1 hafta sonra. Bunun kişiye özel optimal takvim olduğunu söyleme.
Her oturumda ben cevapları görmeden yanıtlayacağım; tarih, yardımsız doğru/yanlış, zorlandığım kodu yerel notuma kaydedeceğim. Gerçek hatırlatma kurma. Üç oturum planı hazır olunca dur.
```

**Örnek çıktı**

Kayıt şablonu: “tarih | soru | yardımsız yanıt | kaynakla kontrol | sonraki tekrar”. Gerçek ilerleme yalnız yapılan oturumlardan doldurulur.

**Ne elde ettik?**

Takvim ile yapılmış öğrenme kaydı birbirinden ayrıldı.

### Orta (Medium)

**Durum**

Bazı kartlar kolay, bazıları sürekli karışıyor.

**Prompt**

```text
Kayıt: 13 Ekim — 200 doğru, 404/500 karıştı; 15 Ekim — 200 doğru, 404 doğru, 500 ipucuyla.
Bu kayda göre bir sonraki oturum için öncelik öner. Basit yerel kural: yanlış/ipucuyla cevaplananı ertesi gün, iki kez yardımsız doğru olanı daha sonraki oturumda sor. Bunun araştırmayla doğrulanmış kişisel zamanlama algoritması olduğunu iddia etme.
Soruların anlamını değiştirerek sorabilirsin ama kaynak tanımını koru. İnsan tarihleri takvimine kendisi uygulasın; veri yoksa yeni başarı kaydı ekleme.
```

**Örnek çıktı**

“500 öncelikli; son yanıt ipucuyla. 200 daha sonraki oturuma alınabilir. 404 için bir yardımsız deneme daha planla.”

**Ne elde ettik?**

Tekrar yoğunluğu, gerçek hata kaydına göre değişti.

### İleri (Hard)

**Durum**

Bir öğrenme kartının kaynak bilgisi değişti.

**Prompt**

```text
Eski kart v1: "Kurgusal sistemde dosya limiti 10 MB". Yeni onaylı kaynak v2: "Limit 20 MB; geçerlilik 1 Kasım". Son tekrar 25 Ekim'de eski kartla yapılmış.
Model yeni ve eski bilgiyi tarihleriyle ayırsın. 1 Kasım sonrası tekrar kartını v2'ye bağlasın; eski doğru yanıtı yeni kurala göre hiç hata yapmamış gibi yeniden yazmasın.
İnsan kaynak sürümünü kontrol etsin. Sonraki gerçek oturumda "Hangi tarihten itibaren hangi limit?" sorusuna kaynaksız cevap versin; sonuç yeni sürüm kaydına eklensin. Oturum gerçekleşmeden tamamlandı deme.
```

**Örnek çıktı**

“v1 geçmiş kaydı korunur. v2 kartı: 1 Kasım’dan itibaren 20 MB. Yeni sürüm için henüz hatırlama sonucu yok.”

**Ne elde ettik?**

Tekrar sistemi eski bilgiyi kalıcı doğruluk gibi öğretmeye devam etmedi.

## Nerede durmalı?

Bu karttaki zaman aralıkları örnektir; her konuya uygun tek takvim iddiası yok. Kaynak setinde aralıklı çalışma için pratisyen rehber, hatırlama etkisi için ayrı insan araştırması bulunuyor. Belirli bir LLM takviminin üstünlüğü doğrulanmış değil. Dış kayıt olmadan modelin ilerlemeyi oturumlar arasında tuttuğunu varsaymayın.

## Kaynaklar

- [A Step-by-Step Process to Teach Yourself Anything (in a Fraction of the Time) - Scott H Young](https://www.scotthyoung.com/blog/2013/05/10/learn-anything-in-less-time/) — Scott H. Young. 2013-05-10. Öğrenmeyi yapılandırma ve tekrar/geri bildirim pratikleri için pratisyen kaynağıdır; kişiye özel aralıkların deneysel garantisi değildir. Kanıt düzeyi: sayfa gövdesi.
- [Test-enhanced learning: taking memory tests improves long-term retention](https://pubmed.ncbi.nlm.nih.gov/16507066/) — Henry L. Roediger III; Jeffrey D. Karpicke. 2006-03. Geri çağırma ve sonraki hatırlama için insan araştırmasıdır; bu karttaki tarih dizisini veya LLM takvimini doğrulamaz. Kanıt düzeyi: özet ve künye.
