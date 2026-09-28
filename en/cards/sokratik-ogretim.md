# Socratic tutoring dialogue

Without giving the answer right away, help the learner find the next step.

## What is it?

Socratic tutoring aims to give questions and hints according to the learner's current understanding. In this card, the human does the work and the model is the guide. The model generating subquestions for itself is a separate method.

## When does it help?

When it matters more that the person can solve it on their own than that the solution arrives ready-made.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will find the first step in a simple equation.

**Prompt**

```text
I am the learner. Question: x + 3 = 8. Do not give the final answer.
First, with a single question, ask how I can remove the 3 while keeping the equality, and wait for my answer. If I say the right step, ask me to calculate the result. If it's wrong, give a smaller hint. At most three rounds; at the end, ask a new question with the same structure.
```

**Sample output**

Model: “Which number could you subtract from both sides to leave x on its own?” Human: “3.” Model: “When you do that, what does the right side become?”

**What did we get?**

The learner set up the operation without copying the final number.

### Medium

**Situation**

With a code bug, the model will get you thinking about the boundary case without stating the fix.

**Prompt**

```text
Rule: 500 TL and above ships free, below that 50 TL. Code: total > 500 ? 0 : 50.
Do not tell me the correct code or the operator to change right away. First ask which input would test the rule. After my answer, ask me to predict what that input returns in the current code.
At most three hints; if I get stuck, first explain the general concept of comparison, then return to the same example. You have no access to run real tests; keep predictions separate from tests.
```

**Sample output**

The human chooses 500 and notices that the code gives 50. Model: “Which group does the rule put this boundary value in?”

**What did we get?**

Instead of a direct patch, the checking habit that leads to the bug was practiced.

### Hard

**Situation**

The learner wants the answer; the level of help must be set explicitly.

**Prompt**

```text
Learning goal: Apply the idea that average speed is total distance/total time. Question: Traveling 60 km at 30 km/h, then the next 60 km at 60 km/h.
First ask for my attempt. If I say "Just tell me the answer", remind me that we are in learning mode and offer a single hint toward finding the times; do not question endlessly.
Order of help: concept question -> hint for the time of the first part -> a similar solved example with different numbers. Show the answer to the actual question only after I explicitly change the learning mode.
After at most three rounds, summarize where I got stuck and a new question to try independently.
```

**Sample output**

Model: “How many hours does the first 60 km part take?” After finding the times, the human sets up the totals. The help level and the mode change stay visible.

**What did we get?**

The guidance handled both making progress without leaking the answer and stopping when stuck.

## Where should you stop?

Just adding a question mark is not Socratic tutoring. Too many hints can give away the answer indirectly; too few can stall the learner. Pisan's automated behavior check is not a human learning experiment. The school mathematics findings of Bastani and colleagues are not a guarantee for every user or course either.

## Sources

- [Teaching a Large Language Model Tutor to Withhold the Answer: A Supervisor Architecture and an Evidence-Driven Method for Tuning Socratic Behavior](https://arxiv.org/html/2608.12292) — Pisan, Yusuf. 2026-08-12. Presents a tutor architecture that controls the level of help and answer-withholding behavior; its evaluation does not include human participants. Evidence level: relevant body sections of the original paper.
- [Generative AI without guardrails can harm learning: Evidence from high school mathematics](https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/) — Hamsa Bastani; Osbert Bastani; Alp Sungu; Haosen Ge; Özge Kabakcı; Rei Mariman. 2025 Jun 25. Examines AI help with and without hint-based safeguards in school mathematics, including performance after the help is removed; the source also has a correction record. Evidence level: relevant body sections of the original paper.
