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
Let $R$ be a ring with $1$, not necessarily commutative.

::: pf

::: {.pf-step #general}
(1) $J(R)$ is the intersection of all maximal left ideals of $R$.
It is a two-sided ideal, it equals the intersection of all maximal right ideals, and $x\in J(R)$ if and only if $1-rx$ is a unit for every $r\in R$.

::: pf-proof
If $x\in J(R)$ and $1-rx$ has no left inverse, then $R(1-rx)$ is a proper left ideal, so it lies in a maximal left ideal $M$; then $rx\in M$ gives $1\in M$, which is impossible.
If $x\notin M$ for a maximal left ideal $M$, then $M+Rx=R$, so $1=m+rx$ with $m\in M$, and $1-rx=m$ has no left inverse.
So $x\in J(R)$ if and only if $1-rx$ has a left inverse for every $r$.
For a maximal left ideal $M$, the module $R/M$ is simple and its annihilator $\{a\in R: aR\subseteq M\}$ is a two-sided ideal inside $M$; conversely the annihilator of a simple module $S=Rs$ is the intersection of the maximal left ideals $\operatorname{ann}(s')$, $0\ne s'\in S$.
Hence $J(R)$ is the intersection of the annihilators of the simple left modules, a two-sided ideal.
Now let $x\in J(R)$ and let $u$ be a left inverse of $1-x$.
Then $u=1+ux$ with $ux\in J(R)$, so $u$ has a left inverse $v$, and $v=vu(1-x)=1-x$; so $1-x$ is a unit, and the same holds for $1-rx$.
This characterization is symmetric under passing to the opposite ring, so $J(R)$ also equals the intersection of the maximal right ideals.
:::

:::

::: pf-step
If $R$ is commutative, $J(R)$ is the intersection of all maximal ideals of $R$ and contains the nilradical $\sqrt{(0)}$.

::: pf-proof
In a commutative ring the maximal left ideals are the maximal ideals, so step [](#general){.pf-ref} gives the first claim.
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
