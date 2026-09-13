# Modüler master prompt

Projenin tekrar kullanılan çalışma kurallarını bir belgede tutun.

## Nedir?

Master prompt, her görevde yeniden yazmak istemediğiniz amacı, sınırları ve teslim ölçütlerini bir araya getiren belgedir. O günün işi değişebilir; ortak kurallar ayrı durur. Belgeyi çağrıya gerçekten eklemeniz gerekir: dosyanın varlığı modelin onu okuduğunu göstermez.

Bu adı burada pratik bir talimat varlığı için kullanıyoruz. Meta prompt başka bir promptu üretir; RUNE belirli bir katman düzeni sunar. Master prompt bu iki yolla hazırlanabilir, ama ikisini zorunlu kılmaz.

## Ne zaman işe yarar?

Aynı projede art arda yazı, kod veya araştırma işleri yürütürken yararlıdır. Ortak kuralları kısa tutun; değişken görev verisini ayrı verin.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Bir atölyenin duyurularında kayıt koşulu her seferinde korunmalı.

**Prompt**

```text
ORTAK KURALLAR v1
Türkçe ve açık yaz. Kayıt, onay e-postasıyla kesinleşir. Tarih verilmediyse tarih ekleme. Çıktı en fazla iki cümle.
BUGÜNKÜ GÖREV
Çizim atölyesine formdan başvuru çağrısı yaz. Kapasite 20 kişi.
```

**Örnek çıktı**

20 kişilik çizim atölyesine formu doldurarak başvurabilirsiniz. Yeriniz, onay e-postası geldiğinde kesinleşir.

**Ne elde ettik?**

Sabit kayıt kuralı tekil duyuruya taşındı. Sonraki görevde de ortak kuralları çağrıya eklemek sizin sorumluluğunuzda.

### Orta (Medium)

**Durum**

Ortak kural ile günlük istek çelişiyor.

**Prompt**

```text
ORTAK KURALLAR v2
Verilen bilgilerin dışına çıkma. Tarih belirsizse belirsizliği koru. Çelişkide kesin tarih yayımlamadan beni uyar.
GÖREV
Taslakta “Atölye cumartesi” yazıyor; organizatörün son notu “Gün henüz kesin değil.” Sosyal medya duyurusunu hazırla; taslaktaki günü kesin bilgi gibi kullanma.
```

**Örnek çıktı**

Tarih kaynakları çelişiyor. Tarihsiz taslak: “Atölye için tarih bilgisi henüz doğrulanmadı.” Gün kesinleşmeden cumartesi ifadesi kullanılmamalı.

**Ne elde ettik?**

Belge bir çatışma davranışı tarif etti. Gerçek yayın ve tarih teyidi insanda kaldı.

### İleri (Hard)

**Durum**

İki aşamalı yazı işinde aynı dosya sınırı sonraki çağrıda kaybolabilir.

**Prompt**

```text
İnsan koordinatör için devir taslağı:
Ortak sözleşme v3: yalnız taslak.md değişebilir; kaynak.md ve arsiv.md salt okunur; dış yayın yok.
Aşama 1 çağrısı: Bu sözleşmeyi ve “Başvuru formuyla alınır; onay e-postasıyla kesinleşir” kaynağını ekle. taslak.md için iki cümle öner.
Aşama 2 çağrısı: Aynı sözleşme v3, aynı kaynak ve birinci çağrının metnini yeniden ekle. Yalnız anlamı koruyan dil düzeltmesi iste.
Her devirde aktarılan sözleşme sürümünü kaydet. En fazla iki çağrı. Gerçek yazma araçları bu dosya listesiyle sınırlandırılmalı; değişiklik listesi dışına çıkarsa işi kabul etme.
```

**Örnek çıktı**

Devir paketi: sözleşme v3 + kaynak cümlesi + taslak metni. İkinci aşamanın beklenen teslimi yalnız taslak.md metnidir; arsiv.md değişikliği kabul dışıdır.

**Ne elde ettik?**

Master prompt’un sonraki çağrıya hangi veriyle taşınacağı belli. Koordinatör gerçek dosya farklarını ve izinleri denetlemeden “tamamlandı” mesajını kabul etmez.

## Nerede durmalı?

Uzun belge daha iyi belge demek değildir. Güncelliğini yitiren kurallar ve aynı alanı farklı söyleyen bölümler çelişki üretir. API mesaj önceliği uygulamanın kullandığı gerçek role bağlıdır. Bir metne “en üst yetki” yazmak teknik erişim kazandırmaz.

## Kaynaklar

- [Master Prompts and System Prompts: The ChatGPT-5 Growth Blueprint](https://www.danmartell.com/master-prompts-system-prompts-and-custom-gpts/) — Dan Martell. 2026-02-23; okunan sürüm 2026-02-23. Master ve system prompt adlarının pratisyen kullanımına örnektir; bu belgenin tek akademik kökeni veya üstünlük kanıtı değildir. Kanıt düzeyi: sayfa gövdesi.
- [Prompt engineering | OpenAI API](https://developers.openai.com/api/docs/guides/prompt-engineering?api-mode=responses) — OpenAI. yayın tarihi doğrulanmadı. Tekrar kullanılan talimat, bağlam ve mesaj rolleri ayrımına dayanak sağlar. Kanıt düzeyi: sayfa gövdesi.
