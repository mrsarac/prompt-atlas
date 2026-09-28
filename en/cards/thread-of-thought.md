# Thread of Thought

Examine a scattered context in small parts, then extract only the answer.

## What is it?

Thread of Thought proposes handling a mixed or distracting context in manageable parts. The first stage organizes the relevant information; the second stage extracts the answer to the question from this work. Here, short sourced notes are used instead of long internal thinking.

## When does it help?

When relevant information is scattered across different places in a long conversation. A short, clean text may not need two stages.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will find the event's new time in the conversation notes.

**Prompt**

```text
A human should make two separate calls. Question: What is the most recently agreed start time?
Notes: N1="At first we said 13:00." N2="The coffee option was discussed." N3="Authorized organizer: I'm changing the start to 14:00."
Call 1: Examine the context in manageable parts. For each part, write a short fact related to the question and its ID; do not treat the old decision as current.
Call 2: Take the question and the real first output. Give only a short answer and the supporting ID. A human should check the match with N3; stop at two calls.
```

**Sample output**

First note: “N1 old time; N2 irrelevant; N3 authorized new decision 14:00.” Final answer: “14:00 [N3].”

**What did we get?**

A thread of information carrying the current decision was extracted from a scattered conversation.

### Medium

**Situation**

The information for two orders is mixed up in the same note.

**Prompt**

```text
Question: What is K42's delivery method and its open gap?
P1="K42 will be picked up from the store." P2="K43 was handed to the courier." P3="The name of the person picking up K42 is missing." P4="K43's address was verified."
The supervisor should give the context to the first call, keeping the part IDs. Prompt: For each part, separate the order, status and missing field in a short note; do not carry information between orders.
The second call should extract the K42 answer from the real notes only. A final check should verify that K43 information was not written into K42. Stop after the two calls and the check.
```

**Sample output**

“K42 will be picked up from the store [P1]; the name of the person picking it up is missing [P3].”

**What did we get?**

Examining part by part prevented similar records from contaminating each other.

### Hard

**Situation**

A condition has been changed by a later note, only for certain people.

**Prompt**

```text
Question: Is Ece's right to a free cancellation definite?
P1="General rule: cancellation 48 hours in advance is free." P2="The hall's lighting was renewed." P3="Late requests may be reviewed for those who submit a medical certificate." P4="Ece cancelled 24 hours in advance and submitted a certificate." P5="There is no review decision yet."
First call: Split the parts, in order, into short sourced notes; connect the general rule/exception/person/decision status. Do not narrate hidden thinking.
Second call: From these notes, answer only the question. Do not turn "may be reviewed" into "approved". The supervisor should check that P3/P5 are preserved; if they are missing, stop without producing a definite answer.
```

**Sample output**

“Not definite. Ece is outside the general period; a review is possible because of the certificate, but no decision has been made yet [P1, P3–P5].”

**What did we get?**

The exception and the decision status did not get lost among the distracting details.

## Where should you stop?

System 2 Attention regenerates the relevant context before answering; Thread of Thought emphasizes the prompt of handling a complex context part by part and then extracting the answer. Although their boundaries are close, the original prompt arrangements are not the same. This teaching format does not count as having reproduced the paper's experimental results.

## Sources

- [Thread of Thought Unraveling Chaotic Contexts](https://arxiv.org/html/2311.08734) — Zhou, Yucheng; Geng, Xiubo; Shen, Tao; Tao, Chongyang; Long, Guodong; Lou, Jian-Guang; Shen, Jianbing. 2023-11-15. Defines the first prompt, which examines a chaotic context in manageable parts, and the second prompt, which then extracts the answer. Evidence level: relevant body sections of the original paper.
