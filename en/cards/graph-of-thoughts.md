# Graph of Thoughts

Work with solution pieces that can merge, instead of a single path.

## What is it?

Graph of Thoughts treats the generated solution pieces as nodes of a graph and the dependencies between them as edges. A controller runs generation, aggregation, scoring and refinement operations. Writing “think like a graph” in a chat does not set up this execution.

## When does it help?

In work where several parts must be processed separately and then combined, or where the same intermediate result must be usable in different branches.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

A single list without repeats will be produced from two short lists.

**Prompt**

```text
A human is the controller; each node is a separate call, and the outputs are kept in a record table. At most 3 calls.
N1 input: "apple, pear, apple". Prompt: Remove duplicates, keep the order of first appearance.
N2 input: "pear, cherry". Same prompt; do not give the N1 output to this call.
N3 input: The real N1 and N2 outputs. Prompt: Merge in the order N1 then N2; remove duplicates.
A human should compare the result with the raw lists. If there is a new word or a missing item, count it as a failure; stop when the budget ends.
```

**Sample output**

N1: “apple, pear”; N2: “pear, cherry”; N3: “apple, pear, cherry”. The edges are N1→N3 and N2→N3.

**What did we get?**

Two separately processed parts met at a single merge point.

### Medium

**Situation**

In an event brief, access and schedule information will be tied to a shared summary.

**Prompt**

```text
In the controller state, the input, output and source ID of each node should be stored. Sources: D1="Start 14:00, end 16:00"; D2="Entrance has a ramp; lift out of order".
Call N1 extracts the schedule from D1. Call N2 extracts access information from D2. N3 produces a 3-point participant note from the real N1+N2.
Check call N4 receives the raw D1/D2 and N3: show the source for each claim; do not present the broken lift as accessible.
The application should block publishing on any unsourced claim. Stop at 4 calls; no publishing tool.
```

**Sample output**

“14:00–16:00 [D1]. There is a ramp at the entrance [D2]. The lift is out of order [D2].” N4 checks that N3 carries only sourced fields.

**What did we get?**

Besides the graph's merge node, a separate check node was also created.

### Hard

**Situation**

When a conflict appears in the merged draft, only the relevant branch will be reprocessed.

**Prompt**

```text
Source A: "Hall 20 people". Source B: "Fire safety capacity 16 people". Source C: "Workshop 90 minutes".
Controller: separate extraction nodes for A/B/C; a merge node; a constraint-check node. Add the source and parent node ID to each record. At most 6 model calls in total.
When the check finds the capacity difference, leave the A/B branch to a human decision; do not regenerate the approved duration from C. If the human says "the operational upper limit is 16", merge this decision in as a new node.
If the budget runs out, report the verified duration so far and the open capacity problem. Without a decision, do not average the capacity or pick the higher one.
```

**Sample output**

“Duration 90 minutes verified [C]. There is a 20/16 split for capacity; an authoritative decision is pending.” After the decision, the new merge is 16 people / 90 minutes.

**What did we get?**

The shared state was preserved; the problematic branch did not restart all the work.

## Where should you stop?

Tree of Thoughts searches branching candidates; Graph of Thoughts additionally allows nodes to merge and be reused. The existence of a graph does not prove correctness. You need a controller, an evaluation criterion, a call budget and stored real outputs.

## Sources

- [Graph of Thoughts: Solving Elaborate Problems with Large Language Models](https://arxiv.org/html/2308.09687) — Besta, Maciej; Blach, Nils; Kubicek, Ales; Gerstenberger, Robert; Podstawski, Michal; Gianinazzi, Lukas; Gajda, Joanna; Lehmann, Tomasz; Niewiadomski, Hubert; Nyczyk, Piotr; Hoefler, Torsten. 2023-08-18; version read 2024-02-06. Defines organizing solution pieces over a graph through generation, aggregation and refinement operations; the example controllers are simple teaching adaptations of the method. Evidence level: relevant body sections of the original paper.
