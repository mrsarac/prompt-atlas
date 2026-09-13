# Skeleton-of-Thought

Önce iskelet çıkar, bağımsız parçaları ayrı çağrılarda doldur.

## Nedir?

Skeleton-of-Thought, cevabın kısa bir iskeletini üretir; ardından her maddeyi ayrı çağrıyla genişletip sonuçları birleştirir. Hız hedefi için genişletmeler paralel yürütülür. Birbirinin sonucuna ihtiyaç duyan parçalar buna uygun değildir.

## Ne zaman işe yarar?

Bağımsız başlıklardan oluşan rehber veya açıklamalarda. Sıralı hesap ve birbirine bağlı kararlar için uygun olmayabilir.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bisiklet bakımı için üç başlıklı bir başlangıç rehberi istiyorsunuz.

**Prompt**

```text
Denetleyici: Önce tek model çağrısıyla şu görev için yalnız üç maddelik iskelet al: "Bisikleti sürüşten önce kontrol etmek". Her madde kısa başlık olsun.
Gerçek iskelet örneği: lastikler, frenler, aydınlatma.
Her madde için ayrı genişletme çağrısı başlat; hepsine aynı görevi ve bütün iskeleti ver. Prompt: Yalnız sana atanmış başlığı iki cümleyle açıkla; diğer başlıkları tekrar etme. Modelde olmayan fiziksel muayeneyi yapılmış sayma.
Denetleyici üç çıktıyı iskelet sırasıyla birleştirsin; insan tekrar/eksik kontrolü yapsın. Toplam 4 çağrı, sonra dur.
```

**Örnek çıktı**

“Lastikler: Basıncı üretici önerisiyle karşılaştır; görünür hasarı kontrol et. Frenler: Güvenli alanda fren tepkisini kontrol et. Aydınlatma: Işıkların çalıştığını ve görünürlüğünü kontrol et.”

**Ne elde ettik?**

Üç bağımsız açıklama ortak iskeletle bir araya geldi.

### Orta (Medium)

**Durum**

Bir etkinlik rehberinde ortak bilgilerin tutarlı kalması gerekiyor.

**Prompt**

```text
Görev: Katılımcı rehberi. Sabit brief: 12 Ekim 14.00–16.00; 8 kişi; malzemeler dahil; yer henüz yok.
1. çağrı yalnız iskelet: zaman, hazırlık, bilinmeyenler. Denetleyici onaylı brief ve iskeleti tüm genişletme çağrılarına aynen taşısın.
Üç paralel çağrının her biri atanmış başlığa 40 kelimeyi aşmayan metin yazsın. Yeni adres/ücret eklemesin.
Birleştirme sonrası insan kontrolü: saatler aynı mı, yer belirsiz kaldı mı, malzeme bilgisi çelişti mi? Hatalı parça için en fazla tek yeniden üretim; diğerlerini değiştirme. En fazla 5 çağrıda dur.
```

**Örnek çıktı**

“Zaman: 12 Ekim 14.00–16.00. Hazırlık: Malzemeler dahil. Bilinmeyenler: Yer henüz açıklanmadı.”

**Ne elde ettik?**

Paralel parçalar aynı gerçekler ve sınırlarla yazıldı.

### İleri (Hard)

**Durum**

Bir rehberde bazı başlıklar birbirinin çıktısına bağımlı.

**Prompt**

```text
Görev: 600 TL sepet, 100 TL indirim; indirimli tutar 550 altındaysa 40 TL kargo. Teslim kaydı D1="Ödeme onayından sonra 2 iş günü içinde kargoya verilir; teslim tarihi belirtilmedi." Fiyat hesaplama ve sipariş rehberi üretilecek.
Denetleyici önce iskelet çağrısından bağımlılık işaretleri istesin: indirimli tutar -> kargo -> ödeme toplamı; ayrıca bağımsız teslim bilgisi açıklaması.
Denetleyici tam görev, D1 ve çıkan iskeleti iki genişletme çağrısına da taşısın. Hesap çağrısı: “İndirimli tutar, kargo ve toplamı sırayla hesapla.” Teslim çağrısı: “Yalnız D1’den iki cümle yaz; kargoya verilme ile teslimi ayır, tarih ekleme.”
Birbirine bağımlı üç hesabı kendi içinde paralel genişletme; tek sıralı hesap dalında çöz. Bu dal ile bağımsız teslim çağrısı paralel çalışabilir. Sonuçları insan iskelet sırasıyla birleştirip tutarı ve D1 uyumunu kontrol etsin.
Toplam 3 çağrıda dur: bir iskelet, iki genişletme; birleştirme insanda. Bu karma düzenin saf Skeleton-of-Thought olmadığını belirt. Yanlış bağımlılık bulunursa hız uğruna devam etme.
```

**Örnek çıktı**

Birleşik rehber: “Ödeme: 600 − 100 = 500; kargo 40; toplam 540 TL. Teslim: Ödeme onayından sonra 2 iş günü içinde kargoya verilir. Teslim tarihi belirtilmemiştir.” Hesap dalının ara işlemleri sırayla yapıldı; teslim dalı bu ara sonuçları beklemedi.

**Ne elde ettik?**

Yöntemin uygun olmadığı bağımlılık sınırı uygulamanın içine girdi.

## Nerede durmalı?

Paralel çağrı desteği gerçek bir uygulama gerektirir; aynı sohbet içinde üç başlık yazdırmak aynı mekanizma değildir. Toplam token veya maliyet azalmak zorunda değil. Son parçaların birleşmesi, tutarlılık kontrolünün yerine geçmez.

## Kaynaklar

- [Skeleton-of-Thought: Prompting LLMs for Efficient Parallel Generation](https://arxiv.org/html/2307.15337) — Ning, Xuefei; Lin, Zinan; Zhou, Zixuan; Wang, Zifu; Yang, Huazhong; Wang, Yu. 2023-07-28; okunan sürüm 2024-03-02. İskelet üretimi, maddelerin paralel genişletilmesi ve birleştirilmesi düzenini tanımlar; çalışma özellikle gecikme hedeflidir, evrensel maliyet düşüşü iddiası değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
