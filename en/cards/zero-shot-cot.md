# Zero-shot CoT

Ask for short intermediate results without giving a solved example; extract the final answer separately.

## What is it?

Zero-shot CoT steers the model toward a step-by-step solution without providing an example solution. The original setup by Kojima and colleagues has two stages: first generating a solution, then extracting the answer from that output. The two stages should not be reduced to a single slogan.

In the adaptations below, the intermediate output is only short equations or checkpoints. You can start the calls yourself and carry the first answer into the second call. This does not require asking for a record of hidden thinking.

## When does it help?

It can be used for small problems for which you have not prepared examples, or when the final answer needs to come out in a specific format. The second stage can carry the same mistake forward.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will calculate the books left on a bookshelf.

**Prompt**

```text
A human starts this; it uses two separate model calls.
Call 1: “There are 18 books on the shelf. 7 books are taken, 4 books are added. Write a short equation and the number of books left.”
Call 2: Paste the first output unchanged and say “From this solution, extract only the number of books left; do not add a new calculation or information.”
If the second response is not a single number, do not accept it; at most these two calls. Check the calculation separately.
```

**Sample output**

First call: 18−7+4=15 books. Second call: 15.

**What did we get?**

Generating the solution and formatting the answer were separated. The second call does not count as independent verification of the first calculation.

### Medium

**Situation**

A reservation splits people across tables.

**Prompt**

```text
The coordinator makes two calls.
1: “23 people are coming. At most 6 people can sit at each table. Give the number of tables needed with a short division and a capacity check. Count a partial table as a full table.”
2: Carry the first output over: “Write only the number of tables and the number of people at the last table.”
Check: everyone must be seated at a table. If the capacity does not work out after the two calls, do not give a final plan.
```

**Sample output**

First output: 3 tables seat 18 people; one more table is needed for the remaining 5. Final output: 4 tables; 5 people at the last table.

**What did we get?**

The need to round up is visible. The actual table layout at the venue is outside this numerical example.

### Hard

**Situation**

The discount base needed to determine shipping is missing; the two calls should not produce a definite number.

**Prompt**

```text
A human starts two calls.
1: “The product costs 600 TL; the discount is 100 TL. The shipping threshold is 550 TL; below the threshold, shipping is 40 TL. It is not stated whether the threshold applies before or after the discount. Write the two possible calculations briefly; do not pick a definite total.”
2: Add the first output and the original question: “In the final answer, keep the possible totals and the one missing rule. Do not close the unknown with a guess.”
Stop: after the second response, the shop's rule is expected from the user; do not make a third guessing call.
```

**Sample output**

Threshold applied to the amount before discount: 600≥550, total 500 TL. Applied to the amount after discount: 500<550, total 540 TL. Missing information: which amount the shipping threshold applies to.

**What did we get?**

Answer extraction did not erase the uncertainty. The one rule needed for a definite result stayed open.

## Where should you stop?

The sentence “Think step by step” is not a guarantee of a correct calculation. The original experiments were run with specific older models and tasks. Example-based CoT uses a different input arrangement; PAL hands the calculation to a real interpreter.

## Sources

- [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/html/2205.11916) — Kojima, Takeshi; Gu, Shixiang Shane; Reid, Machel; Matsuo, Yutaka; Iwasawa, Yusuke. 2022-05-24; version read 2023-01-29. Defines the setup of example-free solution generation followed by answer extraction; the InstructGPT/PaLM conditions do not generalize to every current model. Evidence level: relevant body sections of the original paper.
- [Reasoning best practices | OpenAI API](https://developers.openai.com/api/docs/guides/reasoning-best-practices) — OpenAI. Publication date not verified. Explains that with certain reasoning models, separately asking for CoT may not be necessary. Evidence level: page body.
