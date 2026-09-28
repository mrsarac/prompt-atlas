# PAL

Let the model write the program; let a real interpreter compute the numeric answer.

## What is it?

PAL has the natural-language problem expressed as a program and runs that program in an interpreter. The model has to choose the right variables and operations; an external executor such as Python does the actual computation.

A code block appearing in a chat does not mean it was run. The initiator is the person or application that reviews the generated code. You need a permitted execution environment, and the error output must be kept.

## When does it help?

It can be used for multi-step calculations, counting and symbolic operations. Start by checking that the code to be run does not need network, file access or other side effects.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will calculate the number of pens with a program.

**Prompt**

```text
Model call: “There are five pens in each of four boxes; three are given away. In Python, use only constant numbers and arithmetic; print the result. Do not ask for file/network access.”
A human reviews the code and runs it once in a permitted Python interpreter. If there is an error, the result is not accepted. Representative generated program:
print(4 * 5 - 3)
Without reading the real stdout, the model output is not presented as the calculation result.
```

**Sample output**

Representative program output: `17`. Unit: pens.

**What did we get?**

The program that will do the calculation is visible. The stdout record from your own run shows that the program was actually executed.

### Medium

**Situation**

You want to calculate the total for discounted products plus shipping, in kuruş (hundredths of a lira).

**Prompt**

```text
Ask the model for a Python program for this job: “Three products at 80 TL each, a 25% discount on the product total, then 20 TL shipping. Do the calculation with integer kuruş. Produce only print output.”
A human reviews the code and runs it in the interpreter; limit of one call and one run.
Representative program:
subtotal = 3 * 8000
payable = subtotal * 75 // 100 + 2000
print(payable)
Keep in mind that the result is in kuruş; do not mistake an error output for a price.
```

**Sample output**

Representative stdout: `20000`; equivalent to 200 TL.

**What did we get?**

The unit and the order of calculation can be seen in the program. For other amounts that produce fractional kuruş, the rounding rule must be decided separately.

### Hard

**Situation**

You will separate duplicate applications in a list and check the capacity.

**Prompt**

```text
Model call: “Applications ['A','B','A','C','D','B']; capacity 3. IDs are case-sensitive. Deduplicate while keeping the order of first appearance; the first three are candidates, the rest go on the waitlist. Write Python code; no files/network.”
A human runs the code only on this data. Representative program:
ids = ['A','B','A','C','D','B']
unique = list(dict.fromkeys(ids))
print({'candidates': unique[:3], 'waitlist': unique[3:]})
Check: no ID can be in both lists; there must be 4 unique IDs in total. If there is an error, do not produce confirmation emails. Stop after one generation and one execution.
```

**Sample output**

Representative output: `{'candidates': ['A', 'B', 'C'], 'waitlist': ['D']}`.

**What did we get?**

The calculation and the real registration confirmation were separated. A human verifies whether the IDs represent the same person and whether the selection rule is authorized.

## Where should you stop?

An interpreter can correctly compute a wrongly framed problem. That is why code review and checking the expected behavior matter. Program of Thoughts is a closely related approach of computing with a program; it is not claimed that every code-generating method under the PAL name is the same experiment.

## Sources

- [PAL: Program-aided Language Models](https://arxiv.org/html/2211.10435) — Gao, Luyu; Madaan, Aman; Zhou, Shuyan; Alon, Uri; Liu, Pengfei; Yang, Yiming; Callan, Jamie; Neubig, Graham. 2022-11-18; version read 2023-01-27. Supports the mechanism of expressing the problem as a program and executing it with an external interpreter; the original language/arithmetic tasks are not a run receipt for the programs here. Evidence level: relevant body sections of the original paper.
