# Bounded execution and permissions

Make the permissions, the budget and the stop condition visible at the start of the job.

## What is it?

Bounded agent work defines which steps the model cannot choose as well as which steps it can. The prompt describes the limits; the application enforces them with an allowlist, an operation budget and an approval gate.

## When does it help?

In work that uses files, external services or tools; especially when reading, local changes and external publishing must be kept apart.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You want an assistant to summarize three text files.

**Prompt**

```text
Task: Summarize the contents a.txt="Setup takes 5 minutes", b.txt="Cancellation is free", c.txt="Support on weekdays".
The supervisor should give read-only access to these three files only. Tool budget 3; network and write tools are disabled.
Add the file name and returned text of each call to the state record. The model should produce a summary of at most three points.
If a file is missing, name it; do not widen the search area. Stop when the three files have been read or the budget runs out.
```

**Sample output**

“Setup takes 5 minutes. Cancellation is free. Support on weekdays.” For a missing file, it would additionally say “b.txt could not be read”.

**What did we get?**

For a small task, the access area also stayed small.

### Medium

**Situation**

Only the shipping threshold is to be changed in the code.

**Prompt**

```text
Initiator: Developer. Permitted file shipping.js; rule: 500 TL and above ships free, below that 50 TL. Current code total > 500 ? 0 : 50.
Supervisor: A local patch to this file only; other files, dependencies, commits and external service tools are disabled. At most 1 patch and 1 relevant test command.
The model should give the patch proposal; the application should check the file path and the scope of the diff. Check inputs 499,500,501; expected 50,0,0.
The test result is passed into the state record. If it fails, report the result; do not open a new scope. On success, stop with the diff and the check result.
```

**Sample output**

Proposal: `>=` instead of `>`. “If the three relevant boundary checks give the expected values, the local change is complete.” This sentence is not a claim that a real test was run.

**What did we get?**

Finishing was not left to the model's “let me improve it a bit more” decision.

### Hard

**Situation**

The agent can create an announcement draft but cannot publish it.

**Prompt**

```text
Task: Prepare an announcement draft from the note "Workshop 12 October, 14:00; venue not yet set".
Application permissions: read_note and save_local_draft. No publish or send_message. At most 4 tool calls, 2 corrections.
State: user scope, source note, draft path, verified fields, open gaps, remaining calls.
The agent should not invent the missing information. It should mark the venue information as missing and save the draft locally. If the user says "continue", do not treat that as permission to publish; complete the remaining tasks that are already permitted.
Stop: when the draft and the list of missing information are ready. Publishing needs a separate permission aimed at the specific content and destination.
```

**Sample output**

“The local draft is ready. There is no venue information yet; the text states this explicitly. Nothing was sent externally.”

**What did we get?**

Continuing the work and expanding the scope of permission remained separate decisions.

## Where should you stop?

Spreading approval questions over every small step can also break the workflow. Work continues within permissions already granted; a new side effect needs a separate boundary. A prompt alone is not a firewall.

## Sources

- [Building Effective AI Agents \ Anthropic](https://www.anthropic.com/engineering/building-effective-agents) — Anthropic. 2024-12-19. Explains the importance of stop conditions, feedback and human checkpoints in agents. Evidence level: page body.
- [Safety in building agents | OpenAI API](https://developers.openai.com/api/docs/guides/agent-builder-safety) — OpenAI. Publication date not verified. Describes application-layer measures such as separating untrusted input and tool approvals; the recommendations in the product guide are not a universal guarantee. Evidence level: page body.
