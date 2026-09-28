# Few-shot

Show the behavior you want with a few correct input–output pairs.

## What is it?

Explaining what the labels mean is sometimes not enough. In few-shot use, you give the model a few solved examples and then the new input. The model uses the pattern in the context of that call; giving examples does not train the model's weights.

The examples should complement each other. If you show only easy cases, you may leave open how a borderline input should be handled. A wrong label is as visible as a correct example.

## When does it help?

It suits text labeling, a specific writing format or small data transformations. Start with representative examples whose correct answers you know.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You are sorting support messages by topic.

**Prompt**

```text
Label the message as billing, access or unclear. Write a single label.
Example: “The same product was billed twice.” → billing
Example: “I can't log in with my password.” → access
Example: “I need help.” → unclear
New message: “I can't get into my account.”
```

**Sample output**

access

**What did we get?**

The new message was carried into the same label language as the examples. Do not assume these three examples represent every support request.

### Medium

**Situation**

A message can contain two topics; if there is no topic, an empty list is needed.

**Prompt**

```text
List only the topics that are stated explicitly; use the order billing, access. Do not invent new topics.
“The invoice didn't arrive.” → [billing]
“I can't log in, and my invoice is also wrong.” → [billing, access]
“You are terrible.” → []
New message: “Login is fixed now, but the same charge was listed twice.”
Do not count a resolved issue as an open request. Add a short supporting quote next to the label.
```

**Sample output**

[billing] — “the same charge was listed twice”

**What did we get?**

The examples show not just the format but also the limits for multiple topics and empty answers. Whether “Login is fixed now” is correctly left out as an open fault still needs to be checked.

### Hard

**Situation**

A rule has changed: closed issues will no longer be labeled. One of the old examples contradicts the rule.

**Prompt**

```text
First check the examples against the new rule. Rule: label only issues that are still open; if the topic is unclear, [].
Example 1: “I can't log in.” → [access]
Example 2: “The invoice is fixed.” → [billing]
Example 3: “The invoice is fixed, but the login problem continues.” → [access]
Correct the contradicting example and give the reason in one sentence. Then label the message “The password problem is over; the invoice is still missing.” Do not imitate an example that is inconsistent with the rule.
```

**Sample output**

Example 2 → []; the billing issue is closed. New message → [billing]; the gap is still open.

**What did we get?**

A data error was caught before the example was copied further. In real use, you approve the current example set; a few successful responses are not a measure of overall accuracy.

## Where should you stop?

There is no single ideal number of examples. Order, label distribution and similarity to the new input can affect the result. In Analogical Prompting the model generates the example; here you provide the correct examples. Active Prompting, by contrast, uses separate samples to choose which examples a human should label.

## Sources

- [Language Models are Few-Shot Learners](https://arxiv.org/html/2005.14165) — Brown, Tom B.; Mann, Benjamin; Ryder, Nick; Subbiah, Melanie; Kaplan, Jared; Dhariwal, Prafulla; Neelakantan, Arvind; Shyam, Pranav; Sastry, Girish; Askell, Amanda; Agarwal, Sandhini; Herbert-Voss, Ariel; Krueger, Gretchen; Henighan, Tom; Child, Rewon; Ramesh, Aditya; Ziegler, Daniel M.; Wu, Jeffrey; Winter, Clemens; Hesse, Christopher; Chen, Mark; Sigler, Eric; Litwin, Mateusz; Gray, Scott; Chess, Benjamin; Clark, Jack; Berner, Christopher; McCandlish, Sam; Radford, Alec; Sutskever, Ilya; Amodei, Dario. 2020-05-28; version read 2020-07-22. Studies performing tasks with in-context examples on GPT-3; this is not the same operation as fine-tuning. Evidence level: relevant body sections of the original paper.
- [Prompt engineering | OpenAI API](https://developers.openai.com/api/docs/guides/prompt-engineering?api-mode=responses) — OpenAI. Publication date not verified. Recommends showing relevant examples in the prompt context; an implementation guide tied to current model choices. Evidence level: page body.
