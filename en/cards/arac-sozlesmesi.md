# Tool and result contract

Define what comes back from a tool as carefully as what goes into it.

## What is it?

A tool contract is what the function does, the inputs it accepts, its side effects and its result format. The model chooses the appropriate call; the application validates the input and runs the tool. A well-written tool description does not bring a nonexistent permission into being.

## When does it help?

In applications where similar-looking tools get confused, errors are read as successes, or the result of an operation has to be confirmed.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You want an agent to read product stock information.

**Prompt**

```text
Application contract: stock_read(sku: string), read-only. Output: {status:"ok", sku, available: integer, checked_at} or {status:"not_found", sku}. Negative stock and an empty sku are rejected.
User: Is the blue notebook D7 available?
Model: Propose only the call stock_read("D7"). The application should validate the schema and run it.
Representative return: {status:"ok", sku:"D7", available:3, checked_at:"10:00"}
Give this return unchanged to the next call. The model should report the status in one sentence; it should not reserve or buy anything. Stop after one read.
```

**Sample output**

“In the 10:00 check, 3 units of D7 are shown in stock.”

**What did we get?**

It was kept clear that a stock query and a reservation are different jobs.

### Medium

**Situation**

A search result can be empty; that must not be confused with a network error.

**Prompt**

```text
Supervisor: search_docs(query, limit), limit 1..5. The response is either {status:"ok", hits:[{id,title,excerpt}]} or {status:"error", code, retryable}.
Task: Find a document about the return period. First call search_docs("return period", 3).
Representative return: {status:"error", code:"timeout", retryable:true}.
Model: Do not say "no documents". The supervisor should repeat the same call at most once; if the second result is {status:"ok",hits:[]}, say only that there was no match in this search. Pass the status and call count to the next model; stop at 2 calls.
```

**Sample output**

“The first request timed out. The repeated search completed; no match was found for this query.”

**What did we get?**

Absence of data and a technical error were kept apart.

### Hard

**Situation**

A draft record with side effects must not be created twice on a repeated call.

**Prompt**

```text
This is an application design example; do not send a real record.
Permission: Draft creation only; no publishing. For create_draft(title, body, idempotency_key), the application generates the key and stores it persistently.
Input: title="Workshop", body="12 October, 14:00", key="job-42".
Supervisor: After a human approves this content, validate the schema and run a single call. If the connection drops, do not generate a new key; query the result with the same key/use the provider's documented retry behavior.
Expected return: {status:"created" or "existing", draft_id:"D42", published:false}.
Model: Using draft_id, report only the draft status. If the result is uncertain, do not say success; leave it to human review and stop.
```

**Sample output**

“Draft D42 exists; it has not been published.” When the connection is uncertain: “The record status could not be verified; no second draft was created.”

**What did we get?**

Besides the format, the contract also covered retry and side-effect behavior.

## Where should you stop?

Guarantees such as idempotency come from the real server implementation, not from the prompt. Asking for JSON is not enforcing a strict schema. Tool names, permission checks, error types and measurable tests should be considered together.

## Sources

- [Writing effective tools for AI agents—using AI agents \ Anthropic](https://www.anthropic.com/engineering/writing-tools-for-agents) — Anthropic. 2025-09-11. Supports the design of tool descriptions, meaningful responses and evaluation; the idempotency contract in the example is an adaptation of application design, not a ready-made API from the source. Evidence level: page body.
