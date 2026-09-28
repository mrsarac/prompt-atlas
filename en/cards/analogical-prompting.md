# Analogical Prompting

Generate similar solutions, then show which structure carries over to the target question.

## What is it?

Analogical Prompting asks the model to generate similar problems and solutions that help with the target, then to make use of them. The generated analogies are not real past cases or external sources; wrong examples can also spoil the answer.

## When does it help?

When you want to recognize the structure of a problem and carry over a suitable solution idea from a similar example.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will open up a quantity problem with a similar example.

**Prompt**

```text
Target: There are 8 notebooks in each of 3 boxes, and 5 were handed out; how many are left?
First generate and solve a short problem with the same operational structure but different numbers. Then write in one sentence which relationship is shared. Then solve the target. Do not describe the examples as events that really happened; a short calculation is enough.
```

**Sample output**

Similar example: “Each of 2 packs holds 6 pens, and 4 of the total were given away: 2×6−4=8.” Shared structure: subtracting the amount taken from the total. Target: 3×8−5=19.

**What did we get?**

The operational relationship carried over, rather than the surface objects.

### Medium

**Situation**

A wrong analogy can spoil an average calculation.

**Prompt**

```text
Target: 60 km at 30 km/h, then 60 km at 60 km/h; average speed?
Generate two similar-looking examples: two parts of equal time and two parts of equal distance. In each, do a short check using total distance/total time.
Then state which one the target matches structurally, and solve it. Check the time weighting instead of just averaging the numbers. If you find a faulty example, do not use it.
```

**Sample output**

“The target has the equal-distance arrangement: the times are 2 and 1 hours; 120/3=40 km/h. The result 45 from the equal-time example cannot be carried over here.”

**What did we get?**

The condition where the analogy breaks was seen as clearly as the analogy itself.

### Hard

**Situation**

You will keep the limits when carrying an analogy over into a code design.

**Prompt**

```text
Target: A design that prevents the same draft from being created twice when a file upload is retried. Condition: The network response can be lost; the server may have completed the operation.
First generate two fictional similar problems and write the solution idea: the same ticket being issued twice; reapplying with the same order number. In each analogy, state the role of a shared identity and a result record.
Then separate the components that can be carried over to the target from the assumptions that cannot. Do not assume the real API has an idempotency guarantee until it is documented. The output should be a design proposal and the checks needed; do not run operations.
```

**Sample output**

“A shared request ID and a stored result can distinguish retries. This is only guaranteed if the server provides defined behavior for the same key.”

**What did we get?**

The analogy gave an idea; it did not replace an implementation guarantee.

## Where should you stop?

Few-shot examples can be provided by the user or a data pool; here the model generates examples suited to the target itself. Do not use fictional examples as evidence of real cases. The claim that humans learn through analogy and the model's task success with analogical prompting are separate matters.

## Sources

- [Large Language Models as Analogical Reasoners](https://arxiv.org/html/2310.01714) — Yasunaga, Michihiro; Chen, Xinyun; Li, Yujia; Pasupat, Panupong; Leskovec, Jure; Liang, Percy; Chi, Ed H.; Zhou, Denny. 2023-10-03; version read 2024-03-09. Studies the model generating relevant examples for a target problem and using them in the solution; it is not said that the generated examples are historically accurate or evidence of human learning. Evidence level: relevant body sections of the original paper.
