# Self-Debug

Have the generated code explained, check how it runs, fix the faulty step.

## What is it?

Self-Debug is the model revisiting a program it generated itself using information such as an explanation and execution feedback. In Rubber Duck, a human explains their own code; here, the side that reviews and fixes is the model.

## When does it help?

When you can test the behavior of a code candidate with sample inputs and check small revisions.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

The code behaves wrongly at a boundary value.

**Prompt**

```text
Task: 500 TL and above ships free, below that 50 TL. The model's code candidate: total > 500 ? 0 : 50.
A human is the controller. The first review call should briefly explain what the code does for 499/500/501; it should not present this as a real test result.
Then the application should actually run these inputs in an isolated executor; it should carry the stdout and the expected values 50/0/0 into the fix call.
The model should give only the smallest revision. Stop after one retest; if there is no execution tool, stay at the level of a proposal.
```

**Sample output**

Representative first result 50/50/0; the revision becomes `>=`. The expected new result is 50/0/0.

**What did we get?**

The code explanation was tied to a check of real behavior and a small revision.

### Medium

**Situation**

The program passes on a normal example but fails on an empty list.

**Prompt**

```text
Task: Return None for an empty list, and the largest number for other lists.
Code candidate: def largest(xs): return max(xs)
The supervisor should run the tests in isolation: [2,5] -> 5; [-5,-2] -> -2; [] -> None. Give the real error message to the model.
The review call should connect the error to the code's behavior; it should not do a general rewrite. The revision call should add only the empty-list condition. Run the same tests again; at most two test rounds. Do not declare the code correct before the results pass.
```

**Sample output**

Representative error: `ValueError` on the empty list; candidate fix: `return max(xs) if xs else None`.

**What did we get?**

A successful ordinary example did not turn into an assumption that the empty input is also correct.

### Hard

**Situation**

Even if the explanation looks right, the test coverage may be insufficient.

**Prompt**

```text
Task: Remove duplicates from a list, keeping the order of first appearance. Code candidate: return list(set(xs)).
The model should briefly explain the code's ordering guarantee. The supervisor should not rely on an output that happens to be correct by chance; it should also check the task contract.
Test data: ["B","A","B","C"] -> ["B","A","C"]; [] -> []; ["A","A"] -> ["A"]. Carry the isolated execution results and the order requirement into the revision call.
The model should propose a solution that explicitly preserves order; after two test rounds, report any remaining uncertainty. Do not use only its own explanation as evidence.
```

**Sample output**

Candidate revision: for hashable items, `list(dict.fromkeys(xs))`. The order and the hashable-input limit are stated separately.

**What did we get?**

Debugging checked the contract, beyond a test passing by chance.

## Where should you stop?

The original Self-Debug work has explanation and execution-feedback arrangements depending on the task; it cannot be said that every task needs human correctness labels. This card shows an adaptation with an explicit test oracle. The model's own critique does not always fix things; real tests and correct requirements are still needed.

## Sources

- [Teaching Large Language Models to Self-Debug](https://arxiv.org/html/2304.05128) — Chen, Xinyun; Lin, Maxwell; Schärli, Nathanael; Zhou, Denny. 2023-04-11; version read 2023-10-05. Studies a model reviewing and fixing a program it generated through natural-language explanation and execution results; it is not the learning effect of a human's Rubber Duck practice. Evidence level: relevant body sections of the original paper.
- [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/html/2310.01798) — Huang, Jie; Chen, Xinyun; Mishra, Swaroop; Zheng, Huaixiu Steven; Yu, Adams Wei; Song, Xinying; Zhou, Denny. 2023-10-03; version read 2024-03-14. Presents task/model findings that show the limits of self-correction without external feedback; this does not mean every self-correction arrangement fails. Evidence level: relevant body sections of the original paper.
