# Mutual argument questioning

Question each other's assumptions in turn; keep the final decision open.

## What is it?

Mutual questioning is the human and the model putting short questions to each other's claims. Here it is used not as a single canonical academic prompt name, but as a conversation arrangement with explicit rules. The model's questions do not replace the human's decision.

## When does it help?

When you want to see the assumptions an idea rests on and test a view without rushing to a conclusion.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You think your newsletter is too long.

**Prompt**

```text
My claim: Nobody reads the newsletter because it's too long.
Let's question each other in turn. First ask a single question that opens up an assumption of this claim; wait for my answer. Then I will ask a question about your interpretation. At most two back-and-forth rounds. If there is no data, do not draw a cause-and-effect conclusion.
```

**Sample output**

Model: “From what observation do we know it isn't being read?” Human: “Only two people said to make it shorter.” Human: “Is that enough for all readers?” Model: “No; it's limited to feedback from two people.”

**What did we get?**

The limited observation a strong generalization rests on came to light.

### Medium

**Situation**

Why a feature request matters will be discussed.

**Prompt**

```text
My claim: We should add tags to the notes app. Observation: Three people said they couldn't find an old note.
You first question the link between the solution and the problem. Once I answer, write your provisional interpretation and leave one open point for me to question. In each round, keep the distinction between claim, support and uncertainty.
At most three rounds; at the end, do not act as if the decision to add tags has been made. Write which new observation would change the choice.
```

**Sample output**

Model: “Is not finding a note a classification problem or a search problem?” Human: “We don't know yet.” Final record: “Tags are a candidate solution; the search behavior for lost notes should be examined.”

**What did we get?**

The discussion shifted from defending the first solution to finding the missing information.

### Hard

**Situation**

Two values conflict; there is no single right answer.

**Prompt**

```text
Decision: Should the team meeting be recorded? The goal is later access; the concern is participant privacy. Nobody has given permission for recording.
Let's question each other: first ask a question about a value/assumption; after my answer, briefly write your strongest objection. Then I'll ask about the assumption in your objection.
Do not score personal values as if they were objective facts. After three rounds, write the options, the unresolved difference in values and the human decision needed. Do not start a real recording or assume permission.
```

**Sample output**

“The need for access and the concern about being recorded remained distinct. A written summary is an option; a participant decision is still needed for recording.”

**What did we get?**

Without hiding the disagreement, the conversation went back to the owner of the decision.

## Where should you stop?

This arrangement is not the model-internal recursive algorithm of Recursive Socratic Questioning. Flipped Interaction collects information; here, both sides' claims are questioned. It is not claimed that mutual conversation alone produces better human decisions.

## Sources

- [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT](https://arxiv.org/html/2302.11382) — White, Jules; Fu, Quchen; Hays, Sam; Sandborn, Michael; Olea, Carlos; Gilbert, Henry; Elnashar, Ashraf; Spencer-Smith, Jesse; Schmidt, Douglas C.. 2023-02-21. A neighboring primary source for question-focused interaction patterns; does not support a claim that the mutual arrangement described here has a separate experimental protocol or name. Evidence level: relevant body sections of the original paper.
- [The Art of SOCRATIC QUESTIONING: Recursive Thinking with Large Language Models](https://arxiv.org/html/2305.14999) — Qi, Jingyuan; Xu, Zhiyang; Shen, Ying; Liu, Minqian; Jin, Di; Wang, Qifan; Huang, Lifu. 2023-05-24; version read 2023-11-02. Defines a recursive model algorithm; a boundary source so it is not confused with human–model mutual questioning. Evidence level: relevant body sections of the original paper.
