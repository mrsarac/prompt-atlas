# EmotionPrompt

Emotional emphasis is an instruction variable; it does not give the model emotions.

## What is it?

EmotionPrompt studies adding emotional phrases to a prompt that stress the importance of the task or the user's expectations. It does not mean the model actually becomes anxious, motivated or experiences human emotion.

## When does it help?

When designing a small, controlled comparison to examine the emphasis style of an instruction. In everyday use, concrete quality criteria are easier to check.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will write an emphasized version of a summary request.

**Prompt**

```text
This summary is important to me. Please be careful.
Text: The workshop is on 12 October between 14:00 and 16:00. There are 8 places. Fee information has not been announced.
Summarize in two sentences; keep the date, duration and capacity. Do not add the unknown fee.
```

**Sample output**

“The workshop will take place on 12 October between 14:00 and 16:00, with 8 places. Fee information has not been announced yet.”

**What did we get?**

We got an example of a prompt with emotional emphasis; it was not shown that this output is better than one from the prompt without emphasis.

### Medium

**Situation**

You want to really isolate the effect of adding emphasis.

**Prompt**

```text
A human should make two controlled, separate calls, using the same model/settings and the same text. Do not share the other call's answer.
Shared task: "Announcement: Workshop 12 October, 14:00, 8 people. Summarize in one sentence; do not add details."
A: The shared task only. B: The task with "This work is important to me; answer carefully" added in front.
Evaluate the two real responses with their identities hidden: were the three pieces of information kept, is there new information? Do not infer general superiority from a single example. Stop after the two calls and the evaluation.
```

**Sample output**

Representative evaluation format: “Response X: all three fields present, no extra claims. Response Y: all three fields present, no extra claims.” This is not the result of a comparison that was actually carried out.

**What did we get?**

The single variable expected to make a difference was isolated.

### Hard

**Situation**

Emotional pressure can encourage hiding uncertainty.

**Prompt**

```text
The task is important to me; so, before appearing certain, state the uncertainty correctly.
Decision: Will the outdoor event go ahead on Saturday? Data: No backup hall, capacity 20, no weather forecast given.
Write what is known, the missing decision data and two conditional options. Do not treat the statement of emotional importance as a reason to invent the weather or make a definite decision. The output should be at most 120 words.
```

**Sample output**

“There is no weather forecast; the risk of rain cannot be assessed. If a suitable forecast and safe conditions are confirmed, the outdoor plan goes ahead; in adverse conditions, a postponement option is needed.”

**What did we get?**

The importance of the task was tied to a criterion of care rather than pressure for certainty.

## Where should you stop?

“My career depends on this”, or reward/punishment language, is not always helpful; it can produce unnecessary pressure and overconfidence. The original work's findings on specific models do not count as valid for all current models. Emotional emphasis does not replace sources or checks.

## Sources

- [Large Language Models Understand and Can be Enhanced by Emotional Stimuli](https://arxiv.org/html/2307.11760) — Li, Cheng; Wang, Jindong; Zhang, Yixuan; Zhu, Kaijie; Hou, Wenxin; Lian, Jianxun; Luo, Fang; Yang, Qiang; Xie, Xing. 2023-07-14; version read 2023-11-12. Examines the effect of emotional stimulus phrases on specific LLM tasks; does not prove that the model experiences emotion or a universal gain. Evidence level: relevant body sections of the original paper.
