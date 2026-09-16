---
schema: qual/card@1
id: P-AR3HH
kind: problem
title: $a+I$ is a unit in $R/I$ whenever $(a)+I=R$
classification:
  areas:
  - prelim
  topics:
  - Ideals
  - Rings
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Suppose $R$ is a commutative ring (with 1), $I$ is a proper ideal in $R$, and $a \in R$.
Suppose $(a) + I = R$.
Prove that $a+I$ is a unit (i.e., invertible) in the quotient ring $R/I$.

(For half credit: Prove that if $a$ and $n$ are relatively prime integers, then $a+n\mathbb{Z}$ is a unit in $\mathbb{Z}/n\mathbb{Z}$.)
:::

::: {.solution}
Because $(a)+I=R$, we have $1\in(a)+I$. Hence there exist $r\in R$ and $i\in I$ such that
\[
ra+i=1.
\]
Passing to the quotient gives
\[
(r+I)(a+I)=ra+I=1+I.
\]
Thus $r+I$ is an inverse of $a+I$, so $a+I$ is a unit in $R/I$.

For $R=\mathbb Z$ and $I=n\mathbb Z$, the hypothesis $(a)+n\mathbb Z=\mathbb Z$ is exactly $\gcd(a,n)=1$, recovering the familiar statement for $\mathbb Z/n\mathbb Z$.
:::
