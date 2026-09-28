# Joint ideation

Run ideation together with the human's own ideas and explicit constraints.

## What is it?

In joint ideation, the human and the model propose, transform and eliminate new options. Suggestions from the same model can cluster around similar points; so it helps to keep the human's first ideas and selection criteria visible.

## When does it help?

To widen the space of options when looking for a writing topic, an event format or a product idea.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You are looking for ideas for a book club meeting.

**Prompt**

```text
My first ideas: a short quotation round; everyone brings one question. Constraint: 8 people, 45 minutes, no extra materials.
First keep my two ideas. Then generate three ideas that work differently from these; describe each in two sentences. Do not settle for giving the same idea a new name. At the end, state which idea strains which constraint.
```

**Sample output**

Candidates: “Discussing a character's decision from two different angles; writing questions silently and picking them in turn; rebuilding one section of the book with a different ending.”

**What did we get?**

The options widened without the human's ideas getting lost among the model's suggestions.

### Medium

**Situation**

The model's first ideas are too similar to each other.

**Prompt**

```text
Task: A 30-minute team learning activity. First suggestions: mini presentation, short presentation, quick presentation. Acknowledge that these repeat the same mechanism.
In a new round, generate three different participation formats: everyone trying alone; explaining to each other in pairs; the whole group producing a shared output. In each, make the duration, the participants' action and the resulting output clear. Do not give made-up efficiency scores.
```

**Sample output**

“10 minutes of individual problem + 10 minutes of comparison + 10 minutes of drawing lessons” and “teach-back in pairs” are separated as different action formats.

**What did we get?**

Variety moved from a change of title to a change of behavior.

### Hard

**Situation**

When choosing ideas, novelty and feasibility conflict.

**Prompt**

```text
Goal: Make it easier for first-time library visitors to find their way. Constraints: One week of preparation, no new software, a budget of 500 TL. Human ideas: a map at the entrance; a volunteer welcome hour.
First generate five different ideas; then eliminate all of them, including the human's ideas, against the current constraints. Do not write unmeasured estimates of impact. For each remaining idea, propose one small trial and an observable success criterion.
Do not implement, purchase or send messages before the human makes a choice. Do not remove constraints for the sake of novelty.
```

**Sample output**

“Observation for the entrance map: can a new visitor find the target section without help? Limit of the volunteer hour: support only at certain times.”

**What did we get?**

The list of ideas turned into feasible options and proposals for measurable trials.

## Where should you stop?

AI help can support individual creative output in some contexts while reducing collective diversity; this is not a single result for all creative work. Do not say that an idea the model generated is new, original or has never been done before without researching it.

## Sources

- [Generative AI enhances individual creativity but reduces the collective diversity of novel content](https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532/) — Anil R Doshi; Oliver P Hauser. 2024 Jul 12. Examines how, in a short-story writing experiment, individual creative ratings and collective diversity can change in different directions; does not generalize to all creative fields. Evidence level: relevant body sections of the original paper.
- [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT](https://arxiv.org/html/2302.11382) — White, Jules; Fu, Quchen; Hays, Sam; Sandborn, Michael; Olea, Carlos; Gilbert, Henry; Elnashar, Ashraf; Spencer-Smith, Jesse; Schmidt, Douglas C.. 2023-02-21. Provides a source for the alternative-generation pattern; not a guarantee of originality or commercial success. Evidence level: relevant body sections of the original paper.
