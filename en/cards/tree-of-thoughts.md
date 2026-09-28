# Tree of Thoughts

Open more than one solution path; evaluate the intermediate states and go back when needed.

## What is it?

Tree of Thoughts organizes solving as a search problem. The coordinator generates candidate steps, evaluates the state each candidate reaches, and continues the promising branches. When it hits a dead end, it can return to an earlier state.

In the outlines below, the model that generates candidates and the coordinator that stores and selects states do separate jobs. Drawing a tree in a single response is not running this search.

## When does it help?

It is useful for work where intermediate candidates can be tested, such as ordering, constrained design or puzzles. First decide how the state will be stored, the evaluation rule and the call limit.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

Tasks A and B need to be done; A must come before B.

**Prompt**

```text
A human coordinator keeps the starting state as []. Candidate call: “Remaining tasks A,B. Give two candidates for the first step.”
Evaluate each candidate separately: if B comes first, eliminate it for violating the prerequisite; if A comes first, the state is [A], remaining [B].
New call: “State [A], remaining B. Give the next step that keeps the prerequisites.”
Check the full order for A coming before B. At most two generation calls; if no valid branch remains, stop.
```

**Sample output**

Candidates [A] and [B]. [B] is eliminated; [A] → [A,B]. The final order is valid.

**What did we get?**

Generating candidates, eliminating and continuing became separate steps. A job this small is easier to solve by hand; the example shows the search mechanism.

### Medium

**Situation**

Three tasks will be done by one person; the deadlines differ.

**Prompt**

```text
Start 09:00. A takes 30 minutes, B 20 minutes, C 10 minutes. B must be finished by 09:30 at the latest. C can only be done after A.
As the state, the coordinator stores the completed order, the time and the remaining tasks. From each model call, it asks for at most two suitable next steps.
The evaluator adds up the time; it eliminates a branch on a prerequisite or deadline violation. It keeps at most two branches open; at a dead end, it returns to the previous state. At most six generation calls. It checks the full order against the timeline.
```

**Sample output**

After [A] the time is 09:30; B can no longer finish by 09:30, so the branch is eliminated. [B] 09:20 → [B,A] 09:50 → [B,A,C] 10:00.

**What did we get?**

We saw that an early decision made a later task impossible. The chosen order can be checked against the durations and prerequisites.

### Hard

**Situation**

You will make 24 using each of the numbers 3, 3, 8, 8 exactly once.

**Prompt**

```text
The coordinator keeps the numeric expressions and the identities of the numbers used as the state. Start [3a,3b,8a,8b].
In each call, the model proposes at most three candidates that combine two numbers with one operation. The evaluator does exact fraction arithmetic; it eliminates division by zero and reused numbers. Keep at most three branches that look good; go back on a failed branch.
At most 20 candidate expansions; if no candidates remain, say not found. Accept only an expression that uses every number once and gives exactly 24. A calculator is needed; the model saying “24” is not enough.
```

**Sample output**

Representative successful branch: 8b/3b → 3a−8b/3b → 8a/(3a−8b/3b)=24. Numbers used: two 3s and two 8s.

**What did we get?**

There is a solution candidate and an exact verification criterion. No search run was performed for this write-up; only the arithmetic of the given expression can be checked separately.

## Where should you stop?

The evaluator can rate a wrong branch as good; the cost of the search grows quickly. Running out of budget does not mean there is no solution. Graph of Thoughts also allows branches to merge. Self-Consistency, by contrast, counts completed independent answers; it does not search intermediate branches.

## Sources

- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/html/2305.10601) — Yao, Shunyu; Yu, Dian; Zhao, Jeffrey; Shafran, Izhak; Griffiths, Thomas L.; Cao, Yuan; Narasimhan, Karthik. 2023-05-17; version read 2023-12-03. Defines the arrangement of candidate generation, evaluation and progress through search such as BFS/DFS; the Game of 24, writing and puzzle conditions are not a general planning guarantee. Evidence level: relevant body sections of the original paper.
