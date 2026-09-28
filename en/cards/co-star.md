# CO-STAR

Make the context, objective and reader visible in the same short brief.

## What is it?

CO-STAR is a reminder of six fields: Context, Objective, Style, Tone, Audience and Response. You can use these fields to check the preferences left out of a writing request.

Style describes how the text is built; tone describes the attitude it takes toward the reader. You do not need to invent details you do not know in order to fill the fields. This is a brief structure; it does not set up a search, an agent or an automatic evaluation algorithm.

## When does it help?

It is useful for announcements, explanations, editing briefs and texts aimed at different readers. Separate factual information from writing preferences from the start.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will write an announcement about a library study room.

**Prompt**

```text
Context: The library's study room is closed for maintenance on Tuesday, 14:00–16:00.
Objective: Visitors should not come during the closed hours.
Style: Plain announcement.
Tone: Calm and direct.
Audience: Everyday visitors.
Response: At most two sentences; state the closing window exactly. Do not add information about other services.
```

**Sample output**

The study room is closed for maintenance on Tuesday between 14:00 and 16:00. You can plan your visit outside these hours.

**What did we get?**

The reader, the time and the objective can be seen together. Before the announcement goes out, the person responsible confirms the maintenance information.

### Medium

**Situation**

The same maintenance information goes to two readers; the staff note needs an action.

**Prompt**

```text
Context: The study room is under maintenance on Tuesday, 14:00–16:00. Deniz is responsible for the key.
Objective: Inform visitors; remind staff to prepare.
Style: Short, explanatory. Tone: Polite, unhurried.
Audience: One version for visitors, one for staff.
Response: Two separate short texts. The staff note should include the step of asking Deniz for the key. Do not add staff names to the visitor text. Do not invent additional closures.
```

**Sample output**

Visitors: The study room is closed for maintenance on Tuesday between 14:00 and 16:00.

Staff: For the Tuesday 14:00–16:00 maintenance, ask Deniz for the study room key.

**What did we get?**

The same fact serves two different jobs. The audience field changed which details go into each text.

### Hard

**Situation**

Being short conflicts with explaining an important condition.

**Prompt**

```text
Context: The workshop is free; participants bring their own materials. The registration form collects applications; places are confirmed by email.
Objective: The fee and registration conditions should not be misunderstood.
Style: One paragraph, everyday English. Tone: Inviting, without exaggeration.
Audience: Adults attending for the first time.
Response: At most 35 words. Free participation, responsibility for materials and email confirmation must all be included. Do not delete a condition for the sake of the word limit; if it does not fit, report the conflict.
```

**Sample output**

Joining the workshop is free; please bring your own materials. You can apply by filling in the form. Your place is confirmed when the confirmation email arrives.

**What did we get?**

The short text keeps three pieces of decision information. If the actual materials list lives elsewhere, you can add its link later; the model did not invent it.

## Where should you stop?

You do not need to expand every CO-STAR field for every task. A technical coding task may need acceptance criteria more than a poetic description of tone. Sheila Teo attributes the framework to the GovTech team; here we make no claim of a single inventor or of measured universal superiority.

## Sources

- [Mastering the art of prompt engineering with Empower | Government Technology Agency of Singapore (GovTech Singapore)](https://www.tech.gov.sg/technews/mastering-the-art-of-prompt-engineering-with-empower/) — GovTech Singapore. 2025-04-03. An institutional source explaining how GovTech uses the CO-STAR fields. Evidence level: page body.
- [How I Won Singapore's GPT-4 Prompt Engineering Competition | Towards Data Science](https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41/) — Sheila Teo. 2023-12-29; version read 2025-01-28. Supports Teo's practitioner account and the GovTech attribution; a competition experience is not comparative evidence that transfers to all work. Evidence level: page body.
