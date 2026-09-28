# Step-Back

Before returning to the detailed question, find which general principle applies.

## What is it?

Step-Back takes one step away from the question and identifies the concept or general rule that is needed. The next answer combines that principle with the conditions of the original situation. The goal is not to forget the question but to make visible the relationship that gets lost among the details.

In the two-call adaptation here, the first output is a principle note. It is carried into the second call together with the original problem; no missing information is added to make the principle fit the situation.

## When does it help?

It can be used where a boundary condition, a ratio or a generalizable rule is decisive. Check that the general principle really holds under the conditions of your question.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You are examining the exact-threshold behavior in shipping code.

**Prompt**

```text
A human makes two calls.
1: “Does the phrase ‘at least 500’ include exactly 500? Write only the general comparison rule.”
2: Add this principle and the question: “For free shipping at 500 TL and above, is total > 500 correct? Give the correct expression and one boundary check.”
After the second call, a human evaluates the condition; the code does not count as having been run.
```

**Sample output**

Principle: “at least” includes equality. Application: `total >= 500`; free for total=500.

**What did we get?**

The linguistic threshold was connected to the code comparison. No conclusion came out about other pricing rules.

### Medium

**Situation**

The question asks for the average when the same distance is covered at two different speeds.

**Prompt**

```text
Call 1: “Write in one sentence the general definition of average speed on a journey and which totals are needed.”
Pass this response to Call 2: “I travel 60 km at 30 km/h and the next 60 km at 60 km/h. No breaks. Using the general definition, find the average speed with a short equation.”
The coordinator checks total distance and total time separately. Limit: two calls.
```

**Sample output**

Principle: total distance / total time. The times are 2 and 1 hours; 120/3=40 km/h.

**What did we get?**

Instead of the mistake of averaging the speeds directly, the time calculation became visible. The assumption under which the principle was applied is that there were no breaks.

### Hard

**Situation**

You are questioning whether the newest document should automatically count as valid for an announcement.

**Prompt**

```text
The coordinator makes two calls.
1: “Write, as a short checklist, the role of date, scope and approval status in whether a guideline applies. Do not invent a specific legal rule.”
2: Use the principle with these records: “A: 1 September, approved, in-store returns 30 days. B: 10 September, draft, in-store returns 60 days. Question: Which record should apply to an in-store purchase on 12 September?”
Do not treat the draft as approved. If there is no approval record from the source owner, stop before giving a definite application. The final answer should include the record code and the need to check.
```

**Sample output**

The scope matches; B's newer date does not remove its draft status. Among the given records, A applies: 30 days. A's current approval status should be confirmed with the document owner.

**What did we get?**

A general version check was applied to a concrete choice of record. This is not a real shop's return commitment.

## Where should you stop?

A wrong general principle can spoil even correct details. The problem framing card makes you choose which problem to solve; Step-Back looks for a suitable abstraction for the same question. The principle that emerges is not a new source or external verification.

## Sources

- [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://arxiv.org/html/2310.06117) — Zheng, Huaixiu Steven; Mishra, Swaroop; Chen, Xinyun; Cheng, Heng-Tze; Chi, Ed H.; Le, Quoc V; Zhou, Denny. 2023-10-09; version read 2024-03-12. Examines the approach of extracting an abstract concept/principle and returning to the original question; the task results with PaLM-2L, GPT-4 and Llama2-70B are not universal. Evidence level: relevant body sections of the original paper.
