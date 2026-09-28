# Self-Consistency

Take separate samples for the same question; count the final answers in a common format.

## What is it?

Instead of having a model reread its single answer, Self-Consistency generates differently sampled solutions to the same problem. The final answers are put into a common format and the most frequent answer is chosen. The original method requires sampling that produces diversity, plus aggregation.

The calls should start without seeing each other's answers. They can come from the same model; that does not make them independent sources of knowledge. Writing “think like three experts” inside one chat does not set up this process.

## When does it help?

Use it for numeric, multiple-choice or short-label tasks where the final answers can be compared. A human can open separate chats; in automation, you need a coordinator with access to the sampling settings and a call budget.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will get three separate answers for the same pen calculation.

**Prompt**

```text
The coordinator gives the same input to three separate sampling calls; it does not share the responses between them:
“There are five pens in each of four boxes; three are given away. Write a short check equation and the final number of pens.”
If sampling is supported, use a setting that allows different samples; do not duplicate one copied response.
Read the final answers as integers and count the most frequent one. In a tie, do not pick a result. After the three calls, check the calculation externally.
```

**Sample output**

Representative separate results: 17, 17, 23. Count: 17 twice, 23 once. Selected candidate: 17.

**What did we get?**

A candidate was selected by vote frequency. The calculation 4×5−3 shows whether it is correct; the vote alone is not proof.

### Medium

**Situation**

The same amount of money can be written in different formats.

**Prompt**

```text
Give five separate calls this question: “3 products cost 80 TL each. A 25% discount on the products, then 20 TL shipping. What is the total? Include the currency.”
The coordinator normalizes only the final amount: 200 TL and 200.00 TL are the same value. Mark a response with a different unit, or one that cannot be parsed, as invalid; do not silently convert it.
Report the most frequent amount together with the number of valid/invalid responses. At most five calls; in a tie, human review.
```

**Sample output**

Representative results: 200 TL, 200.00 TL, 200 TL, 195 TL, “I don't know”. 4 valid, 1 invalid; 200 TL appears three times.

**What did we get?**

A difference in format was prevented from splitting the votes. Keeping the invalid samples shows what the selection rests on.

### Hard

**Situation**

When a rule is missing, the majority can make the same assumption.

**Prompt**

```text
The coordinator makes five separate calls:
“The product costs 600 TL, the discount is 100 TL, the free-shipping threshold is 550 TL; paid shipping is 40 TL. It is not stated whether the threshold applies before or after the discount. Write the result and the assumption it requires.”
Answer classes: 500, 540, missing-rule. Keep the count. Even if the majority states a definite amount, a human separately checks the gap in the rule in the original question.
Stop after five calls; do not finalize the payment calculation until the missing rule is resolved.
```

**Sample output**

Representative results: 500, 500, 500, 540, missing-rule. The most frequent answer is 500; the acceptance decision is still pending, because the threshold base was not given.

**What did we get?**

Sampling and the acceptance check were separated. It became visible that a shared assumption error can be amplified by the majority.

## Where should you stop?

The share of the most frequent answer is not a calibrated confidence probability; a vote above 50 percent is not a general requirement of the original method either. The policy for ties and invalid responses belongs to your application. Multiagent Debate adds mutual feedback after the first independent responses.

## Sources

- [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/html/2203.11171) — Wang, Xuezhi; Wei, Jason; Schuurmans, Dale; Le, Quoc; Chi, Ed; Narang, Sharan; Chowdhery, Aakanksha; Zhou, Denny. 2022-03-21; version read 2023-03-07. Supports combining diverse sampled solutions through their final answers; presents findings that depend on model and task conditions. Evidence level: relevant body sections of the original paper.
