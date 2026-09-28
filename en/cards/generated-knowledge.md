# Generated Knowledge

Before answering, generate candidate pieces of relevant knowledge; do not mistake them for sources.

## What is it?

Generated Knowledge Prompting first asks the model to generate knowledge related to the question, then to use that knowledge when answering. The generated knowledge comes from the model; no external document has been retrieved or verified.

## When does it help?

For surfacing related concepts in a question that needs everyday knowledge, and then building the answer. On its own it is not enough for current, sensitive or source-dependent topics.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will handle the question “Why does ice float on water?” in two stages.

**Prompt**

```text
A human should make two separate calls.
1. Write at most two short knowledge candidates that could help with the question: Why does ice float on water? These are model-generated; do not say you have verified sources.
2. Give the real first output and the question to a new call. Write a two-sentence answer using these knowledge candidates. If a candidate is uncertain, do not use it as definite information. Stop at the second answer.
```

**Sample output**

Knowledge candidates: “The density of ice is lower than that of liquid water. Lower density can explain floating.” Answer: “Ice floats because it has a lower density than liquid water.”

**What did we get?**

The relationship to be used in the answer became visible in a separate stage.

### Medium

**Situation**

Two different pieces of supporting knowledge will be generated for an everyday reasoning question.

**Prompt**

```text
Question: Why might tea left with its lid open cool down faster?
The controller should run two separate knowledge-generation calls; each should give at most two candidate explanations related to the question. Store the real outputs as K1/K2.
The final call should receive the question, K1 and K2 together. Separate evaporation from heat exchange with the surroundings; do not give an exact number of minutes, since the ambient conditions were not given. If there is conflicting information, say so. After the three calls, a human should not declare the text verified without checking it against a basic physics source.
```

**Sample output**

“An open surface allows evaporation and heat exchange with the surroundings. The cooling rate also depends on temperature, air flow and the structure of the cup.”

**What did we get?**

The knowledge candidates were combined in the answer; the conditions were not ignored.

### Hard

**Situation**

If the generated knowledge conflicts with a provided document, you will keep clear which is which.

**Prompt**

```text
Task: Why might a fictional museum be closed on Mondays?
1. The knowledge-generation call should write two possibilities for general museum closure reasons; it should not claim real knowledge about the institution.
2. The final call should receive these candidates and the document D1="The City Museum is closed on Mondays for special maintenance".
First answer with the institutional information D1 supports; do not attribute the general possibilities to this institution. The controller should carry the model candidates with the label generated and D1 with the label provided_source. Stop at two calls; do not hide that no search was performed.
```

**Sample output**

“According to D1, the reason for the closure is special maintenance. Generally suggested possibilities such as staff scheduling are not confirmed by this document.”

**What did we get?**

Possible knowledge coming from the model and evidence belonging to the institution were separated.

## Where should you stop?

RAG retrieves relevant documents from an external collection; this method generates relevant knowledge from the model. A model saying the same wrong thing in two calls is not verification. The original work has specific strategies for sampling knowledge and using answers; no success rate is promised here.

## Sources

- [Generated Knowledge Prompting for Commonsense Reasoning](https://arxiv.org/html/2110.08387) — Liu, Jiacheng; Liu, Alisa; Lu, Ximing; Welleck, Sean; West, Peter; Bras, Ronan Le; Choi, Yejin; Hajishirzi, Hannaneh. 2021-10-15; version read 2022-09-28. Defines the method of first generating relevant knowledge and then using it as input for answering questions. Evidence level: relevant body sections of the original paper.
