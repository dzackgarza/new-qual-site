---
schema: qual/card@1
id: FF-HAMDC
kind: fact
title: Factorization of $x^n + a^n$ for odd $n$
slogan: Odd powers make $x+a$ a factor; even powers do not unless $2a^n$ vanishes.
prompts:
- When does $x + a$ divide $x^n + a^n$, and what is the factorization?
- When does $x + y$ divide $x^n + y^n$, and what is the factorization?
classification:
  areas:
  - algebra
  topics:
  - Polynomials
  - Factorization
relations: []
review: draft
---

::: {.fact}
Let $R$ be a commutative ring, let $a\in R$, and let $n\ge1$.
If $n$ is odd, then in $R[x]$
$$
x^n+a^n=(x+a)\sum_{k=0}^{n-1}(-a)^kx^{n-1-k}.
$$
If $n$ is even and $2a^n\ne0$ in $R$, for example if $R$ is a field of characteristic other than $2$ and $a\ne0$, then $x+a$ does not divide $x^n+a^n$ in $R[x]$.
:::

::: {.proof}
For odd $n$, $(-a)^n=-a^n$, so the factorization is [[FF-ED3CD]] applied to $-a$.
Since $x+a$ is monic, division by $x+a$ in $R[x]$ leaves the constant remainder $f(-a)$ for every $f\in R[x]$.
For even $n$ the remainder of $x^n+a^n$ is $(-a)^n+a^n=2a^n\ne0$.
:::

::: {.remark title="Variations"}
Taking $R=\ZZ[y]$ and $a=y$, where $2y^n\neq0$, gives the two-variable form: for odd $n$,
$$
x^n+y^n=(x+y)\sum_{k=0}^{n-1}(-1)^kx^{n-1-k}y^k
$$
in $\ZZ[x,y]$, and for even $n$, $x+y$ does not divide $x^n+y^n$ in $\ZZ[x,y]$.
:::
