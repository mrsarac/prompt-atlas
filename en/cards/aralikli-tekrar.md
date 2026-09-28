# Spaced repetition

Spread review over time; record what you forgot.

## What is it?

Spaced repetition is trying to recall the same information again at different times, instead of seeing it continuously in a single session. The model can prepare the content and a record template; the real passing of time and the recall attempts are carried out by a human or an application.

## When does it help?

When you want to keep using what you learned in the following days. Writing “one week later” in a single chat message is not doing spaced repetition.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will spread three status codes over several days.

**Prompt**

```text
Topic note: 200 success, 404 resource not found, 500 server error.
Prepare three short questions for me that match the source; keep the answer key in a separate section. Sample study schedule: today, 2 days later, 1 week later. Do not say this is a personalized optimal schedule.
In each session I will answer without seeing the answers; I will record the date, unaided correct/incorrect and the code I struggled with in my local notes. Do not set up real reminders. Stop when the three-session plan is ready.
```

**Sample output**

Record template: “date | question | unaided answer | checked against source | next review”. Real progress is filled in only from sessions actually held.

**What did we get?**

The schedule and the record of learning actually done were kept separate.

### Medium

**Situation**

Some cards are easy; others keep getting mixed up.

**Prompt**

```text
Record: 13 October — 200 correct, 404/500 mixed up; 15 October — 200 correct, 404 correct, 500 with a hint.
Based on this record, propose priorities for the next session. Simple local rule: ask items answered wrongly/with a hint the next day, and items answered correctly without help twice in a later session. Do not claim this is a research-validated personal scheduling algorithm.
You may rephrase the questions, but keep the source definition. The human should apply the dates to their own calendar; if there is no data, do not add new success records.
```

**Sample output**

“500 has priority; the last answer was with a hint. 200 can be moved to a later session. Plan one more unaided attempt for 404.”

**What did we get?**

The intensity of review changed according to the real error record.

### Hard

**Situation**

The source information for a learning card has changed.

**Prompt**

```text
Old card v1: "In the fictional system, the file limit is 10 MB". New approved source v2: "Limit 20 MB; valid from 1 November". The last review was done on 25 October with the old card.
The model should separate the new and old information with their dates. It should link the review card after 1 November to v2; it should not rewrite the old correct answer as if it had never made a mistake under the new rule.
The human should check the source version. In the next real session, they should answer "Which limit applies from which date?" without the source; the result should be added to the new version's record. Do not say complete before the session has happened.
```

**Sample output**

“The v1 history record is kept. v2 card: 20 MB from 1 November. There is no recall result for the new version yet.”

**What did we get?**

The review system did not keep teaching old information as if it were permanently correct.

## Where should you stop?

The time intervals in this card are examples; there is no claim of a single schedule suitable for every topic. The source set contains a practitioner guide for spaced study, and separate human research for the retrieval effect. The superiority of any particular LLM schedule has not been verified. Without an external record, do not assume the model keeps track of progress between sessions.

## Sources

- [A Step-by-Step Process to Teach Yourself Anything (in a Fraction of the Time) - Scott H Young](https://www.scotthyoung.com/blog/2013/05/10/learn-anything-in-less-time/) — Scott H. Young. 2013-05-10. A practitioner source for structuring learning and for review/feedback practices; not an experimental guarantee of personalized intervals. Evidence level: page body.
- [Test-enhanced learning: taking memory tests improves long-term retention](https://pubmed.ncbi.nlm.nih.gov/16507066/) — Henry L. Roediger III; Jeffrey D. Karpicke. 2006-03. Human research on retrieval and later recall; does not validate the sequence of dates in this card or an LLM schedule. Evidence level: abstract and citation.
