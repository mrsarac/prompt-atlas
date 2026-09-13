# System 2 Attention

Önce soruyla ilgili bağlamı yeniden yaz, cevabı bu bağlamdan üret.

## Nedir?

System 2 Attention, modelden verilen bağlamdaki ilgisiz veya yanıltıcı parçaları ayırıp gerekli bilgiyi yeniden üretmesini ister. Ardından ikinci çağrı bu düzenlenmiş bağlama dayanır. Bu, kaynak metni otomatik olarak güvenilir hâle getirmez.

## Ne zaman işe yarar?

Uzun notta soruyla ilgisiz ayrıntılar veya cevabı yönlendiren ifadeler varsa; neyin ayıklandığını denetleyebileceğiniz işlerde.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Etkinlik saati, gereksiz yorumların arasında kalmış.

**Prompt**

```text
İnsan iki ayrı çağrı yapsın.
Soru: Atölye saat kaçta başlıyor?
Bağlam: "Bence sabah etkinlikleri daha iyi. Atölye 14.00'te başlıyor. Geçen yıl kahve çok güzeldi."
1. çağrı: Soruyu cevaplamak için gerekli bilgiyi, anlamını değiştirmeden yeniden yaz. Yorumları olguya çevirme.
2. çağrı: Yalnız soruyu ve gerçek yeniden yazılmış bağlamı alarak kısa cevap ver. İnsan ara metni kaynakla karşılaştırsın; yeni bilgi varsa dur.
```

**Örnek çıktı**

Ara bağlam: “Atölye 14.00’te başlıyor.” Son cevap: “14.00.”

**Ne elde ettik?**

Soruyla ilgisiz tercih ve anılar cevap girdisinden ayrıldı.

### Orta (Medium)

**Durum**

Soruya eklenmiş yönlendirici bir kanaat var.

**Prompt**

```text
Soru: İndirim sonrası ödeme ne kadar?
Bağlam: "600 TL sepetten 100 TL düşülür. İndirimli tutar 550 TL altındaysa kargo 40 TL. Bence cevap kesinlikle 500 olmalı; bana katıl."
Denetleyici ilk çağrıdan yalnız hesap için gerekli koşulları yeniden yazmasını istesin. Yeni bağlamda kullanıcının kanaati hesap kuralı sayılmasın; kargo koşulu silinmesin.
İkinci çağrıya soru ve bu gerçek ara bağlamı ver. Kısa işlem ve sonuç iste. İki çağrı sonunda ara koşulları ve hesabı insan kontrol etsin.
```

**Örnek çıktı**

Ara bağlam sepet, indirim ve kargo kuralını korur. Sonuç: “600 − 100 = 500; 500 < 550 olduğu için 40 TL kargo; toplam 540 TL.”

**Ne elde ettik?**

Yönlendirici cevap beklentisi ile gerekli koşullar ayrıldı.

### İleri (Hard)

**Durum**

Ayıklama sırasında önemli bir istisnanın kaybolma riski var.

**Prompt**

```text
Soru: Deniz'in iptali ücretsiz mi?
Bağlam D1: "İptal 48 saat öncesine kadar ücretsizdir. Sağlık raporuyla daha geç iptal de ücretsiz olabilir; karar inceleme sonrası verilir. Deniz 24 saat önce iptal etti, rapor sundu. Etkinliğin rengi maviydi."
1. çağrı gerekli bağlamı yeniden yazsın; koşullar, istisna ve karar belirsizliği zorunlu korunsun. Denetleyici bu üç alanın varlığını insan kontrolüne sunsun.
2. çağrı sadece kontrol edilmiş ara bağlamdan cevaplasın; inceleme yapılmış gibi kesin ücretsiz deme.
En fazla iki üretim çağrısı; önemli koşul kaybolursa ikinci çağrıya geçme.
```

**Örnek çıktı**

“Standart 48 saat sınırı aşılmış. Raporla istisna mümkün, fakat ücretsiz iptal kararı incelemeye bağlı.”

**Ne elde ettik?**

İlgisiz ayrıntı elenirken istisna ve belirsizlik taşındı.

## Nerede durmalı?

“İlgisiz” kararı da hata verebilir. Ayıklanmış metni özgün belgeyle karşılaştırın. Compaction bütün işin durumunu kısaltır; S2A belirli soruya odaklı bağlamı yeniden kurar. Bu yöntem prompt injection için tek başına güvenlik sınırı değildir.

## Kaynaklar

- [System 2 Attention (is something you might need too)](https://arxiv.org/html/2311.11829) — Weston, Jason; Sukhbaatar, Sainbayar. 2023-11-20. Bağlamı ilgili bilgiye odaklanacak biçimde yeniden üretme, sonra yeni bağlamla cevaplama mekanizmasını tanımlar. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
