# Question Refinement

Before answering a question, propose a more useful version of it.

## What is it?

Question Refinement turns the user's question into a more specific and answerable form. The model proposes the new question; if the user's goal would change, it makes this explicit and waits for approval.

## When does it help?

With questions whose criterion and scope are unclear, such as “Which one is best?” or “How do I fix this?”.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will start from the question “Which computer is good?”.

**Prompt**

```text
Instead of answering my question right away, propose a better version. Do not add unknown preferences. Write one short explanation and a single clarifying question.
My question: Which computer is good?
What you know: I write text and carry it around a lot. I haven't mentioned my budget yet.
```

**Sample output**

“Suggestion: Which computer features should I prioritize for writing text and carrying it around often? Before we move on to model recommendations, what is your budget range?”

**What did we get?**

The word “good” was broken down into visible usage criteria.

### Medium

**Situation**

You will turn the complaint “My site is slow” into a question that can be investigated.

**Prompt**

```text
Narrow this question down for a technical review, but do not invent a cause: Why is my site slow?
Data: The product page takes 6 seconds to open on mobile. There is no desktop measurement. The latest change was the product images; whether they are the cause has not been tested yet.
Write the better question, what is known, and the one missing comparison. Do not apply a solution until the user accepts the new question.
```

**Sample output**

“In the 6-second load of the mobile product page, which resource takes the most time? The image change is a hypothesis; network/processing timing has not been measured yet.”

**What did we get?**

The symptom was not locked into an unverified cause.

### Hard

**Situation**

Two different decisions are hidden inside one policy question.

**Prompt**

```text
Question: Should our team use AI completely?
Context: A 6-person design team. Candidate uses: summarizing publicly available text and confidential drawings that belong to clients. The goal is to save time; there is no permission to transfer data.
Split the question into two decision questions. Keep the permission limit. For each question, add the evidence needed and the priority the user must choose. The two questions do not have to reach the same conclusion. Do not finalize an implementation or policy recommendation until the user has made a choice.
```

**Sample output**

“1. How should accuracy and time be measured for summarizing publicly available text? 2. Which local options can be considered without transferring the confidential drawings to an external service? There is currently no transfer permission for the second job.”

**What did we get?**

A single yes/no question was split along different data and decision boundaries.

## Where should you stop?

A fancier question may not be a better question. The new version should not change the user's intent. Problem framing discusses the problem itself and the success criterion; this pattern more narrowly improves the wording of the question.

## Sources

- [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT](https://arxiv.org/html/2302.11382) — White, Jules; Fu, Quchen; Hays, Sam; Sandborn, Michael; Olea, Carlos; Gilbert, Henry; Elnashar, Ashraf; Spencer-Smith, Jesse; Schmidt, Douglas C.. 2023-02-21. Explains how, in the Question Refinement pattern, the model proposes a better question while the user keeps the decision to use it. Evidence level: relevant body sections of the original paper.
