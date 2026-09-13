# Premortem

İşin başarısız olduğunu varsay; bunu doğurabilecek somut nedenleri ara.

## Nedir?

Premortem, bir planı uygulamadan önce gelecekte başarısız olmuş gibi ele alıp olası nedenleri yazmaktır. Bu bir tahmin veya olmuş olay anlatısı değil, planın zayıf noktalarını bulma alıştırmasıdır.

## Ne zaman işe yarar?

Plan hazır görünürken ekip üyelerinin çekincelerini söylemesi zorlaşıyorsa veya önlenebilir sorunları erken görmek istiyorsanız.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Sekiz kişilik atölye planını kontrol edeceksiniz.

**Prompt**

```text
Plan: 12 Ekim 14.00, 8 kişi, malzemeler dahil. Yer henüz belli değil.
Kurgusal varsayım: Atölye iyi işlemedi. Bunun mevcut planla bağlantılı en fazla üç olası nedenini yaz. Her neden için erken işaret ve küçük önlem öner. Olay yaşanmış gibi anlatma; kaynakta olmayan bütçe veya insan davranışı uydurma.
```

**Örnek çıktı**

“Yer geç açıklanırsa katılımcılar hazırlık yapamayabilir. Erken işaret: duyuru gününde adresin hâlâ belirsiz olması. Önlem: adres kararı için sorumlu ve tarih belirlemek.”

**Ne elde ettik?**

Genel kaygı, gözlenebilir işaret ve somut plana bağlandı.

### Orta (Medium)

**Durum**

Aynı risk farklı ekip üyelerince farklı görülüyor.

**Prompt**

```text
Plan: Cuma yeni kullanım rehberi yayımlanacak. Taslak hazır; teknik kontrol yapılmadı; bir editör izinli.
Premortem turu: Önce her insan kendi üç başarısızlık nedenini bağımsız yazsın. Sonra model gerçek notları benzer temalarda toplasın; azınlıkta kalan somut nedeni silmesin.
Girdi örneği A="Yanlış komut okuyucuyu yanıltır", B="Son kontrol için kimse kalmaz", C="Mobilde kod taşar".
Her tema için mevcut kanıt, kontrol adımı ve sorumlu kararı gereken alanı ayır. Yayın veya görev ataması yapma.
```

**Örnek çıktı**

“Teknik doğruluk, kontrol kapasitesi ve mobil okunabilirlik üç ayrı tema. Her biri için ilgili kontrol açık; model kimse adına sorumluluk kabul etmedi.”

**Ne elde ettik?**

Bağımsız insan endişeleri tek baskın görüşte erimedi.

### İleri (Hard)

**Durum**

Her olasılığa önlem almak planı gereksiz büyütebilir.

**Prompt**

```text
Plan: Küçük bir duyurunun yerel taslağını teslim etmek. İzin: Metin ve kaynak kontrolü; yayın, yeni özellik ve sistem değişikliği yok.
Başarısızlık varsayımıyla en fazla beş neden üret. Sonra yalnız istenen teslimi doğrudan etkileyenleri tut; düşük dayanaklı, kapsam dışı senaryoları ayrı kısa notta bırak.
Her tutulan neden için kanıtlanabilir kontrol ve durma ölçütü yaz. Kontroller geçince yeni risk turu açma. Gerçek felaket tahmini veya kapsam genişletme yetkisi üretme.
```

**Örnek çıktı**

“Eksik tarih, desteklenmeyen iddia, bozuk iç bağlantı doğrudan kontrollerdir. İlgisiz sistem yenilemesi bu teslimin parçası olmaz.”

**Ne elde ettik?**

Premortem, sonsuz önlem listesi yerine işin sınırları içinde kaldı.

## Nerede durmalı?

Premortem geleceği bildirmez; olasılık oranları verisiz hesaplanamaz. Red-team belirli bir çıktıyı veya sistemi saldırgan örneklerle sınayabilir; premortem plan başarısız olmuş varsayımından nedenler üretir. Önlem önerisi, onu uygulama yetkisi değildir.

## Kaynaklar

- [Pre-mortem Method of Risk Assessment](https://www.gary-klein.com/premortem) — Gary Klein. 2007 (method date stated; page publication date unknown). Gary Klein’ın premortem yaklaşımını anlatan birincil pratisyen kaynağıdır; sayfanın yayın tarihi doğrulanmadı, yöntemin 2007 bağlantısı sayfa tarihine dönüştürülmez. Kanıt düzeyi: sayfa gövdesi.
