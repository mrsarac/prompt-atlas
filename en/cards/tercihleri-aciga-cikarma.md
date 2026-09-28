# Eliciting preferences

Do not ask for a preference as a single label; bring it out through trade-offs.

## What is it?

Eliciting preferences tries to understand what a person prioritizes through concrete options and comparisons. Instead of guessing your preferences, the model asks questions; if there is a contradiction, it leaves it visible.

## When does it help?

In decisions where words like “high quality”, “comfortable” or “right for me” mean different things for different options.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will choose a place to work on your writing.

**Prompt**

```text
Options: A the library, quiet and 20 minutes away; B home, no travel but occasional noise. My goal is to write for 90 minutes.
Do not infer my preference for me. Ask a single question that would clarify my choice between quiet and travel time, and wait for my answer. Then summarize the priority I stated in one sentence; confirm my decision.
```

**Sample output**

Model: “For a 90-minute session without interruptions, would you accept spending 40 minutes in total on travel?” Human: “Not today.” Summary: “Today, reducing lost time has higher priority.”

**What did we get?**

The preference was tied to today's conditions rather than a permanent personality label.

### Medium

**Situation**

Two priorities pull in opposite directions.

**Prompt**

```text
Laptop preferences: Lightness is very important; a big screen is also very important. Option A 1.2 kg/13 inches; B 1.8 kg/16 inches. Assume the other features are the same.
First ask in which usage situation each of these two priorities dominates. Answer: I carry it four days a week, and I mostly write long texts at home.
Then ask whether an external screen can be used; do not assume. After at most two questions, write a conditional preference summary; do not finalize a product recommendation.
```

**Sample output**

“Carrying is frequent; long writing happens at home. If a screen is available at home, the preference for lightness may get stronger; if not, the cost of the small screen should be weighed separately.”

**What did we get?**

The conflicting preferences were opened up through the context of use.

### Hard

**Situation**

The same person makes different choices under different conditions.

**Prompt**

```text
Decision: A weekly team meetup. My earlier answer: Face-to-face communication is important. My new answer: If travel takes more than 1 hour, it should be online. Attendance is not mandatory.
Write the preference record as a conditional rule rather than a fixed verdict. Ask at most two boundary examples: 40 minutes of travel; 75 minutes of travel. Wait for my answers; do not silently correct a contradiction.
In the final summary, separate hard constraints, preferences and open uncertainty. Do not assume the other team members share my preference; do not create a meeting.
```

**Sample output**

“Preference: face-to-face if the travel is reasonable. Condition: online when it exceeds 1 hour. The other members' preferences are unknown.”

**What did we get?**

The human preference was not reduced to a single context-independent score.

## Where should you stop?

This arrangement can help measure preferences; it does not carry the claim “I know your true wishes better than you do”. The human preference evaluation in the COPE source and offline inference success are different measures. The summary the model gives may need the human's explicit confirmation.

## Sources

- [When and How to Ask: Dynamic Preference Elicitation Strategies for Conversational Recommendation](https://arxiv.org/html/2607.06765v1) — Xia, Feng; Zhang, Shuo; Wang, Xi. 2026-07-07. Examines the approach to eliciting preferences through conversation and its evaluation; human preference findings and offline model measurements are not mixed up. Evidence level: relevant body sections of the original paper.
