---
schema: qual/card@1
id: T-CF6S3
kind: theorem
title: Eisenstein's criterion
classification:
  areas:
  - algebra
  topics:
  - Irreducibility Criteria
  - Polynomials
relations: []
review: draft
---

::: {.theorem}
Let
$$
f(x) = \sum_{i=0}^n a_i x^i = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1 x + a_0 \in \ZZ[x]
$$
with $n\geq1$, and suppose there is a prime $p$ such that

- $p$ divides $a_i$ for $0\leq i\leq n-1$,

- $p$ does not divide $a_n$, and

- $p^2$ does not divide $a_0$.

Then $f$ is [[D-BVMTZ|irreducible]] in $\QQ[x]$.
If moreover the coefficients of $f$ have no common prime factor, then $f$ is irreducible in $\ZZ[x]$.
:::

::: {.proof}
Suppose $f$ is reducible in $\QQ[x]$.
By Gauss's lemma $f=gh$ with $g,h\in\ZZ[x]$ of degrees $r,s\geq1$.
Reducing modulo $p$ gives $\bar a_nx^n=\bar g\bar h$ in $\FF_p[x]$ with $\bar a_n\neq0$.
The leading coefficients of $g$ and $h$ multiply to $a_n$, so they are not divisible by $p$ and $\deg\bar g=r$, $\deg\bar h=s$.
Since $\FF_p[x]$ is a unique factorization domain, $\bar g=bx^r$ and $\bar h=cx^s$ with $b,c\in\FF_p^\times$, so $p$ divides both constant terms $g(0)$ and $h(0)$, and $p^2$ divides $g(0)h(0)=a_0$, a contradiction.
If the coefficients of $f$ have no common prime factor, a factorization of $f$ in $\ZZ[x]$ into nonunits has both factors of positive degree, which the first statement excludes.
:::
