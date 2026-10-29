---
schema: qual/card@1
id: P-LHIOI
kind: problem
title: If $A=Ra$ with $ra=0$ and $(r,s)=(1)$, then $A=sA$ and $A[s]=0$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Cyclic Groups
  - Torsion
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $R$ be a commutative ring, let $A=Ra$ be a cyclic $R$-module, and suppose
$$
ra=0,
\qquad
(r,s)=R.
$$
Show that
$$
A=sA
\qquad\text{and}\qquad
A[s]=\{x\in A:sx=0\}=0.
$$
:::

::: {.solution}
Choose $u,v\in R$ with $ur+vs=1$.

::: pf

::: pf-step
$A=sA$.

::: pf-proof
$a=(ur+vs)a=u(ra)+v(sa)=s(va)$, so the generator $a$ lies in the submodule $sA$, hence $A\subseteq sA$. The reverse inclusion holds because $A$ is a module.
:::

:::

::: pf-step
$A[s]=0$.

::: pf-proof
Let $x\in A[s]$ and write $x=ta$ with $t\in R$. Then $rx=t(ra)=0$ and $sx=0$, so $x=(ur+vs)x=u(rx)+v(sx)=0$.
:::

:::

:::

:::
