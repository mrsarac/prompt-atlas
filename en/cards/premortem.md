# Premortem

Assume the work has failed; look for concrete causes that could lead to it.

## What is it?

A premortem is treating a plan, before carrying it out, as if it had failed in the future, and writing down the possible causes. It is not a forecast or an account of events that happened, but an exercise in finding the plan's weak points.

## When does it help?

When the plan looks ready and it gets harder for team members to voice their reservations, or when you want to see preventable problems early.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will check the plan for an eight-person workshop.

**Prompt**

```text
Plan: 12 October 14:00, 8 people, materials included. The venue is not yet decided.
Fictional assumption: The workshop did not go well. Write at most three possible causes connected to the current plan. For each cause, propose an early sign and a small precaution. Do not narrate it as if it happened; do not invent budgets or human behavior that are not in the source.
```

**Sample output**

“If the venue is announced late, participants may not be able to prepare. Early sign: the address still being unclear on announcement day. Precaution: setting a person responsible and a date for the address decision.”

**What did we get?**

A general worry was tied to an observable sign and a concrete plan.

### Medium

**Situation**

Different team members see the same risk differently.

**Prompt**

```text
Plan: A new usage guide will be published on Friday. The draft is ready; no technical check has been done; one editor is on leave.
Premortem round: First each person should independently write their own three causes of failure. Then the model should group the real notes into similar themes; it should not delete a concrete cause held by a minority.
Sample input A="A wrong command misleads the reader", B="Nobody is left for the final check", C="Code overflows on mobile".
For each theme, separate the available evidence, the check step, and the area where a decision on responsibility is needed. Do not publish or assign tasks.
```

**Sample output**

“Technical accuracy, checking capacity and mobile readability are three separate themes. For each, the relevant check is open; the model did not accept responsibility on anyone's behalf.”

**What did we get?**

Independent human concerns did not dissolve into a single dominant view.

### Hard

**Situation**

Taking precautions against every possibility can bloat the plan unnecessarily.

**Prompt**

```text
Plan: Deliver a local draft of a small announcement. Permission: Checking the text and sources; no publishing, new features or system changes.
Under the assumption of failure, generate at most five causes. Then keep only those that directly affect the requested delivery; leave poorly supported, out-of-scope scenarios in a separate short note.
For each cause kept, write a provable check and a stop criterion. Once the checks pass, do not open a new risk round. Do not produce real disaster forecasts or permission to expand the scope.
```

**Sample output**

“A missing date, an unsupported claim and a broken internal link are direct checks. An unrelated system overhaul is not part of this delivery.”

**What did we get?**

The premortem stayed within the limits of the work instead of producing an endless list of precautions.

## Where should you stop?

A premortem does not tell the future; probability ratios cannot be calculated without data. A red team can test a specific output or system with adversarial examples; a premortem generates causes from the assumption that the plan has failed. A proposed precaution is not permission to carry it out.

## Sources

- [Pre-mortem Method of Risk Assessment](https://www.gary-klein.com/premortem) — Gary Klein. 2007 (method date stated; page publication date unknown). The primary practitioner source describing Gary Klein's premortem approach; the page's publication date is not verified, and the method's 2007 association is not turned into a page date. Evidence level: page body.
