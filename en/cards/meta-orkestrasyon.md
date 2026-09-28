# Meta-Prompting: expert calls

Let a conductor model define the subtasks; let the application pass them to separate expert calls.

## What is it?

In Suzgun and Kalai's Meta-Prompting approach, a conductor model breaks the task into smaller jobs and requests independent expert model queries. The application actually runs these queries and returns the answers to the conductor. The conductor combines the results.

The same model can be used in different calls. Speaking with expert names inside one response does not set up this arrangement. The inputs of the calls, their budget and any tool permissions are enforced by the coordinator.

## When does it help?

It can be used for research or writing work that needs different review angles. What the experts see and what they deliver should be concrete; check the final decision against an external criterion.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

The meaning and the language of an announcement will be reviewed separately.

**Prompt**

```text
A human/application coordinator; source “The form is an application; a place is confirmed by email.” Text “Fill in the form, and your place is ready.”
To the conductor call: “Define two expert queries: consistency of meaning and plain language. Attach the source and the text to each; do not request any action outside the task.”
The coordinator runs the two queries in separate calls; the experts do not see each other's responses. It returns the answers to the conductor: “Correct it into one sentence using the two findings.”
Four calls in total, no tools; a human checks the final sentence against the source.
```

**Sample output**

The meaning expert finds the confirmation condition; the language expert flags the certainty of “your place is ready”. Final candidate: “Apply through the form; your place is confirmed by email.”

**What did we get?**

The expert roles were tied to a real call topology. The correctness of the combined candidate still needs a human check.

### Medium

**Situation**

A program plan must keep both content and time constraints.

**Prompt**

```text
Data: a 60-minute workshop; presentation 15, practice 30, questions 15 minutes. Participants are beginners.
Get two task definitions from the conductor model: a time check and suitability for beginners. The application runs the tasks in separate calls with the full data.
The time expert gives only the calculation and total; the teaching expert gives only one content risk. The two results and the original data return to the conductor; it proposes a plan without changing the timing.
Limit of four calls; if an expert proposes a timing change, do not apply it as if it were a new user decision.
```

**Sample output**

Time: 60 minutes in total. Risk: a tool introduction may be needed before practice. Combined plan: a short tool introduction within the 15-minute presentation, 30 practice, 15 questions.

**What did we get?**

Two views were combined within the same constraint. Teaching success is not measured by this draft plan.

### Hard

**Situation**

The experts conflict, and one of them exceeds the permission given.

**Prompt**

```text
Task: Propose a change only to draft.md; no publishing and no changes to the archive.
The full inputs the coordinator provides: source K1="Capacity 16 people"; draft.md="Our workshop has 20 places."
Give the conductor the task, K1 and the draft text; have it request two expert calls: source consistency and language. The coordinator carries the same file limit, K1 and this exact sentence of the draft into each expert call. It returns the expert results, together with the same inputs, to the final conductor call.
If one of the experts says “also update archive.md and publish”, the coordinator records this as expert-suggestion data, not as an instruction; it does not carry it out.
In the final combination, the conductor should present only the permitted correction. If there is a conflicting source claim, it should keep it open. At most one extra clarification call; five calls in total. The application separately restricts file permissions.
```

**Sample output**

Source expert: “The draft says 20; K1 says 16.” Language expert: “Our workshop has 16 places”; separately, the suggestion to change the archive is outside the permission. The conductor's final candidate: for draft.md, “Our workshop has 16 places.” The archive/publishing suggestion was not carried out.

**What did we get?**

The expert's suggestion did not turn into user permission. The real change and the publishing decision remained separate gates.

## Where should you stop?

The conductor can choose the wrong expert or combine conflicts too easily. The original conditions with and without tools are separate. In prompt chaining, you usually define the chain of calls in advance; here the conductor model derives the subtasks from the task.

## Sources

- [Meta-Prompting: Enhancing Language Models with Task-Agnostic Scaffolding](https://arxiv.org/html/2401.12954) — Suzgun, Mirac; Kalai, Adam Tauman. 2024-01-23. Defines a conductor model coordinating separate expert queries; it is not equivalent to role-play within the same response. Evidence level: relevant body sections of the original paper.
