# CRITIC

Tie the critique to an external tool result, then correct the answer.

## What is it?

CRITIC has the first answer checked with tools and corrects it based on the feedback that comes back. The tool can be a search, code execution or another external check suited to the task. Merely saying “critique yourself” does not cover the tool-supported part of the method.

## When does it help?

In calculation, code or sourced information work where you can check an answer's correctness externally.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

The first answer contains an addition error.

**Prompt**

```text
A human is the controller. Question: 3 pens were taken from 4 boxes of 5 pens each; how many are left? First candidate answer: 18.
Check call: Write the single expression to give to the calculator to verify the answer; do not guess the tool result and present it as real.
The application should run calculator("4*5-3") and add the real return to the check call.
The correction call should receive the question, the first answer and the real tool result; it should briefly write the wrong part and the corrected answer. Stop after one tool check and one revision.
```

**Sample output**

Representative tool result 17; revision: “18 was wrong. 4 × 5 − 3 = 17 pens.”

**What did we get?**

The correction was tied to a calculation check, not to the model's second guess.

### Medium

**Situation**

A sourced answer gives the wrong day.

**Prompt**

```text
Question: Is the fictional City Museum open on Monday? First candidate: "Yes, it's open every day."
The supervisor should allow only the tool that reads the official hours record; at most 2 reads. Representative return D1: "Closed on Mondays; Tuesday–Sunday 10:00–18:00", updated 1 September 2026.
The critique call should compare the first claim with D1 and write which part conflicts. The revision call should take this critique and D1 and correct the answer.
If the tool fails, do not say "checked"; say it could not be verified and stop. With a valid result, one revision is enough.
```

**Sample output**

“The statement that it is open every day conflicts with D1. According to the record dated 1 September, it is closed on Mondays.”

**What did we get?**

The source check became the concrete basis of the critique.

### Hard

**Situation**

It will be checked whether a code fix produces a new boundary error.

**Prompt**

```text
Task: 500 and above ships free, below that 50 TL. First code total > 500 ? 0 : 50.
The supervisor should provide only an isolated test tool; no writing to external files. Test inputs 499,500,501; expected 50,0,0. Store the real test returns.
The critique call should briefly write the failing input and its cause. The revision call should produce the smallest code change. The same tests should actually run again on the new candidate.
At most 2 test rounds/1 revision. If the second round fails, report the remaining error instead of a new success claim. If there are no tests, only make a proposal.
```

**Sample output**

Representative first result 50,50,0; after the `>=` revision, expected 50,0,0. These are not model/tool records run for this card.

**What did we get?**

Whether the fix worked was also tied to a separate tool check.

## Where should you stop?

The tool itself, the choice of source or the test coverage can be wrong. CRITIC differs from Self-Refine in its use of external feedback. Chain-of-Verification sets up verification questions; CRITIC highlights the tool-supported critique and revision loop.

## Sources

- [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/html/2305.11738) — Gou, Zhibin; Shao, Zhihong; Gong, Yeyun; Shen, Yelong; Yang, Yujiu; Duan, Nan; Chen, Weizhu. 2023-05-19; version read 2024-02-21. Defines critiquing and correcting the first model output with feedback from tool interactions; it is not equated with tool-free self-critique. Evidence level: relevant body sections of the original paper.
