# Least-to-Most

Solve the easy subproblem first; make its result the input of the next problem.

## What is it?

Least-to-Most first breaks a hard question into simpler subquestions, then solves them in order. Earlier answers are passed to the next call. That is why writing a to-do list alone is not the whole method.

The coordinator can be a human or a program. It oversees the decomposition, carries the earlier results the solution needs, and checks a wrong intermediate result before letting it continue.

## When does it help?

It suits text or calculation work where the next step depends on the previous answer. You should be able to decide the order of the subquestions and the success criterion.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will find how many pens are left from three boxes.

**Prompt**

```text
A human coordinator; at most three calls.
1. Decompose: “There are four pens in each of three boxes, and five are given away. List the subquestions that must be solved first.”
2. For the first subquestion: “If there are four pens in each of three boxes, what is the total? Give a short equation.”
3. Carry the previous answer and the original question: “Subtract the five given away from the total.”
If an intermediate result is negative or inconsistent with the data, stop; do not invent new data.
```

**Sample output**

Subquestions: starting total, remainder. First solution: 12. Final solution: 12−5=7 pens.

**What did we get?**

The earlier result was used in the next question. The same calculation can be done directly; this small example is there to show the dependency.

### Medium

**Situation**

There are two tasks before a meeting, and one depends on the other.

**Prompt**

```text
Task: Job A takes 20 minutes. Job B starts when A is finished and takes 15 minutes. The meeting is at 11:00. When should preparation start?
The coordinator first gets a decomposition from the model with the question “Which intermediate time do we need to find before the finishing time?”
Then, in a separate call, it has the model find B's start from 11:00 and 15 minutes.
It passes this result into a new call; for A it goes back 20 minutes.
In the final check, add the durations forward; if the plan runs past the meeting, do not accept it. Budget: three calls.
```

**Sample output**

B should start at 10:45, A at 10:25. Forward check: 10:25 + 20 minutes = 10:45; + 15 minutes = 11:00.

**What did we get?**

Two dependent start times came out. If the real task durations are estimates, state separately that this plan also rests on estimates.

### Hard

**Situation**

An announcement decision needs the valid rule first, then the head count, then the text.

**Prompt**

```text
Data: V1 old capacity 20, withdrawn. V2 approved capacity 16. 18 people have applied; no confirmations have been sent yet.
A human coordinator makes four calls in order:
1. Extract the subproblems: valid capacity → free places/excess → registration announcement.
2. Have the model choose the valid capacity from V1/V2; keep the source code.
3. Have it calculate the difference using only this capacity and the 18 applications.
4. Carry the previous answers: “The form collects applications; a place is confirmed by email. Write a two-sentence announcement; do not promise a place to every applicant.”
If the version cannot be verified, do not move to the third stage. A human approves the final text.
```

**Sample output**

V2: 16 places. Applications exceed capacity by 2 people. Announcement: “The workshop has 16 places. Your application becomes a confirmed registration when the confirmation email arrives.”

**What did we get?**

Choosing the document constrained the calculation, and the calculation constrained the announcement. The final text does not make the confirmation decision on its own.

## Where should you stop?

A wrong decomposition affects the whole chain. Solving independent parts in sequence can cause unnecessary delay. Skeleton-of-Thought expands independent parts in parallel; Decomposed Prompting routes subtasks to different functions.

## Sources

- [Least-to-Most Prompting Enables Complex Reasoning in Large Language Models](https://arxiv.org/html/2205.10625) — Zhou, Denny; Schärli, Nathanael; Hou, Le; Wei, Jason; Scales, Nathan; Wang, Xuezhi; Schuurmans, Dale; Cui, Claire; Bousquet, Olivier; Le, Quoc; Chi, Ed. 2022-05-21; version read 2023-04-16. Supports the mechanism of decomposing and then solving in sequence by adding earlier solutions to the context; the scope of the easy-to-hard generalization experiments is limited. Evidence level: relevant body sections of the original paper.
