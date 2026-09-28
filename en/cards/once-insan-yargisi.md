# Human judgment first

Record your own judgment first, then compare it with the model's suggestion.

## What is it?

Human judgment first is an arrangement in which you write a first answer or decision rationale before seeing the model's suggestion. The goal is to pause automatic acceptance. It is not declaring the human's first answer to be unchangeably correct.

## When does it help?

In work where you notice you readily go along with the model's fluent answer and want to keep your own check.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will do a boundary calculation before the model.

**Prompt**

```text
Rule: 500 TL and above ships free, below that 50 TL. Question: Shipping at 500 TL?
Do not give the answer first; ask me to write my own answer and a short justification. Once I answer, give your own answer separately and, if there is a difference, tie it to the rule. Do not rewrite my first judgment as if it had been changed afterwards.
```

**Sample output**

Human: “50, because it isn't greater than 500.” Model: “The rule says ‘and above’; 500 is included, shipping 0. The boundary interpretation in your first answer should change.”

**What did we get?**

The first thought stayed visible; the correction was tied to the source.

### Medium

**Situation**

You will check whether a claim in a text is supported.

**Prompt**

```text
Source: "Three of the five participants preferred the morning." Claim: "All participants want the morning."
First wait for my supported/not supported judgment and my quote. Then show the model's evaluation. If there is disagreement, resolve it by the scope of the source, not by majority or model confidence.
After one comparison round, write the first judgment, the model's judgment and the final decision based on the source as separate fields.
```

**Sample output**

“First judgment: supported. Model: not supported. Final decision based on the source: the preference of three people cannot be generalized to the whole group.”

**What did we get?**

The reason for the change of decision was a scope check, not the model's authority.

### Hard

**Situation**

The human and the model may share the same wrong assumption.

**Prompt**

```text
Decision: Is the fictional service working today? Data: It was working yesterday at 18:00; no live record.
First the human should write their first judgment in a local note; then get the model's answer. Model task: state the time limit of the available data and the check needed.
The supervisor should store the first human answer and the model's answer separately. Even if both say "working", do not treat the agreement as external evidence; put the need for an observation from today on the checklist.
If there is no live tool, the final decision should be not verified. Stop after a single comparison round; do not count a check that was not done as complete.
```

**Sample output**

“The human and the model may agree; today's status is still not verified.”

**What did we get?**

The first-judgment arrangement was complemented by a separate source check against a shared error.

## Where should you stop?

It cannot be said that a human always makes a more accurate decision when thinking first. This design can add extra mental load. The work of Buçinca and colleagues is a specific AI-assisted decision task, not an LLM prompting experiment; less overreliance and overall team performance are not the same result.

## Sources

- [To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making](https://arxiv.org/html/2102.09692) — Buçinca, Zana; Malaya, Maja Barbara; Gajos, Krzysztof Z.. 2021-02-19. Examines the effects of cognitive forcing arrangements on overreliance on AI suggestions and on usability; findings from a specific, non-LLM decision context do not directly guarantee success for this adaptation. Evidence level: relevant body sections of the original paper.
