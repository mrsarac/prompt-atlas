# Contributing / Katkı

This repository is the forward editing source for the open card collection. Contributions are reviewed here. A reviewed change can enter a release; the website imports a pinned version in a separate integration step. A pull request or merge here does not immediately publish a change on the website.

## Kartı düzenlemek

1. İlgili kartı `cards/` altında bulun. Yeni kart için [şablonu](templates/card.md) kullanın; şablonun kendisi kataloğa dahil değildir.
2. Mevcut kartın `id`, `slug` ve dosya adını koruyun. Yeni kart için kullanılmayan bir kimlik ve küçük ASCII harfleriyle, sözcükleri tireyle ayrılmış bir slug seçin. Kimlik ve slug değişikliği mevcut bağlantıları etkiler; bunu incelemede açıkça belirtin.
3. `index.json` içindeki kaydı güncelleyin. Yalnız şu alanlar vardır: `id`, `slug`, `title`, `section`, `tags`, `aliases`, `mark`, `file`, `related_ids`. `file`, tam olarak `slug.md` biçimindedir; `related_ids` alanı tarihsel adına rağmen diğer kartların **slug** değerlerini taşır. Yerel yollar, görsel alanları ve özel kaynak kayıt numaraları eklemeyin.
4. Kataloğu yeniden üretip testleri çalıştırın. `catalog.json` dosyasını elle düzenlemeyin; güncel üretilmiş dosyayı katkınıza dahil edin.
5. Pull request açıklamasında sorunu, değişikliği ve kaynaklarını yazın. İnceleyen kişi metni, yöntemin doğru aktarılmasını, örnekleri ve lisans kapsamını kontrol eder.

```sh
python3 -B scripts/catalog.py generate
python3 -B -m unittest discover -s tests -v
python3 -B scripts/catalog.py check
```

Python 3.10 veya üstü yeterlidir; bağımlılık kurulumu gerekmez. Komutlar kartlardaki kodu ya da promptları çalıştırmaz. Test girdileri sentetiktir. Doğrulayıcı kart sayısını 81'e sabitlemez; yeni kartlar aynı şemayla eklenebilir.

## İçerik ölçüsü

- Kısa ve kendi başına anlaşılır Türkçe kullanın. Ad, kısa açıklama, “Nedir?”, “Ne zaman işe yarar?”, üç örnek, sınırlar ve kaynaklar birlikte bulunmalı.
- **Basit / Orta / İleri** aynı promptun uzatılmış halleri olmamalı. Her düzeyde somut durum, tam kullanılabilir prompt veya aşamalı kontrol taslağı, temsili çıktı/diyalog ve “Ne elde ettik?” bulunmalı.
- Örnekleri kurgusal öğretim örneği olarak belirtin. Gerçekte çalıştırılmamış bir yanıtı ölçüm, benchmark veya kişisel deneyim gibi sunmayın. İnsanların öğrenmesiyle model davranışını ayırın.
- Çok çağrılı, araçlı veya ajanlı yöntemlerde çağrıyı kimin başlattığını, girdilerin aktarımını, dış araç gereksinimini ve durma/kontrol koşulunu gösterin. Bir modelin rol yapmasını bağımsız ajan çalışması diye sunmayın. Kısa, denetlenebilir gerekçe isteyin; gizli düşünce dökümü istemeyin.
- Kaynak bölümünde özgün kaynağın başlığı, yazarı, bilinen tarihi, tam kamuya açık URL'si ve hangi dar iddiayı desteklediği bulunsun. Tarih veya kanıt bilinmiyorsa söyleyin. Atıf tek başına doğruluk kanıtı değildir. Bu derleme bütün yöntemleri kapsadığını iddia etmez.
- Kaynağı olmayan başarı iddiası, gizli bilgi, özel kayıt, görsel veya üçüncü taraf malzemeyi kendi lisansımızla yeniden dağıtma iddiası eklemeyin.

Başlıkları ve kalın alan adlarını şablondaki sırayla koruyun. Dosyalar UTF-8, BOM olmadan, LF satır sonlarıyla ve son satır sonu karakteriyle kaydedilir. `cards/` yalnız indekste listelenen doğrudan Markdown dosyalarını içerir; alt klasör, symlink ve yol geçişi kabul edilmez.

Doğrulayıcı yapıyı, alanları ve kaynak bağlantısının varlığını denetler. Bir iddianın doğruluğunu veya bir örneğin pedagojik kalitesini otomatik olarak doğrulamaz; bunlar insan incelemesinin parçasıdır.

## Contribution license

By submitting original card content or authored documentation for inclusion, you offer that contribution under **CC BY 4.0**. By submitting tooling, tests or workflow changes, you offer them under **MIT** in [LICENSE-CODE](LICENSE-CODE). You retain any rights you hold; attribution does not imply endorsement. Commercial reuse of CC BY 4.0 content is permitted with appropriate attribution, a license link and an indication of changes.

Contribute only material you can offer on these terms, and identify any third-party material and its separate terms. The license covers original expression and compilation only to the extent rights exist, not exclusive rights over techniques, facts, third-party works or wholly unprotectable model output. Images and the private website's code and records are excluded. See [ATTRIBUTION.md](ATTRIBUTION.md) and the complete [content license](LICENSE).
