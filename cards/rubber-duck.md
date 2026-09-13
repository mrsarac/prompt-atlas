# Rubber Duck

Ne yapmak istediğinizi ve hangi adımları izlediğinizi anlatarak eksik kalan noktayı arayın.

## Nedir?

Kodunuzdan belli bir sonuç bekliyorsunuz, ama çalışınca başka bir sonuç çıkıyor. Rubber Duck yönteminde, önce beklentinizi, ardından kodun adımlarını bir dinleyiciye anlatırsınız. Anlatırken, kafanızda birbirine bağladığınız iki adım arasında eksik bir koşul fark edebilirsiniz. Bir yazıdaki düşünce sırasını veya çalışma planını da böyle ele alabilirsiniz.

Klasik uygulamadaki lastik ördek sessizdir. Burada onu bir dil modeliyle uyarlıyoruz: siz anlatırsınız, yapay zekâ dinler; bitirdiğinizde anlattığınız bir noktayı netleştiren soru sorabilir. Bu uyarlamada soruyu bir tane ile sınırlıyoruz. Çözümü hazırlamasını istemiyoruz. Eksikliği siz tarif eder, bulduğunuz açıklamanın doğruluğunu sohbet dışında kontrol edersiniz.

## Ne zaman işe yarar?

Bir duyurunun neden yanlış anlaşıldığını, kodun hangi koşulda farklı davrandığını veya ajanların birbirine nasıl iş devrettiğini incelerken deneyebilirsiniz. Başlamak için hedefinizi ve izlediğiniz adımları anlatabilecek kadar bilgiye ihtiyacınız var.

## Örnekler

Aşağıdaki diyaloglar yöntemi göstermek için yazılmış temsili örnekler; gerçek deneme sonucu değiller.

### Basit (Simple)

**Durum**

Yirmi kişilik bir atölye için duyuru yazıyorsunuz. Form başvuruyu topluyor, yerler daha sonra e-postayla onaylanıyor. Duyuruyu okuyan biri ise formu gönderince yerinin kesinleştiğini düşünüyor.

**Prompt**

```text
Duyurumun nasıl anlaşılmasını beklediğimi ve ne yazdığımı anlatacağım. Sen dinle. “bitirdim” diyene kadar bekle; sonra anlattığım bir ifadeye dayanarak yalnızca bir netleştirme sorusu sor ve cevabımı bekle. Çözüm yazma, tahmin yürütme, test yapma veya araç kullanma.

Atölyede 20 yer var. İnsanların formdan başvurmasını istiyorum. Başvuruları inceleyip yer verebildiklerimize onay e-postası göndereceğiz. Duyuruya “Formu doldurun, atölyede yeriniz hazır” yazdım. Bir okur formu gönderdiğini, dolayısıyla yer ayırttığını söylüyor. Ben formu başvuru adımı olarak düşünmüştüm. bitirdim
```

**Örnek diyalog**

**Yapay zekâ:** “Yeriniz hazır” derken formun gönderildiği anı mı, onay e-postasının geldiği anı mı kastediyorsun?

**Ben:** E-postayı. Ama cümlem formun yeterli olduğunu söylüyor. “Formdan başvurun; yeriniz onay e-postası geldiğinde kesinleşir” diye yazacağım.

**Ne elde ettik?**

Başvuru ile kesin kaydı ayıran yeni bir cümle var. Yayımlamadan önce kayıt yönergesinden, onay e-postasının gerçekten bu anlama geldiğini ben kontrol etmeliyim.

### Orta (Medium)

**Durum**

Bir alışveriş sitesinde 500 TL ve üzeri siparişler için kargo ücretsiz olmalı. Tam 500 TL tutan sepete kargo ücreti ekleniyor. Tutarların sayısal olduğunu ve indirim uygulanmadığını biliyorsunuz.

**Prompt**

```text
Kargo hesabını sana ben açıklayacağım. “bitirdim” diyene kadar bekle. Ardından açıklamamdaki bir noktaya dayanarak tek netleştirme sorusu sor ve cevabımı bekle. Hatayı benim yerime bulma, çözüm veya tahmin üretme; kod çalıştırma, test yapma, araç kullanma.

Kuralım 500 TL ve üzeri siparişlerde ücretsiz kargo. JavaScript kodunda toplam > 500 koşulunu kullanıyorum: doğruysa kargo 0 TL, değilse 50 TL. Toplam sayısal bir değer, indirim yok. Tam 500 TL olan sepette 50 TL kargo görüyorum. Önce toplamı alıyor, sonra bu koşulla kargoyu seçip tutara ekliyorum. bitirdim
```

**Örnek diyalog**

