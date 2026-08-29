---
schema: qual/card@1
id: P-5GGTM
kind: problem
title: Every field is a simple ring
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Ideals
  - Rings
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: problem
- Show that every field is simple.
:::

::: solution
**Goal:** Prove that every field $F$ is a simple ring (its only ideals are $(0)$ and $F$).

<1>1. Definition of a simple ring:
    A non-zero ring $R$ is simple if its only two-sided ideals are the zero ideal $(0)$ and the improper ideal $R$.

<1>2. Classification of ideals in a field:
    *Proof:*
    <2>1. Let $I \subseteq F$ be an ideal of the field $F$.
    <2>2. If $I = (0)$, it is the trivial ideal.
    <2>3. If $I \neq (0)$, there exists a non-zero element $x \in I \setminus \{0\}$.
    <2>4. Because $F$ is a field, $x$ is invertible, so there exists $x^{-1} \in F$ such that $x^{-1} x = 1_F$.
    <2>5. By the absorption property of ideals, $1_F = x^{-1} \cdot x \in I$.
    <2>6. For any element $r \in F$, $r = r \cdot 1_F \in I$.
    <2>7. Thus $F \subseteq I$, which forces $I = F$.

<1>3. Conclusion:
    The only ideals in $F$ are $(0)$ and $F$, so $F$ is a simple ring. Q.E.D.
:::
