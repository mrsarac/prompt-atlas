# Skeleton-of-Thought

First produce a skeleton, then fill in the independent parts in separate calls.

## What is it?

Skeleton-of-Thought produces a short skeleton of the answer; then it expands each point in a separate call and combines the results. For the speed goal, the expansions run in parallel. Parts that need each other's results are not suited to this.

## When does it help?

In guides or explanations made of independent headings. It may not suit sequential calculations and interdependent decisions.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You want a beginner's guide to bicycle maintenance with three headings.

**Prompt**

```text
Controller: First, with a single model call, get only a three-point skeleton for this task: "Checking a bicycle before riding". Each point should be a short heading.
Real skeleton example: tyres, brakes, lights.
Start a separate expansion call for each point; give all of them the same task and the whole skeleton. Prompt: Explain only the heading assigned to you in two sentences; do not repeat the other headings. Do not count a physical inspection the model cannot do as having been done.
The controller should combine the three outputs in skeleton order; a human should check for repeats/gaps. 4 calls in total, then stop.
```

**Sample output**

“Tyres: Compare the pressure with the manufacturer's recommendation; check for visible damage. Brakes: Check the brake response in a safe area. Lights: Check that the lights work and are visible.”

**What did we get?**

Three independent explanations came together through a shared skeleton.

### Medium

**Situation**

In an event guide, shared information must stay consistent.

**Prompt**

```text
Task: Participant guide. Fixed brief: 12 October 14:00–16:00; 8 people; materials included; no venue yet.
Call 1 is skeleton only: time, preparation, unknowns. The controller should carry the approved brief and the skeleton unchanged into all expansion calls.
Each of the three parallel calls should write text of no more than 40 words for its assigned heading. It should not add a new address/fee.
Human check after merging: are the times the same, did the venue stay uncertain, did the materials information conflict? At most one regeneration for a faulty part; do not change the others. Stop at 5 calls at most.
```

**Sample output**

“Time: 12 October 14:00–16:00. Preparation: Materials are included. Unknowns: The venue has not been announced yet.”

**What did we get?**

The parallel parts were written with the same facts and limits.

### Hard

**Situation**

In a guide, some headings depend on each other's output.

**Prompt**

```text
Task: A 600 TL basket, a 100 TL discount; if the discounted amount is below 550, 40 TL shipping. Delivery record D1="Handed to the carrier within 2 working days after payment confirmation; no delivery date stated." A price calculation and ordering guide will be produced.
The controller should first ask the skeleton call for dependency markers: discounted amount -> shipping -> payment total; plus a separate, independent delivery information explanation.
The controller should carry the full task, D1 and the resulting skeleton into both expansion calls. Calculation call: “Calculate the discounted amount, shipping and total in order.” Delivery call: “Write two sentences from D1 only; separate handing to the carrier from delivery, do not add a date.”
Do not expand the three interdependent calculations in parallel among themselves; solve them in a single sequential calculation branch. This branch and the independent delivery call can run in parallel. A human should combine the results in skeleton order and check the amount and consistency with D1.
Stop at 3 calls in total: one skeleton, two expansions; the merging is done by a human. State that this mixed arrangement is not pure Skeleton-of-Thought. If a wrong dependency is found, do not continue for the sake of speed.
```

**Sample output**

Combined guide: “Payment: 600 − 100 = 500; shipping 40; total 540 TL. Delivery: Handed to the carrier within 2 working days after payment confirmation. No delivery date is stated.” The calculation branch's intermediate steps were done in order; the delivery branch did not wait for these intermediate results.

**What did we get?**

The dependency limit where the method does not fit was built into the application.

## Where should you stop?

Parallel call support requires a real application; having three headings written in the same chat is not the same mechanism. Total tokens or cost do not necessarily go down. Combining the final parts does not replace a consistency check.

## Sources

- [Skeleton-of-Thought: Prompting LLMs for Efficient Parallel Generation](https://arxiv.org/html/2307.15337) — Ning, Xuefei; Lin, Zinan; Zhou, Zixuan; Wang, Zifu; Yang, Huazhong; Wang, Yu. 2023-07-28; version read 2024-03-02. Defines the arrangement of skeleton generation, parallel expansion of points and merging; the work targets latency in particular, and is not a claim of universal cost reduction. Evidence level: relevant body sections of the original paper.
