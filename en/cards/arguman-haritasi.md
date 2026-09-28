# Argument map

See the claim, its support and its objection as separate nodes.

## What is it?

An argument map organizes the reasons supporting a view and the objections directed at it, together with their connections. The model can map a text; drawing a connection does not prove that the support is correct.

## When does it help?

When everyone in a long discussion is responding to a different claim, or opinion and evidence are getting mixed up.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will break down a short decision rationale.

**Prompt**

```text
Text: "We should hold the workshop in the morning because three participants preferred the morning. But we don't know the preference of the other five."
Extract the fields claim, support, objection/information gap. Match each quote with the phrase in the text. Then write the connections in plain text: support -> claim; objection -> which support or inference? Do not add new participant preferences.
```

**Sample output**

“Claim: let's do it in the morning. Support: three people preferred the morning. Gap: the other five are unknown. The gap objects to generalizing the preference to the whole group.”

**What did we get?**

The real weak link of the discussion became visible.

### Medium

**Situation**

The same support has been tied to two different conclusions.

**Prompt**

```text
A: "Three people couldn't find their notes; let's add a tagging system." B: "The same observation could also support making the search box more visible."
Generate nodes: the shared observation, A's solution claim, B's solution claim, the assumption of each connection. Give them the IDs D1, I1, I2, V1, V2. Do not treat the assumptions as observed evidence.
At the end, write a single observation question that would distinguish between the two paths; do not finalize the solution.
```

**Sample output**

“The D1→I1 connection assumes a classification problem; the D1→I2 connection assumes a search visibility problem. What does the user do when looking for a note?”

**What did we get?**

Shared data was not presented as leading to a single necessary conclusion.

### Hard

**Situation**

In a group discussion, normative preferences and empirical claims must be separated.

**Prompt**

```text
Texts: A="Recording the meeting makes later access easier." B="Privacy matters more to me than ease of access." C="Everyone will agree to being recorded." Available data: The participants have not been asked yet.
Produce a map of claims, value preferences, evidence needs and objections. Do not classify B as misinformation; do not treat C as a verified consensus. Add the speaker and the textual support to each node.
The result should be a map and open questions. Do not produce a vote or recording permission. If a link in the map is uncertain, write "possible relationship" instead of a definite arrow.
```

**Sample output**

“B is a value preference; C is a generalization that needs evidence. C has no support. A's possible benefit does not logically invalidate B's preference.”

**What did we get?**

The factual, value and permission dimensions of the discussion stayed separate.

## Where should you stop?

Only the abstract and citation of the LLM-assisted argument mapping publication in the source set could be read; no detailed experimental or effectiveness results are claimed. Even if a map looks good, it can contain missing or wrong connections; it must be checked against the original speakers' text.

Names such as steelman, devil's advocate and counterfactual can point to different moves in a discussion. Since separate method origins or LLM effects have not been verified for this selection, they are not treated as synonyms of the argument map or the premortem.

## Sources

- [A Hybrid Human-AI Approach for Argument Map Creation From Transcripts](https://aclanthology.org/2024.delite-1.6/) — Lucas Anastasiou; Anna De Liddo. 2024-05. Supports, at abstract level, the scope of an LLM-assisted argument mapping study; since the PDF body was not read, no method details or effect claims are made. Evidence level: abstract and citation.
