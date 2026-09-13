# Multiagent Debate

Ayrı model çağrılarının cevaplarını karşılaştır, sonra sınırlı tartışma yürüt.

## Nedir?

Multi-Agent Debate, ayrı bağlamlarda üretilen model cevaplarını birbirine gösterip revizyon ve birleştirme turları yürütür. Aynı sohbet içinde “üç uzman konuşsun” rol oyunu bağımsız başlangıç cevapları sağlamaz.

## Ne zaman işe yarar?

Bir problemin farklı çözüm adaylarını ve anlaşmazlık nedenlerini incelemek için; ek çağrı maliyeti ve dış kontrol imkânı göze alınabiliyorsa.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir sınır koşulunu iki ayrı model çağrısına soracaksınız.

**Prompt**

```text
Denetleyici: A ve B ayrı bağlamlarda aynı soruyu alsın; önce birbirlerinin yanıtını görmesinler. Aynı model kullanılabilir, bu istatistiksel bağımsızlık garantisi değildir.
Soru: 500 ve üzeri ücretsiz, altı 50 TL kargo; 500'de ücret?
Her çağrı kısa cevap ve kurala dayalı tek gerekçe versin. Sonra gerçek A/B cevaplarını isimleriyle iki revizyon çağrısına taşı: anlaşmazlığı kural üzerinden incele; sırf diğer ajan söyledi diye değişme.
Bir tartışma turu sonunda denetleyici sonucu ve kural kontrolünü raporlasın. Toplam 4 çağrı; uzlaşı yoksa belirsizliği koru.
```

**Örnek çıktı**

Temsili ilk cevaplar A=0, B=50; tartışma “ve üzeri” ifadesine döner. Son kontrol 500’ün dahil olduğunu göstermelidir.

**Ne elde ettik?**

İki ses rolü yerine ayrı başlangıç cevapları ve kayıtlı revizyon oluştu.

### Orta (Medium)

**Durum**

Çoğunluk yanlış bir hesap üzerinde birleşebilir.

**Prompt**

```text
Soru: 600 TL sepetten 100 TL indirim; indirimli tutar 550 altındaysa 40 TL kargo.
Denetleyici üç ayrı ilk çağrı ve bir tartışma turu yürütsün; her ajana gerçek diğer cevapları aktar. En fazla 6 model çağrısı.
Temsili ilk oylar A=500, B=500, C=540. Ajanlar kısa işlem ve kullanılan eşik tutarını yazsın. Son birleşim çoğunluğu otomatik doğruluk saymasın; izole hesaplayıcıda kaynak kuralın hesap kontrolünü ayrıca yap.
Araç yoksa dış doğrulama yapılmadığını söyle. Bütçe bitince en iyi dayanaklı sonucu veya kalan uyuşmazlığı raporla.
```

**Örnek çıktı**

“C’nin işlemi indirimli 500 tutarına 40 kargoyu ekliyor. İki başlangıç oyunun aynı olması 500’ü doğru yapmıyor.”

**Ne elde ettik?**

Tartışma, oy sayısından ziyade kontrol edilebilir uyuşmazlığa bağlandı.

### İleri (Hard)

**Durum**

Farklı kaynaklara bakan ajanlar kaynak çelişkisini çözemez.

**Prompt**

```text
Görev: Kurgusal salonun kapasitesini belirlemek. A'nın kaynağı D1="genel kapasite 20"; B'nin kaynağı D2="yangın düzeni 16". Kaynakların yetki ilişkisi açıklanmadı.
Denetleyici ilk çağrıları ayrı çalıştırsın, sonra gerçek cevap ve alıntıları iki tarafa versin. Revizyon görevi: Hangi farklı koşul/otorite varsayımı sonucu değiştirebilir? Kaynaksız öncelik kuralı üretme.
İki ilk + iki revizyon + bir birleştirme çağrısı sınırı. Birleştirici kesin kapasite yerine koşul farkını ve gerekli insan teyidini yazsın. Yeni ajan ekleyerek tartışmayı sonsuza uzatma.
```

**Örnek çıktı**

“20 genel kapasite, 16 yangın düzeni kaydı. Geçerli operasyonel sınır için yetkili kayıt teyidi gerekli; 18 gibi bir ortalama anlamsız.”

**Ne elde ettik?**

Çelişkili kanıtlar yapay uzlaşıyla kapatılmadı.

## Nerede durmalı?

Çoklu ajan, otomatik olarak self-consistency’den üstün değildir. Kaynaktaki tartışma bulguları belirli görev/model ayarlarına aittir; başka çalışmalarda kazanç görülmeyebilir. Dış araç sonucu veya yetkili kaynak, bir model grubunun oyundan farklı kanıttır.

IMAD / debate-based post-training adayının özgün kaynağı bu seçkide doğrulanmadı; bu ad, burada anlatılan çağrı tabanlı tartışmanın eşanlamlısı olarak kullanılmıyor.

## Kaynaklar

- [Improving Factuality and Reasoning in Language Models through Multiagent Debate](https://arxiv.org/html/2305.14325) — Du, Yilun; Li, Shuang; Torralba, Antonio; Tenenbaum, Joshua B.; Mordatch, Igor. 2023-05-23. Ayrı model örneklerinin cevaplarını tartışma turlarıyla revize edip birleştiren multi-agent debate düzenini tanımlar. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
- [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/html/2310.01798) — Huang, Jie; Chen, Xinyun; Mishra, Swaroop; Zheng, Huaixiu Steven; Yu, Adams Wei; Song, Xinying; Zhou, Denny. 2023-10-03; okunan sürüm 2024-03-14. İncelenen belirli aritmetik koşullarda multi-agent debate’in self-consistency’ye üstünlük göstermediği karşılaştırmayı içerir; bütün tartışma sistemleri için tek sonuç çıkarılmaz. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
