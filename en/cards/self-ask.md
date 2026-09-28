# Self-Ask

Answer the missing subquestion before returning to the main question.

## What is it?

Self-Ask determines whether a question needs a follow-up question; it makes the necessary subquestion and its intermediate answer visible. The original work also shows a version combined with a search engine. If there is an external search, the intermediate answer must actually be provided by the tool.

## When does it help?

For questions that cannot be answered without linking two pieces of information; especially when the next query depends on the previous answer.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

From two given records, you will find a person's city of birth.

**Prompt**

```text
Question: What is the city of birth of the author of the fictional book Gölgeler?
Given records: D1="The author of Gölgeler is Deniz Arı." D2="Deniz Arı was born in Eskişehir."
First state whether a follow-up question is needed. If so, write a single subquestion and its intermediate answer from these records; then return to the main question. No external search. Do not add details that are not in the sources.
```

**Sample output**

“Follow-up question: Who is the author of Gölgeler? Intermediate answer: Deniz Arı [D1]. Final answer: Eskişehir [D2].”

**What did we get?**

The intermediate information the main question depends on was separated out.

### Medium

**Situation**

For the same question, the records are not given up front.

**Prompt**

```text
The supervisor should provide a read-only lookup(query) tool; at most 2 queries. Starting question: What is the city of birth of the author of Gölgeler?
The model should generate the first subquestion. The application should run the query and add the real result to the history.
Representative 1st result: "Gölgeler — author Deniz Arı" [D1]. The next subquestion should depend on this name.
Representative 2nd result: "Deniz Arı — city of birth Eskişehir" [D2].
The model should combine the two real intermediate answers with their source IDs. If there is no result, it should not guess; stop when the budget ends.
```

**Sample output**

Queries: “Gölgeler author” → “Deniz Arı city of birth”. Answer: “Based on the author match in the records, Eskişehir [D1, D2].”

**What did we get?**

The subquestion was generated from the previous tool result.

### Hard

**Situation**

Two people with the same name make the search ambiguous.

**Prompt**

```text
Task: Find the city of birth of the author of Gölgeler. There is a lookup tool; limit of 3 queries in total.
1st real return: "Gölgeler (2018), author Deniz Arı, translator." 2nd real return: "Deniz Arı: athlete, İzmir; Deniz Arı: translator, no city information."
The model should not jump to the İzmir result based on name similarity alone. The final subquestion should look for an identity match using both translator and the 2018 work.
If the 3rd return has no city, separate the resolved intermediate information from the unresolved information in the final answer. The supervisor should carry all question/intermediate answer/source records; stop at three queries.
```

**Sample output**

“It matches that the author is Deniz Arı the translator; the city of birth is not in the available records. I did not use the İzmir information, which belongs to the athlete.”

**What did we get?**

The subquestions also made the wrong-person match visible.

## Where should you stop?

Self-Ask is not interviewing the user; it is the model organizing subquestions of information for the main question. It should be stated whether the intermediate answer came from the model, a given document or a search. A search result also needs source and identity checks.

## Sources

- [Measuring and Narrowing the Compositionality Gap in Language Models](https://arxiv.org/html/2210.03350) — Press, Ofir; Zhang, Muru; Min, Sewon; Schmidt, Ludwig; Smith, Noah A.; Lewis, Mike. 2022-10-07; version read 2023-10-17. Defines the structure of follow-up question, intermediate answer and final answer, as well as the Self-Ask version combined with a search engine. Evidence level: relevant body sections of the original paper.
