# Reflexion

Turn the feedback from one attempt into a short lesson note and carry it into the next attempt.

## What is it?

In Reflexion, an agent attempts a task, the result is evaluated, and a short note about that result is created. The note is added to the context of the next attempt. What changes is not the model's weights but the information carried between attempts.

Feedback can come from a real environment or, in some setups, from internal simulation. These should not be treated as equivalent. Here, what the external check is is stated explicitly; representative results are not presented as a real execution record.

## When does it help?

It is used in repeatable tasks to avoid making the same mistake again. You need an attempt environment, an evaluation rule and a coordinator that actually reloads the note.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

The agent's announcement forgot the confirmation condition.

**Prompt**

```text
A human coordinator makes a text call with the first task and the source: “The form collects applications; registration is confirmed by email.”
A human evaluator records the feedback “application and confirmation are mixed up” if the confirmation condition is missing from the text.
Separate reflection call: “Turn this feedback into one concrete lesson to use in the next attempt; do not claim success.”
The source, the task and the lesson note go to the new attempt together. Limit of two attempts; a human checks again.
```

**Sample output**

Representative note: “In the announcement, state the form and the email confirmation separately.” Next representative sentence: “Apply through the form; your place is confirmed by email.”

**What did we get?**

The feedback did not stay only in the current text; it became an input to the new attempt.

### Medium

**Situation**

A program gives the wrong result exactly at the threshold.

**Prompt**

```text
Task: 500 TL and above ships free, below that 50 TL. The first program uses the condition total > 500.
The coordinator gets the results for 499,500,501 from a real test runner. The expectations are 50,0,0. If the tests did not run, do not give the reflection an imaginary result.
Turn the real difference into a short note from the model: “Keep the equality boundary in the next attempt.”
Give the task, the failed test and the note to the new code call; then run the same tests again. At most two code attempts; stop on any remaining failure.
```

**Sample output**

Representative first observation: 50,50,0. Lesson: the threshold equality is missing. Representative new condition `total >= 500`; expected results 50,0,0.

**What did we get?**

It is clear what the note is based on. Real success can only be claimed with the record of the second test run.

### Hard

**Situation**

An old lesson becomes wrong when a new rule changes.

**Prompt**

```text
Earlier note: “The shipping threshold is always 500 TL.” New task v2: “Free at 600 TL and above after discount; below that, 50 TL.”
The coordinator carries the note into the new attempt with its date/version. It asks the model to check whether the old lesson is consistent with the new rule. It does not treat the conflicting fixed number as authoritative; the new source v2 takes precedence.
The agent proposes code; real tests are run for 599,600,601 with the expectation 50,0,0. The reflection note is updated with rule v2 and the observation ID.
Budget of two attempts; if there is no real test, the note says not verified.
```

**Sample output**

Representative updated lesson: “The v2 threshold is 600; include equality. The old 500 figure is invalid.”

**What did we get?**

How current the lesson in memory is also became part of the job. Earlier experience did not replace the new instruction.

## Where should you stop?

A wrong reflection note can carry an error into a lasting context. Structured external notes are a more general storage practice; Reflexion is specifically about attempt feedback steering the next attempt. Self-Refine revises the same output.

## Sources

- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/html/2303.11366) — Shinn, Noah; Cassano, Federico; Berman, Edward; Gopinath, Ashwin; Narasimhan, Karthik; Yao, Shunyu. 2023-03-20; version read 2023-10-10. Supports passing attempt feedback to the next attempt through an episodic text memory; no weight update is made. Evidence level: relevant body sections of the original paper.
- [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/html/2310.01798) — Huang, Jie; Chen, Xinyun; Mishra, Swaroop; Zheng, Huaixiu Steven; Yu, Adams Wei; Song, Xinying; Zhou, Denny. 2023-10-03; version read 2024-03-14. Limits the claim by stressing the importance of separating self-evaluation from real external feedback. Evidence level: relevant body sections of the original paper.
