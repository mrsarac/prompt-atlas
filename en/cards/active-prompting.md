# Active Prompting

Have a human label the examples the model is most uncertain about.

## What is it?

Active Prompting generates several separate answers across a pool of questions and measures uncertainty; for the selected questions, it has a human prepare annotated correct examples. These examples then become few-shot input. This is an example-selection process; it is not automatic model training.

## When does it help?

When human labeling time is limited and you want to choose systematically which questions to prepare good examples for.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will choose which of two toy arithmetic questions to turn into an annotated example.

**Prompt**

```text
Controller pool: Q1="2+2?", Q2="Under a free-shipping rule with an inclusive 500 TL threshold, what is the shipping fee for 500 TL?" Rule: below 50, at the threshold and above 0.
Make 3 independent calls for each question; do not show earlier answers to the other calls. Normalize the real answers to numeric form.
Fix the uncertainty measure in advance: 1 - the share of the most frequent answer. Have a human pick the one question with the highest uncertainty.
The human should write the correct answer and a short check. Add this approved example as few-shot to the next new question. Budget 6 samples + 1 inference call; then stop.
```

**Sample output**

Representative sampling: Q1=[4,4,4], uncertainty 0; Q2=[0,50,0], uncertainty 1/3. The human prepares the example “500 ≥ 500, shipping 0” for Q2.

**What did we get?**

The labeling effort was directed by uncertainty that is actually measured.

### Medium

**Situation**

Answer formats can create fake disagreement.

**Prompt**

```text
Finite pool: Q1="23 people, at most 6 people per table; how many tables?"; Q2="Free shipping with an inclusive 500 TL threshold; 50 TL below. Shipping for a 500 TL basket?"; Q3="2+2?"
The controller should get 4 calls per question that do not see each other's answers. Representative answers: Q1=["4","four tables","4 tables","3"], Q2=["0","50","0 TL","50 TL"], Q3=["4","four","4","4"]. First normalize the number/unit meaning.
Uncertainty = 1 − the share of the most frequent answer. Select the two highest questions; in a tie, the smaller Q ID comes first. A human should write the correct answer and a short rationale only for these two questions; do not use an unapproved example.
If the two labels cannot be approved, stop without moving to new inference. Carry these two approved examples to a separate new question: "25 people, at most 6 people per table; how many tables?" This question's answer does not enter the selection stage. Budget 3×4=12 samples, 2 human labels, 1 new inference; 13 model calls in total, then stop.
```

**Sample output**

After normalization Q1=[4,4,4,3], Q2=[0,50,0,50], Q3=[4,4,4,4]; uncertainties 1/4, 1/2, 0 respectively. Selection Q2 and Q1. Human labels: “500 ≥ 500, shipping 0”; “3 tables seat 18 people; 4 tables seat 24, so 4 are needed.” Representative answer to the new question: “4 tables seat 24 people; 25 people need 5 tables.”

**What did we get?**

Different ways of writing were not counted as different views.

### Hard

**Situation**

Uncertainty is low, but a shared wrong answer is possible.

**Prompt**

```text
Finite pool: Q1="Basket 600 TL, coupon 100 TL; after the discount, shipping 40 TL if below 550, otherwise 0. Payment total?"; Q2="23 people, at most 6 people per table; how many tables?"; Q3="2+2?"
Make 3 independent calls per question. Representative numeric answers Q1=[500,500,500], Q2=[4,3,4], Q3=[4,4,4]. Uncertainty = 1 − modal share. Select the one most uncertain question; in a tie, the smaller ID comes first. A human should prepare the correct answer and a short rationale.
Fix the extra human-check rule before the results: check the one question with the smallest ID among the unselected zero-uncertainty questions. This is a teaching adaptation added on top of uncertainty selection. Two human labels is the upper limit; do not add an unverifiable label to the pool.
If the two labels cannot be approved, stop without moving on to evaluation. Have a single separate evaluation question answered with the two approved examples: "Basket 620 TL, coupon 100 TL; after the discount, shipping 40 TL if below 550, otherwise 0. Payment total?" The evaluation answer is not used for selection/updating. Budget 9 samples + 1 evaluation call and at most 2 human labels; then stop.
```

**Sample output**

Uncertainties Q1=0, Q2=1/3, Q3=0. The first selection is Q2; the human verifies the label “4 tables are needed” by calculation. The extra check selects Q1; the human adds the label “600−100=500; 500<550, so 500+40=540”. Representative final evaluation: 620−100+40=560 TL. The shared wrong answer with zero uncertainty became visible through a separate human check.

**What did we get?**

The model's uncertainty and the human's correctness check remained separate measures.

## Where should you stop?

Self-consistency answers the question itself by combining separate answers; Active Prompting uses uncertainty to select the examples a human will label. The original work has human-written explanations. The short rationales here are a teaching adaptation; they do not guarantee the method's gain.

## Sources

- [Active Prompting with Chain-of-Thought for Large Language Models](https://arxiv.org/html/2302.12246) — Diao, Shizhe; Wang, Pengcheng; Lin, Yong; Pan, Rui; Liu, Xiang; Zhang, Tong. 2023-02-23; version read 2024-07-21. Defines estimating uncertainty with multiple samples, selecting questions accordingly, and the few-shot use of human-annotated examples. Evidence level: relevant body sections of the original paper.
