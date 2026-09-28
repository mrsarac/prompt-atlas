# Retrieval practice

Recall without seeing the answer, then compare with the source.

## What is it?

Retrieval practice is calling information back from memory before reading it again. The model can prepare questions and compare the answer with the source; the one recalling must be the human. The model answering its own question is not the same learning activity.

## When does it help?

When a topic feels familiar as you read it, but you cannot explain it without looking at the book.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will study HTTP status codes.

**Prompt**

```text
Source note: 200 the request succeeded; 404 the requested resource was not found; 500 an error on the server.
Ask me a single open-ended question from this note. Do not show the answer in the same message; wait for my answer. Then compare it with the note and correct only the missing or wrong part. Stop after two questions. I will close the source note while I answer.
```

**Sample output**

Model: “Which code would you expect when the requested resource is not found?” Human: “404.” Model: “That matches the note.”

**What did we get?**

Instead of recognition, recalling the answer without the source was practiced.

### Medium

**Situation**

You will apply a memorized definition to a new example.

**Prompt**

```text
Source: Average speed is total distance divided by total time; a simple average of speeds is not always correct.
First ask me to state the definition without looking at the source. Then ask a different application question: if 90 km is covered in 3 hours, what is the average speed?
Wait for my answer to each question; if you give a hint, note that help was given. The final feedback should check the definition, the calculation and the unit separately. Do not have me repeat it while keeping the correct answer in front of me.
```

**Sample output**

Human: “Total distance / total time; 90/3=30 km/h.” The feedback says all three parts are correct.

**What did we get?**

Recalling the definition and a simple application were checked separately.

### Hard

**Situation**

Wrong questions can reinforce wrong information.

**Prompt**

```text
An arrangement for preparing questions for a teacher. Source rule: 500 TL and above ships free, below that 50 TL.
The model should produce three questions and a separate answer key: recalling the rule, the 500 boundary, applying it to 499. It should not be presented to students before the teacher checks the key against the source.
In the student version, the answer key stays hidden. Record whether each answer was unaided or with hints; on a wrong answer, give a short sourced correction. At the end, instead of having the same numbers repeated, ask a new question for 501.
At most four questions; do not present this session as a measure of long-term learning.
```

**Sample output**

Teacher key: “threshold included; 500→0; 499→50; 501→0.” The student sees only the questions, in order.

**What did we get?**

An exercise was created in which question quality, answer leakage and the level of help are checked.

## Where should you stop?

Feedback can matter, but if its source is wrong, the error is reinforced. Human retrieval research does not prove that every LLM-generated question is of good quality. A short success within a lesson is not the same measurement as unaided recall days later.

## Sources

- [Test-enhanced learning: taking memory tests improves long-term retention](https://pubmed.ncbi.nlm.nih.gov/16507066/) — Henry L. Roediger III; Jeffrey D. Karpicke. 2006-03. Examines the relationship between retrieval through testing and later recall in humans; only the abstract and citation were read here. Evidence level: abstract and citation.
- [Enhancing Student Learning with LLM-Generated Retrieval Practice Questions: An Empirical Study in Data Science Courses](https://arxiv.org/html/2507.05629) — An, Yuan; Liu, John; Acharya, Niyam; Hashmi, Ruhma. 2025-07-08; version read 2025-07-29. A quasi-experimental study of LLM-prepared retrieval questions in a course context; explicitly states the need for teacher verification. Evidence level: relevant body sections of the original paper.
