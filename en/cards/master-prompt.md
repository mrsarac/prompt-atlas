# Modular master prompt

Keep a project's reusable working rules in one document.

## What is it?

A master prompt is a document that brings together the goal, limits and delivery criteria you do not want to rewrite for every task. The day's job can change; the shared rules stay separate. You have to actually add the document to the call: the file existing does not show that the model read it.

Here we use this name for a practical instruction asset. A meta prompt produces another prompt; RUNE offers a specific layer structure. A master prompt can be prepared in either of these ways, but it does not require either.

## When does it help?

It is useful when you run writing, coding or research jobs one after another in the same project. Keep the shared rules short; give the changing task data separately.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

The registration condition must be kept every time in a workshop's announcements.

**Prompt**

```text
SHARED RULES v1
Write in clear English. Registration is confirmed by the confirmation email. If no date was given, do not add one. Output at most two sentences.
TODAY'S TASK
Write a call to apply for the drawing workshop through the form. Capacity 20 people.
```

**Sample output**

You can apply for the 20-person drawing workshop by filling in the form. Your place is confirmed when the confirmation email arrives.

**What did we get?**

The fixed registration rule was carried into the individual announcement. In the next task, adding the shared rules to the call is also your responsibility.

### Medium

**Situation**

A shared rule and the day's request conflict.

**Prompt**

```text
SHARED RULES v2
Do not go beyond the information given. If a date is uncertain, keep the uncertainty. In a conflict, warn me before publishing a definite date.
TASK
The draft says “The workshop is on Saturday”; the organizer's latest note says “The day is not final yet.” Prepare the social media announcement; do not use the day in the draft as if it were definite information.
```

**Sample output**

The date sources conflict. Undated draft: “The date for the workshop has not been confirmed yet.” The word Saturday should not be used until the day is final.

**What did we get?**

The document described a conflict behavior. The actual publishing and the date confirmation stayed with a human.

### Hard

**Situation**

In a two-stage writing job, the same file limit can get lost in the next call.

**Prompt**

```text
A handoff outline for a human coordinator:
Shared contract v3: only draft.md may change; source.md and archive.md are read-only; no external publishing.
Stage 1 call: Add this contract and the source “Applications are taken through the form; a place is confirmed by the confirmation email.” Propose two sentences for draft.md.
Stage 2 call: Add the same contract v3, the same source and the text from the first call again. Ask only for a language fix that keeps the meaning.
Record the contract version passed on at each handoff. At most two calls. Real writing tools must be restricted to this file list; if the change goes outside the list, do not accept the work.
```

**Sample output**

Handoff package: contract v3 + source sentence + draft text. The expected delivery of the second stage is only the draft.md text; a change to archive.md is not accepted.

**What did we get?**

It is clear with which data the master prompt is carried into the next call. The coordinator does not accept a “done” message without checking the real file diffs and permissions.

## Where should you stop?

A longer document is not a better document. Rules that have gone out of date and sections that say different things about the same area produce conflicts. API message priority depends on the actual role the application uses. Writing “highest authority” into a text does not grant technical access.

## Sources

- [Master Prompts and System Prompts: The ChatGPT-5 Growth Blueprint](https://www.danmartell.com/master-prompts-system-prompts-and-custom-gpts/) — Dan Martell. 2026-02-23; version read 2026-02-23. An example of practitioner use of the names master prompt and system prompt; not the single academic origin of this document or evidence of superiority. Evidence level: page body.
- [Prompt engineering | OpenAI API](https://developers.openai.com/api/docs/guides/prompt-engineering?api-mode=responses) — OpenAI. Publication date not verified. Provides grounding for the distinction between reusable instructions, context and message roles. Evidence level: page body.
