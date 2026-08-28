---
schema: qual/card@1
id: E-MUN-1-5
kind: exercise
title: Membership in unions and intersections of collections
classification:
  areas:
  - topology
  topics:
  - Fundamental Concepts
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Let $\mathcal{A}$ be a nonempty collection of sets.
Determine the truth of each of the following statements and of their converses:

(a) $x \in \bigcup_{A \in \mathcal{A}} A \Rightarrow x \in A$ for at least one $A \in \mathcal{A}$ .

(b) $x \in \bigcup_{A \in \mathcal{A}} A \Rightarrow x \in A$ for every $A \in \mathcal{A}$ .

(c) $x \in \bigcap_{A \in \mathcal{A}} A \Rightarrow x \in A$ for at least one $A \in \mathcal{A}$ .

(d) $x \in \bigcap_{A \in \mathcal{A}} A \Rightarrow x \in A$ for every $A \in \mathcal{A}$ .
:::

::: {.solution}
**Goal.** Determine the truth of each statement and its converse.

<1>1. (a) $x \in \bigcup_{A \in \mathcal A} A \Rightarrow x \in A$ for at least one $A \in \mathcal A$: TRUE.
Proof: this is the definition of union: $x$ is in the union iff it is in at least one member.
<2>1. Converse: $x \in A$ for at least one $A \Rightarrow x \in \bigcup A$: TRUE.
Proof: also the definition of union.

<1>2. (b) $x \in \bigcup_{A \in \mathcal A} A \Rightarrow x \in A$ for every $A \in \mathcal A$: FALSE.
Proof: $x$ need only be in one member, not all.
<2>1. Converse: $x \in A$ for every $A \Rightarrow x \in \bigcup A$: TRUE.
Proof: if $x$ is in every member, it is in at least one, hence in the union.

<1>3. (c) $x \in \bigcap_{A \in \mathcal A} A \Rightarrow x \in A$ for at least one $A \in \mathcal A$: TRUE.
Proof: if $x$ is in the intersection, it is in every member, hence in at least one (the collection is nonempty).
<2>1. Converse: $x \in A$ for at least one $A \Rightarrow x \in \bigcap A$: FALSE.
Proof: being in one member does not imply being in all.

<1>4. (d) $x \in \bigcap_{A \in \mathcal A} A \Rightarrow x \in A$ for every $A \in \mathcal A$: TRUE.
Proof: this is the definition of intersection.
<2>1. Converse: $x \in A$ for every $A \Rightarrow x \in \bigcap A$: TRUE.
Proof: also the definition of intersection.

<1>5. Q.E.D.
Proof: <1>1–<1>4 give the truth values and converses.
:::
