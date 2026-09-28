# Multiagent Debate

Compare the answers of separate model calls, then run a bounded debate.

## What is it?

Multi-Agent Debate shows model answers generated in separate contexts to each other and runs revision and aggregation rounds. A “let three experts talk” role-play inside the same chat does not provide independent starting answers.

## When does it help?

For examining different candidate solutions to a problem and the reasons for disagreement; when the extra call cost and the possibility of an external check can be afforded.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will ask two separate model calls about a boundary condition.

**Prompt**

```text
Supervisor: A and B should receive the same question in separate contexts; they should not see each other's answers first. The same model can be used; this is not a guarantee of statistical independence.
Question: 500 and above ships free, below that 50 TL; what is the fee at 500?
Each call should give a short answer and a single rule-based reason. Then carry the real A/B answers, with their names, into two revision calls: examine the disagreement through the rule; do not change your answer just because the other agent said so.
After one debate round, the supervisor should report the result and the rule check. 4 calls in total; if there is no agreement, keep the uncertainty.
```

**Sample output**

Representative first answers A=0, B=50; the debate turns to the phrase “and above”. The final check should show that 500 is included.

**What did we get?**

Instead of two voices as roles, separate starting answers and a recorded revision were created.

### Medium

**Situation**

A majority can converge on a wrong calculation.

**Prompt**

```text
Question: A 100 TL discount on a 600 TL basket; if the discounted amount is below 550, 40 TL shipping.
The supervisor should run three separate first calls and one debate round; pass the real other answers to each agent. At most 6 model calls.
Representative first votes A=500, B=500, C=540. The agents should write a short calculation and the amount the threshold was applied to. The final aggregation should not count the majority as automatically correct; separately run a calculation check of the source rule in an isolated calculator.
If there is no tool, say no external verification was done. When the budget runs out, report the best-supported result or the remaining disagreement.
```

**Sample output**

“C's calculation adds the 40 shipping to the discounted amount of 500. Two starting votes being the same does not make 500 correct.”

**What did we get?**

The debate was tied to a checkable disagreement rather than the number of votes.

### Hard

**Situation**

Agents looking at different sources cannot resolve a conflict between the sources.

**Prompt**

```text
Task: Determine the capacity of a fictional hall. A's source D1="general capacity 20"; B's source D2="fire safety arrangement 16". The relationship of authority between the sources is not explained.
The supervisor should run the first calls separately, then give the real answers and quotes to both sides. Revision task: Which different condition/authority assumption could change the result? Do not produce a priority rule without a source.
Limit of two first + two revision + one aggregation call. The aggregator should write the difference in conditions and the human confirmation needed instead of a definite capacity. Do not extend the debate forever by adding new agents.
```

**Sample output**

“20 is the general capacity, 16 the fire safety record. Confirmation from the authoritative record is needed for the valid operational limit; an average such as 18 is meaningless.”

**What did we get?**

Conflicting evidence was not closed off with an artificial consensus.

## Where should you stop?

Multiple agents are not automatically superior to self-consistency. The debate findings in the source belong to specific task/model settings; gains may not appear in other studies. An external tool result or an authoritative source is different evidence from a group of models' vote.

The original source of the IMAD / debate-based post-training candidate was not verified for this selection; this name is not used as a synonym for the call-based debate described here.

## Sources

- [Improving Factuality and Reasoning in Language Models through Multiagent Debate](https://arxiv.org/html/2305.14325) — Du, Yilun; Li, Shuang; Torralba, Antonio; Tenenbaum, Joshua B.; Mordatch, Igor. 2023-05-23. Defines the multi-agent debate arrangement that revises and aggregates the answers of separate model instances through debate rounds. Evidence level: relevant body sections of the original paper.
- [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/html/2310.01798) — Huang, Jie; Chen, Xinyun; Mishra, Swaroop; Zheng, Huaixiu Steven; Yu, Adams Wei; Song, Xinying; Zhou, Denny. 2023-10-03; version read 2024-03-14. Includes a comparison in which, under the specific arithmetic conditions studied, multi-agent debate did not show superiority over self-consistency; no single conclusion is drawn for all debate systems. Evidence level: relevant body sections of the original paper.
