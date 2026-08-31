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

::: problem
Let $R$ be a commutative ring with $1$.
We say $R$ is a local ring if $R$ has exactly one maximal ideal, $M$.
Prove that, in a local ring $R$, any $r \in R$ is either a unit or an element of the maximal ideal $M$.
:::

::: {.solution}
**Goal.** In a local ring $R$ with unique maximal ideal $M$, show every $r \in R$ is a unit or lies in $M$.

<1>1. Suppose $r \notin M$.
::: {.proof}
consider an element not in the maximal ideal.
:::

<1>2. The ideal $(r)$ is not contained in $M$.
::: {.proof}
$r \in (r)$ and $r \notin M$.
:::

<1>3. $(r)$ is not contained in any maximal ideal.
::: {.proof}
$M$ is the unique maximal ideal, and $(r) \not\subseteq M$, so $(r)$ is contained in no maximal ideal.
:::

<1>4. Hence $(r) = R$.
::: {.proof}
every proper ideal is contained in a maximal ideal (Zorn's lemma); since $(r)$ is contained in no maximal ideal, it is not proper, so $(r) = R$.
:::

<1>5. Hence $1 \in (r)$, so $r$ is a unit.
::: {.proof}
$1 \in (r)$ means $1 = sr$ for some $s \in R$, so $r$ has a left inverse $s$; in a commutative ring this makes $r$ a unit.
:::

<1>6. Q.E.D.
::: {.proof}
<1>1–<1>5 show $r \notin M$ forces $r$ to be a unit, so every element is a unit or lies in $M$.
:::
:::
