# Alternative approaches

Put other paths next to the first solution; compare them with the same criteria.

## What is it?

Alternative Approaches is a pattern that generates different ways of doing a job and compares their pros and cons. The options need to be different courses of action, not different names. The choice depends on the user's goals and constraints.

## When does it help?

When you do not want to commit early to the first tool or solution that comes to mind.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will announce the workshop time to readers.

**Prompt**

```text
Task: Site visitors should find the workshop time easily. Information: 12 October 14:00. The site is small; maintenance time is 1 hour a week.
Propose three different paths: a prominent field on the existing page, a separate event page, a Q&A tool. For each, compare the setup effort, maintenance effort and the reader's number of steps qualitatively. Do not invent unmeasured times/numbers. Give a conditional recommendation based on the current constraint.
```

**Sample output**

“A prominent time field on the existing page is the candidate needing the least new maintenance. A separate page may be useful for sharing. A Q&A tool adds extra maintenance for this single piece of information.”

**What did we get?**

A feature request was compared through different courses of action.

### Medium

**Situation**

A text summary must be prepared without sharing the data.

**Prompt**

```text
Goal: Prepare an internal summary of customer notes. Hard constraint: Data cannot be transferred to an external service. First filter the options by this constraint, then compare them by effort and the possibility of checking.
Consider at least three different paths: a human's local summary, a locally run tool approved by the organization, an external API. Do not assume the local tool is actually installed or approved.
Write down the unsuitable option with the reason it was eliminated; for the remaining ones, state the missing information. Do not install tools, transfer data or open services.
```

**Sample output**

“The external API does not meet the current data constraint. A human summary is feasible; the local tool needs confirmation that it exists and is approved by the organization.”

**What did we get?**

Generating alternatives did not mean carrying out an option outside the permissions.

### Hard

**Situation**

One option is strong on speed, the other on accuracy checks.

**Prompt**

```text
Job: Update 100 product descriptions. Data: The source fields are in a well-structured CSV; measurements are missing for some products. The user has not chosen an order of priority yet.
Generate and compare options: fully by hand; automatic template drafts + human check; model drafts + field validator + human check.
For each path, explain how missing measurements, claims outside the source and repetitive workload will be handled. Do not give unmeasured success scores. At the end, ask the single question that would change the choice between speed/accuracy/maintenance; do not start a bulk update.
```

**Sample output**

“For well-structured fields, the template is a strong candidate; the model can add variety in wording but needs field validation. Missing measurements should stay open on every path.”

**What did we get?**

The comparison was made not only by tool names, but by error and maintenance behavior.

## Where should you stop?

Increasing the number of alternatives alone does not bring a good decision. Three rewrites of the same approach are not variety. Cognitive Verifier gathers additional information; this pattern compares different paths to the existing goal. The source is a pattern definition, not a measurement of superiority.

## Sources

- [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT](https://arxiv.org/html/2302.11382) — White, Jules; Fu, Quchen; Hays, Sam; Sandborn, Michael; Olea, Carlos; Gilbert, Henry; Elnashar, Ashraf; Spencer-Smith, Jesse; Schmidt, Douglas C.. 2023-02-21. Defines, in the Alternative Approaches pattern, presenting alternative paths and their pros/cons; does not determine which option is better in every case. Evidence level: relevant body sections of the original paper.
