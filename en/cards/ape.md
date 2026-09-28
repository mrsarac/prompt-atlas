# Automatic Prompt Engineer

Generate candidate instructions; choose which one works based on the target model's real outputs.

## What is it?

Automatic Prompt Engineer generates instruction candidates from example input–output pairs and evaluates them on the target task. The model that writes a candidate and the model that applies it do not do the same job. The score comes from comparing the output obtained with the correct answer, not from the candidate praising itself.

A human sets the dataset, the criterion and the call budget. In automation, a program that runs these jobs is needed. The small datasets below teach the mechanism; they are not enough for a sound performance estimate.

## When does it help?

It suits repeated classification and data transformations. You need development examples with known correct answers and separate check examples that are not used in selecting candidates.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

A support labeling prompt is to be selected.

**Prompt**

```text
The coordinator gives the development pairs: “I can't log in”→access; “The invoice is wrong”→billing.
Generator call: “Propose two different complete instructions that perform this transformation. The only output field is access/billing.”
Run each candidate separately on the target model with the two inputs. Match the four real outputs with the correct label; use the number of matches as the score.
Choose the best candidate; in a tie, take the shorter one. At most one generator + four target calls. Do not score a candidate that has not been run.
```

**Sample output**

Representative candidate: “Write the explicit topic of the message as access or billing; add no other text.” If the representative results are correct, it would be 2/2; that score was not measured here.

**What did we get?**

It is clear which observation the choice of instruction will rest on. No general conclusion about success can be drawn from two examples.

### Medium

**Situation**

Unclear messages are being mislabeled.

**Prompt**

```text
Development: “I can't log in”→access; “The invoice came twice”→billing; “Help me”→unclear.
Ask the generator for two candidates; the unclear class and a single-label output are mandatory.
Run each candidate on the three development inputs; calculate the exact-match score from the real results. After selection, freeze the prompt.
Separate check: “My password is not accepted”→access; “I don't know what to do”→unclear. Do not show these two inputs to the candidate generator.
Budget 1+6+2 calls. If the check result is low, do not declare success; do not copy the test examples into the prompt.
```

**Sample output**

Representative good candidate: “If the topic is not explicit, choose unclear.” The check outputs should be access/unclear; real accuracy can only be calculated after running.

**What did we get?**

The data for choosing a candidate and for testing that choice were separated. The unclear class stopped being just a label tacked on afterwards.

### Hard

**Situation**

A short output and a source-based justification are two separate acceptance conditions.

**Prompt**

```text
Development inputs: “The invoice is wrong”→billing|The invoice is wrong; “I can't log in”→access|I can't log in; “Help”→unclear|Help.
The generator proposes three instruction candidates. The target model processes the three examples with each candidate. Software first checks the label|quote format, then label correctness and whether the quote appears in the input.
A candidate that breaks the format is eliminated; the rest are ranked by the number of correct records. Independent check input: “I can't get into my account”→access; the justification must be a short quote from the input.
Limit of one generator, nine development and one check call. A prompt that does not pass the check is not put into automatic use.
```

**Sample output**

Representative `access|I can't get into my account` is acceptable. `access|wrong password` fails because the quote is not in the source.

**What did we get?**

Format and evidence errors that a single success count could hide are checked separately. The decision to put the prompt into use is still with the coordinator.

## Where should you stop?

Overfitting to development data and test data leaking into candidate generation are easy to fall into. A general meta prompt can only write instructions; APE adds real evaluation of candidates. OPRO, in turn, explicitly carries earlier candidates and scores into the next generation.

## Sources

- [Large Language Models are Human-Level Prompt Engineers](https://arxiv.org/html/2211.01910) — Zhou, Yongchao; Muresanu, Andrei Ioan; Han, Ziwen; Paster, Keiran; Pitis, Silviu; Chan, Harris; Ba, Jimmy. 2022-11-03; version read 2023-03-10. Defines generating instruction candidates, evaluating them on the target model and selecting them; the Instruction Induction/BIG-Bench findings are not superiority on every task. Evidence level: relevant body sections of the original paper.
