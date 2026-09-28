# Inverse Prompting

Rank candidates by measuring, as a probability, how well the generated text predicts the starting prompt.

## What is it?

This academic use of Inverse Prompting computes the probability of the original prompt from the generated text. During beam search, candidate continuations are evaluated with this inverse probability signal. In this way it tries to keep the relationship between the starting topic and the text.

This requires a model/executor with access to token probabilities and the generation search. Asking in a chat “which prompt might I have used?”, or having the model ask the user questions, is not the same method.

## When does it help?

It can be used in research on controlled long-text or poetry generation. Without a model interface that computes probabilities, it stays only a conceptual outline.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will rank drift from the topic when generating a single sentence about a library.

**Prompt**

```text
Prompt x: “Describe a quiet library.”
The coordinator keeps two candidate continuations in the same model's generation search: A “The sound of pages can be heard between the shelves.”; B “The stadium crowd is shouting.”
For each candidate, build the inverse context in the same model and compute logP(x|candidate); use the same inverse prompt template and the same starting prompt. Inverse template: "Text: [actual candidate]. The request for this text:"; after this prefix, read the real log probability of the x tokens; do not ask the model to estimate a score. These must be real probability readings from the model.
Continue the candidate with the higher inverse score; stop at the single-sentence terminator. If there is no probability access, do not present the flow as having run.
```

**Sample output**

Teaching-only scores: A −4, B −11; A is selected because −4 is higher. These values are not measured model probabilities.

**What did we get?**

It is clear which number should come from where. A subjective chat score does not replace these probabilities.

### Medium

**Situation**

The topic drifts in the second sentence of a paragraph.

**Prompt**

```text
Prompt: “Describe the quiet of the library study room in two sentences.” First sentence: “Open books wait on the tables.”
The inverse scoring template is the same at this level: prefix = "Text: [the whole candidate text, including the first sentence]. The request for this text:"; target tokens = the whole prompt “Describe the quiet of the library study room in two sentences.” above. Do not score the prefix; sum only the real log probabilities of the target tokens after the prefix and divide by the number of target tokens to get the average inverse logP.
The coordinator keeps the beam width at 2; each round, it gets candidate continuations from the model. For each completed sentence, it actually reads the inverse prompt probability and the forward generation log probability of the whole candidate. In this teaching adaptation, score = 0.5 × average inverse logP + 0.5 × (forward logP / number of generated tokens). The coefficients are fixed in advance; they are not claimed to be the paper's original settings. It re-ranks the candidates with this score.
Finish at two sentences or a 60-token limit. For each branch, the text, the inverse template used and the real score are kept. No file or network tool is needed; a local/model interface that supports probabilities is needed.
```

**Sample output**

Representative remaining branch: “Open books wait on the tables. Only the sound of turning pages can be heard.”

**What did we get?**

Candidate selection after the first sentence was also tied to the starting prompt. A nice-sounding text does not show that the score was actually computed.

### Hard

**Situation**

Even with a high inverse score, the text can distort a given fact.

**Prompt**

```text
Prompt: “Describe the hall's closing time. Correct record K1: 17:00.”
The coordinator applies at most 2 beams and 3 expansion rounds. Inverse template: prefix = "Text: [the whole actual candidate]. The request for this text:"; target = all tokens of the prompt “Describe the hall's closing time. Correct record K1: 17:00.” For each candidate, in the same model, it reads only the sum of the real log probabilities of the target tokens after this prefix; it ranks by score using the same target. It stores the prefix, the target and the measured score in the branch record.
Additional application check: If the final candidate contains a time that contradicts K1, reject it. Inverse probability is not a test of consistency with the source.
Even if “The hall closes at 18:00” scores high, do not publish it. If there is no source-consistent candidate after three rounds, say not found; do not have the model estimate the probability value.
```

**Sample output**

Representative result: the 18:00 candidate is eliminated in the source check; a 17:00 candidate, if there is one, can pass the separate check.

**What did we get?**

A checkable topic relationship and factual accuracy were not squeezed into the same score.

## Where should you stop?

The original work is on Chinese poetry and long-answer generation. Depending on the application, the inverse score is combined with additional terms such as length-normalized forward probability and poetic form; the simple scenario shows only the core inverse score. The examples here are not a measured adaptation of the method. Flipped Interaction is the model asking the user questions; Reversing CoT reconstructs the problem from the solution. The “inverse” here depends on real probability and decoding mechanics.

## Sources

- [Controllable Generation from Pre-trained Language Models via Inverse Prompting](https://arxiv.org/html/2103.10685) — Zou, Xu; Yin, Da; Zhong, Qingyang; Ding, Ming; Yang, Hongxia; Yang, Zhilin; Tang, Jie. 2021-03-19; version read 2021-11-09. Defines computing the probability of the original prompt from text generated by the same model and selecting beam candidates; does not show that a normal chat interface offers this access. Evidence level: relevant body sections of the original paper.
