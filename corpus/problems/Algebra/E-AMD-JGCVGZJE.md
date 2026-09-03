---
schema: qual/card@1
id: E-AMD-JGCVGZJE
kind: problem
title: $R\units$ need not be closed under addition
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that $R^\times$ need not be closed under addition.
:::

::: solution
**Goal:** Prove that the set of units $R^\times$ of a ring with identity $R$ is generally not closed under addition.

<1>1. Universal obstruction via additive inverses:
    *Proof:*
    <2>1. Let $R$ be any non-zero ring with identity ($1_R \neq 0_R$).
    <2>2. The identity $1_R$ is a unit ($1_R \cdot 1_R = 1_R$), so $1_R \in R^\times$.
    <2>3. The additive inverse $-1_R$ is also a unit, since $(-1_R)(-1_R) = 1_R$, so $-1_R \in R^\times$.
    <2>4. The sum of these two units is:
        $$1_R + (-1_R) = 0_R.$$
    <2>5. Because $1_R \neq 0_R$, the zero element $0_R$ is not invertible ($0_R \cdot r = 0_R \neq 1_R$ for all $r \in R$), so $0_R \notin R^\times$.
    <2>6. Thus $1_R, -1_R \in R^\times$ but $1_R + (-1_R) \notin R^\times$.

<1>2. Concrete specimen in the ring of integers $\mathbb{Z}$:
    *Proof:*
    <2>1. In $R = \mathbb{Z}$, the group of units is $\mathbb{Z}^\times = \{1, -1\}$.
    <2>2. The sum $1 + 1 = 2 \notin \mathbb{Z}^\times$ (since $1/2 \notin \mathbb{Z}$).
    <2>3. The sum $1 + (-1) = 0 \notin \mathbb{Z}^\times$.
    <2>4. Thus $\mathbb{Z}^\times$ is not closed under addition.

<1>3. Conclusion:
    $R^\times$ is not closed under addition in any non-zero ring. Q.E.D.
:::
