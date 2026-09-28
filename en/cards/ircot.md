# IRCoT

Use the intermediate information you found to change the direction of the next search.

## What is it?

IRCoT combines retrieval and short intermediate results in turn. The first documents give a new clue; that clue forms the next query. The earlier passages and the question are kept in context, and the answer is put together once there is enough evidence.

The teaching setup below carries intermediate facts with source codes instead of long dumps of thinking. You need a real search tool and a coordinator that runs this loop; search results the model imagines are not observations.

## When does it help?

It suits questions whose answer needs two or more connected documents to be found. Set the number of queries and a stop condition for when sources are insufficient from the start.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

From two records, you will find which city a fictional book's publisher is in.

**Prompt**

```text
Question: “In which city is the publisher of the book Kıyı Defteri?”
Store: B1 “Kıyı Defteri was published by Ada Yayınları.” B2 “Ada Yayınları is headquartered in İzmir.”
The coordinator runs the first search with the book title. With the returned B1, it asks the model for a single intermediate fact: the publisher's name.
With this intermediate fact, it searches “Ada Yayınları headquarters city”. It carries B1 and B2 into the final call: “Answer in one sentence with the source codes.”
At most two searches; if there is no intermediate link, do not jump to the conclusion.
```

**Sample output**

Intermediate fact: the publisher is Ada Yayınları. [B1] Final answer: The publisher is in İzmir. [B1, B2]

**What did we get?**

The second query came out of the result of the first document. In real research, separately check the possibility that two different organizations share the same name.

### Medium

**Situation**

There are two workshops with the same name; you are looking for the capacity of the right venue.

**Prompt**

```text
Question: How many people does the room for the September drawing workshop hold?
Store results: E1 “The September drawing workshop is in Room A”; E2 “The August drawing workshop is in Room B”; S1 “Room A capacity 16”; S2 “Room B capacity 30”.
The coordinator uses the month and the workshop together in the first search. It briefly extracts the matching event and room code from the model. It sets aside the record for the wrong month.
It runs the next search with the room it found; it gives the event record and the capacity passage to the answer call. At most two searches and three model calls; if the month does not match, stop.
```

**Sample output**

September → Room A [E1]. Room A → 16 people [S1]. Answer: The room for the September workshop holds 16 people. [E1, S1]

**What did we get?**

By keeping the intermediate identity, the capacity of the wrong event was eliminated. Similar words alone were not enough to match documents.

### Hard

**Situation**

Two links are made, but the final piece of information cannot be found.

**Prompt**

```text
Question: When is the next seminar given by the editor of Kıyı Defteri?
Store: K1 “The editor of Kıyı Defteri is Derya Ak”; K2 “Derya Ak's spring seminar is on 3 May 2026”; K3 “The autumn seminar will be announced.” Today is 13 September 2026.
The coordinator runs the second search with the book→editor intermediate fact. In the intermediate results, it keeps the date and the distinction between future and past. At most three searches; stop if results repeat or no date is found.
Final call: “Separate what the sources say from the part that remains unanswered. Do not present a past date as the next seminar.”
```

**Sample output**

The editor is Derya Ak. [K1] The 3 May seminar is in the past. [K2] The date of the autumn seminar is not in these records. [K3]

**What did we get?**

The search chain found a name, but it did not find the requested date. No final answer was produced that hides the gap.

## Where should you stop?

A wrong intermediate fact also steers the next search wrong. The loop can drag on by retrieving the same documents. The difference from one-shot RAG is that the query is renewed with intermediate information; in Self-Ask, subquestions can also be answered by the model without a search.

## Sources

- [Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions](https://arxiv.org/html/2212.10509) — Trivedi, Harsh; Balasubramanian, Niranjan; Khot, Tushar; Sabharwal, Ashish. 2022-12-20; version read 2023-06-23. Examines intermediate reasoning and retrieval steps guiding each other; the multi-step QA results with GPT-3/Flan-T5 are not general research accuracy. Evidence level: relevant body sections of the original paper.
