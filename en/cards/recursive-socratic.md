# Recursive Socratic Questioning

Split a subquestion again when needed; combine the answers upwards.

## What is it?

Recursive Socratic Questioning is an algorithm in which the model splits the main problem into subquestions and, when needed, applies the same operation to the subquestions too. A controller combines the solved sub-answers. It is not the same as the method of teaching a human student through questions.

## When does it help?

In tasks with traceable dependencies, where a subquestion itself also needs to be broken down.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will solve a numerical question made of two parts.

**Prompt**

```text
The controller should keep a question tree. Main question: Each of 3 boxes holds 8 notebooks, and 5 of the total were handed out; how many are left? Maximum depth 2 and 4 model calls in total.
The root call should identify the necessary subquestions: total notebooks; remaining after handing out.
After the first subquestion is solved, pass the real answer 24 to the second. Each node should give only a short calculation and answer; do not split solvable leaves again.
The combining call should check the result from the main question and the sub-answers. If the budget runs out, name the missing node; do not invent a result.
```

**Sample output**

Leaf: “3×8=24”. Upper combination: “24−5=19”. The result is 19 notebooks.

**What did we get?**

Where the sub-answers were carried stayed clear.

### Medium

**Situation**

A subquestion of the shipping question also needs two operations.

**Prompt**

```text
Main question: 3 products at 80 TL each, a 25% discount on the product total, shipping 20 TL; what is the payment?
Controller: depth at most 3, 6 calls in total. The model should split the root into "discounted product total" and "total with shipping". The first subquestion should be split again, if needed, into raw total and discount.
The leaf outputs should be stored with their IDs: raw total 240; discounted 180; payment 200. These are representative expected values; the real call outputs should be recorded separately.
The combination should keep the unit of each number. If a node is solved, do not ask the same input again; stop after the root check.
```

**Sample output**

Tree: 3×80 → 240; 240×0.75 → 180; 180+20 → 200 TL.

**What did we get?**

The subproblem was also split as much as needed; all branches were tied to a single root answer.

### Hard

**Situation**

If a leaf has no data, recursion cannot create it.

**Prompt**

```text
Main question: What is the total cost of the workshop in TL? Known: 8 people, materials 30 TL per person. The hall fee is not stated.
The controller should set a limit of depth 3 and 5 calls in total; each node should return one of the statuses solved/missing_data/failed.
The model should separate the materials and hall subquestions. Materials can be solved as 8×30. If there is no hall data, it should not produce a number by inventing a new subquestion; it should carry the missing_data status up to the parent node.
The combination should write only the conditional result "240 TL + hall fee". Stop on missing data or at the budget limit; do not give a definite total.
```

**Sample output**

“Materials 240 TL. Since the hall fee is unknown, the total cost cannot be finalized.”

**What did we get?**

More subquestions did not turn a missing fact into a fake answer.

## Where should you stop?

This method needs a real call tree, state records and a stop limit. In Socratic tutoring the learner is a human; here the model's problem-solving flow is organized. The visible short sub-answers are a simple adaptation of the original method; no effect on human learning can be inferred.

## Sources

- [The Art of SOCRATIC QUESTIONING: Recursive Thinking with Large Language Models](https://arxiv.org/html/2305.14999) — Qi, Jingyuan; Xu, Zhiyang; Shen, Ying; Liu, Minqian; Jin, Di; Wang, Qifan; Huang, Lifu. 2023-05-24; version read 2023-11-02. Defines a divide-and-conquer algorithm that recursively generates subquestions and combines their answers; not a human tutoring conversation or a learning experiment. Evidence level: relevant body sections of the original paper.
