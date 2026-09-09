---
schema: qual/card@1
id: P-2E7UB
kind: problem
title: Every non-unit lies in a maximal ideal
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Ideals
  - Zorn's Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Stated the correct one-sided hypothesis and applied Zorn directly to proper left ideals over Rx.
---

::: {.exercise}
Let $R$ be a ring with $1\ne0$. Show that any element $x$ having no left inverse is contained in a maximal left ideal. In a commutative ring, this applies to every nonunit.
:::

::: {.solution}
If $x$ has no left inverse, then the principal left ideal
\[
Rx
\]
is proper: otherwise $1\in Rx$, so $rx=1$ for some $r\in R$.

Consider the set of proper left ideals containing $Rx$, ordered by inclusion. It is nonempty. The union of a chain is again a left ideal containing $Rx$, and it is proper because if it contained $1$, then some member of the chain would contain $1$ and hence equal $R$. Thus every chain has an upper bound.

By Zorn's lemma there is a maximal element $M$ in this poset. Any proper left ideal strictly containing $M$ would also contain $Rx$, contradicting maximality. Hence $M$ is a maximal left ideal and
\[
x\in Rx\subseteq M.
\]

In a commutative ring, an element is left-invertible exactly when it is a unit, so every nonunit is contained in a maximal ideal.
:::
