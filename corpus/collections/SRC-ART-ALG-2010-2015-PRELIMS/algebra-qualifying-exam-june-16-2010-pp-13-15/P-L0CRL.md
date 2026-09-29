---
schema: qual/card@1
id: P-L0CRL
kind: problem
title: In a local ring every element is a unit or lies in the unique maximal ideal
classification:
  areas:
  - algebra
  topics:
  - Local Rings
  - Maximal Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $R$ be a commutative ring with $1$.
We say $R$ is a local ring if $R$ has exactly one maximal ideal, $M$.
Prove that, in a local ring $R$, any $r \in R$ is either a unit or an element of the maximal ideal $M$.
:::

::: {.solution}
Let $r\in R$ with $r\notin M$.

::: pf

::: {.pf-step #s1}

The ideal $(r)$ equals $R$.

::: pf-proof

Every proper ideal of a commutative ring with $1$ is contained in a maximal ideal, by Zorn's lemma [@DF04], and $M$ is the only maximal ideal of $R$.
Since $r\in(r)$ and $r\notin M$, the ideal $(r)$ is not contained in $M$, so it is not proper.

:::

:::

::: pf-qed

By step [](#s1){.pf-ref}, $1=sr$ for some $s\in R$, so $r$ is a unit. Hence every element of $R$ is a unit or lies in $M$.

:::

:::

:::
