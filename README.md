# Prompt Atlas

Prompt Atlas is a curated collection of **81 prompting and learning cards** with **243 Simple / Medium / Hard scenarios**, available in English at [`en/`](en/) and in the original Turkish at [`cards/`](cards/). It is not a benchmark, a model comparison or a claim to cover every technique.

**English edition:** [`en/`](en/) contains English translations of all 81 cards / 243 scenarios. Each English card keeps the Turkish card's ID, slug, file name, section, tags, relations, source links and scenario structure; only the reader-facing text, title and aliases are translated. The Turkish cards remain the original collection. The examples are fictional teaching examples, not executed model or benchmark results. The website imports a pinned release separately; changes here, including the English edition, are not published there automatically.

Card content is available under **CC BY 4.0**, including commercial reuse with attribution, a license link and an indication of changes. The small validation tooling is **MIT**. See [license scope and attribution](ATTRIBUTION.md), the complete [content license](LICENSE) and [tooling license](LICENSE-CODE). Credit does not imply endorsement. Images and the private website's code are excluded.

Public repository: **[mrsarac/prompt-atlas](https://github.com/mrsarac/prompt-atlas)**. The collection is published, and its website reading surfaces were verified live on **2026-09-14**. The website pins the card content from commit `82b2a48fbed05caffc6d8a204ab243de622ef0a6`; later repository changes are not automatically deployed to the website.

## Türkçe kullanım

İşinize yakın bir kartı aşağıdaki dizinden seçin. **Basit** örnekle yöntemin küçük bir işte nasıl kullanıldığını görün; **Orta** örnekte ek koşulu, **İleri** örnekte birbirine bağlı adımları izleyin. Bunlar başarı sıralaması veya ölçülmüş model yetenek seviyeleri değildir.

Her kartta yöntemin açıklaması, ne zaman işe yaradığı, üç durum ve prompt, kısa temsili çıktı/diyalog, elde edilen sonuç, sınırlar ve özgün kaynaklar bulunur. Örnekler **kurgusal öğretim örnekleridir**; çalıştırılmış model veya benchmark sonuçları değildir. Çok çağrılı ya da araç gerektiren bir yöntemi kullanırken kartta belirtilen aşamalar ve dış araçlar ayrıca gerekir.

Kartları doğrudan Markdown olarak okuyabilir veya `catalog.json` ile kendi arama arayüzünüze aktarabilirsiniz. Başlık, etiket ve alternatif adlar `index.json` içindedir; katalog bunlara **tam kart metnini** ekler. Katalogda görsel bulunmaz.

Canlı okuma adresleri [Prompt Atlası](https://mustafasarac.com/prompt-atlasi/) ve [kısa rehber](https://mustafasarac.com/posts/prompting-atlasi-master-meta-prompt-ve-ajan-teknikleri/); ikisi de 2026-09-14 tarihinde gerçek tarayıcıyla doğrulandı. Bu README güncellemesi kartları, kataloğu veya sitenin sabitlediği içerik sürümünü değiştirmez.

## Dosyalar ve veri biçimi

| Dosya | İçerik |
| --- | --- |
| `cards/*.md` | Düzenlenecek asıl kart metinleri |
| [index.json](index.json) | Sıralı, kamuya açık kart metadata dizisi |
| [catalog.json](catalog.json) | Metadata ve tam Markdown içeren üretilmiş katalog |
| [templates/card.md](templates/card.md) | Yeni katkılar için şablon; katalog kartı değildir |
| [scripts/catalog.py](scripts/catalog.py) | Bağımsız Python üretici ve doğrulayıcı |
| [CONTRIBUTING.md](CONTRIBUTING.md) | İçerik, inceleme ve lisans koşulları |
| `en/cards/*.md`, [en/index.json](en/index.json), [en/catalog.json](en/catalog.json) | İngilizce sürüm: aynı kimlik ve ilişkilerle çevrilmiş kartlar, indeks ve üretilmiş katalog (`language: "en"`) |

Katalog şeması: `schema: "prompt-atlas.catalog"`, `version: 1`, `language: "tr"`, `content_license: "CC-BY-4.0"`, `cards: [...]`. `version` veri şemasının sürümüdür; bir Git etiketi veya yayın kimliği değildir. Her kart, indeksteki dokuz alanın tamamını ve `markdown` alanını taşır:

- `id`, `slug`, `title`, `section`, `tags`, `aliases`, `mark`, `file`, `related_ids`.
- `file`, `cards/` altındaki basit dosya adıdır; mutlak veya yerel sistem yolu değildir.
- `related_ids`, tarihsel alan adına rağmen ilgili kartların **slug** değerlerini taşır.
- Kartların sırası indeks sırasıdır. Üretim zaman damgası veya görsel metadata eklenmez.

Bugünkü 81/243 sayıları başlangıç koleksiyonunu anlatır. Şema ve testler gelecekteki katkılar için başka kart sayılarını destekler.

## Yerel doğrulama

Python 3.10+ ve standart kütüphane yeterlidir; ek paket kurulumu veya ağ erişimi gerekmez:

```sh
python3 -B -m unittest discover -s tests -v
python3 -B scripts/catalog.py generate
python3 -B scripts/catalog.py check
```

`generate` yalnız `catalog.json` dosyasını, `en/` varsa ayrıca `en/catalog.json` dosyasını üretir. İngilizce kartlar İngilizce başlık/alan adlarıyla doğrulanır ve Türkçe kartlarla birebir eşleşmelidir: aynı sıra, kimlik, slug, bölüm, etiket, işaret, dosya ve ilişkiler; aynı kaynak URL'leri, kod çitleri, liste öğesi sayısı ve çıktı/diyalog türü. Herhangi bir doğrulama hatasında hiçbir katalog yazılmaz. `check` kaynakları doğrular ve kataloğun bunlardan birebir üretilebildiğini denetler; dosya yazmaz. Aynı girdiler aynı UTF-8/LF baytlarını üretir. Kart içindeki kod ve promptlar çalıştırılmaz. Testler sentetik girdiler kullanır. Yapı denetimi, akademik iddiaların doğrulandığı anlamına gelmez.

## Katkı ve sitenin güncellenmesi

Kart düzenlemelerinin bundan sonraki kaynağı bu depodur. [Katkı rehberini](CONTRIBUTING.md) izleyerek değişikliği burada önerin. İncelenen katkılar bir sürüme alınır; site belirli bir sürümü/tam commit kimliğini ve içerik hash'ini sabitleyerek ayrı bir adımda içe aktarır. Buradaki bir katkı veya birleştirme siteyi anında yayımlamaz; site çalışma anında GitHub'dan kart çekmez.

Lisans, Mustafa Saraç'ın özgün kart anlatımı ve derlemesine hakların var olduğu ölçüde uygulanır. Teknikler, olgular, üçüncü taraf eserler veya bütünüyle korunamayan model çıktısı üzerinde sahiplik iddiası değildir. Kaynak verilen makale ve sitelerin kendi koşulları geçerlidir. Görseller, özel site kodu, eşlik eden rehber yazısı, araştırma arşivleri ve iç kayıtlar bu pakete dahil değildir.

## Kart dizini

Bölümler: `temel` başlangıç, `yazi` yazı, `kod` kod, `arastirma` araştırma, `ajan` ajan iş akışları, `ogrenme` düşünme ve öğrenme. Bir kartın etiketleri birden fazla işe işaret edebilir. Sayfada arama yapmak veya aşağıdaki bağlantıları açmak yeterlidir.

| Kimlik | Kart | Bölüm |
| --- | --- | --- |
| T01 | [Görev ve çıktı sözleşmesi](cards/gorev-sozlesmesi.md) | temel |
| T02 | [Few-shot](cards/few-shot.md) | temel |
| T03 | [Rol ve persona](cards/rol-persona.md) | yazi |
| T04 | [CO-STAR](cards/co-star.md) | yazi |
| T05 | [Chain-of-Thought](cards/chain-of-thought.md) | kod |
| T06 | [Zero-shot CoT](cards/zero-shot-cot.md) | kod |
| T07 | [Least-to-Most](cards/least-to-most.md) | kod |
| T08 | [Step-Back](cards/step-back.md) | arastirma |
| T09 | [Self-Consistency](cards/self-consistency.md) | kod |
| T10 | [Tree of Thoughts](cards/tree-of-thoughts.md) | kod |
| T11 | [PAL](cards/pal.md) | kod |
| T12 | [RAG — Kaynağı bul, cevabı ona dayandır](cards/rag.md) | arastirma |
| T13 | [Atıf sözleşmesi](cards/atif-sozlesmesi.md) | arastirma |
| T14 | [HyDE](cards/hyde.md) | arastirma |
| T15 | [IRCoT](cards/ircot.md) | arastirma |
| T16 | [Structured Outputs](cards/structured-outputs.md) | kod |
| T17 | [Ayraçlar ve etiketli bağlam](cards/ayraclar.md) | temel |
| T18 | [Self-Refine](cards/self-refine.md) | yazi |
| T19 | [Chain-of-Verification](cards/chain-of-verification.md) | arastirma |
| T20 | [Reflexion](cards/reflexion.md) | ajan |
| T21 | [LLM-as-a-judge](cards/llm-judge.md) | yazi |
| T22 | [Prompt üreten meta prompt](cards/meta-prompt-uretimi.md) | yazi |
| T23 | [Meta-Prompting: uzman çağrıları](cards/meta-orkestrasyon.md) | ajan |
| T24 | [Meta Prompting: yapısal şema](cards/meta-yapisal-sema.md) | kod |
| T25 | [Automatic Prompt Engineer](cards/ape.md) | kod |
| T26 | [OPRO](cards/opro.md) | kod |
| T27 | [GEPA](cards/gepa.md) | kod |
| T28 | [DSPy](cards/dspy.md) | kod |
| T29 | [Inverse Prompting](cards/inverse-prompting.md) | yazi |
| T30 | [ReAct](cards/react.md) | ajan |
| T31 | [Prompt chaining](cards/prompt-chaining.md) | ajan |
| T32 | [Araç ve sonuç sözleşmesi](cards/arac-sozlesmesi.md) | ajan |
| T33 | [Sınırlı yürütme ve yetki](cards/sinirli-yurutme.md) | ajan |
| T34 | [Modüler master prompt](cards/master-prompt.md) | ajan |
| T35 | [Context compaction](cards/context-compaction.md) | ajan |
| T36 | [Yapılandırılmış harici notlar](cards/harici-notlar.md) | ajan |
| T37 | [Flipped Interaction](cards/flipped-interaction.md) | arastirma |
| T38 | [Question Refinement](cards/question-refinement.md) | arastirma |
| T39 | [Belirsizlik ve yanıt vermeme](cards/belirsizlik-sozlesmesi.md) | arastirma |
| T40 | [Güvenilmeyen girdiyi ayırma](cards/guvenilmeyen-girdi.md) | ajan |
| R01 | [RUNE](cards/rune.md) | ajan |
| E01 | [Chain of Draft](cards/chain-of-draft.md) | kod |
| E02 | [Graph of Thoughts](cards/graph-of-thoughts.md) | kod |
| E03 | [Generated Knowledge](cards/generated-knowledge.md) | arastirma |
| E04 | [Plan-and-Solve](cards/plan-and-solve.md) | kod |
| E06 | [Self-Ask](cards/self-ask.md) | arastirma |
| E07 | [EmotionPrompt](cards/emotion-prompting.md) | yazi |
| E08 | [Skeleton-of-Thought](cards/skeleton-of-thought.md) | yazi |
| E09 | [System 2 Attention](cards/system-2-attention.md) | arastirma |
| E10 | [Chain-of-Density](cards/chain-of-density.md) | yazi |
| E11 | [Directional Stimulus Prompting](cards/directional-stimulus.md) | yazi |
| E12 | [Medprompt](cards/medprompt.md) | arastirma |
| E13 | [CRITIC](cards/critic.md) | arastirma |
| E14 | [Thread of Thought](cards/thread-of-thought.md) | arastirma |
| E15 | [Program of Thoughts](cards/program-of-thoughts.md) | kod |
| C01 | [Reversing Chain-of-Thought](cards/reversing-cot.md) | kod |
| C02 | [Active Prompting](cards/active-prompting.md) | kod |
| C03 | [Decomposed Prompting](cards/decomposed-prompting.md) | kod |
| M01 | [Rubber Duck](cards/rubber-duck.md) | yazi |
| M02 | [Kendine açıklama](cards/kendine-aciklama.md) | ogrenme |
| M03 | [Teach-back](cards/teach-back.md) | ogrenme |
| M06 | [Öğretilebilir ajan](cards/ogretilebilir-ajan.md) | ogrenme |
| M07 | [Sokratik öğretici diyalog](cards/sokratik-ogretim.md) | ogrenme |
| M08 | [Karşılıklı sav sorgulama](cards/karsilikli-sorgulama.md) | arastirma |
| M09 | [Recursive Socratic Questioning](cards/recursive-socratic.md) | kod |
| M10 | [Hatırlama alıştırması](cards/hatirlama-alistirmasi.md) | ogrenme |
| M11 | [Aralıklı tekrar](cards/aralikli-tekrar.md) | ogrenme |
| M12 | [Problem çerçeveleme](cards/problem-cerceveleme.md) | arastirma |
| M14 | [Tercihleri açığa çıkarma](cards/tercihleri-aciga-cikarma.md) | ogrenme |
| M15 | [Self-Debug](cards/self-debug.md) | kod |
| M17 | [Metacognitive Prompting](cards/metacognitive-prompting.md) | arastirma |
| M18 | [Cognitive Verifier](cards/cognitive-verifier.md) | arastirma |
| M19 | [Alternatif yaklaşımlar](cards/alternatif-yaklasimlar.md) | yazi |
| M20 | [Analogical Prompting](cards/analogical-prompting.md) | kod |
| M21 | [Ortak fikir üretimi](cards/ortak-fikir-uretimi.md) | yazi |
| M22 | [Premortem](cards/premortem.md) | ajan |
| M23 | [Argüman haritası](cards/arguman-haritasi.md) | arastirma |
| M24 | [Önce insanın yargısı](cards/once-insan-yargisi.md) | ogrenme |
| M25 | [Grup tartışmasını kolaylaştırma](cards/grup-kolaylastirma.md) | ajan |
| M26 | [Multiagent Debate](cards/multiagent-debate.md) | ajan |
| M27 | [Tutor gözetmeni](cards/tutor-gozetmeni.md) | ajan |

Status / limits: This repository contains the card sources and generated catalogs; examples are fictional teaching examples, not benchmark results.
