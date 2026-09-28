# Medprompt

Select similar examples, shuffle the options, and combine separate answers by mapping them back.

## What is it?

Medprompt brings together dynamic few-shot example selection, rationales generated and checked for the examples, and an arrangement that combines separate answers while shuffling the options. The original work starts from medical question answering; here, safe toy arithmetic questions are used.

## When does it help?

In multiple-choice tasks with a pool of labeled examples, similarity search, multiple model calls and evaluation questions with known correct answers.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will set up the simplest version of the whole flow for a small arithmetic question.

**Prompt**

```text
A controller and an embedding model are needed. Pool example Q1="3 pens in each of 2 boxes: 6"; the correct label is known by a human. Separate test question Q2="4 pens in each of 3 boxes?" options 7,12,16.
Preparation: Generate a short calculation rationale for Q1; if the final answer does not match the known 6, discard the example. Store the embeddings of the pool questions.
Inference: Select the example closest to Q2 by real embedding similarity. Make two independent calls with this example and Q2; change the option order in the second call. Ask for a short, checkable calculation and an option.
The controller should map the letters back to the actual answer values and combine the votes. If the two votes conflict, abstain; the budget is two inference calls.
```

**Sample output**

The first call may say B=12, the shuffled second call A=12. After mapping, both answers are 12; B and A are not counted directly.

**What did we get?**

Votes were collected for the same actual answer, not just for option letters.

### Medium

**Situation**

A rationale in the pool may contain a wrong calculation despite the correct label.

**Prompt**

```text
Pool: Q1="600−100+40?", correct answer 540. The model's representative rationale: "600−100=510; 510+40=540".
Second synthetic pool record Q2="25% discount on 400 TL, then 20 TL shipping?", correct answer 320. Representative rationale: "400 × 0.75 = 300; 300 + 20 = 320". The two rationales are given ready-made in this example; there is no new preparation call.
The preparation controller should first filter the final answers against the labels; then, in this adaptation, a human/arithmetic check should also check the intermediate operations. Reject Q1's rationale; accept Q2 only if it passes the calculation check. If no accepted record remains, stop without running inference.
Test question: 20% discount on 625 TL; shipping 0 if 500 or more after discount, 50 below that. Options 500,550,625.
Build the embedding index with only the accepted Q2; run a real similarity query with the test question and retrieve the top-1 Q2. Carry this example and the test question into 3 separate calls; the option orders should be [500,550,625], [550,625,500], [625,500,550] respectively. Map the real answers to their original values, and report uncertain if there is no majority. Stop after one embedding search and three inference calls.
```

**Sample output**

Q1 is rejected; Q2's rationale 300 + 20 = 320 passes the check and is selected as the example. Representative check for the test: “625 × 0.8 = 500; shipping 0; answer 500.” Representative votes A, C, B; all three map to the value 500 in their own option orders.

**What did we get?**

The final label being correct did not verify all the operations in the explanation.

### Hard

**Situation**

You will prevent the test answer from leaking into the example pool during dynamic selection.

**Prompt**

```text
The data manager should separate the training/example pool, development and final test questions. Rewritten copies of the same question should also go to the same split.
Controller: Generate and check preparation rationales only in the labeled example pool; build the embedding index from this pool. For each test, store the selected example IDs, the option permutation and the real answers.
Sample test: 7 of 18 tickets were sold, 4 new tickets were added; options 11,15,22. Shuffle the options in three inference calls; map the values back.
Do not adjust the example-selection rule for the same test after looking at the final test result. After three votes, report the result or the unresolved disagreement; do not make a real clinical decision.
```

**Sample output**

Representative calculation 18 − 7 + 4 = 15. The audit record should separately show that the selected examples do not contain the test question.

**What did we get?**

The success of the combined method was not confused with data leakage.

## Where should you stop?

Dynamic example selection and ensembling need a real call/search arrangement. Having three doctor roles played in the same chat is not Medprompt. Unanimous votes do not guarantee medical reliability; this card does not offer a clinical decision protocol. Examples with short rationales are a teaching adaptation of the original long explanation format.

## Sources

- [Can Generalist Foundation Models Outcompete Special-Purpose Tuning? Case Study in Medicine](https://arxiv.org/html/2311.16452) — Nori, Harsha; Lee, Yin Tat; Zhang, Sheng; Carignan, Dean; Edgar, Richard; Fusi, Nicolo; King, Nicholas; Larson, Jonathan; Li, Yuanzhi; Liu, Weishung; Luo, Renqian; McKinney, Scott Mayer; Ness, Robert Osazuwa; Poon, Hoifung; Qin, Tao; Usuyama, Naoto; White, Chris; Horvitz, Eric. 2023-11-28. Defines the components of dynamic few-shot selection, filtering model-generated rationales by the correct answer, and choice-shuffle ensembling; the arithmetic check of intermediate operations here is an explicit additional adaptation. Evidence level: relevant body sections of the original paper.
