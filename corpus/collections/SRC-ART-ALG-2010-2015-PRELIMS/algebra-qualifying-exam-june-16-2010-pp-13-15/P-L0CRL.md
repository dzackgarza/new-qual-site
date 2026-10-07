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
<1>1. If $r\notin M$, then the principal ideal $(r)$ is not proper.

::: {.proof}
Suppose instead that $(r)$ were proper. Every proper ideal in a
commutative unital ring is contained in a maximal ideal. Since $M$ is the
unique maximal ideal, this would imply
$$
(r)\subseteq M.
$$
But $r\in(r)$, contradicting $r\notin M$. Hence $(r)=R$.
:::

<1>2. If $r\notin M$, then $r$ is a unit.

::: {.proof}
By step <1>1, $(r)=R$, so $1\in(r)$. Hence there exists $s\in R$ with
$$
sr=1.
$$
Because $R$ is commutative, also $rs=1$, so $r$ is a unit.
:::

<1>3. Every element of $R$ is either a unit or belongs to $M$.

::: {.proof}
For $r\in R$, either $r\in M$ or $r\notin M$. In the latter case,
step <1>2 shows that $r$ is a unit.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required assertion.
:::
:::
