# Facilitating group discussion

Make the group's different pieces of knowledge visible; do not manufacture an artificial consensus.

## What is it?

Group facilitation is organizing participants' notes, their common ground and their open disagreements. The model can be a moderation assistant; it cannot produce preferences, approvals or decisions on behalf of the people in the group.

## When does it help?

When knowledge in a team is spread across different people, the same topic keeps being discussed again, or a minority view is getting lost.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will gather three people's event notes.

**Prompt**

```text
Fictional inputs used instead of real participant notes: A="I'm available in the morning", B="I'm available in the afternoon", C="The time doesn't matter, the entrance must have a ramp".
Keep the notes with the person's ID. Summarize them as shared points, differences and missing information for the decision. Do not write a majority time or write as if everyone had approved. Propose a single clarifying question; do not send messages to anyone.
```

**Sample output**

“The time preference is split. The access condition was stated by C. For deciding a suitable time, A/B's range of flexibility is unknown.”

**What did we get?**

The group summary did not squeeze the views into a single preference.

### Medium

**Situation**

When scattered pieces of information are considered together, a new constraint emerges.

**Prompt**

```text
Notes: A="The hall holds 16 people", B="There are 18 participation requests", C="There is no budget for another hall".
Separate each piece of information with its source person. Calculate the constraint that arises from them together; do not complete the records with your own guesses. Then write at most three decision options and, for each, the human decision needed.
Do not change the participant list, eliminate people or arrange an alternative hall. Do not write the options as decisions already taken before the group confirms.
```

**Sample output**

“18 requests, 16 capacity: there is a difference of 2 people. The options of a waiting list, two sessions or confirming the requests each need a separate group decision.”

**What did we get?**

Different people's information turned into a shared constraint; no authority to act was created.

### Hard

**Situation**

At the end of a meeting, silence could be mistakenly counted as approval.

**Prompt**

```text
Minutes: A="Let's split it into two sessions", B="The facilitator may not have enough time", C did not speak on this. Decision rule: everyone must approve explicitly.
The model should prepare a decision summary: proposal, objection, unanswered question, explicit approvals. Do not count C's silence as approval; do not delete B's objection as merely a negative tone.
The human facilitator should have the participants confirm the summary themselves. The model sends no messages in this example. If there is no confirmation, the result should be "decision pending"; stop after at most one revision of the summary.
```

**Sample output**

“The proposal is two sessions. B's time objection has not been resolved; C's view is missing. Under the unanimity rule, no decision was taken.”

**What did we get?**

Facilitation did not turn missing approval into an artificial consensus.

## Where should you stop?

Better information sharing does not mean the final decision is better. In the source's real human group study, these measures are separate; it is not presented as if a significant increase in final decision quality had been shown. The model's summary needs to be verified by the speakers.

## Sources

- [Bringing Everyone to the Table: An Experimental Study of LLM-Facilitated Group Decision Making](https://arxiv.org/html/2508.08242v2) — Alsobay, Mohammed; Rothschild, David M.; Hofman, Jake M.; Goldstein, Daniel G.. 2025-08-11; version read 2026-07-02. Examines information sharing and decision measures under LLM facilitation in real human groups; the information-sharing finding is not carried over as an increase in final decision quality. Evidence level: relevant body sections of the original paper.
