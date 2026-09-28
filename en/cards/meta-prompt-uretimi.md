# Meta prompt that writes prompts

Ask the model not to do the job, but to write the instruction that will be used for that job.

## What is it?

In general usage, a meta prompt is a request that produces or edits another prompt. You give the goal and the limits; the model produces a usable instruction draft. You check the quality of that draft separately on the target task.

Having a prompt written once is not the whole of optimization processes such as APE or OPRO, which select candidates through measurement. Here we do not invent an automatic success score.

## When does it help?

Use it when you will repeat the same job, or when you want to turn a scattered request into a clear task text. Do not let the model decide a missing requirement on your behalf.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You want a short, reusable instruction for workshop announcements.

**Prompt**

```text
Do not write the announcement itself; create the prompt that will have the announcement written.
Requirements: English, two sentences, only the given information, the form is an application; a place is confirmed by the confirmation email. No missing date is added.
Sample usage data: Drawing workshop, 20 people, date not yet set.
In the output, give the prompt together with this sample data; then stop.
```

**Sample output**

Representative prompt: “Write two English sentences for a 20-person drawing workshop. State that the form is an application and that a place is confirmed by the confirmation email. The date is not set; do not add one.”

**What did we get?**

There is an instruction ready to use directly. How the model will respond to this instruction has not been tested yet.

### Medium

**Situation**

An old prompt makes the model add details that are not in the source.

**Prompt**

```text
Old prompt: “Promote this event in an exciting and detailed way.”
Problem: From the source “The workshop is free”, a date and material support are being invented.
Rewrite the prompt. Keep promotion as the goal; add the conditions to use only the source information and to state missing fields. Let the sample source be “The workshop is free.” Output: the new full prompt and the single reason for the change. Do not produce the promotional text now.
```

**Sample output**

New prompt: “Source: The workshop is free. Write a short promotion with this information. No date, venue or material support has been given; do not add them. If needed, say that these fields have not been specified yet.”

**What did we get?**

The error the instruction targets is clear. The effect of the fix should then be checked by getting output on the same source.

### Hard

**Situation**

Two prompt versions differ in scope; combining them must not increase permissions.

**Prompt**

```text
As a prompt designer, combine these two texts; do not carry out the task.
A: “Fix the language only in draft.md; source.md is read-only.”
B: “Edit all documents; publish when the work is done.”
Valid user limit: only draft.md, no publishing. Goal: a language fix that keeps the source meaning.
Write the new prompt in full; state the removed conflicts in two short bullet points. Do not read/write files or call tools.
```

**Sample output**

New prompt: “Keeping the source meaning, propose a language fix only for draft.md. source.md is read-only. Do not change other documents; do not publish. In the result, report the changed phrases and any remaining uncertainties.”

**What did we get?**

The combination did not expand permissions. The instruction text should still be backed by real file permissions and an output check.

## Where should you stop?

The word meta carries different meanings in different research. Meta-Prompting with expert calls is an orchestration architecture; structural Meta Prompting organizes the form of a task. Producing a prompt does not automatically make it the same method as these.

## Sources

- [The Prompt Report: A Systematic Survey of Prompt Engineering Techniques](https://arxiv.org/html/2406.06608v6) — Schulhoff, Sander; Ilie, Michael; Balepur, Nishant; Kahadze, Konstantine; Liu, Amanda; Si, Chenglei; Li, Yinheng; Gupta, Aayush; Han, HyoJung; Schulhoff, Sevien; Dulepet, Pranav Sandeep; Vidyadhara, Saurav; Ki, Dayeon; Agrawal, Sweta; Pham, Chau; Kroiz, Gerson; Li, Feileen; Tao, Hudson; Srivastava, Ashay; Da Costa, Hevander; Gupta, Saloni; Rogers, Megan L.; Goncearenco, Inna; Sarli, Giuseppe; Galynker, Igor; Peskoff, Denis; Carpuat, Marine; White, Jules; Anadkat, Shyamal; Hoyle, Alexander; Resnik, Philip. 2024-06-06; version read 2025-02-26. A secondary survey that classifies the scope of the terms meta prompting and prompt engineering; not, on its own, evidence of an original effect. Evidence level: relevant body sections of the original paper.
- [Large Language Models are Human-Level Prompt Engineers](https://arxiv.org/html/2211.01910) — Zhou, Yongchao; Muresanu, Andrei Ioan; Han, Ziwen; Paster, Keiran; Pitis, Silviu; Chan, Harris; Ba, Jimmy. 2022-11-03; version read 2023-03-10. Provides a primary example of a model generating candidate instructions; APE additionally performs real evaluation and selection. Evidence level: relevant body sections of the original paper.
- [Master Prompts and System Prompts: The ChatGPT-5 Growth Blueprint](https://www.danmartell.com/master-prompts-system-prompts-and-custom-gpts/) — Dan Martell. 2026-02-23; version read 2026-02-23. Shows how reusable master/system prompts are used in practitioner language. Evidence level: page body.
