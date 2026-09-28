# Teach-back

Explain back what you understood in your own words; check where the explanation fell short.

## What is it?

Teach-back is asking the other person to explain back, in their own words, the information they were given. The goal is not to catch the person out as in an exam, but to see whether the explanation was understandable. The LLM use here is a teaching adaptation of a human communication method.

## When does it help?

To see whether, after reading a usage rule or a sequence of steps, you are really able to apply it.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You are learning a rule for saving files.

**Prompt**

```text
Rule: First save the work to the drafts folder. Once it has been checked, copy it to the final folder; do not delete the draft.
Briefly explain the rule to me, then ask me to explain it back in my own words. Wait for my answer; if a step is missing, correct your explanation and ask me to explain it back again. Do not present this as an exam that measures my intelligence.
```

**Sample output**

Human: “I save it to the final folder and delete the draft.” Model: “I may not have explained it clearly enough: you need to save to the drafts first and keep it. How would you explain the order again?”

**What did we get?**

The misunderstanding became visible without judgment.

### Medium

**Situation**

A returns rule has an exception.

**Prompt**

```text
Rule text: An unused product can be returned within 14 days. Custom-made products are excluded. This is only a fictional shop rule.
First give a short explanation. Then ask "How would you explain to a friend which products they can return and within what period?" Wait for my answer. If I left out the period or the exception, explain only that part again; at most two explain-back rounds.
```

**Sample output**

Human: “We return everything within 14 days.” Model: “You got the period right. The rule applies only to unused products; custom-made products are excluded. Could you explain it again in your own sentence?”

**What did we get?**

The scope and the exception that got lost in the general sentence were checked.

### Hard

**Situation**

In a workflow, different error cases need different steps.

**Prompt**

```text
Fictional process: If a file upload has a "format error", export it again as PDF; if there is a "connection error", retry once. On a second connection error, open a support ticket. Do not resend the same file repeatedly.
First explain the process; then ask me to describe two cases in my own words: the format error and the second connection error. Do not show the solution before I answer.
Check the answers against the rule; briefly re-explain the missing branches and ask for another explain-back in a different order. At most three rounds; do not do a real upload or send a support message.
```

**Sample output**

If the human says to retry on a format error, the model explains the PDF step again. The condition of stopping at the second connection error and preparing a support ticket is checked separately.

**What did we get?**

Not just a memorized order, but the action that changes by condition was understood.

## Where should you stop?

The source is AHRQ's guide to human health communication; this card does not give medical advice and does not offer evidence of learning gains with an LLM. Self-explanation opens up the “why?” connections; teach-back checks how the person understood what they were told. The possibility that the model misinterprets the source rule must be checked separately.

## Sources

- [Use the Teach-Back Method: Tool #5](https://www.ahrq.gov/health-literacy/improve/precautions/tool5.html) — Agency for Healthcare Research and Quality. Publication date not verified. Defines the method of checking understanding by having a person explain back, in their own words, what they need to know/do; not an experiment on LLM effects. Evidence level: page body.
