# OPRO

Generate new candidates by showing earlier candidates together with their real scores.

## What is it?

In OPRO, the model sees earlier solution or prompt candidates and their measured values. It proposes a new candidate; an external evaluator runs and scores that candidate. The candidate and its score are added to the history, and the next round uses this history.

The optimization objective and the measurement procedure are defined outside the model. A model statement such as “I gave this prompt 95 points” is not a measurement. Here we show OPRO's prompt-optimization use on a small labeling task.

## When does it help?

Use it for repeatable work with a clear criterion. You need a coordinator that keeps records of the real calls and check data kept apart from the candidate search.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

A labeling instruction will be developed on two records.

**Prompt**

```text
Development: “I can't log in”→access; “The invoice is wrong”→billing. Starting prompt: “Write the topic.”
The coordinator runs the starting prompt in two target calls and calculates the exact-match score.
It gives the optimizer call this package: task “Label the support message by topic”; permitted labels access (login problem), billing (invoice problem); the two development input/label pairs above; the full text of the starting prompt and the score just measured. Request: “For this task and these examples, using the earlier candidate/score pair, propose one new complete instruction; do not invent a score.”
It runs the new candidate on the same two inputs and adds the measured score to the history. One improvement round; five calls in total. Leave any score not yet observed blank.
```

**Sample output**

Representative history: “Write the topic” → 1/2; “Write only the label access or billing” → 2/2. These numbers are made-up teaching data to show the flow.

**What did we get?**

It is clear at which stage the score is produced. The model is prevented from producing the score itself while proposing a candidate.

### Medium

**Situation**

The first improvement fixed the format but still misses the unclear class.

**Prompt**

```text
Data: “I can't log in”→access; “The invoice is wrong”→billing; “Help”→unclear.
Task: label the support message; login problem access, invoice problem billing, unclear if there is no explicit topic. Starting candidate “Write only the label access or billing.” The coordinator measures it on the three development records.
Each optimizer call receives the task, the meaning of the three permitted labels, these three development pairs and all earlier full candidate/measured score pairs together. It generates one new candidate; the target model processes the three records, and software calculates the exact-match score and adds it to the history. The check input and its label do not enter this package.
At most two improvement rounds; if there is no improvement, stop early. The best prompt is frozen. Budget: 3 target calls for the start + 2 optimizer and 6 target calls for the two rounds + 1 separate check; at most 12 in total.
Separate check: “My account won't open”→access. Do not put this example into the search history; check it once with the frozen candidate.
```

**Sample output**

Representative new candidate: “If the message has no explicit topic, unclear; otherwise access or billing.” The expected label for the check is access.

**What did we get?**

The history shows which problem the new candidate targets. A single check example does not give a reliable success rate.

### Hard

**Situation**

The optimizer's instruction may change the objective.

**Prompt**

```text
Task: classify the support topic as access/billing/unclear. Development: “I can't log in”→access; “No invoice”→billing; “Hello”→unclear.
Contract: login problem access, invoice problem billing, unclear if there is no explicit topic; no action other than labeling. The coordinator measures the starting candidate “Write billing for every input” on the three development examples and records it in the candidate/score history.
Every optimizer call in the two improvement rounds receives the task/contract, the three development pairs and the full candidate/measured score history so far. The input and label of the final test stay only on the evaluation side.
Before each new candidate is run, the class set and the ban on actions outside the source are checked. Reject a “let's change the labels” proposal and stop the round; measure a valid candidate on the three development records and add it to the history. Freeze the best valid candidate by its development score.
Test: “My password is being rejected”→access, kept separate from the search. Budget: 3 start + 2 optimizer + 6 development + 1 test call; at most 12 in total. If the test fails, do not produce a new success label or reopen the search against the same test.
```

**Sample output**

The representative always-billing candidate matches 1/3. A candidate that changes the label set is rejected before running.

**What did we get?**

The definition of the task did not change for the sake of a higher-looking score. The final choice stayed tied to real measurements and a fixed objective.

## Where should you stop?

If the criterion is narrow, the model can find prompts that fit that criterion but not the real purpose of the work. OPRO's numerical optimization and prompt optimization experiments are not the same use. Data separation and call cost must be checked separately.

## Sources

- [Large Language Models as Optimizers](https://arxiv.org/html/2309.03409) — Yang, Chengrun; Wang, Xuezhi; Lu, Yifeng; Liu, Hanxiao; Le, Quoc V.; Zhou, Denny; Chen, Xinyun. 2023-09-07; version read 2024-04-15. Defines the optimization loop that carries earlier candidate/value pairs into generating new solutions; the score must come from external evaluation. Evidence level: relevant body sections of the original paper.
