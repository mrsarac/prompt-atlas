# Task and output contract

Turn a request into a job with a clear deliverable and a clear way to check it.

## What is it?

When you say “improve the announcement”, the model can pick both the problem and the solution. In a task contract, you write the goal, the information to use, the output format and the completion criterion. What the model should do when information is missing is also part of the contract.

Writing instructions without giving a solved example is zero-shot use. The expansions of acronyms such as RTF, CRISPE, RISEN, CARE, CRAFT and RACE can vary between sources; here we do not count them as independent algorithms and instead write out the shared brief fields explicitly.

## When does it help?

You can start with an announcement, a comparison or a small coding job. First decide what output you will accept as correct and which inputs the model may use.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

A workshop collects applications through a form; a place is confirmed only by email. You will write the announcement in two sentences.

**Prompt**

```text
Write an application announcement. Information: The drawing workshop has 20 places. The form is for applying; a place is confirmed when the confirmation email arrives. Use two sentences. No date or fee was given; do not add one. Make it clear that submitting the form is not a confirmed registration.
```

**Sample output**

You can apply for the drawing workshop by filling in the form. Your place in the 20-person workshop is confirmed when the confirmation email arrives.

**What did we get?**

Two checkable sentences: the capacity is kept, and application and confirmation are separated. You check that the announcement matches the real conditions.

### Medium

**Situation**

You are comparing two venues; accessibility information for one of them is missing.

**Prompt**

```text
A: 800 TL, 25 people, has a lift. B: 600 TL, 20 people, no access information. For an 18-person workshop, compare only cost, capacity and step-free access. On each line, write A, B and what is unknown. Do not treat the lift information alone as evidence of step-free entry. Without picking a final venue, state the one piece of information to ask about.
```

**Sample output**

Cost: A 800 TL; B 600 TL. Capacity: both fit 18 people. Step-free access: A has a lift, entry not verified; no information for B. Question: Can both venues be reached from the street without steps?

**What did we get?**

Missing data was not filled in as a positive feature. The choice is not complete until the venue owners confirm access.

### Hard

**Situation**

You are going to give a developer a change to the shipping-fee calculation. Scope and acceptance criterion are both needed.

**Prompt**

```text
Propose a change only to the shipping condition in shipping.js. Current expression: total > 500 ? 0 : 50. Rule: if the numeric, undiscounted total is 500 or more, shipping is free; below that, it is 50 TL. Output: the new expression, the expected results at three boundary values, and the behavior that must not change. Do not add other files, currencies or a discount system. If you have no access to run code, label the results as expectations.
```

**Sample output**

New expression: `total >= 500 ? 0 : 50`. Expected: 499 → 50; 500 → 0; 501 → 0. The 50 TL fee below the threshold does not change. This response does not show that any test was run.

**What did we get?**

Both the narrow change and the acceptance examples are clear. The developer checks the expression in the real file and in the tests; the prompt does not technically restrict file access.

## Where should you stop?

An output contract does not retrieve sources, run calculations or enforce a JSON schema at the API level. A plain-language request such as “ELI5” sets the reading level; it does not measure whether you have learned the concept. Checking learning needs the explain-back order in the Teach-back card.

## Sources

- [Prompt engineering | OpenAI API](https://developers.openai.com/api/docs/guides/prompt-engineering?api-mode=responses) — OpenAI. Publication date not verified. A guide to organizing task, context, example and output instructions; provider-scoped advice is not a universal guarantee of success. Evidence level: page body.
- [Prompt design strategies  |  Gemini API  |  Google AI for Developers](https://ai.google.dev/gemini-api/docs/prompting-strategies) — Google. Publication date not verified. Supports the advice on clear instructions and output format; it is not a success test of these examples. Evidence level: page body.
