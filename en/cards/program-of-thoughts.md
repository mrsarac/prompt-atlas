# Program of Thoughts

Hand the numerical calculation over from the language model to an executor.

## What is it?

Program of Thoughts generates the necessary part of numerical reasoning as a program and has an interpreter compute the result. The model carries the quantities in the problem into the program; the external executor provides the real numerical result.

## When does it help?

In numerical question answering, repeated calculations and tasks where operation errors can be checked. Code generation and execution are separate stages.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will have Python do the calculation of pens in boxes.

**Prompt**

```text
Supervisor: Code only in an isolated Python executor; no network/file access, 1-second limit. One generation and one run.
Model task: 5 pens in each of 4 boxes, 3 pens handed out. Generate only Python code that names these quantities and prints the result: boxes, pens per box, handed out, remaining. Do not give a dump of hidden thinking.
The application should check that the code contains nothing beyond permitted arithmetic and run it. The real stdout should be passed to the next answer call; if there is no tool, do not say the calculation was run. Report the result with its unit and stop.
```

**Sample output**

Code candidate: `boxes=4; per_box=5; given=3; print(boxes*per_box-given)`. Representative stdout: `17`. Final answer: “17 pens.”

**What did we get?**

It was set up so that the numerical result would come from actually executing the code, not from writing it.

### Medium

**Situation**

You will reduce ambiguous rounding by using kuruş (hundredths of a lira) in a money calculation.

**Prompt**

```text
Input: 3 products, unit price 80 TL; a 25% discount on the products; shipping 20 TL.
The model should write only the calculation part in Python. Unit kuruş: price 8000, shipping 2000; check that the discounted subtotal comes out in whole kuruş in this example. Print the result in kuruş.
The supervisor should run the code in the isolated executor and carry the real output together with the task into the final call. The final call should convert to TL and answer briefly. Stop on unpermitted code or an execution error; at most one calculation run.
```

**Sample output**

Code candidate: `subtotal=3*8000*75//100; print(subtotal+2000)`. Representative output: `20000`, that is, 200 TL.

**What did we get?**

The language model turned the rules into a program; the arithmetic and the unit conversion stayed checkable.

### Hard

**Situation**

You do not want decimal errors in an expression that needs exact fractions.

**Prompt**

```text
Task: Calculate the expression 8 / (3 - 8/3) with exact fractions.
The supervisor should allow only fractions.Fraction and basic arithmetic in Python; no network/files. The model should generate code that carries the numerator/denominator structure exactly; division by zero and execution errors should be separate outcomes.
The application should store the code and the real stdout/stderr. The final call should answer only from a successful execution result. Then a human should check that the expression has the same bracket structure as the code; if it differs, even a correct stdout should not count as the answer to the task. Stop after one run.
```

**Sample output**

Code candidate: `from fractions import Fraction; print(Fraction(8)/(3-Fraction(8,3)))`. Representative stdout: `24`.

**What did we get?**

Besides the correctness of the calculation, it was also checked that the question was carried into the program correctly.

## Where should you stop?

An executor can flawlessly compute a wrong problem that was written correctly. PAL also uses program execution; Program of Thoughts particularly emphasizes separating the numerical calculation from the linguistic task. Having code written is not, on its own, the real execution part of either method. A safe execution environment is the application's responsibility.

## Sources

- [Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks](https://arxiv.org/html/2211.12588) — Chen, Wenhu; Ma, Xueguang; Wang, Xinyi; Cohen, William W.. 2022-11-22; version read 2023-10-23. Defines the approach of handing numerical computation to a generated program and an external executor; the example code here is for teaching purposes. Evidence level: relevant body sections of the original paper.
