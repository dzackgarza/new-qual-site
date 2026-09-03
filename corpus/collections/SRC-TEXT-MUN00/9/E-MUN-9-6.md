---
schema: qual/card@1
id: E-MUN-9-6
kind: problem
title: Paradoxes of the set of all sets
classification:
  areas:
  - topology
  topics:
  - Infinite Sets and the Axiom of Choice
relations: []
review: draft
---

::: {.exercise}

Most of the famous paradoxes of naive set theory are associated in some way or other with the concept of the "set of all sets."
None of the rules we have given for forming sets allows us to consider such a set.
And for good reason—the concept itself is self-contradictory.
For suppose that $\mathcal{A}$ denotes the "set of all sets."

(a) Show that $\mathcal{P}(\mathcal{A})\subset \mathcal{A}$ ; derive a contradiction.

(b) (Russell's paradox.)
Let $\mathcal{B}$ be the subset of $\mathcal{A}$ consisting of all sets that are not elements of themselves;

$$
\mathcal {B} = \{A \mid A \in \mathcal {A} \text { and } A \notin A \}.
$$

(Of course, there may be no set $A$ such that $A \in A$ ; if such is the case, then $\mathcal{B} = \mathcal{A}$ .) Is $\mathcal{B}$ an element of itself or not?
:::
