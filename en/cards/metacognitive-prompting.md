# Metacognitive Prompting

Make understanding the task, the first solution and the final check separate, visible steps.

## What is it?

Metacognitive Prompting organizes the model's stages of interpreting the task, first judgment, evaluation and final answer. The “metacognition” here is not a claim that the model has conscious self-awareness; it is the name of a prompt structure.

## When does it help?

When you want to see whether a task was misread, a condition was skipped, or the confidence level matches the support in an answer.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will check whether it reads a short rule correctly.

**Prompt**

```text
Rule: 500 TL and above ships free, below that 50 TL. Question: What is the shipping for a 500 TL basket?
Answer with four short fields: understanding the task; first answer; check against the rule; final answer and the limit of its support. Each field should be one sentence. I do not want a dump of hidden thinking or claims of consciousness.
```

**Sample output**

“Task: evaluate the threshold value. First answer: 0 TL. Check: ‘and above’ includes 500. Final answer: 0 TL under the given rule.”

**What did we get?**

Which interpretation and check the answer rests on became visible.

### Medium

**Situation**

There is an alternative to the model's first interpretation.

**Prompt**

```text
Data: Three out of five people did not use the save button. No interviews. Question: Is it because the button is small?
First summarize the task and the available evidence. Do not set up your first judgment as a definite cause. Then propose an alternative that could explain the same observation and a check that would tell the two apart. In the final answer, separate what you know from what you are guessing; do not invent a percentage confidence.
```

**Sample output**

“A small button is one possibility; it is also possible that they did not feel a need to save. The cause cannot be determined without a task observation.”

**What did we get?**

The first explanation did not become more certain than the evidence supports.

### Hard

**Situation**

Self-evaluation must not cover over a lack of external evidence.

**Prompt**

```text
Task: Say whether a fictional service is working today. The only record given: "It was working yesterday at 18:00." There is no live status tool.
Stages: understand the time the question refers to; make a first assessment from the available data; check the time gap and the missing tool; revise the final answer. Each stage should be a short, observable check.
Do not treat today as verified by giving a self-confidence score. The final answer should include what is missing and which real check is needed; do not act as if a new tool exists.
```

**Sample output**

“Yesterday's record does not confirm today's status. A live status record or a current check is needed.”

**What did we get?**

More careful self-evaluation did not create a nonexistent observation.

## Where should you stop?

This method does not make the same claim as metacognition research that measures human learning. Self-Refine critiques and renews a draft of the product; here, the stages of understanding the task and evaluating the judgment come to the fore. Self-evaluation does not replace external verification.

## Sources

- [Metacognitive Prompting Improves Understanding in Large Language Models](https://arxiv.org/html/2308.05342) — Wang, Yuqing; Zhao, Yun. 2023-08-10; version read 2024-03-20. Defines the Metacognitive Prompting approach, which organizes the model's response into stages of task understanding, judgment and evaluation. Evidence level: relevant body sections of the original paper.
- [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/html/2310.01798) — Huang, Jie; Chen, Xinyun; Mishra, Swaroop; Zheng, Huaixiu Steven; Yu, Adams Wei; Song, Xinying; Zhou, Denny. 2023-10-03; version read 2024-03-14. Shows cases where internal feedback does not provide correct fixes; limits any claim of universal superiority for this card. Evidence level: relevant body sections of the original paper.
