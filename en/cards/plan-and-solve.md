# Plan-and-Solve

First set up the solution plan, then carry out the steps of that same plan.

## What is it?

Plan-and-Solve proposes first identifying the necessary steps instead of solving the problem directly, and then carrying out the plan. The PS+ version includes additional guidance for variables and calculation details. Short, checkable operations are enough in the visible plan.

## When does it help?

In small planning and calculation jobs where skipped steps or a wrong order of operations affect the result.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will calculate the number of pens in boxes.

**Prompt**

```text
There are 6 pens in each of 4 boxes; 7 pens are handed out. How many pens are left?
First write a two-point solution plan. Then carry out the plan with short calculation lines and give a single result. I do not want a dump of hidden thinking; only the plan and a checkable calculation.
```

**Sample output**

Plan: “Find the total; subtract what was handed out.” Execution: “4 × 6 = 24; 24 − 7 = 17. Result: 17 pens.”

**What did we get?**

The order of operations became visible before the result.

### Medium

**Situation**

The order of discount and shipping can be misread.

**Prompt**

```text
The basket is 625 TL. A 20% discount is applied first. If the amount after discount is 500 TL or more, shipping is free; below that, 50 TL.
With the PS+ approach, first list the variables and numbers, then write the plan, then carry it out. Keep the currency; check that the threshold is inclusive. The final answer should be one sentence.
```

**Sample output**

“Plan: apply the discount, compare the discounted amount with the threshold, add shipping. 625 × 0.8 = 500; 500 ≥ 500; shipping 0. The amount to pay is 500 TL.”

**What did we get?**

A plan was created that checks the equality case at the boundary.

### Hard

**Situation**

If a work schedule does not meet its constraints, the plan must be revised.

**Prompt**

```text
We start at 09:00. A takes 30 minutes; B takes 20 minutes and must finish by 09:30 at the latest; C takes 10 minutes and comes after A. The tasks are done by one person, without overlap.
First extract the constraints and plan an order. Then calculate the start/end times. The final check should test each rule against the plan. If the plan breaks a rule, make one revision; if it is still not suitable, say it could not be solved. Do not narrate internal thinking; a visible plan and a check table are enough.
```

**Sample output**

“B 09:00–09:20; A 09:20–09:50; C 09:50–10:00. B's end-time condition is met; C comes after A; no overlap.”

**What did we get?**

The plan was not just listed; it was carried out and compared with the constraints.

## Where should you stop?

Writing a plan does not guarantee that the plan is correct. Least-to-Most focuses on solving subquestions and carrying their results forward; Plan-and-Solve first lays out a path for the whole solution. Here, a short plan and check are used instead of the original prompts' request for long thinking; it is not an exact replication of the experiment.

## Sources

- [Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](https://arxiv.org/html/2305.04091) — Wang, Lei; Xu, Wanyu; Lan, Yihuai; Hu, Zhiqiang; Lan, Yunshi; Lee, Roy Ka-Wei; Lim, Ee-Peng. 2023-05-06; version read 2023-05-26. Explains planning first, then solving, and the additional PS+ instructions; it does not follow that the same effect will appear with every model. Evidence level: relevant body sections of the original paper.
