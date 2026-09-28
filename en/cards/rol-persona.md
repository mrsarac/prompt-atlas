# Role and persona

State which details the model should look at, and for which reader.

## What is it?

Giving a role means choosing the angle from which a text is read. When you say “editor for a beginner reader”, you can ask it to focus on unclear terms; when you say “developer reviewing the tests”, on boundary conditions. Explaining the role's job with concrete verbs is easier to check than writing a job title alone.

An expert persona does not give the model new knowledge, a diploma or tool access. Having three characters speak inside one response is also not three independent agent calls.

## When does it help?

Use it when you edit the same text for different readers or choose a specific review goal. Also give the object the role should look at and the change it should deliver.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

New participants do not understand the phrase “registration verification”.

**Prompt**

```text
Review this as an editor for a beginner-level reader. Sentence: “Subsequent to registration verification, your participation will be activated.” Meaning: the place is confirmed when the confirmation email arrives. Simplify the formal words; write one sentence without adding a new condition.
```

**Sample output**

Your place is confirmed when the confirmation email arrives.

**What did we get?**

The role narrowed down which language problem to look at. Check separately that the sentence describes the registration process correctly.

### Medium

**Situation**

You want to read the shipping function separately from an interface-text angle and a testing angle.

**Prompt**

```text
Use two review angles within a single response; they are not independent agents.
Information: “Free shipping for 500 TL and above.” Code: total > 500 ? 0 : 50.
Editor: state in one sentence the threshold the text promises.
Test reviewer: propose one boundary test for this promise and its expected result.
Do not claim that you ran the code.
```

**Sample output**

Editor: Exactly 500 TL falls in the free range. Test reviewer: for total=500 the expected shipping is 0; the current expression produces 50.

**What did we get?**

The two roles produced different review questions. Both are parts of the same response; the real test is the developer's job.

### Hard

**Situation**

In a decision note, cost and accessibility conflict. You do not want the role to take over the decision.

**Prompt**

```text
You are the editor of a decision note; do not make the choice for me.
Venue A: 800 TL, step-free entry verified. B: 600 TL, three steps at the entrance. For an 18-person team, step-free access is mandatory. The budget ceiling is 700 TL.
First separate the mandatory conditions. Then state which condition each option fails. Do not assume a budget change that is mine to make. Write at most the next decision question.
```

**Sample output**

A exceeds the budget by 100 TL; B does not meet the access condition. With the current information, there is no suitable option. Should we look for a third venue that is step-free and costs at most 700 TL?

**What did we get?**

The role organized the note; it did not create new budget authority. The decision to start a search or change the scope stayed with you.

## Where should you stop?

Do not treat adjectives such as “the world's best expert” as a guarantee of factual accuracy. The results of persona studies depend on the task and the model. CO-STAR organizes brief fields such as context, objective and reader together instead of a role; multi-agent methods also need a real call infrastructure.

## Sources

- [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT](https://arxiv.org/html/2302.11382) — White, Jules; Fu, Quchen; Hays, Sam; Sandborn, Michael; Olea, Carlos; Gilbert, Henry; Elnashar, Ashraf; Spencer-Smith, Jesse; Schmidt, Douglas C.. 2023-02-21. Defines the persona pattern as a form of interaction; it is not a certificate of professional competence. Evidence level: relevant body sections of the original paper.
- [When “A Helpful Assistant” Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models](https://arxiv.org/html/2311.10054v3) — Zheng, Mingqian; Pei, Jiaxin; Logeswaran, Lajanugen; Lee, Moontae; Jurgens, David. 2023-11-16; version read 2024-10-09. Examines how, in the models studied, adding a persona did not bring consistent improvement on factual tasks. Evidence level: relevant body sections of the original paper.
- [[2512.05858] Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy](https://arxiv.org/abs/2512.05858) — Basil, Savir; Shapiro, Ina; Shapiro, Dan; Mollick, Ethan; Mollick, Lilach; Meincke, Lennart. 2025-12-05. Provides an abstract-level limit on the relationship between expert personas and accuracy; the full experimental body was not read for this record. Evidence level: abstract only.
