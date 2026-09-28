# Context compaction

When you shorten a long history, do not lose the decisions and the open tasks.

## What is it?

Context compaction extracts from a conversation or tool history the state needed for the next step. This summary is not an exact backup of the history. If source markers and uncertainties are kept, you can go back to the details.

## When does it help?

When the same decisions keep being forgotten in a long session, or when carrying the whole history into a new call is costly.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will carry the agreed features of a piece of writing into a new chat.

**Prompt**

```text
A human starts this: Turn the history below into a handoff note.
History: At first we said 1000 words. Later I reduced the target to 400 words. The readers are beginners. The tone is plain. No title has been chosen.
Fields: current target, decision no longer valid, unchanged constraint, open question. Do not mix the latest decision with the earlier one.
A human should compare the note with the history; the approved note becomes the first input of the new chat. Do not invent a title; stop when the four fields are complete.
```

**Sample output**

“Target: 400 words. Old decision: 1000 words, no longer valid. Constraint: plain language for beginners. Open: title.”

**What did we get?**

Shortening did not turn the old and new decisions into a single average.

### Medium

**Situation**

Most of the tool logs are repetitive; one piece of error information matters.

**Prompt**

```text
The supervisor should give the logs to the summarization call:
L1 test_a passed. L2 test_a passed again. L3 test_b timeout; result unknown. L4 user: only parser.js may change.
Handoff note: permission, verified result, uncertain result, next permitted step, source lines. Do not write the timeout as a failed test result or as passed.
A human should check L3 and L4 in particular. The new call should get read-only access to L1-L4 when needed, along with the approved note. Old logs should not be deleted before the summary is verified.
```

**Sample output**

“Permission parser.js [L4]. test_a passed [L1–L2]. test_b uncertain due to timeout [L3]. Next step: examine the relevant error log.”

**What did we get?**

Repetitions were reduced; the uncertainty and the file limit were preserved.

### Hard

**Situation**

In a project handoff, two notes contradict each other.

**Prompt**

```text
Input: N1, 09:00: "Delivery Friday; draft ready." N2, 11:00: "Delivery Monday; visual not approved yet." Who made the decision is not recorded.
The supervisor should carry a state summary of at most 180 words into the new context; it should keep the original N1/N2 records.
Model: Separate the fields that are clearly current, the conflicts, and the one clarification to ask the decision owner for. Do not automatically treat the later-dated record as authoritative.
Handoff check: the delivery date must remain unconfirmed. The new agent may only review the status of the draft and the visual; it cannot promise delivery. End the compaction once the conflict has been handed over.
```

**Sample output**

“Draft ready [N1]; visual not approved [N2]. The delivery day is contradictory and there is no authoritative decision record. Confirmation of Friday/Monday is needed from the decision owner.”

**What did we get?**

Compaction did not silently turn missing authority information into a decision.

## Where should you stop?

A summary can also be wrong. Check critical numbers, permission limits and completion criteria against the source. Just because context capacity has grown, it is not safe to assume information at every position of a long text will be used equally; results from old experiments cannot be carried directly to every new model.

## Sources

- [Effective context engineering for AI agents \ Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Anthropic. 2025-09-29. Discusses the compaction approach, preserving important state and the risk of over-compression. Evidence level: page body.
- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/html/2307.03172) — Liu, Nelson F.; Lin, Kevin; Hewitt, John; Paranjape, Ashwin; Bevilacqua, Michele; Petroni, Fabio; Liang, Percy. 2023-07-06; version read 2023-11-20. Shows that, in the models and tasks studied, where relevant information sits in the context can affect performance; does not prove that summarization will succeed in every case. Evidence level: relevant body sections of the original paper.
