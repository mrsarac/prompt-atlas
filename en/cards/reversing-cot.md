# Reversing Chain-of-Thought

Reconstruct backwards which question the solution assumes, and compare it with the actual question.

## What is it?

Reversing Chain-of-Thought reconstructs a problem from the generated solution; by comparing it with the original problem, it tries to find factual inconsistencies. The method, presented under the name RCOT, is not external source verification.

## When does it help?

When a number, relationship or condition in a solution may have been misread. Especially in calculations where a difference in the input goes unnoticed because the solution is fluent.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

The solution calculates correctly but uses the wrong number.

**Prompt**

```text
A human is the controller. Original question: There are 5 pens in each of 4 boxes; 3 pens were handed out. How many are left?
Candidate solution: "4×5=20; 20−2=18".
1. Give only the candidate solution to a separate call: Briefly reconstruct the question these operations assume. Do not show the actual question to this call.
2. Give the original question and the real reconstructed question to a comparison call; find the fact that changed.
3. Pass the original question and the difference found to a correction call. Stop after one correction; a short calculation is enough.
```

**Sample output**

The reconstructed question assumes that 2 pens were handed out. Difference: the original number is 3. Revision: “20 − 3 = 17.”

**What did we get?**

A wrong input in a solution with no calculation error came to light.

### Medium

**Situation**

The discount and shipping thresholds were applied in a different order.

**Prompt**

```text
Original question: 100 TL is deducted from a 600 TL basket; if the discounted amount is below 550, 40 TL shipping.
Candidate solution: "600≥550, no shipping; 600−100=500."
The controller should use three separate calls: reconstruct the assumed problem from the solution alone; compare this result with the original question; correct the solution with the difference found.
Store the real output of each stage with an ID. The reconstruction call should not invent unknown conditions; it should describe only the threshold application visible in the solution. Stop at 3 calls at most.
```

**Sample output**

“The solution applies the shipping threshold to the amount before the discount. The original condition is after the discount. Correction: 500 + 40 = 540 TL.”

**What did we get?**

The error was found not only in the result number but in the assumed rule.

### Hard

**Situation**

The problem reconstructed backwards may not be unique.

**Prompt**

```text
Original question: 23 people, at most 6 people per table; what is the minimum number of tables needed?
The candidate solution just says "4"; no calculation or constraint.
1. Give only this answer to the reverse-reconstruction call. Prompt: Can you uniquely derive the original problem from this answer? Do not produce numbers or relationships that are not proven.
2. The controller should carry the insufficient-information result, together with the original question, into a check call. Separately ask for the visible relationship needed to verify the answer: the capacity of 3 tables and the capacity of 4 tables.
Do not treat the failure of reverse reconstruction as evidence that the solution is correct. At most two calls; if there is no explicit check result, say uncertain.
```

**Sample output**

“The problem cannot be reconstructed from 4 alone. Separate check: 3×6=18 < 23; 4×6=24 ≥ 23, so 4 tables are needed.”

**What did we get?**

The limit where the method does not work when information is insufficient was clearly seen.

## Where should you stop?

The reconstructed question resembling the original is not enough to show that the solution is correct. The same model can keep the same mistake across two stages. The method brings no new independent evidence; it is not the same as tool-supported verification like CRITIC or a real calculation check.

## Sources

- [RCOT: Detecting and Rectifying Factual Inconsistency in Reasoning by Reversing Chain-of-Thought](https://arxiv.org/html/2305.11499) — Xue, Tianci; Wang, Ziqi; Wang, Zhenhailong; Han, Chi; Yu, Pengfei; Ji, Heng. 2023-05-19; version read 2023-10-02. Defines the RCOT arrangement that reconstructs the problem from the solution and compares factual consistency with the original problem; results on arithmetic datasets do not generalize to all verification work. Evidence level: relevant body sections of the original paper.
