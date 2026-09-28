# Teachable agent

Let the model keep the student role with a limited knowledge state; you are the one explaining.

## What is it?

In the teachable agent approach, a human teaches a topic to an artificial student. AlgoBo, in TeachYou, uses a flow that regulates the knowledge state and response behavior; it is more comprehensive than just the sentence “pretend you don't know”. The model's weights are not trained by this chat.

## When does it help?

For noticing the knowledge you assume and the gaps in your explanation while teaching a concept.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will explain to an artificial student what a loop does.

**Prompt**

```text
Human teacher; model student simulation. This is not the full TeachYou system but a limited chat adaptation.
Knowledge state: You know lists; you don't know loops yet. Do not reason as if you knew concepts I have not explained to you. My explanation: "A loop does the same thing for each item in the list."
Say in one sentence only what you understood from this explanation; then ask a single why/how question. Wait for my answer. In at most two rounds, let's summarize together what changed in the knowledge state.
```

**Sample output**

Student: “The same operation is applied to each item. How many times does it run if the list is empty?” Human: “It doesn't run at all.”

**What did we get?**

The person teaching had to add the boundary case to their explanation.

### Medium

**Situation**

The student simulation must not act as if it knows more than the teacher said.

**Prompt**

```text
Application state: known=[list, loop], open_concepts=[condition], taught=[].
Human explanation: "To pick the positive numbers, we check whether each number is greater than zero."
Stage 1, a separate model call: Make a short state proposal of which concept this explanation taught and which uncertainty it left.
The supervisor should store the approved state update. Stage 2, a separate response call: Give a student answer using only this state; check with a question whether zero is included.
After the human's answer, one more round can be done; stop at 4 model calls in total. Do not claim to remember state that was not saved.
```

**Sample output**

Student: “I'm taking the ones greater than zero; is zero left out?” The teacher's answer is added to the next knowledge record.

**What did we get?**

The student role was bounded by a visible state; where the knowledge came from was tracked.

### Hard

**Situation**

The teacher has a wrong generalization; a helper channel should support the teaching.

**Prompt**

```text
Design a stateful teachable agent and a separate teaching helper. Topic: finding the largest number in a list. Human: "The largest value starts at 0."
The student response call should briefly say how it would handle the list [-5,-2] with the rule it has learned; it should not give the fully correct solution from outside knowledge.
A separate helper call should examine the conversation and the topic rule; it should give the teacher only a suggested counterexample question. Do not present the helper message as the student's answer.
When the human corrects the explanation, the state should be updated; a teaching check should be done with a new negative list. At most two teaching rounds; do not declare a learning gain without a final independent human exercise.
```

**Sample output**

If the student heads toward the result 0, the helper suggests the question to the teacher: “If all the numbers are negative, what should the starting value be?”

**What did we get?**

The error in the teacher's explanation and the helper's role were seen in separate channels.

## Where should you stop?

A model talking like a student is not a real independent student or weight training. AlgoBo's finding about knowledge-building conversation should not be confused with a post-test gain. The learning results of a separate music education study are not the results of this coding system either.

## Sources

- [Teach AI How to Code: Using Large Language Models as Teachable Agents for Programming Education](https://arxiv.org/html/2309.14534) — Jin, Hyoungwook; Lee, Seonghee; Shin, Hyungyu; Kim, Juho. 2023-09-25; version read 2024-03-11. Defines the TeachYou/AlgoBo flow that limits the knowledge state and regulates Reflect–Respond and questioning behavior; conversation measures are not the same as a learning test. Evidence level: relevant body sections of the original paper.
- [Exploring the Impact of an LLM-Powered Teachable Agent on Learning Gains and Cognitive Load in Music Education](https://arxiv.org/html/2504.00636) — Jin, Lingxi; Lin, Baicheng; Hong, Mengze; Zhang, Kun; So, Hyo-Jeong. 2025-04-01. A teachable agent study in a separate music education context; its results do not carry over to AlgoBo's coding study. Evidence level: relevant body sections of the original paper.
