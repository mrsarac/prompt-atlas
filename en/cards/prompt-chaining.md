# Prompt chaining

Split a job into small calls whose output is checked.

## What is it?

Prompt chaining gives predefined tasks to separate model calls in sequence. The output of one step becomes the input of the next. A check at each handoff prevents a wrong intermediate result from being carried through the whole chain.

## When does it help?

In repeated work where stages such as extraction, drafting and formatting are clearly separated.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You are preparing a workshop announcement in two steps.

**Prompt**

```text
Initiator: A human; two separate chat calls with a human check in between.
Call 1: From this note, extract only the definite information: "Drawing workshop, 12 October, 14:00, 8 people. Venue to be announced later." Write the fields date, time, capacity, venue.
Check: Confirm that the four fields match the source; if the venue is unknown, keep it as empty information.
Call 2: Using the checked fields, write a two-sentence announcement. Do not add a new venue, fee or registration link. Finish if the final text keeps the four fields.
```

**Sample output**

Intermediate output: “12 October; 14:00; 8 people; venue not announced.” Final output: “The drawing workshop will take place on 12 October at 14:00 with 8 places. The venue will be announced later.”

**What did we get?**

The information stayed fixed while the writing style changed.

### Medium

**Situation**

You are turning three customer reviews into an anonymous summary.

**Prompt**

```text
The application should run 3 separate calls; carry only the previous approved output.
Input: "Ada: Setup is easy." "Bora: Setup is easy but the text is small." "Cem: The text is small."
1. Remove the names; give each review the ID y1, y2, y3. Human check: if a name remains, stop.
2. From the anonymous reviews, extract themes and the IDs of the supporting reviews. Every ID must exist; if not, try one correction, then stop.
3. From the theme list, write a two-point product summary. Do not add causes beyond frequency, or generalizations to all customers.
```

**Sample output**

“Easy setup: y1, y2. Small text: y2, y3.” Then: “Two of the three reviews mention easy setup, and two mention small text.”

**What did we get?**

Each stage did a different job; personal data did not reach the final writing call.

### Hard

**Situation**

A release draft will be produced from document changes, but if there is a conflict, the chain must stop.

**Prompt**

```text
Supervisor state object: documents, extracted_changes, conflicts, draft. At most 4 model calls; no publishing tool.
Input A: "v2: Export to CSV and JSON." Input B: "v2: Only CSV is supported."
1. Extract each claim with its A/B ID.
2. Check for disagreement about the same feature. Do not assume either source is authoritative.
Handoff gate: if conflicts is not empty, do not run the writing call. Show the human only which information needs to be chosen.
If the human separately reports that source B is valid, add this decision to the state record; in call 3, write the release draft only from the approved information. Stop at draft generation.
```

**Sample output**

“JSON support is contradictory: A says yes, B says no. The draft stage was not entered before the authoritative record was determined.”

**What did we get?**

Instead of a fast chain, we got a checkable handoff.

## Where should you stop?

Opening a separate call for every paragraph may be unnecessary. The value of the chain lies in dividing the work and checking the handoffs. ReAct chooses its path based on observations; in this method the path is known in advance. Keeping calls separate does not, on its own, provide independent verification.

## Sources

- [Building Effective AI Agents \ Anthropic](https://www.anthropic.com/engineering/building-effective-agents) — Anthropic. 2024-12-19. Explains the prompt chaining pattern of splitting work into predefined subtasks checked through intermediate gates; a provider engineering guide. Evidence level: page body.
