# Self-explanation

You build the explanation; the model makes the connection you skipped visible.

## What is it?

Self-explanation is explaining in your own words why an example works. If the model produces the explanation for you, the learning work the human does changes. In this card, the model gives short questions and source-bounded feedback.

## When does it help?

When a solution feels familiar as you read it, but you struggle to apply the same idea to a new example.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will explain a percentage discount calculation in your own sentence.

**Prompt**

```text
I am the learner. Rule: a 20% discount means paying 80% of the price. Example: 100 TL -> 80 TL.
First ask me "Why do we multiply 100 by 0.8?" and wait for my answer. Do not write the explanation for me. Point out the correct connection in my answer; if something is missing, ask a single follow-up question. At most two questions.
```

**Sample output**

Model: “Why do we multiply by 0.8?” Human: “When 20 percent goes, 80 percent is left.” Model: “You connected the remaining share correctly. So what does the same rate change for 200 TL?”

**What did we get?**

Instead of repeating the result, the meaning of the remaining share was explained.

### Medium

**Situation**

You will explain why a line of code covers the boundary case.

**Prompt**

```text
Code: total >= 500 ? 0 : 50. Rule: 500 and above ships free, below that 50 TL.
My explanation: "If it's greater than 500, shipping is free."
Compare my explanation with the rule and the code. Point out the correct part; ask a question about the one missing boundary. Do not tell me the fix right away. Once I explain again, it is enough to ask for predictions for 499/500/501; do not claim you ran a real code test.
```

**Sample output**

Model: “You described the larger amounts. What does the `=` sign change when it is exactly 500?” Human: “500 is free too; 50 for 499, 0 for 500 and 501.”

**What did we get?**

The equality missing from the verbal explanation was carried into a new boundary example.

### Hard

**Situation**

Your seemingly correct explanation does not work in a new situation.

**Prompt**

```text
Source rule: Average speed is total distance / total time.
My explanation: "If you go 60 km at 30 km/h, then 60 km at 60 km/h, the average is 45 km/h; I averaged the two speeds."
First, with a single question, show me which assumption of my explanation I need to check. Wait for me to calculate the times without giving the answer. Then ask me to connect total distance and total time in my own words.
At most three questions; at the end, give a new task: why would it be different if you traveled at these speeds for two equal amounts of time? Do not treat the quality of an explanation as the same measure as a correct answer given without help.
```

**Sample output**

Model: “Are you spending equal time on the two parts?” Human: “The first part is 2 hours, the second 1 hour; 120/3=40.” The model asks them to explain again the difference between equal distance and equal time.

**What did we get?**

A wrong generalization came to light by comparing it with another condition.

## Where should you stop?

Self-explanation is an explanation made by the human; the same learning claim cannot be made for a model explaining its own answer. Plain-language explanation approaches associated with the Feynman name are related to this card, but they are not presented as a single original four-step academic protocol. A nicer explanation does not mean a correct answer or a long-term gain in learning.

## Sources

- [Self-explanations: How students study and use examples in learning to solve problems](https://education.asu.edu/lcl/publications/chi-m-t-h-bassok-m-lewis-m-reimann-p-glaser-r-1989-self-explanations-how-students) — Michelene T. H. Chi; Miriam Bassok; Matthew W. Lewis; Peter Reimann; Robert Glaser. 1989. Confirms the title, authors and 1989 citation of the human self-explanation study; no experimental details or effect size are derived from this record. Evidence level: bibliographic record only.
- [Practice Less, Explain More: LLM-Supported Self-Explanation Improves Explanation Quality on Transfer Problems in Calculus](https://arxiv.org/html/2604.00142) — Chen, Eason; Tang, Xinyi; Zhao, Yvonne; Chen, Meiyi; Elmir, Meryam; McLaughlin, Elizabeth; Yuan, Mingyu; Wang, Yumo; Agarwal, Shyam; Cochrane, Jared; Lin, Jionghao; Wu, Tongshuang; Koedinger, Ken. 2026-03-31; version read 2026-05-30. Examines a self-explanation condition with LLM feedback; explanation quality and post-test performance are separate measures, and no significant post-test difference between conditions is reported. Evidence level: relevant body sections of the original paper.
- [Learn Faster with the Feynman Technique](https://www.scotthyoung.com/blog/2011/09/01/learn-faster/) — Scott H. Young. 2011-09. Confirms practitioner use of the name Feynman Technique; no original steps or effect claims are drawn from the unwatched video. Evidence level: page text; the embedded video was not reviewed.
