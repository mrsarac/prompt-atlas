# Uncertainty and abstention

Make clear where the answer ends and which information is missing.

## What is it?

An uncertainty contract describes when the model can answer, when it should speak conditionally and when it should stop. It helps to tie the sentence “say so if you don't know” to a concrete data threshold: for example, not writing a definite schedule if there is no date and approval record.

The goal is not to make every answer timid. It is to say what is clear in the source and keep what is not clear separate. The model's own confidence percentage does not count as an independent accuracy measurement.

## When does it help?

Use it for work with missing documents, conflicting versions or missing information that a decision requires. State which gap would change the result.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

An event note has a time but no fee.

**Prompt**

```text
Note: The drawing workshop starts at 15:00.
Question: When does it start, and is there a fee?
Answer only with the information in the note. If there is no fee information, write “This note does not state a fee.” Do not guess free or paid.
```

**Sample output**

It starts at 15:00. This note does not state a fee.

**What did we get?**

The known time and the unknown fee were separated. The note not mentioning a fee does not show that the event is free.

### Medium

**Situation**

Two documents give different times for the same day.

**Prompt**

```text
A: “The workshop is at 14:00.” B: “The workshop is at 15:00.” Neither has approval or update information.
Do not pick one time as correct. Give the two conflicting pieces of information with their source codes. Ask for the one missing piece of information that would change the decision; do not invent a confidence percentage.
```

**Sample output**

A says 14:00, B says 15:00. Which record is the organizer's latest approved announcement?

**What did we get?**

The question of source authority needed for the decision came out. The time was not picked by majority or by the more fluent sentence.

### Hard

**Situation**

An agent is trying to move forward with a schedule whose source is incomplete.

**Prompt**

```text
Task: Propose only a draft schedule; do not send real invitations.
Data: The hall is available 10:00–12:00. The trainer's note says “morning might work”; there is no confirmed availability. The session is 90 minutes.
Calculate the possible slot based on the hall; do not assume the trainer's availability. Do not write the invitation text as if it were confirmed. State the condition under which to stop until the trainer replies. Propose the one independent preparation that can be completed while waiting for information.
```

**Sample output**

From the hall's side, 10:00–11:30 is possible. The trainer's approval for this slot is missing; the schedule is not final. Independent preparation: a draft of the 90-minute content flow.

**What did we get?**

Missing information did not stop all thinking; but no dependent decision was made either. This prompt has no real permission to send invitations.

## Where should you stop?

The model can misjudge uncertainty: it can needlessly refuse a correct answer or fail to notice missing information. A human should check the scope of the sources. The citation contract shows the support; this card sets the behavior when the support is not enough.

## Sources

- [Prompt design strategies  |  Gemini API  |  Google AI for Developers](https://ai.google.dev/gemini-api/docs/prompting-strategies) — Google. Publication date not verified. Provides grounding for instruction design with a clear task and missing context; does not guarantee calibration. Evidence level: page body.
- [Enabling Large Language Models to Generate Text with Citations](https://arxiv.org/html/2305.14627) — Gao, Tianyu; Yen, Howard; Yu, Jiatong; Chen, Danqi. 2023-05-24; version read 2023-10-31. Shows that source support and a correct answer must be evaluated separately; it is not, on its own, an effect test of this abstention contract. Evidence level: relevant body sections of the original paper.
