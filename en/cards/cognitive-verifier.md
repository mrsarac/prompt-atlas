# Cognitive Verifier

Before building the main answer, clarify the necessary subquestions with the user.

## What is it?

Cognitive Verifier is a prompt pattern that generates additional questions to give a better answer to the main question and combines their answers. In the definition by White and colleagues, the subquestions are put to the user. The name “verifier” here is not a guarantee of independent correctness.

## When does it help?

When a decision has different dimensions and the necessary information lies with the user.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You are asking whether a study plan suits you.

**Prompt**

```text
My question: How should I start studying Python this week?
Use the Cognitive Verifier pattern: Identify at most three additional questions that will determine the answer; ask me each of them in turn and wait for my answer. Then combine my answers into a short plan.
Known: I am a beginner. Do not ask again for the same information. Stop asking questions once the necessary fields are complete.
```

**Sample output**

Questions: “What is your target task? Which days and how much time do you have? How will you check success?” If the answers are list filtering / three days of 20 minutes / an unaided example, the plan is tied to them.

**What did we get?**

The general plan was shaped by the sub-answers taken from the user.

### Medium

**Situation**

Three conditions are needed together to choose an event venue.

**Prompt**

```text
Main question: Is the fictional Room A suitable for our workshop? Room information: 16 people, 2 hours of use, ramped entrance; no information about a lift.
Ask the additional questions that affect the decision in turn: number of participants, time needed, access needs. Wait for my answers; do not invent preferences that were not given.
My answers: 12 people, 90 minutes, one participant needs access to the upper floor. In the result, match each sub-answer with the relevant room information; do not finalize it as suitable while the access record is missing.
```

**Sample output**

“The number of people and the duration fit. Information on upper-floor access is missing; the suitability decision cannot be completed until this condition is confirmed.”

**What did we get?**

While the subquestions were combined, a single missing condition stayed visible.

### Hard

**Situation**

The user's answers contradict each other.

**Prompt**

```text
Main question: Create the weekly content plan. Known: two articles are requested, each article needs at least 3 hours.
First ask the necessary subquestions; at most four questions in total. My answers: I have 4 hours in total per week; for quality, 3 hours per article cannot be reduced; two articles are not mandatory, a preference.
When combining the answers, do not present 6 hours of work as fitting into 4 hours. Separate the hard constraint from the preference; offer one conditional suggestion and one open decision. Stop with a suitable plan or an explicit conflict report.
```

**Sample output**

“With 4 hours and the condition of 3 hours per article, two articles are not possible. There is the option of one article + 1 hour of preparation; for two articles, the time or the quality condition must change.”

**What did we get?**

Combining did not hide contradictory inputs inside a reasonable-looking schedule.

## Where should you stop?

Flipped Interaction is a general question-gathering arrangement; Cognitive Verifier specifically describes combining the answers to subquestions that contribute to the main question. CoVe mostly checks the claims in a generated answer; here, missing user information is gathered. The “verifier” in the name does not provide external evidence.

## Sources

- [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT](https://arxiv.org/html/2302.11382) — White, Jules; Fu, Quchen; Hays, Sam; Sandborn, Michael; Olea, Carlos; Gilbert, Henry; Elnashar, Ashraf; Spencer-Smith, Jesse; Schmidt, Douglas C.. 2023-02-21. Defines, in the Cognitive Verifier pattern, asking the user additional questions and combining the answers into the main response; not an independent verification experiment. Evidence level: relevant body sections of the original paper.
