# Structured external notes

Keep the state that needs to be remembered outside the chat, in a note with sources.

## What is it?

Structured external notes are a persistent working record that an agent or a human can read in the next session. They do not change the model's weights. Writing, storing and reading back the note must actually be done by the application or a human.

## When does it help?

In research, content or code work spread over days, when decisions, open questions and evidence need to outlive the session.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will leave a short note for the next writing session.

**Prompt**

```text
A human starts this. Today's state: topic bicycle maintenance; target beginners; the chain cleaning section is written; the brakes section is missing.
The model should produce a Markdown note with these fields: goal, completed, open task, unverified information.
A human should actually save the note as project-note.md and open it again to check it. In the next session, they should add the file's content to the new call.
New call: Propose only the open task; if you have not seen the file, do not say you have. Stop when the note and the next step are ready.
```

**Sample output**

“Completed: chain cleaning draft. Open: brakes section. Next step: decide the scope and sources for this section.”

**What did we get?**

Instead of saying “remember this”, a record that can be read again was created.

### Medium

**Situation**

You do not want the source and the interpretation to get mixed up in a research note.

**Prompt**

```text
Application: notes_read and notes_write only in this project; at most one read and one write.
Existing record: claim C1="The museum is closed on Mondays", source D1="Official opening schedule, 1 September", status=verified_against_D1.
New information: The user said "It might be different during the holiday"; no source given.
Model: Do not delete C1. Add the new line as assumption A1, with the user's statement as the source and the status unverified. The application should validate the record schema, save it and return the write result. Say saved only after a successful write response; then stop.
```

**Sample output**

“A1: Hours may change during the holiday; not verified. C1 was kept as the record for the usual Monday hours.”

**What did we get?**

The new possibility was not written over the sourced finding.

### Hard

**Situation**

Two sessions may update the same decision record.

**Prompt**

```text
The supervisor should store versioned notes. v3: target 400 words; open task source check.
The agent read v3. In the meantime, a human changed the target to 600 in v4. The agent's proposal: source check completed; support D7.
Write rule: an update with expected_version=3 should be rejected; v4 should be read again. The model should merge only its own evidenced change into v4 and keep the 600 target. If D7 is not accessible, "completed" should not be added.
At most one re-read/merge; if it conflicts again, leave it to human review. Finish if the application returns an approved v5.
```

**Sample output**

“v5: target 600 words; source check completed based on D7.” If there is no access to the source, it stays as an open task.

**What did we get?**

The note became a checked record instead of a memory where the last writer overwrites all history.

## Where should you stop?

A persistent note does not mean persistent accuracy. Dates, sources, scope and decisions that are no longer valid should be visible. Compaction shrinks the current context; an external note stores the state to be retrieved in later sessions. Do not make sensitive data persistent unnecessarily.

## Sources

- [Effective context engineering for AI agents \ Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Anthropic. 2025-09-29. Describes structured note-taking and bringing notes kept outside the session back into context; the version-conflict example is an application design of this principle. Evidence level: page body.
