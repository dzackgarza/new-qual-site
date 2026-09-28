---
schema: qual/card@1
id: P-HCAO8
kind: problem
title: Rings in which every prime ideal is maximal
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Maximal Ideals
  - Artinian Rings
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Give a general class of rings in which every prime ideal is maximal.
:::

::: {.solution}
<1>1. In a commutative Artinian ring $R$, every prime ideal is maximal, so
$\dim R=0$.

::: {.proof}
Let $\mathfrak p\subseteq R$ be prime; then $D=R/\mathfrak p$ is an Artinian
integral domain. For $0\ne x\in D$, the chain
$(x)\supseteq(x^2)\supseteq(x^3)\supseteq\cdots$ stabilizes, so
$x^n=x^{n+1}y$ for some $n\ge1$ and $y\in D$. Cancelling $x^n$ in the domain
$D$ gives $1=xy$. Hence $D$ is a field and $\mathfrak p$ is maximal.
:::

::: {.example}
Finite commutative rings and quotients $k[x_1,\ldots,x_n]/I$ with
$\dim_k k[x_1,\ldots,x_n]/I<\infty$ are Artinian, since every chain of ideals
is a chain of subgroups of a finite set or of $k$-subspaces of a
finite-dimensional space.
:::

<1>2. In a commutative von Neumann regular ring $R$, that is, one in which for
each $x\in R$ there is $y\in R$ with $x^2y=x$, every prime ideal is maximal.
In particular this holds for every Boolean ring, in which $x^2=x$ for all $x$.

::: {.proof}
Let $\mathfrak p$ be prime and let $\bar x\ne0$ in $R/\mathfrak p$. From
$\bar x^2\bar y=\bar x$ we get $\bar x(\bar x\bar y-1)=0$, so
$\bar x\bar y=1$ in the domain $R/\mathfrak p$. Hence $R/\mathfrak p$ is a
field. A Boolean ring is von Neumann regular with $y=1$; there, each
$R/\mathfrak p$ is a domain in which $\bar x(\bar x-1)=0$ for every $\bar x$,
so $R/\mathfrak p\cong\mathbb F_2$.
:::

<1>3. If $R$ is integral over a subfield $k$, then every prime ideal of $R$ is
maximal.

::: {.proof}
For a prime $\mathfrak p\subseteq R$, the domain $R/\mathfrak p$ is integral
over the image of $k$, which is a field. An integral domain integral over a
field is a field: for $0\ne x$, a monic equation for $x$ of least degree has
nonzero constant term and expresses $x^{-1}$ as a polynomial in $x$.
:::
:::
