---
schema: qual/card@1
id: P-NHWAK
kind: problem
title: Jacobson radical
classification:
  areas:
  - algebra
  topics:
  - Jacobson Radical
  - Ideals
  - Maximal Ideals
  - Prime Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
(1) What is the Jacobson radical $J(R)$ of a ring $R$? State its equivalent characterizations.

(2) If $R$ is a finitely generated commutative algebra over a field $k$, what can you say about $J(R)$ (Jacobson rings and Hilbert's Nullstellensatz)?
:::

::: {.solution}
Let $R$ be a commutative ring with $1$.

::: pf

::: pf-step
(1) $J(R)$ is the intersection of all maximal ideals of $R$, and $x\in J(R)$ if and only if $1-rx$ is a unit for every $r\in R$; it contains the nilradical $\sqrt{(0)}$.

::: pf-proof
If $x\in J(R)$ and $1-rx$ is not a unit, then $1-rx$ lies in a maximal ideal $\mathfrak m$, and $x\in\mathfrak m$ gives $1\in\mathfrak m$, which is impossible.
If $x\notin\mathfrak m$ for a maximal ideal $\mathfrak m$, then $\mathfrak m+(x)=R$, so $1=m+rx$ with $m\in\mathfrak m$, and $1-rx=m$ is not a unit.
The nilradical is the intersection of all prime ideals, and every maximal ideal is prime.
:::

:::

::: {.pf-step #jacobson}
If $R$ is a finitely generated $k$-algebra, then $R$ is a Jacobson ring: every prime ideal $\mathfrak p$ is the intersection of the maximal ideals containing it.

::: pf-proof
This is a form of Hilbert's Nullstellensatz; its weak form says that the residue field at each maximal ideal of $R$ is a finite extension of $k$.
:::

:::

::: pf-step
(2) If $R$ is a finitely generated $k$-algebra, then $J(R)=\sqrt{(0)}$; in particular $J(R)=0$ when $R$ is reduced.

::: pf-proof
By step [](#jacobson){.pf-ref}, the intersection of all maximal ideals equals the intersection of all prime ideals, which is the nilradical.
:::

:::

:::

:::

::: {.remark}
If moreover $R$ is finite-dimensional over $k$, then $R$ is Artinian, $J(R)$ is nilpotent, and $R/J(R)$ is a finite product of finite field extensions of $k$.
:::
