# Context compaction

Uzun geçmişi kısaltırken kararları ve açık işleri kaybetme.

## Nedir?

Bağlam sıkıştırma, konuşma veya araç geçmişinden sonraki adım için gerekli durumu çıkarır. Bu özet, geçmişin birebir yedeği değildir. Kaynak işaretleri ve belirsizlikler korunursa ayrıntıya yeniden dönülebilir.

## Ne zaman işe yarar?

Uzayan oturumda aynı kararlar unutuluyorsa veya yeni çağrıya bütün geçmişi taşımak maliyetliyse.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir yazının kararlaştırılmış özelliklerini yeni sohbete taşıyacaksınız.

**Prompt**

```text
İnsan başlatır: Aşağıdaki geçmişi bir devir notuna dönüştür.
Geçmiş: Başta 1000 kelime dedik. Sonra hedefi 400 kelimeye indirdim. Okur yeni başlayanlar. Ton sade. Başlık seçilmedi.
Alanlar: güncel hedef, geçersiz kalan karar, değişmeyen kısıt, açık soru. Son kararı öncekiyle karıştırma.
İnsan notu geçmişle karşılaştırsın; onaylı not yeni sohbetin ilk girdisi olsun. Başlık uydurma; dört alan tamamlanınca dur.
```

**Örnek çıktı**

“Hedef: 400 kelime. Eski karar: 1000 kelime, geçersiz. Kısıt: yeni başlayanlara sade dil. Açık: başlık.”

**Ne elde ettik?**

Kısalma, eski ve yeni kararları tek bir ortalamaya dönüştürmedi.

### Orta (Medium)

**Durum**

Araç kayıtlarının çoğu tekrar; bir hata bilgisi ise önemli.

**Prompt**

```text
Denetleyici kayıtları özetleme çağrısına versin:
L1 test_a geçti. L2 test_a tekrar geçti. L3 test_b timeout; sonuç bilinmiyor. L4 kullanıcı: yalnız parser.js değişebilir.
Devir notu: yetki, doğrulanmış sonuç, belirsiz sonuç, sonraki izinli adım, kaynak satırları. Timeout'u başarısız test sonucu veya geçti diye yazma.
İnsan L3 ve L4'ü özellikle kontrol etsin. Yeni çağrıya onaylı notla birlikte gerektiğinde L1-L4'e salt okunur erişim verilsin. Özet doğrulanmadan eski kayıt silinmesin.
```

**Örnek çıktı**

“Yetki parser.js [L4]. test_a geçti [L1–L2]. test_b zaman aşımı nedeniyle belirsiz [L3]. Sonraki adım: ilgili hata kaydını incele.”

**Ne elde ettik?**

Tekrarlar küçüldü; belirsizlik ve dosya sınırı korundu.

### İleri (Hard)

**Durum**

Bir proje devrinde iki not arasında çelişki var.

**Prompt**

```text
Girdi: N1, 09.00: "Teslim cuma; taslak hazır." N2, 11.00: "Teslim pazartesi; görsel henüz onaylanmadı." Kararı kimin verdiği kayıtlı değil.
Denetleyici yeni bağlama en fazla 180 kelimelik durum özeti taşısın; N1/N2 özgün kayıtlarını saklasın.
Model: Güncel olduğu açık alanları, çelişkileri ve karar sahibinden istenecek tek açıklamayı ayır. Daha geç tarihli kaydı otomatik yetkili sayma.
Geçiş kontrolü: teslim tarihi kesinleştirilmemiş olarak kalmalı. Yeni ajan yalnız taslak ve görsel durumunu inceleyebilir; teslim sözü veremez. Çelişkiyi devredince sıkıştırmayı bitir.
```

**Örnek çıktı**

“Taslak hazır [N1]; görsel onaysız [N2]. Teslim günü çelişkili ve yetkili karar kaydı yok. Karar sahibinden cuma/pazartesi teyidi gerekli.”

**Ne elde ettik?**

Sıkıştırma, eksik yetki bilgisini sessizce karara çevirmedi.

## Nerede durmalı?

Özet de yanlış olabilir. Kritik sayıları, yetki sınırlarını ve tamamlanma ölçütlerini kaynakla kontrol edin. Bağlam kapasitesi büyüdü diye uzun metnin her konumundaki bilgi eşit kullanılacak varsayımı güvenli değildir; eski deney sonuçları her yeni modele doğrudan taşınamaz.

## Kaynaklar

- [Effective context engineering for AI agents \ Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Anthropic. 2025-09-29. Compaction yaklaşımını, önemli durumun korunmasını ve aşırı sıkıştırmanın riskini tartışır. Kanıt düzeyi: sayfa gövdesi.
- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/html/2307.03172) — Liu, Nelson F.; Lin, Kevin; Hewitt, John; Paranjape, Ashwin; Bevilacqua, Michele; Petroni, Fabio; Liang, Percy. 2023-07-06; okunan sürüm 2023-11-20. İncelenen modeller ve görevlerde ilgili bilginin bağlam içindeki yerinin performansı etkileyebildiğini gösterir; özetlemenin her durumda başarı sağlayacağını kanıtlamaz. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
