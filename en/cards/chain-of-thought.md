# Chain-of-Thought

Carry the short, checkable intermediate results from a solved example over to a new problem.

## What is it?

In the original, example-based form of Chain-of-Thought prompting, you show not only the question and answer but also the solution steps in between. The goal is to demonstrate a way of solving to the model. Here we use equations, assumptions and short checkable explanations instead of long dumps of internal thinking.

These visible explanations are not a record of how the model actually thinks. A fluent but wrong solution can be written in the same form; checking the result remains a separate step.

## When does it help?

You can try it for arithmetic, ordering and problems where several connections must be held together. Your example solution must be correct and structurally related to the target question.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will count the pens in boxes; the example shows the order of multiplication and subtraction.

**Prompt**

```text
Example: There are three pens in each of two boxes, and one is given away. Calculation: 2×3=6; 6−1=5. Answer: 5 pens.
Example: There are two pens in each of three boxes, and two are given away. Calculation: 3×2=6; 6−2=4. Answer: 4 pens.
New question: There are five pens in each of four boxes, and three are given away. In the same format, write short equations and the final answer.
```

**Sample output**

4×5=20; 20−3=17. Answer: 17 pens.

**What did we get?**

We can see the intermediate calculation and the unit of the result. You can check the arithmetic with a separate calculation.

### Medium

**Situation**

A discount and a fixed fee are applied together.

**Prompt**

```text
Example: A 10% discount on a 100 TL product, then a 5 TL service fee. Discounted product: 100×0.90=90; total: 90+5=95 TL.
Example: A 25% discount on a 200 TL product, then a 10 TL fee. 200×0.75=150; 150+10=160 TL.
Question: A 25% discount is applied to the product total of three products costing 80 TL each; then 20 TL shipping is added. Keep the rule that the discount does not apply to shipping. Give short equations and the total.
```

**Sample output**

Products: 3×80=240 TL. After discount: 240×0.75=180 TL. Total: 180+20=200 TL.

**What did we get?**

The discount base stayed explicit. We cannot infer another shop's rule from this example.

### Hard

**Situation**

The free-shipping threshold depends on the amount after the discount.

**Prompt**

```text
Example: Product 600 TL, 10% discount → 540 TL. Rule: if at least 500 TL after discount, shipping is free: total 540 TL.
Example: Product 400 TL, 10% discount → 360 TL. Below the threshold, 50 TL shipping: total 410 TL.
New question: The product total is 625 TL; there is a 20% discount. Shipping is 0 if the amount after discount is 500 TL or more, and 50 TL if it is below. No tax is added separately. Write the threshold comparison used and the total; also, what would change if the product total were 620 TL?
```

**Sample output**

625×0.80=500; 500≥500, shipping 0; total 500 TL. 620×0.80=496; shipping 50; total 546 TL.

**What did we get?**

The expected behavior on both sides of the threshold is visible. In real code, the number type and currency rounding must be checked separately.

## Where should you stop?

Do not treat example-based CoT and example-free prompting as the same operation. Some reasoning models are designed to work with direct instructions; extra solution narration may not help in every case. In the human self-explanation card, you are the one explaining and learning; this card is about the structure of model output.

## Sources

- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/html/2201.11903) — Wei, Jason; Wang, Xuezhi; Schuurmans, Dale; Bosma, Maarten; Ichter, Brian; Xia, Fei; Chi, Ed; Le, Quoc; Zhou, Denny. 2022-01-28; version read 2023-01-10. Studies prompting with example solution steps on arithmetic, commonsense and symbolic tasks; the scenarios given here are not the paper's experiments. Evidence level: relevant body sections of the original paper.
- [Reasoning best practices | OpenAI API](https://developers.openai.com/api/docs/guides/reasoning-best-practices) — OpenAI. Publication date not verified. Provides the advice to use short, direct instructions with certain reasoning models; limits carrying earlier CoT findings over to all models. Evidence level: page body.
