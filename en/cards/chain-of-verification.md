# Chain-of-Verification

Break the draft into small check questions; get the answers again without being influenced by the draft.

## What is it?

Chain-of-Verification first produces a draft answer, then prepares check questions for the claims in the draft. A separate answering stage answers these questions; the final stage revises the draft according to the check answers. In the factored form, the check calls do not see the answer the draft proposes.

This separation of context does not provide external sources. In the document examples below, we are the ones who additionally give the source to the check call; this is a teaching adaptation that makes the source check visible.

## When does it help?

It can help when a draft contains several verifiable facts. Decide which information each check question tests and which data the answerer can access.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

An announcement has left out the confirmation condition.

**Prompt**

```text
Coordinator:
1. Draft call: “K1: The form collects applications; a place is confirmed by the confirmation email. Write a short announcement.”
2. Give the draft to a separate call: “Generate one question that checks the registration claim; do not answer it.”
3. Give only the question and K1 to a new call; do not carry the draft over.
4. Combine the first draft, K1 and the check answer: “If there is false certainty, correct it.”
At most four calls; if the check answer is not in K1, ask for human review.
```

**Sample output**

Representative draft: “Fill in the form, and your place is ready.” Check question: “When is a place confirmed?” Answer: “By the confirmation email.” The final text includes this condition.

**What did we get?**

The draft's missing condition became visible through a separate question. The example is not a measurement of automatic model success.

### Medium

**Situation**

Two facts in the announcement will be checked separately.

**Prompt**

```text
Sources: K1 “The workshop has 16 places”; K2 “Pens are provided; participants bring the notebook”.
1. Get an announcement draft from the model with these sources.
2. From the draft, get two check questions, one for capacity and one for materials.
3. Have each question answered in a separate new call with the relevant source; do not show the other check's answer or the first draft.
4. Have the final text written by combining the draft and the two answers.
The coordinator does not exceed five calls in total. It removes claims outside the sources or marks them as unknown.
```

**Sample output**

Representative checks: capacity 16 [K1]; material provided is pens, notebook to be brought [K2]. The final text cannot say “all materials are provided”.

**What did we get?**

Different claims were not buried in one general “I checked” message. The authenticity of the sources is still checked separately.

### Hard

**Situation**

The sources do not answer one of the check questions.

**Prompt**

```text
Draft goal: Describe the workshop's capacity, materials and video access.
Sources: K1 “Capacity 16”; K2 “Pens are provided”. No video information.
The coordinator runs the flow draft → check questions → a separate answer to each question → final revision. Only the question and K1/K2 go to the check calls; guessing is forbidden.
At most six calls. Do not derive the missing video information from another check answer. In the final revision, separate the two supported pieces of information from the open video question; do not promise definite access unless a source is found.
```

**Sample output**

Representative video check: “This information is not in K1/K2.” Final text: “The workshop has 16 places; pens are provided. These sources contain no information about video access.”

**What did we get?**

The check chain did not erase the missing information from the result. A new source requires separate research.

## Where should you stop?

The same model in a separate context can repeat the same mistake. Do not present the checks taken from the model in the original CoVe as independent factual evidence. CRITIC uses external tool observations; Self-Refine is a more general generate–critique–correct loop.

## Sources

- [Chain-of-Verification Reduces Hallucination in Large Language Models](https://arxiv.org/html/2309.11495) — Dhuliawala, Shehzaad; Komeili, Mojtaba; Xu, Jing; Raileanu, Roberta; Li, Xian; Celikyilmaz, Asli; Weston, Jason. 2023-09-20; version read 2023-09-25. Defines the sequence of draft, check questions, separate answering and final revision; Llama 65B and selected factual tasks do not prove every use case. Evidence level: relevant body sections of the original paper.
