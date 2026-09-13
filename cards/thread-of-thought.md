# Thread of Thought

Dağınık bağlamı küçük parçalarla incele, sonra yalnız cevabı çıkar.

## Nedir?

Thread of Thought, karışık veya dikkat dağıtan bağlamı yönetilebilir parçalar hâlinde ele almayı önerir. İlk aşama ilgili bilgileri düzenler; ikinci aşama bu çalışmadan sorunun cevabını çıkarır. Burada uzun iç düşünce yerine kaynaklı kısa notlar kullanılıyor.

## Ne zaman işe yarar?

İlgili bilgi uzun bir konuşmanın farklı yerlerine dağılmışsa. Kısa ve temiz bir metinde iki aşama gerekmeyebilir.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Etkinliğin yeni saatini konuşma notlarından bulacaksınız.

**Prompt**

```text
İnsan iki ayrı çağrı yapsın. Soru: Son kararlaştırılan başlangıç saati ne?
Notlar: N1="Önce 13.00 dedik." N2="Kahve seçeneği konuşuldu." N3="Yetkili düzenleyici: başlangıcı 14.00 olarak değiştiriyorum."
1. çağrı: Bağlamı yönetilebilir parçalarda incele. Her parça için soruyla ilgili kısa olgu ve kimlik yaz; eski kararı güncel sayma.
2. çağrı: Soruyu ve gerçek ilk çıktıyı al. Yalnız kısa cevap ve dayanak kimliği ver. İnsan N3 eşleşmesini kontrol etsin; iki çağrıda dur.
```

**Örnek çıktı**

İlk not: “N1 eski saat; N2 ilgisiz; N3 yetkili yeni karar 14.00.” Son cevap: “14.00 [N3].”

**Ne elde ettik?**

Dağınık konuşmadan güncel kararı taşıyan bir bilgi dizisi çıkarıldı.

### Orta (Medium)

**Durum**

İki siparişin bilgileri aynı notta karışmış.

**Prompt**

```text
Soru: K42'nin teslim şekli ve açık eksiği nedir?
P1="K42 mağazadan alınacak." P2="K43 kuryeye verildi." P3="K42 için alacak kişinin adı eksik." P4="K43 adresi doğrulandı."
Denetleyici ilk çağrıya parça kimliklerini koruyarak bağlamı versin. Prompt: Her parçadaki sipariş, durum ve eksik alanı kısa notla ayır; siparişler arasında bilgi taşıma.
İkinci çağrı yalnız gerçek notlardan K42 cevabını çıkarsın. Son kontrol K43 bilgisinin K42'ye yazılmadığını denetlesin. İki çağrı ve kontrol sonunda dur.
```

**Örnek çıktı**

“K42 mağazadan alınacak [P1]; alacak kişinin adı eksik [P3].”

**Ne elde ettik?**

Parça parça inceleme, benzer kayıtların birbirine bulaşmasını önledi.

### İleri (Hard)

**Durum**

Bir koşul, sonraki bir notla yalnız belli kişiler için değişmiş.

**Prompt**

```text
Soru: Ece'nin ücretsiz iptal hakkı kesin mi?
P1="Genel kural: 48 saat önce iptal ücretsiz." P2="Salonun ışığı yenilendi." P3="Sağlık raporu sunanlar için geç başvurular incelenebilir." P4="Ece 24 saat önce iptal etti ve rapor sundu." P5="İnceleme kararı henüz yok."
İlk çağrı: Parçaları sırayla kısa, kaynaklı notlara ayır; genel kural/istisna/kişi/karar durumunu bağla. Gizli düşünce anlatma.
İkinci çağrı: Bu notlardan yalnız soruya cevap ver. "İncelenebilir" ifadesini "onaylandı"ya çevirme. Denetleyici P3/P5'in korunmasını kontrol etsin; eksikse kesin cevap üretmeden dur.
```

**Örnek çıktı**

“Kesin değil. Ece genel sürenin dışında; rapor nedeniyle inceleme mümkün, fakat karar henüz verilmemiş [P1, P3–P5].”

**Ne elde ettik?**

İstisna ve karar durumu, dikkat dağıtan ayrıntıların arasında kaybolmadı.

## Nerede durmalı?

System 2 Attention cevaptan önce ilgili bağlamı yeniden üretir; Thread of Thought karmaşık bağlamı parça parça ele alma ve ardından cevap çıkarma istemini vurgular. Sınırları yakın olsa da özgün prompt düzenleri aynı değildir. Bu öğretim biçimi makalenin deneysel sonuçlarını yeniden üretmiş sayılmaz.

## Kaynaklar

- [Thread of Thought Unraveling Chaotic Contexts](https://arxiv.org/html/2311.08734) — Zhou, Yucheng; Geng, Xiubo; Shen, Tao; Tao, Chongyang; Long, Guodong; Lou, Jian-Guang; Shen, Jianbing. 2023-11-15. Kaotik bağlamı yönetilebilir parçalarla inceleyen ilk istemi ve ardından cevap çıkaran ikinci istemi tanımlar. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
