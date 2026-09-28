# Rubber Duck

Look for the missing point by explaining what you want to do and which steps you follow.

## What is it?

You expect a certain result from your code, but when it runs, a different result comes out. In the Rubber Duck method, you first explain your expectation, then the steps of the code, to a listener. While explaining, you may notice a missing condition between two steps you had linked in your head. You can approach the line of thought in a piece of writing, or a work plan, the same way.

The rubber duck in the classic practice is silent. Here we adapt it with a language model: you explain, the AI listens; when you finish, it can ask a question that clarifies a point you explained. In this adaptation we limit it to one question. We do not ask it to prepare the solution. You describe the gap, and you check whether the explanation you found is correct outside the chat.

## When does it help?

You can try it when examining why an announcement is misunderstood, under which condition code behaves differently, or how agents hand work to each other. To start, you need enough information to explain your goal and the steps you follow.

## Examples

The dialogues below are representative examples written to show the method; they are not the results of real trials.

### Simple

**Situation**

You are writing an announcement for a twenty-person workshop. The form collects applications, and places are confirmed later by email. But someone reading the announcement thinks their place is confirmed once they submit the form.

**Prompt**

```text
I am going to explain how I expect my announcement to be understood and what I wrote. You listen. Wait until I say “done”; then, based on something I said, ask only one clarifying question and wait for my answer. Do not write a solution, speculate, run tests or use tools.

The workshop has 20 places. I want people to apply through the form. We will review the applications and send a confirmation email to those we can give a place to. In the announcement I wrote “Fill in the form, and your place at the workshop is ready.” A reader says they submitted the form and therefore reserved a place. I had thought of the form as the application step. done
```

**Sample dialogue**

**AI:** When you say “your place is ready”, do you mean the moment the form is submitted, or the moment the confirmation email arrives?

**Me:** The email. But my sentence says the form is enough. I'll write “Apply through the form; your place is confirmed when the confirmation email arrives.”

**What did we get?**

There is a new sentence that separates applying from confirmed registration. Before publishing, I should check against the registration guidelines that the confirmation email really means this.

### Medium

**Situation**

On a shopping site, shipping should be free for orders of 500 TL and above. A shipping fee is being added to a basket of exactly 500 TL. You know the amounts are numeric and no discount is applied.

**Prompt**

```text
I am going to explain the shipping calculation to you. Wait until I say “done”. Then, based on a point in my explanation, ask a single clarifying question and wait for my answer. Do not find the bug for me, and do not produce a solution or a guess; do not run code, run tests or use tools.

My rule is free shipping for orders of 500 TL and above. In the JavaScript code I use the condition total > 500: if true, shipping is 0 TL, otherwise 50 TL. The total is a numeric value, and there is no discount. For a basket of exactly 500 TL, I see 50 TL shipping. First I take the total, then I choose the shipping with this condition and add it to the amount. done
```

**Sample dialogue**

**AI:** What behavior does the phrase “500 TL and above” in your rule describe for exactly 500 TL?

**Me:** Free shipping. I wrote `>`; I left equality out. I'll change the condition to `>=` and check that it also covers the amount at the boundary.

**What did we get?**

There is a concrete fix to check. In my own environment, I should run the shipping calculation for 499, 500 and 501 TL. My expectation is 50, 0 and 0 TL respectively; these are not yet test results.

### Hard

**Situation**

One agent produces a draft from source notes, and a second agent edits the text. Only `draft.md` may be changed. After the second stage, `archive.md` also appears in the change list; yet the final message says the job is complete.

**Prompt**

```text
I am going to describe the two agents' workflow; do not run this workflow. Wait until I say “done”. Then ask a single clarifying question based only on a step I described, and wait for my answer. Do not propose a solution, speculate or run tests; do not start agents, read or change files, or use tools.

I told the first agent to read the source notes and write only to the file draft.md. I passed the draft to the second agent and said “Edit the documents, and say complete when you're done.” I expect both of them to change only the file draft.md. In the change list after the second stage, archive.md is there too. I accepted the job by looking at the final message saying “complete”. done
```

**Sample dialogue**

**AI:** In the “edit the documents” instruction you gave the second agent, how did you specify which files could be changed?

**Me:** I didn't; I assumed it knew the first agent's limit. On top of that, I looked at the final message and didn't review the file changes when accepting. I should also explicitly add permission to write only to `draft.md` to the second instruction.

**What did we get?**

We identified the file limit that was missing from the handoff. Where the `archive.md` change came from still needs checking: I should compare the stage logs and file diffs against the list of permitted files. Correcting the instruction does not, on its own, technically restrict file access.

## Where should you stop?

If the model starts producing a solution, it takes the explaining over from you. The model reviewing and fixing its own code falls under Self-Debug; here, you are the one explaining. The guiding question sequence in Socratic tutoring, or asking the model to teach a simple lesson, is also a different interaction. The gap you find in a chat may sometimes be a wrong assumption; check it with documents, working code or operation logs. Remove sensitive details before sharing private code and logs.

## Sources

- [Rubber Duck Debugging](https://rubberduckdebugging.com/) — rubberduckdebugging.com; the page names “~Andy” for the original contribution. Publication and update dates unknown; the inventor or date of origin is not verified. Supports the practice of a person explaining the expected behavior and the code's steps to a silent duck.
- ["It's like a rubber duck that talks back": Understanding Generative AI-Assisted Data Analysis Workflows through a Participatory Prompting Study](https://arxiv.org/html/2407.02903) — Ian Drosos, Advait Sarkar, Xiaotong Xu, Carina Negreanu, Sean Rintel and Lev Tankelevitch; 3 July 2024. Studies human–AI data analysis workflows. It is not a success test of the prompts here or evidence of a causal effect of the single-question adaptation.
- [Teaching Large Language Models to Self-Debug](https://arxiv.org/html/2304.05128) — Xinyun Chen, Maxwell Lin, Nathanael Schärli and Denny Zhou; first published 11 April 2023, updated 5 October 2023. Covers a model explaining and fixing a program it generated itself; supports the difference in roles from a human's Rubber Duck practice.
