# ReAct

Choose the next step based on the tool result that actually came back.

## What is it?

ReAct alternates a short decision rationale with actions and observations. The model proposes a tool call; the application runs the tool and carries the real result into the next call. A search result imagined in a chat does not count as an observation.

## When does it help?

For work where you cannot decide all the steps at the start, and the direction changes based on a result from a document or environment.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You want to find out whether a museum is open on Monday.

**Prompt**

```text
User task: Is the fictional City Museum open on Monday?
Application: There is only a read-only museum_hours(name) tool. At most 2 calls; if there is no tool, say so and stop.
Model: Write the required action and a one-sentence reason. Do not say open/closed before the application's result arrives.
Representative tool result: {name:"City Museum", monday:"closed", source:"official hours record", updated:"2026-09-01"}
Next model call: Take the task and this real tool result; answer while stating the record's date, and finish if it is sufficient.
```

**Sample output**

Action: `museum_hours("City Museum")`. After the observation arrives: “In the official hours record dated 1 September, Monday is shown as closed.”

**What did we get?**

The decision did not rest on an observation invented before the tool call.

### Medium

**Situation**

The first document has no application date; a second source becomes necessary.

**Prompt**

```text
Task: Find the application deadline for the fictional exhibition.
The supervisor should run at most 3 read-only document-reading calls. Each round should carry the task, the IDs of the documents read and the quotes to the model.
1. read_document("exhibition-notice") -> "For the date, see the conditions document: exhibition-conditions."
Ask the model for a single next action; do not return to the same document without reason.
2. read_document("exhibition-conditions") -> "Applications close on 20 October 2026 at 17:00."
Model: Write the result with the document ID. If the dates conflict, do not give a definite date; if the budget runs out, report the gap.
```

**Sample output**

The second action is `read_document("exhibition-conditions")`. Result: “20 October 2026, 17:00 — exhibition-conditions.”

**What did we get?**

The first observation determined the second step.

### Hard

**Situation**

A support diagnosis must tell successful and failed queries apart.

**Prompt**

```text
Task: Why is order K42 not showing? There is no permission to write or resend.
Supervisor: At most 3 tool calls. Permitted tools order_read(id), sync_status(id). State: call ID, response status, finding, remaining budget.
order_read("K42") -> {status:"not_found"}
Model: Do not interpret a missing record as a deleted order. Choose the next read-only check.
sync_status("K42") -> {status:"pending", next_retry:"14:30"}
Model: Evaluate this result together with the earlier observation; write the limit of the diagnosis and the follow-up time for the customer. Do not rerun the tool; stop once you have produced a status explanation.
```

**Sample output**

“No record was found in the order lookup; it is waiting in the sync queue. The next automatic retry is at 14:30. There is no evidence that it was deleted.”

**What did we get?**

The failed query and the actual cause were not confused with each other.

## Where should you stop?

ReAct does not create tool access. The supervisor must enforce permissions and the call budget. Unlike a fixed-step prompt chain, the next action is chosen based on the observation. Instead of asking for a dump of internal thinking, a record of decision, action, source and result is enough.

## Sources

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/html/2210.03629) — Yao, Shunyu; Zhao, Jeffrey; Yu, Dian; Du, Nan; Shafran, Izhak; Narasimhan, Karthik; Cao, Yuan. 2022-10-06; version read 2023-03-10. Defines the ReAct mechanism in which decisions, actions and external observations alternate; the examples are simple adaptations written for this collection. Evidence level: relevant body sections of the original paper.
