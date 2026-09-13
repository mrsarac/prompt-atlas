# Karşılıklı sav sorgulama

Varsayımları sırayla birbirinize sorun; son kararı açık tutun.

## Nedir?

Karşılıklı sorgulama, insanın ve modelin birbirlerinin iddialarına kısa sorular yöneltmesidir. Burada tek bir kanonik akademik prompt adı değil, açık kurallı bir konuşma düzeni olarak kullanılıyor. Modelin soruları insan kararının yerine geçmez.

## Ne zaman işe yarar?

Bir fikrin dayandığı varsayımları görmek, acele bir sonuca varmadan görüşü sınamak istediğinizde.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bülteninizin çok uzun olduğunu düşünüyorsunuz.

**Prompt**

```text
İddiam: Kimse bülteni okumuyor, çünkü çok uzun.
Sırayla sorgulayalım. Önce bu iddianın bir varsayımını açan tek soru sor; cevabımı bekle. Sonra senin yorumuna ben soru soracağım. En fazla iki karşılıklı tur. Veri yoksa neden-sonuç sonucu çıkarma.
```

**Örnek çıktı**

Model: “Okunmadığını hangi gözlemden biliyoruz?” İnsan: “Yalnız iki kişi kısa olsun dedi.” İnsan: “Bu, bütün okurlar için yeterli mi?” Model: “Hayır; iki kişinin geri bildirimiyle sınırlı.”

**Ne elde ettik?**

Güçlü bir genellemenin dayandığı sınırlı gözlem ortaya çıktı.

### Orta (Medium)

**Durum**

Bir özellik isteğinin neden önemli olduğu tartışılacak.

**Prompt**

```text
İddiam: Not uygulamasına etiket eklemeliyiz. Gözlem: Üç kişi eski notu bulamadığını söyledi.
Sen önce çözümle sorun arasındaki bağı sorgula. Ben yanıtlayınca geçici yorumunu yaz ve onu sorgulamam için tek açık nokta bırak. Her turda iddia, dayanak, belirsizlik ayrımını koru.
En fazla üç tur; sonunda etiket eklemeye karar verilmiş gibi davranma. Hangi yeni gözlemin seçimi değiştireceğini yaz.
```

**Örnek çıktı**

Model: “Notu bulamama, sınıflama mı yoksa arama sorunu mu?” İnsan: “Henüz bilmiyoruz.” Son kayıt: “Etiket bir aday çözüm; kayıp not arama davranışı incelenmeli.”

**Ne elde ettik?**

Tartışma, ilk çözümü savunmaktan eksik bilgiyi bulmaya yöneldi.

### İleri (Hard)

**Durum**

İki değer çatışıyor; tek doğru cevap yok.

**Prompt**

```text
Karar: Ekip toplantısı kaydedilsin mi? Amaç sonradan erişim; kaygı katılımcı mahremiyeti. Hiç kimse kayıt için izin vermedi.
Karşılıklı sorgulama yapalım: önce bir değer/varsayım sorusu sor; cevabımdan sonra en güçlü itirazını kısa yaz. Ben de itirazındaki varsayımı sorayım.
Kişisel değerleri nesnel gerçek gibi puanlama. Üç tur sonunda seçenekleri, çözülemeyen değer farkını ve gerekli insan kararını yaz. Gerçek kayıt başlatma veya izin var sayma.
```

**Örnek çıktı**

“Erişim ihtiyacı ile kayda alınma kaygısı ayrı kaldı. Yazılı özet bir seçenek; kayıt için katılımcı kararı hâlâ gerekli.”

**Ne elde ettik?**

Konuşma uyuşmazlığı gizlemeden kararın sahibine geri döndü.

## Nerede durmalı?

Bu düzen, Recursive Socratic Questioning’in model içi özyinelemeli algoritması değildir. Flipped Interaction bilgi toplar; burada iki tarafın iddiaları sorgulanır. Karşılıklı konuşmanın tek başına daha iyi insan kararları ürettiği iddia edilmiyor.

## Kaynaklar

- [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT](https://arxiv.org/html/2302.11382) — White, Jules; Fu, Quchen; Hays, Sam; Sandborn, Michael; Olea, Carlos; Gilbert, Henry; Elnashar, Ashraf; Spencer-Smith, Jesse; Schmidt, Douglas C.. 2023-02-21. Soru odaklı etkileşim örüntüleri için komşu birincil kaynaktır; burada anlatılan karşılıklı düzenin ayrı bir deneysel protokolü veya adı olduğu iddiasını desteklemez. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
- [The Art of SOCRATIC QUESTIONING: Recursive Thinking with Large Language Models](https://arxiv.org/html/2305.14999) — Qi, Jingyuan; Xu, Zhiyang; Shen, Ying; Liu, Minqian; Jin, Di; Wang, Qifan; Huang, Lifu. 2023-05-24; okunan sürüm 2023-11-02. Özyinelemeli model algoritmasını tanımlar; insan-model karşılıklı sorgulamasıyla karıştırılmaması için sınır kaynağıdır. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
