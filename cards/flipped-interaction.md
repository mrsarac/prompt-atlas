# Flipped Interaction

Cevabı hazırlamadan önce, eksik bilgiyi model sorsun.

## Nedir?

Flipped Interaction, soru sorma sırasını modele verir. Kullanıcı hedefi ve sınırları söyler; model görevi tamamlamak için gereken bilgileri toplar. Sorular amaç değil, yeterli bilgiye ulaşmanın yoludur.

## Ne zaman işe yarar?

Ne istediğinizi kabaca bildiğiniz ama doğru brief için hangi ayrıntıların gerektiğini bilmediğiniz durumlarda.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir atölye duyurusu yazılacak; temel bilgiler eksik.

**Prompt**

```text
Bir atölye duyurusu hazırlayacağız. Eksik zorunlu alanları birer birer sor: konu, tarih/saat, katılım yolu. Verdiğim bilgiyi tekrar sorma. Üç alan tamamlanınca iki cümlelik taslak yaz; bilinmeyen bağlantıyı uydurma.
Şu an bildiğin: Konu suluboya. Tarih 12 Ekim, saat 14.00. Katılım yolu henüz belli değil.
```

**Örnek çıktı**


Model: “Katılım için hangi yolu belirtelim?” Kullanıcı: “Duyuruya yanıt versinler.” Model: “Suluboya atölyesi 12 Ekim saat 14.00’te. Katılmak için bu duyuruya yanıt verebilirsiniz.”

**Ne elde ettik?**

Tek gerekli soru, kullanılabilir taslağa bağlandı.

### Orta (Medium)

**Durum**

Bir haftalık çalışma planı için süre ve öncelikler bilinmiyor.

**Prompt**

```text
Bana plan yapmadan önce eksik bilgileri topla. Hedefim Python listelerini öğrenmek; başlangıç seviyesindeyim. En fazla üç soru sor, her seferinde bir tane. Süre, kullanılabilir günler ve öğrenme ölçütü yeterli olunca dur; cevapları özetleyip bir haftalık plan çıkar.
```

**Örnek çıktı**


Model: “Çalışmaya günde kaç dakika ayırabilirsin?”

Kullanıcı: “20 dakika.”

Model: “Hangi günler uygunsun?”

Kullanıcı: “Pazartesi, çarşamba, cuma.”

Model: “Hafta sonunda neyi yardım almadan yapabilmek istiyorsun?”

Kullanıcı: “Liste filtreleme kodu yazmak.”

Model: “Bilgi yeterli: üç gün, günde 20 dakika; hedef yardımsız liste filtreleme. Pazartesi liste/erişim, çarşamba koşullu filtreleme, cuma yeni bir listede yardımsız alıştırma. Her oturum 20 dakika.” Başka soru sorulmaz.

**Ne elde ettik?**

Plan varsayılan boş zamana göre değil, verilen kapasiteye göre kuruldu.

### İleri (Hard)

**Durum**

Bir ekip araştırma sorusu belirleyecek; katılımcılar her ayrıntıyı henüz bilmiyor.

**Prompt**

```text
Hedef: Küçük ekibin kullanıcı araştırması briefini tamamlamak. Bilinenler: 5 görüşme yapılabilir; ürün bir not uygulaması; toplam 1 hafta var.
Önce kararın neyi değiştireceğini sor ve gerçek yanıtımı bekle. Başlangıçta bilinmeyen bir alanı cevabı varmış gibi doldurma.
Sonra yalnız tasarımı değiştiren eksikleri sor; toplam en fazla 4 soru. Kullanıcı bilmiyorum derse seçenekleri ve etkilerini kısaca göster, karar vermiş gibi yazma.
Yeterli bilgi ölçütü: hedef davranış, katılımcı ölçütü, görüşme süresi, karar sahibi. Eksik kalırsa varsayımları ayrı işaretle. Sonunda brief taslağını teyide sun; yeterli bilgide yeni soru sorma, onay gelmeden yeni anket veya işe alım başlatma.
```

**Örnek çıktı**


Model: “Araştırmanın sonucu hangi kararı değiştirecek?”

Kullanıcı: “İlk notu kaydetmeyi engelleyen hangi sorunu önce düzelteceğimize karar vereceğiz.”

Model: “Görüşmeye kimleri dahil edelim?”

Kullanıcı: “Kaydolduğu ilk gün ilk notunu kaydetmemiş kişileri.”

Model: “Her görüşme kaç dakika olabilir?”

Kullanıcı: “15 dakika.”

Model: “Öncelik kararını kim verecek?”

Kullanıcı: “Ürün sorumlusu Ayşe.”

Model: “Bilgi yeterli. Teyide sunulan brief: bir haftada, belirtilen ölçüte uyan beş kişiyle 15’er dakika; amaç ilk notun kaydındaki engelleri anlamak, düzeltme önceliğini Ayşe belirleyecek.” Dört soruda durulur; görüşme başlatılmaz.

**Ne elde ettik?**

Soru sayısı sınırlı kaldı; bilinmeyenler sahte kesinliğe dönüşmedi.

## Nerede durmalı?

Bütün bilgilerin verildiği bir işte yeniden mülakat yapmak gereksizdir. Question Refinement sorunun ifadesini iyileştirir; Flipped Interaction eksik girdileri kullanıcıdan toplar. Tercihleri açığa çıkarma ise özellikle değerler ve ödünleşimler üzerinde durur.

## Kaynaklar

- [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT](https://arxiv.org/html/2302.11382) — White, Jules; Fu, Quchen; Hays, Sam; Sandborn, Michael; Olea, Carlos; Gilbert, Henry; Elnashar, Ashraf; Spencer-Smith, Jesse; Schmidt, Douglas C.. 2023-02-21. Modelin kullanıcıya soru sorarak belirli bir hedefe ulaşmasını sağlayan Flipped Interaction örüntüsünü tanımlar. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
