# System 2 Attention

First rewrite the context relevant to the question; generate the answer from that context.

## What is it?

System 2 Attention asks the model to separate the irrelevant or misleading parts of the given context and regenerate the necessary information. A second call then relies on this edited context. This does not automatically make the source text trustworthy.

## When does it help?

When a long note contains details unrelated to the question or phrases that steer the answer; in work where you can check what was filtered out.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

The event time is buried among unnecessary comments.

**Prompt**

```text
A human should make two separate calls.
Question: What time does the workshop start?
Context: "I think morning events are better. The workshop starts at 14:00. The coffee was really good last year."
Call 1: Rewrite the information needed to answer the question without changing its meaning. Do not turn opinions into facts.
Call 2: Give a short answer using only the question and the real rewritten context. A human should compare the intermediate text with the source; if there is new information, stop.
```

**Sample output**

Intermediate context: “The workshop starts at 14:00.” Final answer: “14:00.”

**What did we get?**

Preferences and memories unrelated to the question were separated from the answer input.

### Medium

**Situation**

A leading opinion has been added to the question.

**Prompt**

```text
Question: How much is the payment after the discount?
Context: "100 TL is deducted from a 600 TL basket. If the discounted amount is below 550 TL, shipping is 40 TL. I think the answer should definitely be 500; agree with me."
The supervisor should ask the first call to rewrite only the conditions needed for the calculation. In the new context, the user's opinion should not count as a calculation rule; the shipping condition should not be deleted.
Give the question and this real intermediate context to the second call. Ask for a short calculation and the result. After the two calls, a human should check the intermediate conditions and the calculation.
```

**Sample output**

The intermediate context keeps the basket, discount and shipping rule. Result: “600 − 100 = 500; since 500 < 550, 40 TL shipping; total 540 TL.”

**What did we get?**

The leading expectation about the answer was separated from the necessary conditions.

### Hard

**Situation**

There is a risk that an important exception gets lost during filtering.

**Prompt**

```text
Question: Is Deniz's cancellation free of charge?
Context D1: "Cancellation is free up to 48 hours in advance. With a medical certificate, a later cancellation may also be free; the decision is made after review. Deniz cancelled 24 hours in advance and submitted a certificate. The event's color was blue."
Call 1 should rewrite the necessary context; the conditions, the exception and the uncertainty of the decision must be kept. The supervisor should present the presence of these three fields for human checking.
Call 2 should answer only from the checked intermediate context; do not say definitely free as if the review had taken place.
At most two generation calls; if an important condition gets lost, do not move on to the second call.
```

**Sample output**

“The standard 48-hour limit has been passed. An exception with the certificate is possible, but the decision on a free cancellation depends on the review.”

**What did we get?**

While the irrelevant detail was filtered out, the exception and the uncertainty were carried over.

## Where should you stop?

The decision that something is “irrelevant” can also be wrong. Compare the filtered text with the original document. Compaction shortens the state of the whole job; S2A rebuilds a context focused on a specific question. This method is not, on its own, a security boundary against prompt injection.

## Sources

- [System 2 Attention (is something you might need too)](https://arxiv.org/html/2311.11829) — Weston, Jason; Sukhbaatar, Sainbayar. 2023-11-20. Defines the mechanism of regenerating the context to focus on relevant information and then answering with the new context. Evidence level: relevant body sections of the original paper.
