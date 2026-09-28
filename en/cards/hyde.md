# HyDE

Generate a draft that resembles the document you are looking for; use it to find the real documents.

## What is it?

In HyDE, the model first writes a hypothetical document that could answer the question. An embedding model turns this text into a vector; the real document store is searched by vector similarity. The evidence carried into the answer stage is the real documents found by that search.

The generated hypothetical text can contain wrong details. Presenting it as a source reverses the purpose of the method. Writing “use HyDE” does not set up an embedding model or a search index.

## When does it help?

You can try it with dense vector search when the words of the question differ from the language of the documents. You need an embedding model, real documents indexed in the same space and a search executor.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will find the book loan period in an archive. Real documents: K1 “The loan period is 14 days”; K2 “The café closes at 16:00”.

**Prompt**

```text
The coordinator first calls the model: “Write a short hypothetical library guideline that could answer the question of how many days a book can be borrowed. This is a search aid, not a claim about real policy.”
Then it encodes this draft with the embedding model and retrieves the single closest document from the real vector index of K1/K2.
Final call: “Answer the period using only the retrieved document; add the document code.” The hypothetical draft does not enter the final evidence package.
One generation, one vector search, one answer; if there is no match, stop.
```

**Sample output**

Representative draft: “Borrowed books are returned at the end of the set period.” Representative search: K1. Answer: 14 days. [K1]

**What did we get?**

The hypothetical text guided the search; the 14-day information came from a real store record. This vector search was not run here.

### Medium

**Situation**

The question “closing my account” appears in the documents as “terminating membership”.

**Prompt**

```text
Store: U1 “An application form is required to terminate membership.” U2 “The password reset link is valid for 15 minutes.”
The coordinator gets a draft from the model with the prompt “Write a hypothetical help text about the process required to close my account; do not treat any conditions you invent as evidence.”
It turns the draft into an embedding and retrieves two candidates from the store. A human checks which passage describes closing the account; only the suitable record is carried into the answer call.
Final prompt: “Which process is required? Do not state a confirmation period that is not in the source.” At most two candidates; if there is no suitable source, stop the answer.
```

**Sample output**

Representative suitable result U1; U2 is only about resetting a password. Answer: An application form is required to terminate membership. [U1]

**What did we get?**

Similar-looking account operations were told apart through the passage. No actual termination took place.

### Hard

**Situation**

The hypothetical document produces a wrong period; the versions also conflict.

**Prompt**

```text
Question: What is the current return period for in-store purchases?
Store: I1 old/unapproved 14 days; I2 in force/approved 30 days; I3 online purchases 60 days.
The coordinator generates a HyDE draft and retrieves at most three real candidates through embedding search. Even if the draft mentions “60 days”, it removes that from the evidence package.
A human reviews the scope and approval status of the candidates; only the in-force record for in-store purchases is given to the next call.
Final prompt: “Answer using only the selected record; write the code and the scope.” If the approval status cannot be verified, do not give a definite period; stop after two model calls in total.
```

**Sample output**

The representative draft may have said 60 days. The accepted record is I2; the answer for in-store purchases is 30 days. [I2]

**What did we get?**

Search assistance and source authority were separated. Whether the index retrieves the right candidate is still a system behavior that has to be measured separately.

## Where should you stop?

A wrong hypothetical text can lead the search into the wrong neighborhood. A similarity score is not an accuracy score. RAG describes the whole of finding and answering; HyDE describes one specific retrieval strategy within that whole. In Generated Knowledge the generated knowledge can be a direct input to the answer; here a real store search is a mandatory part.

## Sources

- [Precise Zero-Shot Dense Retrieval without Relevance Labels](https://arxiv.org/html/2212.10496) — Gao, Luyu; Ma, Xueguang; Lin, Jimmy; Callan, Jamie. 2022-12-20. Defines the method that links a hypothetical document to a real corpus through embeddings; the InstructGPT/Contriever experiments do not generalize to all search systems. Evidence level: relevant body sections of the original paper.
