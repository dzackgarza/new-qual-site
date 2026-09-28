---
schema: qual/card@1
id: E-AMD-U47HVKBS
kind: problem
title: $I$ is a prime ideal iff $R/I$ is an integral domain
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Integral Domains
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}
Show that $I \normal R$ is prime iff $R/I$ is an integral domain.
:::

::: {.solution}
Let $R$ be a commutative ring with identity and $I$ an ideal of $R$.
Recall that $I$ is prime if $I\neq R$ and $ab\in I$ implies $a\in I$ or $b\in I$, and that a commutative ring $S$ is an integral domain if $1_S\neq0_S$ and $xy=0$ implies $x=0$ or $y=0$.

<1>1. $I\neq R$ if and only if $1+I\neq 0+I$ in $R/I$.

::: {.proof}
$1+I=0+I$ if and only if $1\in I$, if and only if $I=R$.
:::

<1>2. For $a,b\in R$, $ab\in I$ if and only if $(a+I)(b+I)=0$ in $R/I$, and $a\in I$ if and only if $a+I=0$.

::: {.proof}
$(a+I)(b+I)=ab+I$, and $x+I=0+I$ if and only if $x\in I$.
:::

<1>3. Q.E.D.

::: {.proof}
By step <1>1, the condition $I\neq R$ is the condition $1\neq0$ in $R/I$.
By step <1>2, the implication "$ab\in I\Rightarrow a\in I$ or $b\in I$" for all $a,b\in R$ is the implication "$\bar a\bar b=0\Rightarrow\bar a=0$ or $\bar b=0$" for all $\bar a,\bar b\in R/I$, since every element of $R/I$ has the form $a+I$.
Hence $I$ is prime if and only if $R/I$ is an integral domain.
:::
:::
