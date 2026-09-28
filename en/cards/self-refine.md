# Self-Refine

Pass the first text through a separate critique call and correct it with concrete feedback.

## What is it?

Self-Refine links generation, feedback and revision calls together. The same model can do these jobs in different calls. The coordinator carries the original task, the latest text and the feedback; it stops when the set criterion is met or the budget runs out.

This loop is not model training. The model's own critique can be wrong; especially for factual questions where no new evidence comes in, thinking again does not guarantee accuracy.

## When does it help?

You can use it for clarity of writing, a format condition or a small testable change. First choose a checkable criterion instead of “better”.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

An announcement confuses an application with a confirmed registration.

**Prompt**

```text
The coordinator makes three separate calls.
1. Generate: “The form collects applications; a place is confirmed by email. Write one announcement sentence.”
2. Carry the task and the first text: “Check the application/confirmation distinction. Write only the concrete flaw and the direction of the fix.”
3. Carry the task, the text and the critique: “Write one sentence that fixes this flaw.”
A human checks the confirmation condition in the final sentence. After three calls, do not open a new round.
```

**Sample output**

Representative first text: “Fill in the form, and your place is ready.” Critique: the form looks like a confirmed registration. Revision: “Apply through the form; your place is confirmed by the confirmation email.”

**What did we get?**

The critique was tied to the sentence that changed. A human checks that the condition in the source is actually correct.

### Medium

**Situation**

As the text gets shorter, required information is lost.

**Prompt**

```text
Source: The workshop is free; participants bring the notebook, pens are provided. Target: at most 25 words.
After the generation call, give the source, the target and the text to a separate critique call. Have it check each of the fee/notebook/pens items as present or missing.
Add the same package and the check result to the revision call. Have it fill in only the missing information; do not ask for new details.
A human checks the word count and the three conditions. Finish with one revision; if it does not fit, report the conflict between constraints.
```

**Sample output**

Representative revision: “The workshop is free. Bring your notebook; pens are provided at the workshop.”

**What did we get?**

The shortening criterion did not override the accuracy condition. The word count of the real text can be counted separately.

### Hard

**Situation**

The first revision adds a new error; the loop must stay bounded.

**Prompt**

```text
Source: Registration is confirmed by email; the time is not yet set. The first draft is “The registration form is enough.”
The critique call should find only mismatches with the source. The revision call should correct using the source and the critique.
The coordinator should have the revision checked against the source again. If a new date such as “Saturday 10:00” appears in the revision, it should ask for one final correction: “Remove the time that is not in the source.”
At most two revisions; if the second check still finds a flaw, leave it to human review. The earlier flaw and the source should be carried into every revision.
```

**Sample output**

Representative intermediate revision: “Your registration for Saturday 10:00 is confirmed by email.” New flaw: the time was invented. Final text: “Your registration is confirmed by email; the time is not yet set.”

**What did we get?**

The revision producing a new error was also checked. Instead of an endless correction loop, there is a defined stopping limit.

## Where should you stop?

Self-Debug examines program behavior; in Rubber Duck the one explaining is a human. Critique/revision according to a principle in the Constitutional AI source may look similar, but the original Constitutional AI also includes supervised fine-tuning and RLAIF; these three calls do not perform that training.

## Sources

- [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/html/2303.17651) — Madaan, Aman; Tandon, Niket; Gupta, Prakhar; Hallinan, Skyler; Gao, Luyu; Wiegreffe, Sarah; Alon, Uri; Dziri, Nouha; Prabhumoye, Shrimai; Yang, Yiming; Gupta, Shashank; Majumder, Bodhisattwa Prasad; Hermann, Katherine; Welleck, Sean; Yazdanbakhsh, Amir; Clark, Peter. 2023-03-30; version read 2023-05-25. Defines the generate–feedback–revise calls and the passing of history; the results on seven tasks are not the success of every form of self-critique. Evidence level: relevant body sections of the original paper.
- [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/html/2310.01798) — Huang, Jie; Chen, Xinyun; Mishra, Swaroop; Zheng, Huaixiu Steven; Yu, Adams Wei; Song, Xinying; Zhou, Denny. 2023-10-03; version read 2024-03-14. Shows that self-correction without new external feedback can be limited and dependent on the initial setup. Evidence level: relevant body sections of the original paper.
- [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/html/2212.08073) — Bai, Yuntao; Kadavath, Saurav; Kundu, Sandipan; Askell, Amanda; Kernion, Jackson; Jones, Andy; Chen, Anna; Goldie, Anna; Mirhoseini, Azalia; McKinnon, Cameron; Chen, Carol; Olsson, Catherine; Olah, Christopher; Hernandez, Danny; Drain, Dawn; Ganguli, Deep; Li, Dustin; Tran-Johnson, Eli; Perez, Ethan; Kerr, Jamie; Mueller, Jared; Ladish, Jeffrey; Landau, Joshua; Ndousse, Kamal; Lukosuite, Kamile; Lovitt, Liane; Sellitto, Michael; Elhage, Nelson; Schiefer, Nicholas; Mercado, Noemi; DasSarma, Nova; Lasenby, Robert; Larson, Robin; Ringer, Sam; Johnston, Scott; Kravec, Shauna; Showk, Sheer El; Fort, Stanislav; Lanham, Tamera; Telleen-Lawton, Timothy; Conerly, Tom; Henighan, Tom; Hume, Tristan; Bowman, Samuel R.; Hatfield-Dodds, Zac; Mann, Ben; Amodei, Dario; Joseph, Nicholas; McCandlish, Sam; Brown, Tom; Kaplan, Jared. 2022-12-15. Defines principle-based critique/revision together with model training stages; it cannot be reduced to a chat loop alone. Evidence level: relevant body sections of the original paper.
