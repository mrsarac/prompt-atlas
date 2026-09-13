# Grup tartışmasını kolaylaştırma

Grubun farklı bilgilerini görünür yap; yapay bir uzlaşı üretme.

## Nedir?

Grup kolaylaştırma, katılımcıların notlarını, ortak noktalarını ve açık uyuşmazlıklarını düzenlemektir. Model moderasyon yardımcısı olabilir; gruptaki insanlar adına tercih, onay veya karar üretemez.

## Ne zaman işe yarar?

Bir ekipte bilgi farklı kişilerde dağılmışsa, aynı konu tekrar konuşuluyorsa veya azınlık görüşü kayboluyorsa.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Üç kişinin etkinlik notlarını toparlayacaksınız.

**Prompt**

```text
Gerçek katılımcı notları yerine kullanılan kurgusal girdiler: A="Sabah uygunum", B="Öğleden sonra uygunum", C="Saat fark etmez, giriş rampalı olmalı".
Notları kişi kimliğiyle koru. Ortaklaşanlar, farklılaşanlar ve karar için eksik bilgi olarak özetle. Çoğunluk saati veya herkesin onayı varmış gibi yazma. Tek açıklayıcı soru öner; kimseye mesaj gönderme.
```

**Örnek çıktı**

“Saat tercihi bölünmüş. Erişim koşulu C tarafından belirtilmiş. Uygun saat kararı için A/B’nin esneklik aralığı bilinmiyor.”

**Ne elde ettik?**

Grup özeti görüşleri tek bir tercihe sıkıştırmadı.

### Orta (Medium)

**Durum**

Dağınık bilgiler birlikte değerlendirilince yeni kısıt ortaya çıkıyor.

**Prompt**

```text
Notlar: A="Salon 16 kişilik", B="18 katılım talebi var", C="Başka salon için bütçe yok".
Her bilgiyi kaynak kişisiyle ayır. Birlikte doğan kısıtı hesapla; kayıtları kendi tahmininle tamamlama. Sonra en fazla üç karar seçeneği ve her biri için gereken insan kararı yaz.
Katılımcı listesini değiştirme, kişileri eleme veya alternatif salon ayarlama. Grup teyidi gelmeden seçenekleri alınmış karar diye yazma.
```

**Örnek çıktı**

“18 talep, 16 kapasite: 2 kişilik fark var. Bekleme listesi, iki oturum veya talep teyidi seçenekleri ayrıca grup kararı gerektiriyor.”

**Ne elde ettik?**

Farklı kişilerin bilgileri ortak kısıta dönüştü; eylem yetkisi yaratılmadı.

### İleri (Hard)

**Durum**

Toplantı sonunda sessizlik yanlışlıkla onay sayılabilir.

**Prompt**

```text
Tutanak: A="İki oturuma bölelim", B="Kolaylaştırıcı zamanı yetmeyebilir", C bu konuda konuşmadı. Karar kuralı: herkes açıkça onay vermeli.
Model karar özeti hazırlasın: öneri, itiraz, cevaplanmamış soru, açık onaylar. C'nin sessizliğini onay sayma; B'nin itirazını yalnız olumsuz ton diye silme.
İnsan kolaylaştırıcı özeti katılımcılara kendisi teyit ettirsin. Model bu örnekte hiçbir mesaj göndermez. Teyit yoksa sonuç "karar bekliyor" olsun; en fazla bir özet revizyonunda dur.
```

**Örnek çıktı**

“Öneri iki oturum. B’nin zaman itirazı çözülmedi; C’nin görüşü yok. Oybirliği kuralına göre karar alınmadı.”

**Ne elde ettik?**

Kolaylaştırma, eksik onayı yapay uzlaşıya çevirmedi.

## Nerede durmalı?

Bilgi paylaşımının iyileşmesi son kararın daha iyi olduğu anlamına gelmez. Kaynaktaki gerçek insan grup çalışmasında bu ölçütler ayrıdır; anlamlı nihai karar kalitesi artışı gösterilmiş gibi sunulmaz. Model özetinin konuşmacılara doğrulatılması gerekir.

## Kaynaklar

- [Bringing Everyone to the Table: An Experimental Study of LLM-Facilitated Group Decision Making](https://arxiv.org/html/2508.08242v2) — Alsobay, Mohammed; Rothschild, David M.; Hofman, Jake M.; Goldstein, Daniel G.. 2025-08-11; okunan sürüm 2026-07-02. Gerçek insan gruplarında LLM kolaylaştırmasının bilgi paylaşımı ve karar ölçütlerini inceler; bilgi paylaşımı bulgusu nihai karar kalitesi artışı diye aktarılmaz. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
