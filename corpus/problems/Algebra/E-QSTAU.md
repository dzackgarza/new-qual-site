---
schema: qual/card@1
id: E-QSTAU
kind: problem
title: Nontrivial solutions of $Ax=0$ versus $\det A=0$ over an integral domain
classification:
  areas:
  - algebra
  topics:
  - Determinants
  - Matrices
  - Integral Domains
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
4. If $R$ is an integral domain and $A$ is an $n \times n$ matrix over $R$, prove that if a system of linear equations $A x=0$ has a nonzero solution then $\operatorname{det} A=0$.
   Is the converse true?
   What if we drop the assumption that $R$ is an integral domain?
:::

::: {.solution}

::: pf

::: pf-step
If $R$ is an integral domain, $A\in M_n(R)$, and $Ax=0$ for some $0\neq x\in R^n$, then $\det A=0$.

::: pf-proof
The adjugate identity $\operatorname{adj}(A)A=(\det A)I_n$ gives $(\det A)x=\operatorname{adj}(A)Ax=0$.
Some coordinate $x_j$ is nonzero, and $(\det A)x_j=0$ in the domain $R$ forces $\det A=0$.
:::

:::

::: pf-step
Over an integral domain the converse holds: if $\det A=0$, then $Ax=0$ has a nonzero solution in $R^n$.

::: pf-proof
Let $F=\operatorname{Frac}(R)$.
Since $\det A=0$, $A$ is singular over the field $F$, so $Ay=0$ for some $0\neq y\in F^n$.
Write $y_i=a_i/b_i$ with $a_i,b_i\in R$, $b_i\neq0$, and put $d=b_1\cdots b_n\neq0$.
Then $x=dy\in R^n$ is nonzero and $Ax=d\,Ay=0$.
:::

:::

::: pf-step
Without the domain hypothesis, a nonzero solution of $Ax=0$ does not force $\det A=0$.

::: pf-proof
Over $R=\ZZ/4\ZZ$ with $n=1$, $A=(2)$ and $x=(2)$ satisfy $Ax=4=0$ and $x\neq0$, while $\det A=2\neq0$.
:::

:::

::: pf-step
Over an arbitrary nonzero commutative ring $R$, $Ax=0$ has a nonzero solution in $R^n$ if and only if $r\det A=0$ for some $0\neq r\in R$ (McCoy's theorem).
In particular, $\det A=0$ still implies a nonzero solution.

::: pf-proof
This is McCoy's theorem for an $n\times n$ matrix, whose ideal of $n\times n$ minors is $(\det A)$.
If $\det A=0$, then $r=1$ annihilates it.
:::

:::

:::

:::
