# Few-shot

İstediğiniz davranışı birkaç doğru girdi–çıktı çiftiyle gösterin.

## Nedir?

Etiketlerin ne anlama geldiğini anlatmak bazen yeterli olmaz. Few-shot kullanımda modele birkaç çözülmüş örnek, ardından yeni girdi verirsiniz. Model o çağrının bağlamındaki örüntüyü kullanır; örnek vermek modelin ağırlıklarını eğitmez.

Örnekler birbirini tamamlamalı. Yalnız kolay durumlar gösterirseniz sınırdaki bir girdinin nasıl ele alınacağını açık bırakabilirsiniz. Yanlış etiket de doğru örnek kadar görünürdür.

## Ne zaman işe yarar?

Metin etiketleme, belirli bir yazım biçimi veya küçük veri dönüşümleri için uygundur. Doğru cevaplarını sizin bildiğiniz, temsil gücü olan örneklerle başlayın.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Destek iletilerini konuya göre ayıracaksınız.

**Prompt**

```text
İletiyi fatura, erisim veya belirsiz diye etiketle. Tek etiket yaz.
Örnek: “Aynı ürün iki kez faturalandı.” → fatura
Örnek: “Şifremle giriş yapamıyorum.” → erisim
Örnek: “Yardım istiyorum.” → belirsiz
Yeni ileti: “Hesabıma giremiyorum.”
```

**Örnek çıktı**

erisim

**Ne elde ettik?**

Yeni ileti örneklerle aynı etiket diline taşındı. Bu üç örneğin bütün destek taleplerini temsil ettiğini varsaymayın.

### Orta (Medium)

**Durum**

Bir iletide iki konu bulunabiliyor; konu yoksa boş liste gerekiyor.

**Prompt**

```text
Yalnız açıkça söylenen konuları listele; sıralama fatura, erisim olsun. Yeni konu uydurma.
“Fatura gelmedi.” → [fatura]
“Giremiyorum, ayrıca faturam hatalı.” → [fatura, erisim]
“Çok kötüsünüz.” → []
Yeni ileti: “Giriş düzeldi ama aynı ücret iki kere yazılmış.”
Çözülmüş konuyu yeniden açık talep sayma. Etiketin yanına kısa dayanak alıntısı ekle.
```

**Örnek çıktı**

[fatura] — “aynı ücret iki kere yazılmış”

**Ne elde ettik?**

Örnekler yalnız biçimi değil, çoklu konu ve boş cevap sınırını da gösteriyor. “Giriş düzeldi” ifadesini açık hata saymamak ayrıca kontrol edilecek.

### İleri (Hard)

**Durum**

Bir kural değişti: kapatılmış sorunlar etiketlenmeyecek. Eski örneklerden biri kuralla çelişiyor.

**Prompt**

```text
Önce örnekleri yeni kurala göre denetle. Kural: yalnız halen açık sorunları etiketle; konu belirsizse [].
Örnek 1: “Giremiyorum.” → [erisim]
Örnek 2: “Fatura düzeldi.” → [fatura]
Örnek 3: “Fatura düzeldi ama giriş sorunu sürüyor.” → [erisim]
Çelişen örneği düzeltip nedenini bir cümlede yaz. Sonra “Şifre sorunu bitti, fatura hâlâ eksik.” iletisini etiketle. Kuralla tutarlı olmayan örneği taklit etme.
```

**Örnek çıktı**

Örnek 2 → []; fatura sorunu kapanmış. Yeni ileti → [fatura]; eksiklik sürüyor.

**Ne elde ettik?**

Örneği çoğaltmadan önce veri hatası yakalandı. Gerçek kullanımda güncel örnek paketini siz onaylayın; birkaç başarılı yanıt genel doğruluk ölçümü değildir.

## Nerede durmalı?

Örnek sayısı için tek ideal değer yoktur. Sıra, etiket dağılımı ve yeni girdiye benzerlik sonucu etkileyebilir. Analogical Prompting’de örneği model üretir; burada doğru örnekleri siz verirsiniz. Active Prompting ise hangi örneklerin insan tarafından etiketleneceğini ayrı örneklemelerle seçer.

## Kaynaklar

- [Language Models are Few-Shot Learners](https://arxiv.org/html/2005.14165) — Brown, Tom B.; Mann, Benjamin; Ryder, Nick; Subbiah, Melanie; Kaplan, Jared; Dhariwal, Prafulla; Neelakantan, Arvind; Shyam, Pranav; Sastry, Girish; Askell, Amanda; Agarwal, Sandhini; Herbert-Voss, Ariel; Krueger, Gretchen; Henighan, Tom; Child, Rewon; Ramesh, Aditya; Ziegler, Daniel M.; Wu, Jeffrey; Winter, Clemens; Hesse, Christopher; Chen, Mark; Sigler, Eric; Litwin, Mateusz; Gray, Scott; Chess, Benjamin; Clark, Jack; Berner, Christopher; McCandlish, Sam; Radford, Alec; Sutskever, Ilya; Amodei, Dario. 2020-05-28; okunan sürüm 2020-07-22. GPT-3 üzerinde bağlam içi örneklerle görev yapmayı inceler; fine-tuning ile aynı işlem değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
- [Prompt engineering | OpenAI API](https://developers.openai.com/api/docs/guides/prompt-engineering?api-mode=responses) — OpenAI. yayın tarihi doğrulanmadı. İlgili örnekleri prompt bağlamında göstermeyi önerir; güncel model seçimine bağlı bir uygulama rehberidir. Kanıt düzeyi: sayfa gövdesi.
