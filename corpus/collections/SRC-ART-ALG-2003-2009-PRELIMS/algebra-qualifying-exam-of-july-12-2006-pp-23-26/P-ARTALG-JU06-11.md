---
schema: qual/card@1
id: P-ARTALG-JU06-11
kind: problem
title: Non-free submodule of a free module
classification:
  areas:
  - algebra
  topics:
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Give an example of an integral domain $R$, a free $R$-module $M$, and an $R$-submodule $N$ of $M$ such that $N$ is not a free $R$-module.
:::

::: {.solution}
Let $R=\ZZ[x]$, an integral domain; let $M=R$, a free $R$-module of rank $1$ with basis $\{1\}$; and let $N=(2,x)=\{2p+xq : p,q\in\ZZ[x]\}$, an ideal of $R$ and hence an $R$-submodule of $M$.

<1>1. If $N$ is a free $R$-module, then $N=(f)$ for some nonzero $f\in R$.

::: {.proof}
For nonzero $a,b\in N$, the relation $b\cdot a-a\cdot b=0$ has nonzero coefficients $b$ and $-a$, so any two elements of $N$ are linearly dependent over $R$.
A basis of $N$ therefore has at most one element.
Since $N\ne0$, a basis is a single element $f\ne0$, and $N=Rf=(f)$.
:::

<1>2. The ideal $N$ is not principal.

::: {.proof}
Suppose $N=(f)$.
Since $2\in N$, $f$ divides $2$ in $\ZZ[x]$; degrees add in the domain $\ZZ[x]$, so $f\in\{\pm1,\pm2\}$.
If $f=\pm1$, then $1\in N$; but every element $2p+xq$ of $N$ has even constant term $2p(0)$, a contradiction.
If $f=\pm2$, then $N=2\ZZ[x]$; but $x\in N$ has coefficient $1\notin2\ZZ$, a contradiction.
:::

<1>3. Q.E.D.

::: {.proof}
By steps <1>1 and <1>2, the submodule $N=(2,x)$ of the free $\ZZ[x]$-module $M=\ZZ[x]$ is not free.
:::
:::
