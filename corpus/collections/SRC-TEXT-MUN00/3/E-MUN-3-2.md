---
schema: qual/card@1
id: E-MUN-3-2
kind: problem
title: The restriction of an equivalence relation is an equivalence relation
classification:
  areas:
  - topology
  topics:
  - Relations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §3 Exercise 2, printed p. 28: for a relation
    C on A and A_0 a subset of A, the restriction of C to A_0 is C cap (A_0 x A_0), and
    the exercise asks that the restriction of an equivalence relation be an equivalence
    relation. The stored statement matches, including the definition of restriction.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.2,
    printed p. 19 (tmp/sources/munkres-solutions-whitman.pdf). His proof of the three
    properties is the one below, with the observation that C_0 is a relation on A_0
    because it lies in A_0 x A_0.
---

::: {.exercise}

Let $C$ be a relation on a set $A$. If $A_0 \subset A$, define the restriction of $C$ to $A_0$ to be the relation $C \cap (A_0 \times A_0)$. Show that the restriction of an equivalence relation is an equivalence relation.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.2, printed p. 19** (`tmp/sources/munkres-solutions-whitman.pdf`); the three verifications below are his.

Let $C$ be an equivalence relation on $A$ and put $C_0=C\cap(A_0\times A_0)$. Since $C_0\subset A_0\times A_0$, it is a relation on $A_0$.

*Reflexive.* Let $a\in A_0$. Then $a\in A$, so $aCa$ because $C$ is reflexive, and $(a,a)\in A_0\times A_0$; hence $(a,a)\in C_0$.

*Symmetric.* Let $a,b\in A_0$ with $aC_0b$. Then $aCb$ since $C_0\subset C$, so $bCa$ because $C$ is symmetric, and $(b,a)\in A_0\times A_0$; hence $bC_0a$.

*Transitive.* Let $a,b,c\in A_0$ with $aC_0b$ and $bC_0c$. Then $aCb$ and $bCc$, so $aCc$ because $C$ is transitive, and $(a,c)\in A_0\times A_0$; hence $aC_0c$.

So $C_0$ is an equivalence relation on $A_0$.
:::
