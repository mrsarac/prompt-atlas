# Chain-of-Density

Bring in the important information left in the source without making the summary longer.

## What is it?

Chain-of-Density first writes a sparser summary; then it makes the summary denser by adding missing important entities and details within the same word budget. Every added element must be in the source, and earlier important information must be kept.

## When does it help?

When you want short summaries to carry more and more information. Readability and accuracy take priority over density.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will develop a ten-word event summary.

**Prompt**

```text
Source: The watercolor workshop is on 12 October. There are eight places. The venue and fee have not been announced yet.
First summary: "Workshop held in October; limited places; venue, fee announced later."
Do one densification round in the same call: list the three missing elements, then rewrite the summary in exactly 10 words. Words are counted as items separated by spaces. Keep the earlier venue/fee uncertainty; do not add new information.
A human should check the count and the match with the source, and stop after one round.
```

**Sample output**

“Missing: watercolor, 12 October, eight people. New summary: Watercolor workshop on 12 October; eight places; venue, fee unknown.”

**What did we get?**

While the length stayed fixed, the topic, date and capacity became clear.

### Medium

**Situation**

Density will increase over two rounds, but earlier information must not drop out.

**Prompt**

```text
Source: The watercolor workshop will take place on 12 October. There are eight places. Materials are included. The venue and fee have not been announced.
First write a sparse summary of exactly 15 words. Then apply two rounds: name the 1–3 source elements missing at that point; add them and again write 15 words. Keep the earlier important facts. In each round, state the word count outside the summary.
A human should check the source, the preservation of earlier information and the 15-word condition. If no new elements remain, do not force-fill the second round; stop at two rounds at most.
```

**Sample output**

Example final summary: “Watercolor workshop on 12 October; eight places, materials included; venue and fee not yet announced.”

**What did we get?**

The target was not just shortening, but more source information at the same length.

### Hard

**Situation**

Densification can make an exception disappear.

**Prompt**

```text
Source: Applications close on 20 October. Students attend free of charge. Other participants pay 200 TL. There are 16 places. Access support must be requested in advance.
Write a summary of exactly 20 words; then find the missing elements and do at most two densification rounds. Do not extend the free attendance to everyone; do not assume access support is automatically ready.
In each round, a human should check these fields: closing date, who the fee depends on, capacity, the advance-request condition. If they do not fit into 20 words, do not invent details or delete a condition; report that the budget is insufficient.
```

**Sample output**

“Applications close 20 October; students attend free, others pay 200 TL. Capacity is 16 people; request access support in advance.”

**What did we get?**

The denser summary did not mix up the conditions for different groups.

## Where should you stop?

Density alone is not a measure of quality; an unreadable sentence or a lost exception is a failure. Adding details that are not in the source is not this method. The summarization context of the original work does not generalize directly to all kinds of writing.

## Sources

- [From Sparse to Dense: GPT-4 Summarization with Chain of Density Prompting](https://arxiv.org/html/2309.04269) — Adams, Griffin; Fabbri, Alexander; Ladhak, Faisal; Lehman, Eric; Elhadad, Noémie. 2023-09-08. Describes successive densification by adding missing, source-supported entities to a fixed-length summary; the scenarios are not a replication of the original news experiment. Evidence level: relevant body sections of the original paper.
