# GEPA

Derive prompt changes from error traces; keep candidates that are strong on different examples together.

## What is it?

GEPA generates new candidates by reading the traces and feedback produced while running prompt candidates. Instead of looking only at a single average score, it can keep candidates that are strong on different examples with a Pareto approach; it tries to combine complementary lessons.

You need an optimization system that manages real execution, evaluation and the candidate history. Telling a model “evolve my prompt” does not run this setup. Here we use a small, teaching-oriented control outline.

## When does it help?

It is useful when the causes of errors can be recorded in a system containing one or a few prompts. You need data with known correct answers, and the traces must be cleaned of sensitive information.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

Different errors appear on two support examples.

**Prompt**

```text
Development: “The invoice is wrong”→billing; “I can't log in”→access.
The coordinator runs the current candidate in two calls; it stores the prompt, input, output and exact-match result as a trace.
Reflection call: “Propose a prompt change aimed only at the label/format error in this trace.”
Run the new candidate on the same two examples. Keep the success vector for each example; consider a candidate superior if it is worse than the old one on no example and better on one.
One change round; five calls. If there is no real trace, do not write a score.
```

**Sample output**

Representative old vector [1,0], new [1,1]. The new candidate is at least as good on both examples and better on one.

**What did we get?**

The error the change rests on and the selection rule can be seen. These two records are not a real performance experiment.

### Medium

**Situation**

Two candidates are good on different examples; their averages are the same.

**Prompt**

```text
Data: “The invoice is wrong”→billing; “I can't log in”→access; “Help”→unclear.
The coordinator evaluates A and B with real target calls. Representative vectors A=[1,1,0], B=[0,1,1]. Keep both; neither is superior to the other on every example.
Give the reflection the two prompts and the error traces: “Propose a candidate that keeps the unclear class without losing the billing distinction.”
Try one combined candidate on the three records; compare it only against real results. Candidate generation is one call; at most four calls in this round.
```

**Sample output**

Representative combined candidate: “If there is an explicit topic, billing/access; if there is no topic, unclear. Write a single label.” Its result vector is only known once it is run.

**What did we get?**

The reason for keeping complementary candidates is explicit. It was not assumed that the combination would be better than either.

### Hard

**Situation**

A prompt derived from traces can memorize the test example.

**Prompt**

```text
Development records: “The invoice is wrong”→billing; “I can't log in”→access; “Help”→unclear. Separate check: “My payment receipt was issued twice”→billing.
The coordinator runs at most two GEPA revision rounds. The reflection sees only the development traces; the check input and its label do not enter candidate generation.
For each change, keep the old/new success vector; keep complementary candidates. Freeze the selected prompt and apply the separate check once.
If individual development sentences have been added to the candidate, a human reviews the generalization risk. If the budget runs out, stop with the best observed candidate and the unresolved error.
```

**Sample output**

Representative risky rule: “Say unclear for the word help.” More general candidate: “If there is no explicit topic, unclear.” The result of the separate check is reported as a new observation.

**What did we get?**

The candidate's measurement record and the independence of the final check are preserved. Having written a general rule is not, on its own, evidence of generalization.

## Where should you stop?

A Pareto set does not promise a single absolute winner. A wrong evaluation or a missing trace can produce a wrong revision. Keep the task/model limits of the original GEPA findings; do not carry the same percentage gain over to your own examples.

## Sources

- [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://arxiv.org/html/2507.19457) — Agrawal, Lakshya A; Tan, Shangyin; Soylu, Dilara; Ziems, Noah; Khare, Rishi; Opsahl-Ong, Krista; Singhvi, Arnav; Shandilya, Herumb; Ryan, Michael J; Jiang, Meng; Potts, Christopher; Sen, Koushik; Dimakis, Alexandros G.; Stoica, Ion; Klein, Dan; Zaharia, Matei; Khattab, Omar. 2025-07-25; version read 2026-02-14. Supports reflection on execution traces, candidate updates and Pareto-based selection/combination; results on six selected tasks are not universal superiority. Evidence level: relevant body sections of the original paper.
