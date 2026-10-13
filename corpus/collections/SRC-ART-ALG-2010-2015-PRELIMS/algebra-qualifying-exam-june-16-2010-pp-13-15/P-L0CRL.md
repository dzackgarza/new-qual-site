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

::: pf

::: {.pf-step #s1}

If $r\notin M$, then the principal ideal $(r)$ is not proper.

::: pf-proof

Suppose instead that $(r)$ were proper. Every proper ideal in a
commutative unital ring is contained in a maximal ideal. Since $M$ is the
unique maximal ideal, this would imply
$$
(r)\subseteq M.
$$
But $r\in(r)$, contradicting $r\notin M$. Hence $(r)=R$.

:::

:::

::: {.pf-step #s2}

If $r\notin M$, then $r$ is a unit.

::: pf-proof

By step [](#s1){.pf-ref}, $(r)=R$, so $1\in(r)$. Hence there exists $s\in R$ with
$$
sr=1.
$$
Because $R$ is commutative, also $rs=1$, so $r$ is a unit.

:::

:::

::: {.pf-step #s3}

Every element of $R$ is either a unit or belongs to $M$.

::: pf-proof

For $r\in R$, either $r\in M$ or $r\notin M$. In the latter case,
step [](#s2){.pf-ref} shows that $r$ is a unit.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required assertion.

:::

:::

:::
