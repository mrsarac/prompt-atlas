# Öğretilebilir ajan

Model öğrenci rolünü sınırlı bir bilgi durumuyla sürdürsün; açıklayan sen ol.

## Nedir?

Öğretilebilir ajan yaklaşımında insan, konuyu bir yapay öğrenciye öğretir. TeachYou içindeki AlgoBo, bilgi durumunu ve yanıt davranışını düzenleyen bir akış kullanır; sadece “bilmiyormuş gibi yap” cümlesinden daha kapsamlıdır. Model ağırlıkları bu sohbetle eğitilmiş olmaz.

## Ne zaman işe yarar?

Bir kavramı öğretirken varsaydığınız bilgileri ve açıklamadaki boşlukları fark etmek için.

## Örnekler

Aşağıdaki durumlar ve yanıtlar kurgusal öğretim örnekleridir; çalıştırılmış model, araç veya benchmark sonuçları değildir.

### Basit (Simple)

**Durum**

Döngünün ne yaptığını yapay bir öğrenciye anlatacaksınız.

**Prompt**

```text
İnsan öğretmen; model öğrenci benzetimi. Bu, tam TeachYou sistemi değil, sınırlı sohbet uyarlaması.
Bilgi durumu: Listeyi biliyorsun, döngüyü henüz bilmiyorsun. Sana anlatmadığım kavramları biliyormuş gibi çözümleme. Benim açıklamam: "Döngü listedeki her öğe için aynı işi yapar."
Yalnız bu açıklamadan anladığını bir cümleyle söyle; ardından tek neden/nasıl sorusu sor. Cevabımı bekle. En fazla iki turda bilgi durumunda ne değiştiğini birlikte özetleyelim.
```

**Örnek çıktı**

Öğrenci: “Her öğeye aynı işlem uygulanıyor. Liste boşsa kaç kez çalışır?” İnsan: “Hiç çalışmaz.”

**Ne elde ettik?**

Öğreten kişi, açıklamasına sınır durumunu eklemek zorunda kaldı.

### Orta (Medium)

**Durum**

Öğrenci benzetimi, öğretmenin söylediğinden fazlasını biliyormuş gibi davranmamalı.

**Prompt**

```text
Uygulama durumu: bilinenler=[liste, döngü], açık_kavramlar=[koşul], öğretilenler=[].
İnsan açıklaması: "Pozitif sayıları seçmek için her sayının sıfırdan büyük olup olmadığına bakarız."
Aşama 1, ayrı model çağrısı: Bu açıklamanın hangi kavramı öğrettiğini ve hangi belirsizliği bıraktığını kısa durum önerisi yap.
Denetleyici onaylı durum güncellemesini saklasın. Aşama 2, ayrı yanıt çağrısı: Yalnız bu durumla öğrenci cevabı ver; sıfırın dahil olup olmadığını bir soruyla kontrol et.
İnsan yanıtından sonra bir tur daha yapılabilir; toplam 4 model çağrısında dur. Kaydedilmeyen durumun hatırlandığını iddia etme.
```

**Örnek çıktı**

Öğrenci: “Sıfırdan büyük olanları alıyorum; sıfır dışarıda mı?” Öğretmen yanıtı sonraki bilgi kaydına eklenir.

**Ne elde ettik?**

Öğrenci rolü görünür durumla sınırlandı; bilginin nereden geldiği izlendi.

### İleri (Hard)

**Durum**

Öğretenin bir yanlış genellemesi var; yardımcı kanal öğretimi desteklemeli.

**Prompt**

```text
Durumlu öğretilebilir ajan ve ayrı öğretim yardımcısı tasarla. Konu: listedeki en büyük sayıyı bulma. İnsan: "En büyük değer 0'dan başlatılır."
Öğrenci yanıt çağrısı, öğrendiği kuralla [-5,-2] listesini nasıl ele alacağını kısa biçimde söylesin; tam doğru çözümü dış bilgiden vermesin.
Ayrı yardımcı çağrı konuşmayı ve konu kuralını incelesin; öğretmene yalnız karşı örnek sorusu önerisi versin. Yardımcı mesajı öğrenci yanıtı diye sunma.
İnsan açıklamayı düzeltince durum güncellensin; yeni negatif listeyle öğretim kontrolü yapılsın. En fazla iki öğretim turu; son bağımsız insan alıştırması olmadan öğrenme kazanımı ilan etme.
```

**Örnek çıktı**

Öğrenci 0 sonucuna yönelirse yardımcı öğretmene “Bütün sayılar negatifse başlangıç değeri ne olmalı?” sorusunu önerir.

**Ne elde ettik?**

Öğretmenin açıklamasındaki hata ve yardımcının rolü ayrı kanallarda görüldü.

## Nerede durmalı?

Bir modelin öğrenci gibi konuşması gerçek bağımsız öğrenci veya ağırlık eğitimi değildir. AlgoBo’daki bilgi yoğun konuşma bulgusu son-test kazanımıyla karıştırılmamalı. Ayrı bir müzik eğitimi çalışmasının öğrenme sonucu da bu kodlama sisteminin sonucu değildir.

## Kaynaklar

- [Teach AI How to Code: Using Large Language Models as Teachable Agents for Programming Education](https://arxiv.org/html/2309.14534) — Jin, Hyoungwook; Lee, Seonghee; Shin, Hyungyu; Kim, Juho. 2023-09-25; okunan sürüm 2024-03-11. Bilgi durumunu sınırlayan, Reflect–Respond ve soru davranışını düzenleyen TeachYou/AlgoBo akışını tanımlar; konuşma ölçütleri öğrenme testiyle aynı değildir. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
- [Exploring the Impact of an LLM-Powered Teachable Agent on Learning Gains and Cognitive Load in Music Education](https://arxiv.org/html/2504.00636) — Jin, Lingxi; Lin, Baicheng; Hong, Mengze; Zhang, Kun; So, Hyo-Jeong. 2025-04-01. Ayrı bir müzik eğitimi bağlamındaki öğretilebilir ajan çalışmasıdır; sonuçları AlgoBo’nun kodlama çalışmasına taşınmaz. Kanıt düzeyi: özgün makalenin ilgili gövde bölümleri.
