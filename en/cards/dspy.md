# DSPy

Define model calls as input–output modules; tie optimization to a metric.

## What is it?

DSPy is a framework for writing language model programs with modules and data flows. You define which output should be produced from which input, and you compose modules. A chosen optimizer can adjust prompts or demonstrations using training/development examples and a metric.

DSPy is not a single prompt or a single optimizer. Writing a signature does not optimize the system; you need a model connection, real module calls, data and evaluation. The outlines below are module contracts to implement, rather than version-specific API code.

## When does it help?

Use it when you want to combine the same components across different jobs or build a measurable model pipeline. You need a Python environment and an installed DSPy of known version; the card does not set these up.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

A single classifier module is to be defined.

**Prompt**

```text
The developer sets up this signature in a DSPy program: message:string → label:string.
Module instruction: “Only access/billing/unclear; if there is no explicit topic, unclear.”
Full input: “I can't log in”. Expected label: access.
The program calls the module once through the configured model adapter. It checks whether the output is in the permitted label set and whether it matches the expected one. There is no optimizer at this step.
On an API error, do not produce a result; do not save output that has not passed the output contract.
```

**Sample output**

Representative module result: label=access. This is only a sample input for the program to run.

**What did we get?**

The signature, the task and the check criterion are clear. A single module call does not yet count as compilation/optimization.

### Medium

**Situation**

Retrieval and answering will be connected as two modules.

**Prompt**

```text
Store: K1 “Room A holds 16 people”; K2 “Room B holds 30 people”. Question: How many people does Room A hold?
DSPy application: retrieve(question) → passages; answer(question,passages) → answer,source_codes.
A real search component runs over K1/K2. The answer module uses only the retrieved passage. Along with the signatures, the rule “no passage, no answer” is applied.
The coordinator checks the link between the search result and the answer fields. One search, one answer call; stop on a missing record.
```

**Sample output**

Representative flow: retrieve → K1; answer → “16 people”, [K1].

**What did we get?**

The data contract between the modules is explicit. Setting up and running the program is a separate engineering step.

### Hard

**Situation**

The choice of examples will be optimized for the same program.

**Prompt**

```text
Program: message → label. Development: “I can't log in”→access; “No invoice”→billing; “Hello”→unclear.
The developer chooses an example-based optimizer in the installed DSPy version; sets metric=exact-match and at most 12 target calls. The optimizer generates candidate demonstrations and evaluates them with real module outputs.
Freeze the final program. Separate check “The account won't open”→access; do not give this example to the optimizer.
Record the compiled program's instructions/demonstrations and the check result. If there is no valid candidate within the budget, do not automatically count the starting program as successful.
```

**Sample output**

Representative deliverable: frozen signature, selected demonstrations, measurement records. The output of the separate check is not known without running it.

**What did we get?**

Using the framework and having a really optimized program were separated. Without a metric and data, no success claim remained.

## Where should you stop?

The API and optimizer behavior of the installed version may not be exactly the same as in the original paper. If you choose the wrong evaluation metric, a well-compiled program can do the wrong job more consistently. APE, OPRO and GEPA are specific search approaches; DSPy is not one and the same method as these.

## Sources

- [DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines](https://arxiv.org/html/2310.03714) — Khattab, Omar; Singhvi, Arnav; Maheshwari, Paridhi; Zhang, Zhiyuan; Santhanam, Keshav; Vardhamanan, Sri; Haq, Saiful; Sharma, Ashutosh; Joshi, Thomas T.; Moazam, Hanna; Miller, Heather; Zaharia, Matei; Potts, Christopher. 2023-10-05. Defines declarative modules, language model call graphs and compiling against a metric. Evidence level: relevant body sections of the original paper.
- [stanfordnlp/dspy: DSPy: The framework for programming—not prompting—language models](https://github.com/stanfordnlp/dspy) — DSPy contributors. Publication date not verified. Shows the framework's public repository and implementation scope; the repository and the paper's versions are not treated as the same. Evidence level: page body.
