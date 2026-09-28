# Meta Prompting: structural schema

Instead of solved content examples, give a schema that shows the structure of the task.

## What is it?

The Meta Prompting approach of Zhang and colleagues puts the form of the task and its transformations first. You write which kind of input turns into which kind of intermediate result, and from there into which output. The schema does not have to depend on the content of a particular solved example.

Here we adapt this approach with short task schemas. Preserving the formal structure in the paper is not a guarantee of semantic correctness or of improvement with every revision. The recursive setup in the version read also includes a proposer, a schema validator and an executor.

## When does it help?

Use it for tasks that process different inputs with a similar structure. You should be able to write out the input and output types, the permitted transformations and the check conditions.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will organize an arithmetic problem without showing an example solution.

**Prompt**

```text
Task schema:
Input → starting amount, added, removed, unit.
Transformation → start + added − removed.
Check → are the units the same, does the result make sense?
Output → short equation and result with unit.
Input: There were 18 books, 4 were added, 7 were taken. Apply the schema; I do not want a dump of hidden thinking.
```

**Sample output**

18+4−7=15 books; the amounts have the same unit.

**What did we get?**

The structure of the calculation was given without a content example. The numeric result can be checked separately.

### Medium

**Situation**

You will extract conditional process information from a text.

**Prompt**

```text
Schema: event → precondition → permitted result → missing information.
Rule: if it is not clear that the precondition has been met, do not write the result as if it had happened.
Input: “The application form was submitted. A place is confirmed only when the confirmation email arrives. The email has not arrived yet.”
Fill in the schema fields and give a one-sentence result. Do not add a duration that is not in the source.
```

**Sample output**

Event: form submitted. Precondition: confirmation email. Permitted result: application received, no confirmed registration yet. Missing information: when the confirmation will arrive.

**What did we get?**

The structure of the process was separated from a completed result. A filled-in schema field does not verify a source claim.

### Hard

**Situation**

The schema version will be changed automatically; not every proposal should be applied.

**Prompt**

```text
A simple recursive schema adaptation for a coordinator:
Starting schema: input, source, result. Task: summarize the notes “K1 capacity 16; K2 capacity unknown”.
Proposer call: propose a change that only adds an “uncertainty” field.
Software validator: only permitted fields can be added; the source field cannot be deleted. An invalid change is rejected.
The executor answers in a separate call with the approved schema and the original notes. A human checks that K2's gap is preserved.
One proposal and one execution; without a validator, do not apply the schema automatically. This outline does not rebuild the whole original MP-CR experiment.
```

**Sample output**

Acceptable schema: input, source, result, uncertainty. For K2, capacity is not specified. A “delete the source field” change should not pass the validator.

**What did we get?**

Revising the schema and solving the task became separate stages. A format validator does not count as having checked the meaning of the answer in place of a human.

## Where should you stop?

This use of “meta” is different from Meta-Prompting with expert calls. It is also not the same formalization as RUNE's layer names. Even when a schema looks logical, it can set up a wrong relationship; keep the check of going back to the original data.

## Sources

- [Meta Prompting for AI Systems](https://arxiv.org/html/2311.11482) — Zhang, Yifan; Yuan, Yang; Yao, Andrew Chi-Chih. 2023-11-20; version read 2026-08-03. Supports Meta Prompting, which separates task structure from content examples, and the recursive schema setup in the version read on 3 August 2026; the formalization is not a guarantee of correctness/convergence. Evidence level: relevant body sections of the original paper.
