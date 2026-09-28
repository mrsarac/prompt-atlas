# RUNE

Turn a scattered request into a layered instruction structure with a known version.

## What is it?

RUNE is an open-source prompt structuring project signed by Mustafa Saraç / NeuraByte Labs. Its public README describes an approach that organizes requests into eight layers, and the tools that use it. The examples here apply the layer idea by hand; they do not assume that the tools were installed or that a provider was called.

## When does it help?

When the goal, context, limits and output format keep getting mixed up in the same job. A clear one-sentence question may not need eight sections.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You will turn the request “Make this note into an announcement” into a clear instruction.

**Prompt**

```text
Organize the task below with the RUNE README/RUNE.md L0–L7 names; do not carry out the task yet. Do not add missing facts. This is an example of templating by hand.
Raw request: Watercolor workshop 12 October 14:00, 8 people; make a two-sentence announcement.
L0 System Core: task role. L1 Context: the given information. L2 Intent: the goal.
L3 Governance: limits. L4 Cognitive Engine: short working method, not a dump of hidden thinking.
L5 Capabilities: available tools. L6 Quality Assurance: checks.
L7 Output & Meta: output format.
A human should compare the eight fields with the raw request. They should give the approved instruction to a second call and have the announcement produced; stop after one structuring call and one execution call.
```

**Sample output**

“L0: Announcement editor. L1: Watercolor, 12 October 14:00, 8 people. L2: Describe how to take part. L3: Do not invent a venue/fee. L4: Extract the information, write it in two sentences. L5: No tools. L6: Check the date/time/capacity. L7: Two sentences.”

**What did we get?**

A reusable task frame was created without producing new information.

### Medium

**Situation**

You will adapt a review prompt to the working area.

**Prompt**

```text
A human initiator; use the L0–L7 structure. Task: Review the given shipping rule.
Context: The code is total > 500 ? 0 : 50; the rule is 500 and above ships free. Permission: proposal only, no writing to files. Tools: none.
Place this information in the appropriate spots of the layered instruction. The check field should include the expected values 50/0/0 for the inputs 499/500/501. Output: the problem, the smallest patch proposal, how to check it.
A human should verify the permission field; they should give the frame and the code together to a second call. Stop after the review output. If no test was run, do not write as if it had been.
```

**Sample output**

Review: “The 500 boundary is left out; `>=` is recommended. The expected boundary values are 50/0/0. No real test was run for this response.”

**What did we get?**

The layers carried permissions and check expectations as well as the role.

### Hard

**Situation**

A team with more than one template wants to prevent version confusion.

**Prompt**

```text
Human-supervised local design: Document the template choice without running tools.
Option A: RUNE README/RUNE.md L0–L7: System Core, Context, Intent, Governance, Cognitive Engine, Capabilities, Quality Assurance, Output & Meta.
Option B: prompts/README.md MP v4.3 L1–L8: Identity, Mission, Constraints, Methodology, Output, Error Taxonomy, Personalization, Context.
Task: A sourced summary of three weekly notes. Notes N1="Setup done", N2="Test pending", N3="No permission to publish".
Choose A; write the template name/version family into the record. Do not paste B's numbering into A. The generation call should receive only the approved frame and N1-N3. A separate check call should match each claim to a note ID. At most 3 calls; no publishing tool. If there is a completion statement without evidence, leave it to human correction.
```

**Sample output**

“Setup done [N1]. Test pending [N2]. No permission to publish [N3].” Template record: “README/RUNE.md L0–L7 family; not mixed with MP v4.3 L1–L8.”

**What did we get?**

It was not assumed that similar eight-part structures share the same version or the same section mapping.

## Where should you stop?

RUNE is not a universal guarantee of success or, on its own, model training. The project's own evaluation score does not count as independent evidence of correctness. A master prompt is the main working instruction that provides continuity; meta prompting works on the structure of a task or prompt; RUNE is one implementation of this with specific layers and tools. Version and layer names in the public documents may differ from one another.

## Sources

- [RUNE: project description and eight layers](https://github.com/neurabytelabs/rune/blob/main/README.md) — Mustafa Saraç / NeuraByte Labs. Publication date not verified. Defines the project's eight-layer request transformation approach and tool scope; no claim of effectiveness or model superiority is made here. Evidence level: local original document of the public project; no new remote version confirmation.
- [RUNE.md: L0–L7 instruction structure](https://github.com/neurabytelabs/rune/blob/main/RUNE.md) — Mustafa Saraç / NeuraByte Labs. Publication date not verified. Gives the names and roles of the L0–L7 layers; the README's version label and this file's version label are not assumed to be equal. Evidence level: local original document of the public project; no new remote version confirmation.
- [MP v4.3 Prompt Library: L1–L8 templates](https://github.com/neurabytelabs/rune/blob/main/prompts/README.md) — Mustafa Saraç / NeuraByte Labs. Publication date not verified. Defines the separate L1–L8 schema in the MP v4.3 library; no one-to-one number mapping to L0–L7 is made. Evidence level: local original document of the public project; no new remote version confirmation.
