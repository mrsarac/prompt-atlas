# Decomposed Prompting

Route subtasks to named handlers; carry their results like a program.

## What is it?

Decomposed Prompting sets up a decomposer that splits a problem into subtasks, and reusable handlers that solve those tasks. A controller actually runs the generated sequence of calls and links the intermediate answers to the next step.

## When does it help?

When the same subtasks recur across different questions, and different task types need different prompts or tools.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will sort a list of names alphabetically.

**Prompt**

```text
The controller should define two handlers: split_names turns text into a list of names; sort_names sorts the list in the given simple Latin alphabetical order. Both are separate prompt calls.
Input: "Cem, Ada, Bora".
The decomposer call should generate a program using only permitted handlers: v1=split_names(input); v2=sort_names(v1); return v2.
The application should check the handler names and store the real v1/v2 outputs. Stop if a name is added or lost. At most 1 decomposition + 2 handler calls.
```

**Sample output**

v1: [Cem, Ada, Bora]. v2: [Ada, Bora, Cem]. The controller ends with return v2.

**What did we get?**

The subtask names and the data passed between them became explicit.

### Medium

**Situation**

Reading a document and calculating need different capabilities.

**Prompt**

```text
Input D1="3 packs, 8 notebooks per pack; 5 notebooks handed out". Question: notebooks remaining?
Permitted handlers: extract_quantities(D1) as a separate model call; calculate(expression) as an isolated arithmetic tool.
The decomposer should generate a program that first extracts the numbers and relationships, then builds an expression from the real intermediate result and calculates it. The controller should validate the tool names and the schema; it should allow references only to existing variables.
extract return: {packs:3,per_pack:8,given:5}; calculate input 3*8-5. Carry the real calculation result into the final answer. Each handler once; stop on an error or a missing field.
```

**Sample output**

The program flow is extraction → calculation → answer. The representative result is 19 notebooks.

**What did we get?**

Understanding the text and doing the arithmetic were given to different handlers.

### Hard

**Situation**

A subtask will be reused; the controller must bound the loop.

**Prompt**

```text
Question: What is the total capacity of events A and B?
Sources: D1="A capacity 8"; D2="B capacity 12". Handlers lookup_capacity(event,document), add_numbers(values).
The decomposer should generate a program of two lookups and one add. The controller should store each call with its ID, input, output and source; A's result must not stand in for B's source. If the same input/source pair is requested again, it may use the verified intermediate result.
A program with an unknown handler, a forward reference or more than 4 steps in total should be rejected. If there is no capacity in the source, the add call should not run. On a successful total, finish with the source IDs.
```

**Sample output**

“A: 8 [D1]; B: 12 [D2]; total 20.” With a missing B record, a missing-data notice comes instead of a total.

**What did we get?**

Modularity was tied to a checkable program structure instead of uncontrolled tool calls.

## Where should you stop?

Prompt chaining runs stages defined in advance; Decomposed Prompting highlights the decomposer and reusable task handlers. Writing separate roles is not running handlers. A real call arrangement, variable passing and permission checks are needed.

## Sources

- [Decomposed Prompting: A Modular Approach for Solving Complex Tasks](https://arxiv.org/html/2210.02406) — Khot, Tushar; Trivedi, Harsh; Finlayson, Matthew; Fu, Yao; Richardson, Kyle; Clark, Peter; Sabharwal, Ashish. 2022-10-05; version read 2023-04-11. Defines a decomposer generating prompting programs made of subtask/handler calls, and a controller running them. Evidence level: relevant body sections of the original paper.
