# HyDE

Aranacak belgeye benzeyen bir taslak üretin; onu gerçek belgeleri bulmak için kullanın.

## Nedir?

HyDE’de model önce soruyu yanıtlayabilecek varsayımsal bir belge yazar. Bir embedding modeli bu metni vektöre dönüştürür; vektör benzerliğiyle gerçek belge deposunda arama yapılır. Cevap aşamasına taşınacak kanıt, bu aramada bulunan gerçek belgelerdir.

Üretilen varsayımsal metin yanlış ayrıntılar içerebilir. Onu kaynak diye göstermek yöntemin amacını tersine çevirir. “HyDE kullan” yazısı embedding modeli veya arama indeksi kurmaz.

## Ne zaman işe yarar?

Sorunun sözcükleriyle belgelerin dili farklı olduğunda yoğun vektör aramasında deneyebilirsiniz. Bir embedding modeli, aynı uzayda indekslenmiş gerçek belgeler ve arama yürütücüsü gerekir.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Arşivde kitap ödünç alma süresini bulacaksınız. Gerçek belgeler: K1 “Ödünç süresi 14 gündür”; K2 “Kafe 16.00’da kapanır”.

**Prompt**

```text
Koordinatör önce modeli çağırır: “Kitap kaç gün ödünç alınır sorusuna cevap verebilecek kısa varsayımsal kütüphane yönergesi yaz. Bu bir arama yardımcısı; gerçek politika iddiası değil.”
Sonra bu taslağı embedding modeliyle kodlar ve K1/K2’nin gerçek vektör indeksinde en yakın bir belgeyi getirir.
Son çağrı: “Yalnız getirilen belgeyle süreyi cevapla; belge kodunu ekle.” Varsayımsal taslak son kanıt paketine girmez.
Bir üretim, bir vektör araması, bir cevap; eşleşme yoksa dur.
```

**Örnek çıktı**

Temsili taslak: “Ödünç alınan kitaplar belirlenen süre sonunda iade edilir.” Temsili arama: K1. Cevap: 14 gün. [K1]

**Ne elde ettik?**

Varsayımsal metin aramayı yönlendirdi; 14 gün bilgisi gerçek depo kaydından geldi. Bu vektör araması burada çalıştırılmadı.

### Orta (Medium)

**Durum**

“Hesabımı kapatma” sorusu, belgelerde “üyelik sonlandırma” diye geçiyor.

**Prompt**

```text
Depo: U1 “Üyelik sonlandırma için başvuru formu gerekir.” U2 “Parola yenileme bağlantısı 15 dakika geçerlidir.”
Koordinatör modelden “Hesabımı kapatmak için gereken işlem hakkında varsayımsal yardım metni yaz; gerçek koşul uydurduğunu kanıt sayma” istemiyle taslak alır.
Taslağı embedding’e çevirip depodan iki aday getirir. İnsan hangi pasajın hesabı kapatmayı anlattığını kontrol eder; yalnız uygun kaydı cevap çağrısına taşır.
Son prompt: “Hangi işlem gerekiyor? Kaynakta olmayan onay süresini belirtme.” En fazla iki aday; uygun kaynak yoksa yanıtı durdur.
```

**Örnek çıktı**

Temsili uygun sonuç U1; U2 yalnız parola sıfırlamadır. Cevap: Üyelik sonlandırma için başvuru formu gerekir. [U1]

**Ne elde ettik?**

Benzer görünen hesap işlemleri pasaj üzerinden ayrıldı. Gerçek sonlandırma yapılmış olmadı.

### İleri (Hard)

**Durum**

Varsayımsal belge yanlış süre üretiyor; sürümler de çelişiyor.

**Prompt**

```text
Soru: Mağaza alışverişinin güncel iade süresi nedir?
Depo: I1 eski/onaysız 14 gün; I2 yürürlükte/onaylı 30 gün; I3 internet alışverişi 60 gün.
Koordinatör HyDE taslağı üretir, embedding aramasıyla en fazla üç gerçek aday getirir. Taslakta “60 gün” geçse bile bunu kanıt paketinden çıkarır.
İnsan adayların kapsam ve onay durumunu inceler; yalnız mağazaya ait yürürlükteki kaydı sonraki çağrıya verir.
Son prompt: “Yalnız seçilmiş kayıtla cevap ver; kod ve kapsamı yaz.” Onay durumu doğrulanamazsa kesin süre verme; toplam iki model çağrısında dur.
```

**Örnek çıktı**

Temsili taslak 60 gün demiş olabilir. Kabul edilen kayıt I2; cevap mağaza için 30 gün. [I2]

**Ne elde ettik?**

Arama yardımı ile kaynak otoritesi ayrıldı. İndeksin doğru adayı getirmesi hâlâ ayrıca ölçülmesi gereken bir sistem davranışıdır.

## Nerede durmalı?

Yanlış varsayımsal metin aramayı yanlış mahalleye götürebilir. Benzerlik puanı doğruluk puanı değildir. RAG bulma ve cevaplama bütününü; HyDE bu bütünün belirli bir bulma stratejisini anlatır. Generated Knowledge’de üretilen bilgi doğrudan cevap girdisi olabilir; burada gerçek depo araması zorunlu parçadır.

## Kaynaklar

- [Precise Zero-Shot Dense Retrieval without Relevance Labels](https://arxiv.org/html/2212.10496) — Gao, Luyu; Ma, Xueguang; Lin, Jimmy; Callan, Jamie. 2022-12-20. Varsayımsal belgeyi embedding üzerinden gerçek korpusa bağlayan yöntemi tanımlar; InstructGPT/Contriever deneyleri bütün arama sistemlerine genellenmez. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
