# Problem framing

Before choosing a solution, clarify which problem you are solving.

## What is it?

Problem framing separates the symptom, the goal, the constraints and the success criterion. The model can propose alternative frames, but it does not decide on its own which problem is worth solving. Here it is used as a practical thinking arrangement.

## When does it help?

When you have chosen a tool or a feature, but it is unclear which user need it will meet.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will start from the idea “Let's build a chatbot”.

**Prompt**

```text
My idea: Let's add a chatbot to my site. Observation: People can't find the opening hours. Constraint: A small site, 1 hour a week for maintenance.
Separate the solution idea, the observed problem and the unknown. Define success not as the tool being installed but as the reader being able to find the opening-hours information. Ask one clarifying question; do not start designing a new product.
```

**Sample output**

“Solution candidate: chatbot. Problem: access to the opening-hours information. Unknown: on which page are people looking? Success: completing the task of finding the opening hours.”

**What did we get?**

The tool's name did not take the place of the problem definition.

### Medium

**Situation**

The same symptom can point to two different problems.

**Prompt**

```text
Observation: Three of five new users did not save their first note. There are no interviews or screen recordings. Proposed solution: A bigger save button.
Write at most three problem frames: not finding the button, not understanding how saving works, not wanting to enter a note. For each, propose one distinguishing observation. Do not write them as confirmed causes.
At the end, propose the smallest information-gathering step; do not carry out user research or send messages.
```

**Sample output**

“If they notice the save button but can't be sure of the result, the problem may be feedback rather than visibility. A short task observation could reveal this distinction.”

**What did we get?**

It became clear that the same solution does not fit every explanation.

### Hard

**Situation**

When goals conflict, you must not start optimizing too early.

**Prompt**

```text
Team goals: Reduce support time; maintain answer accuracy. Data: 20 sample requests; the average handling time is known but there is no accuracy measurement. Constraint: Customer data cannot be exported.
Write a problem brief: decision, goals, what can be measured, what cannot be measured yet, hard constraints. Do not make time the only success criterion. Leave as an open question who will define an accuracy criterion.
Propose two alternative frames: help with preparing drafts; fully automatic answering. Do not assume the second is feasible with the current permissions or data.
```

**Sample output**

“First, the effect of draft support on time and on human-approved accuracy can be evaluated. Fully automatic answering needs a separate accuracy and permissions decision.”

**What did we get?**

Optimization was not tied to a notion of success that has not been defined yet.

## Where should you stop?

Question Refinement improves the sentence of the question; problem framing questions what the decision and the success criterion are. Research on clarification before optimization is a neighbor of this approach; it cannot be said to determine automatically which human problem is worth solving.

## Sources

- [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT](https://arxiv.org/html/2302.11382) — White, Jules; Fu, Quchen; Hays, Sam; Sandborn, Michael; Olea, Carlos; Gilbert, Henry; Elnashar, Ashraf; Spencer-Smith, Jesse; Schmidt, Douglas C.. 2023-02-21. Provides a source for interactive questioning and alternative-generation patterns; not experimental evidence of the effectiveness of the broad problem framing approach. Evidence level: relevant body sections of the original paper.
- [Ask Before You Optimize: Dynamic Pre-Formulation Clarification for Interactive Optimization](https://arxiv.org/html/2609.05258) — Ge, Sihan; Lin, Yichen; Zhou, Chenyu; Lin, Jianghao; Yao, Tao; Ge, Dongdong. 2026-09-04; version read 2026-09-08. Examines clarifying goals/constraints before optimization formulation with a simulated user; does not represent the whole problem-selection process of real people. Evidence level: relevant body sections of the original paper.
