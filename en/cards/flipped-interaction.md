# Flipped Interaction

Before preparing the answer, let the model ask for the missing information.

## What is it?

Flipped Interaction hands the turn of asking questions to the model. The user states the goal and the limits; the model gathers the information needed to complete the task. The questions are not the goal; they are the way to reach enough information.

## When does it help?

When you roughly know what you want but do not know which details are needed for a correct brief.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

A workshop announcement is to be written; basic information is missing.

**Prompt**

```text
We are going to prepare a workshop announcement. Ask for the missing required fields one at a time: topic, date/time, how to take part. Do not ask again for information I have given. When the three fields are complete, write a two-sentence draft; do not invent an unknown link.
What you know right now: The topic is watercolor. The date is 12 October, the time 14:00. How to take part is not decided yet.
```

**Sample output**


Model: “Which way of taking part should we state?” User: “They should reply to the announcement.” Model: “The watercolor workshop is on 12 October at 14:00. To take part, you can reply to this announcement.”

**What did we get?**

The single necessary question was tied to a usable draft.

### Medium

**Situation**

For a one-week study plan, the time available and the priorities are unknown.

**Prompt**

```text
Before you make a plan for me, collect the missing information. My goal is to learn Python lists; I am a beginner. Ask at most three questions, one at a time. Stop when the time, available days and learning criterion are sufficient; summarize the answers and produce a one-week plan.
```

**Sample output**


Model: “How many minutes a day can you spend studying?”

User: “20 minutes.”

Model: “Which days are you available?”

User: “Monday, Wednesday, Friday.”

Model: “By the end of the week, what do you want to be able to do without help?”

User: “Write code that filters a list.”

Model: “That is enough information: three days, 20 minutes a day; goal: filtering a list without help. Monday lists/indexing, Wednesday conditional filtering, Friday an unassisted exercise on a new list. Each session 20 minutes.” No further questions are asked.

**What did we get?**

The plan was built on the capacity given, not on assumed free time.

### Hard

**Situation**

A team will decide on a research question; the participants do not yet know every detail.

**Prompt**

```text
Goal: Complete a small team's user research brief. What is known: 5 interviews can be done; the product is a note-taking app; there is 1 week in total.
First ask what the decision will change and wait for my real answer. Do not fill in a field that is unknown at the start as if it had an answer.
Then ask only about gaps that change the design; at most 4 questions in total. If the user says I don't know, briefly show the options and their effects; do not write as if a decision had been made.
Sufficient-information criterion: target behavior, participant criterion, interview length, decision owner. If anything remains missing, mark the assumptions separately. At the end, present the brief draft for confirmation; do not ask new questions once the information is sufficient, and do not start a new survey or recruitment before approval.
```

**Sample output**


Model: “Which decision will the result of the research change?”

User: “We'll decide which problem blocking people from saving their first note to fix first.”

Model: “Whom should we include in the interviews?”

User: “People who didn't save their first note on the day they signed up.”

Model: “How many minutes can each interview last?”

User: “15 minutes.”

Model: “Who will make the priority decision?”

User: “Ayşe, the product lead.”

Model: “That is enough information. Brief presented for confirmation: within one week, 15 minutes each with five people who meet the stated criterion; the aim is to understand the obstacles to saving the first note, and Ayşe will set the priority of fixes.” It stops at four questions; no interviews are started.

**What did we get?**

The number of questions stayed limited; unknowns did not turn into false certainty.

## Where should you stop?

Interviewing again for a job where all the information has been given is unnecessary. Question Refinement improves the wording of the question; Flipped Interaction collects missing inputs from the user. Eliciting preferences focuses specifically on values and trade-offs.

## Sources

- [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT](https://arxiv.org/html/2302.11382) — White, Jules; Fu, Quchen; Hays, Sam; Sandborn, Michael; Olea, Carlos; Gilbert, Henry; Elnashar, Ashraf; Spencer-Smith, Jesse; Schmidt, Douglas C.. 2023-02-21. Defines the Flipped Interaction pattern, in which the model reaches a specific goal by asking the user questions. Evidence level: relevant body sections of the original paper.
