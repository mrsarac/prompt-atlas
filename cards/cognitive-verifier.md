# Cognitive Verifier

Ana cevabı kurmadan önce, gerekli alt soruları kullanıcıyla netleştir.

## Nedir?

Cognitive Verifier, ana soruya daha iyi cevap vermek için ek sorular üretip bunların yanıtlarını birleştiren bir prompt örüntüsüdür. White ve arkadaşlarının tanımında alt sorular kullanıcıya yöneltilir. Buradaki “verifier” adı bağımsız doğruluk garantisi değildir.

## Ne zaman işe yarar?

Bir kararın farklı boyutları var ve gerekli bilgiler kullanıcıda bulunuyorsa.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir çalışma planının size uygun olup olmadığını soruyorsunuz.

**Prompt**

```text
Sorum: Bu hafta Python çalışmaya nasıl başlayayım?
Cognitive Verifier düzenini kullan: Cevabı belirleyecek en fazla üç ek soruyu çıkar; her birini sırayla bana sor ve yanıtımı bekle. Sonra cevaplarımı birleştirerek kısa plan yap.
Bilinen: Başlangıç seviyesindeyim. Aynı bilgiyi tekrar sorma. Gerekli alanlar tamamlanınca soru sormayı bitir.
```

**Örnek çıktı**

Sorular: “Hedef işin ne? Hangi günler ve ne kadar süren var? Başarıyı neyle kontrol edeceksin?” Yanıtlar liste filtreleme / üç gün 20 dakika / yardımsız örnek olursa plan bunlara bağlanır.

**Ne elde ettik?**

Genel plan, kullanıcıdan alınan alt cevaplarla şekillendi.

### Orta (Medium)

**Durum**

Bir etkinlik mekânını seçmek için üç koşul birlikte gerekli.

**Prompt**

```text
Ana soru: Kurgusal Salon A atölyemize uygun mu? Salon bilgisi: 16 kişi, 2 saat kullanım, giriş rampalı; asansör bilgisi yok.
Kararı etkileyen ek soruları sırayla sor: katılımcı sayısı, gerekli süre, erişim ihtiyacı. Yanıtlarımı bekle; verilmemiş tercihi uydurma.
Yanıtlarım: 12 kişi, 90 dakika, bir katılımcı üst kata erişim gerektiriyor. Sonuçta her alt cevabı ilgili salon bilgisiyle eşleştir; eksik erişim kaydı varken uygun diye kesinleştirme.
```

**Örnek çıktı**

“Sayı ve süre uyuyor. Üst kata erişim bilgisi eksik; uygunluk kararı bu koşul teyit edilmeden tamamlanamaz.”

**Ne elde ettik?**

Alt sorular birleşirken tek bir eksik koşul görünür kaldı.

### İleri (Hard)

**Durum**

Kullanıcının yanıtları birbiriyle çelişiyor.

**Prompt**

```text
Ana soru: Haftalık içerik planını oluştur. Bilinen: iki yazı isteniyor, her yazıya en az 3 saat gerekiyor.
Önce gerekli alt soruları sor; toplam en fazla dört soru. Yanıtlarım: Haftalık toplam 4 saatim var; kalite için yazı başına 3 saat azaltılamaz; iki yazı zorunlu değil, tercih.
Cevapları birleştirirken 6 saatlik işi 4 saate sığmış gibi gösterme. Sert kısıt ile tercihi ayır; bir koşullu öneri ve bir açık karar sun. Uygun plan veya açık çatışma raporuyla dur.
```

**Örnek çıktı**

“4 saatte, yazı başına 3 saat koşuluyla iki yazı mümkün değil. Bir yazı + 1 saat hazırlık seçeneği var; iki yazı için süre veya kalite koşulu değişmeli.”

**Ne elde ettik?**

Birleştirme, çelişkili girdileri makul görünen bir takvime gizlemedi.

## Nerede durmalı?

Flipped Interaction genel soru toplama düzenidir; Cognitive Verifier ana soruya katkı veren alt soruların cevaplarını birleştirmeyi özellikle tarif eder. CoVe çoğunlukla üretilmiş cevaptaki iddiaları kontrol eder; burada eksik kullanıcı bilgileri toplanır. İsimdeki “verifier” dış kanıt sağlamaz.

## Kaynaklar

- [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT](https://arxiv.org/html/2302.11382) — White, Jules; Fu, Quchen; Hays, Sam; Sandborn, Michael; Olea, Carlos; Gilbert, Henry; Elnashar, Ashraf; Spencer-Smith, Jesse; Schmidt, Douglas C.. 2023-02-21. Cognitive Verifier örüntüsünde ek soruların kullanıcıya sorulması ve cevapların ana yanıtta birleştirilmesini tanımlar; bağımsız doğrulama deneyi değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
