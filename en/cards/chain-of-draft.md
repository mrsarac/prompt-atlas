# Chain of Draft

Instead of narrating intermediate steps at length, limit them to short, checkable notes.

## What is it?

Chain of Draft proposes keeping intermediate reasoning text as short drafts. The original work includes an instruction to use very few words per step. The practical equivalent for the reader is to write variables, operations and checks briefly, and not to ask for a dump of hidden thinking.

## When does it help?

When long explanations overshadow the result in simple calculations or constraint checks. The depth of explanation needed is not the same for every job.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

Some of the notebooks in three boxes are handed out.

**Prompt**

```text
There are 8 notebooks in each of 3 boxes. 5 notebooks were handed out. How many notebooks are left?
Use a short draft format: only the necessary calculation lines and the final answer. Keep each intermediate note to at most 5 words. Do not narrate a hidden thought process; the visible operations should be checkable.
```

**Sample output**

“Total: 3 × 8 = 24. Remaining: 24 − 5 = 19. Answer: 19 notebooks.”

**What did we get?**

Instead of an explanation, enough of a trace remained to check the calculation.

### Medium

**Situation**

You will keep the order of discount and shipping with short notes.

**Prompt**

```text
The basket is 600 TL. First a 100 TL coupon is deducted. If the discounted amount is below 550 TL, shipping is 40 TL; otherwise 0 TL.
Show the necessary variables with short notes; each note at most 5 words. Make clear which amount you applied the shipping threshold to. At the end, write the amount to be paid.
```

**Sample output**

“Discounted: 600 − 100 = 500. Threshold: 500 < 550. Shipping: 40. Payment: 500 + 40 = 540 TL.”

**What did we get?**

Brevity did not erase the order of the operations.

### Hard

**Situation**

You will check whether a meeting plan meets its conditions.

**Prompt**

```text
Plan: A 09:00–09:20, B 09:20–09:35, C 09:35–09:45. Rules: A 20 minutes; B 15 minutes and after A; C 10 minutes; B must finish by 09:30 at the latest. There must be no overlap.
For each rule, give a short check note of at most 5 words and a pass/fail label. If a condition fails, do not summarize the plan as suitable. If the conditions contradict each other, state the gap clearly instead of lengthening the short draft.
```

**Sample output**

“A duration: pass. B duration/order: pass. C duration: pass. Overlap: none. B end time: fail, 09:35. Result: not suitable.”

**What did we get?**

The failure of one condition stayed visible even in a short format.

## Where should you stop?

A word limit can cut the details a hard problem needs. The specific model and task findings in the original paper do not guarantee cost or accuracy for every model. This method is the idea of shortening CoT's visible explanation; it does not mean you are checking the model's inaccessible internal computation.

## Sources

- [Chain of Draft: Thinking Faster by Writing Less](https://arxiv.org/html/2502.18600) — Xu, Silei; Xie, Wenhao; Zhao, Lingxiao; He, Pengcheng. 2025-02-25; version read 2025-03-03. Defines the approach of limiting visible reasoning text by using short intermediate drafts; the checks here are not a replication of the original experiment. Evidence level: relevant body sections of the original paper.