**Yapay zekâ:** Kuralındaki “500 TL ve üzeri” ifadesi, tam 500 TL için hangi davranışı tarif ediyor?

**Ben:** Ücretsiz kargo. Ben `>` yazmışım; eşitliği dışarıda bırakmışım. Koşulu `>=` yapıp sınırdaki tutarı da kapsadığını kontrol edeceğim.

**Ne elde ettik?**

Kontrol edilecek somut bir düzeltme var. Kendi ortamımda 499, 500 ve 501 TL için kargo hesabını çalıştırmalıyım. Beklentim sırasıyla 50, 0 ve 0 TL; bunlar henüz alınmış test sonuçları değil.

### İleri (Hard)

**Durum**

Bir ajan kaynak notlarından taslak çıkarıyor, ikinci ajan metni düzenliyor. Yalnızca `taslak.md` değiştirilebilir. İkinci aşamadan sonra değişiklik listesinde `arsiv.md` de görünüyor; son mesaj ise işin tamamlandığını söylüyor.

**Prompt**

```text
İki ajanın iş akışını ben anlatacağım; sen bu akışı yürütme. “bitirdim” diyene kadar bekle. Sonra yalnızca anlattığım bir adıma dayanan tek netleştirme sorusu sor ve cevabımı bekle. Çözüm önerme, tahmin yürütme, test yapma; ajan başlatma, dosya okuma veya değiştirme, araç kullanma.

İlk ajana kaynak notlarını okuyup yalnızca taslak.md dosyasına yazmasını söyledim. İkinci ajana taslağı iletip “Dokümanları düzenle, bitince tamamlandı de” dedim. İkisinin de sadece taslak.md dosyasını değiştirmesini bekliyorum. İkinci aşamadan sonraki değişiklik listesinde arsiv.md de var. Ben son mesajda “tamamlandı” yazmasına bakıp işi kabul ettim. bitirdim
```

**Örnek diyalog**

**Yapay zekâ:** İkinci ajana verdiğin “dokümanları düzenle” talimatında değiştirilebilecek dosyaları nasıl belirttin?

**Ben:** Belirtmemişim; ilk ajanın sınırını bildiğini varsaymışım. Üstelik son mesaja bakmış, dosya değişikliklerini kabul sırasında incelememişim. İkinci talimata da yalnızca `taslak.md` yazma iznini açıkça eklemeliyim.

**Ne elde ettik?**

İş devrinde eksik kalan dosya sınırını belirledik. `arsiv.md` değişikliğinin kaynağı hâlâ kontrol istiyor: aşama kayıtlarını ve dosya farklarını izin verilen dosya listesiyle ben karşılaştırmalıyım. Talimatı düzeltmek tek başına dosya erişimini teknik olarak sınırlamaz.

## Nerede durmalı?

Model çözüm üretmeye başlarsa açıklamayı sizden devralır. Kendi kodunu inceleyip düzeltmesi Self-Debug kapsamına girer; burada açıklayan kişi sizsiniz. Sokratik öğretimdeki yönlendirici soru dizisi veya modelden basit bir ders anlatmasını istemek de başka bir etkileşimdir. Sohbette bulduğunuz boşluk bazen yanlış bir varsayım olabilir; belge, çalışan kod veya işlem kaydıyla kontrol edin. Özel kod ve kayıtları paylaşmadan önce hassas ayrıntıları ayıklayın.

## Kaynaklar

- [Rubber Duck Debugging](https://rubberduckdebugging.com/) — rubberduckdebugging.com; sayfada özgün katkı için “~Andy” adı geçiyor. Yayın ve güncelleme tarihi bilinmiyor; mucit veya köken tarihi doğrulanmış değil. İnsanın beklenen davranışı ve kodun adımlarını sessiz bir ördeğe anlatması pratiğini destekler.
- ["It's like a rubber duck that talks back": Understanding Generative AI-Assisted Data Analysis Workflows through a Participatory Prompting Study](https://arxiv.org/html/2407.02903) — Ian Drosos, Advait Sarkar, Xiaotong Xu, Carina Negreanu, Sean Rintel ve Lev Tankelevitch; 3 Temmuz 2024. İnsan–yapay zekâ veri analizi iş akışlarını inceler. Buradaki promptların başarı testi veya tek soru uyarlamasının nedensel etki kanıtı değildir.
- [Teaching Large Language Models to Self-Debug](https://arxiv.org/html/2304.05128) — Xinyun Chen, Maxwell Lin, Nathanael Schärli ve Denny Zhou; ilk yayın 11 Nisan 2023, güncelleme 5 Ekim 2023. Modelin kendi ürettiği programı açıklayıp düzeltmesini ele alır; insanın Rubber Duck uygulamasından rol farkını destekler.
