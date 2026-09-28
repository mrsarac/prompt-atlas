# Citation contract

Match every claim with the passage that actually supports it.

## What is it?

A citation contract is an output rule that makes visible which document the answer relies on. The model adds a source code next to the claim; the reader can open that passage and check the relationship. Attaching a code to a claim that is not in the source does not make it supported.

If the documents are already in your hands, this task is only answering with sources. RAG also includes the stage that finds and fetches the relevant document. Here we do not pretend a search was run.

## When does it help?

Use it for document summaries, research notes and explaining conditions with their sources. Each document should have a short code and a readable body.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will extract the reading room's closing time from a short note.

**Prompt**

```text
Question: What time does the reading room close?
[K1] The reading room is open on weekdays, 09:00–17:00.
Use only K1. Put the source code next to the answer and briefly quote the supporting sentence. Do not add information about weekends.
```

**Sample output**

It closes at 17:00 on weekdays. [K1] Support: “open on weekdays, 09:00–17:00.”

**What did we get?**

It is clear which passage the time comes from. The source code does not independently verify the room's actual current hours.

### Medium

**Situation**

Two documents explain registration and materials separately.

**Prompt**

```text
Question: How do I register for the workshop; do I need a notebook and pens?
[K1] Fill in the form. Your place is confirmed by the confirmation email.
[K2] Bring your notebook; pens are provided at the workshop.
Add the correct code to each independent piece of information. Do not use a single code as if it were evidence for the whole paragraph. Do not add duration or fee information that is not in the documents.
```

**Sample output**

Apply with the form; your place is confirmed by the confirmation email. [K1] Bring your notebook; pens are provided. [K2]

**What did we get?**

The support for each sentence can be traced separately. There is no impression that K1 supports the materials condition.

### Hard

**Situation**

A draft sentence draws a stronger conclusion than the two sources allow.

**Prompt**

```text
Draft: “The workshop provides free materials and a later video recording for all participants.”
[K1] Participation is free.
[K2] Participants bring their own notebook; pens are provided.
Sort each claim into supported / contradicted / not in the sources. Then write a new text using only the supported information. Do not make a definite statement that there is no video recording; say that there is no information about it.
```

**Sample output**

That participation is free is supported [K1]. That all materials are provided is contradicted [K2]. A video recording is not in the sources. New text: “Participation is free. [K1] Bring your notebook; pens are provided. [K2] These documents contain no information about a video recording.”

**What did we get?**

The strength of the claim was limited by the source. Missing information and negative information did not get mixed up.

## Where should you stop?

Citation quality, answer correctness and the reliability of the source itself are separate things. The model can tie a correct source to a wrong claim. ALCE is a research setup that evaluates these; the short contract we write here does not rebuild its whole system.

## Sources

- [Enabling Large Language Models to Generate Text with Citations](https://arxiv.org/html/2305.14627) — Gao, Tianyu; Yen, Howard; Yu, Jiatong; Chen, Danqi. 2023-05-24; version read 2023-10-31. ALCE evaluates fluency, correctness and citation quality separately; supports the point that a source code alone is not enough. Evidence level: relevant body sections of the original paper.
- [Prompt engineering | OpenAI API](https://developers.openai.com/api/docs/guides/prompt-engineering?api-mode=responses) — OpenAI. Publication date not verified. Provides grounding for stating the given context and the output instructions explicitly. Evidence level: page body.
