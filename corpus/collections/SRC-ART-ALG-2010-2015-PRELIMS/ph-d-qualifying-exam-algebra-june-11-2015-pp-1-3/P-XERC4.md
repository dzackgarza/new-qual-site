---
schema: qual/card@1
id: P-XERC4
kind: problem
title: Prime and maximal ideals $(x^2+1)$, $(6,x)$, and $(y^2-x^3)$
classification:
  areas:
  - prelim
  topics:
  - Maximal Ideals
  - Prime Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
In each item, a commutative ring $R$ and an ideal $I \subseteq R$ are given.
Determine whether $I$ is prime, maximal, both, or neither.

a. $R = \mathbb{C}[x]$, $I = (x^2+1)$.

b. $R = \mathbb{Z}[x]$, $I = (6, x)$.

c. $R = \mathbb{C}[x,y]$, $I = (y^2 - x^3)$.
:::

::: {.solution}
An ideal $I$ is prime if and only if $R/I$ is an integral domain, and maximal if and only if $R/I$ is a field.

<1>1. In part (a), $(x^2+1)$ is $\boxed{\text{neither prime nor maximal}}$.
::: {.proof}
Over $\CC$, $x^2+1=(x-i)(x+i)$. Neither factor lies in $(x^2+1)$, since every nonzero element of that ideal has degree at least $2$, but their product does. So $(x^2+1)$ is not prime, and hence not maximal.
:::

<1>2. In part (b), $(6,x)$ is $\boxed{\text{neither prime nor maximal}}$.
::: {.proof}
The surjection $\ZZ[x]\to\ZZ/6\ZZ$, $f\mapsto f(0)\bmod 6$, has kernel $(6,x)$: a polynomial $f$ lies in the kernel exactly when $f=f(0)+xg$ with $6\mid f(0)$. Hence $\ZZ[x]/(6,x)\cong\ZZ/6\ZZ$, which has the zero divisors $2\cdot3=0$ and is not a domain.
:::

<1>3. In part (c), $(y^2-x^3)$ is $\boxed{\text{prime but not maximal}}$.
::: {.proof}
View $y^2-x^3$ as a monic polynomial in $y$ over $\CC[x]$. A factorization would be $(y-g)(y+g)$ with $g\in\CC[x]$ and $g^2=x^3$, which is impossible since $x^3$ has odd degree. Hence $y^2-x^3$ is irreducible in the UFD $\CC[x,y]$, so it is a prime element and $(y^2-x^3)$ is a prime ideal. It is properly contained in the proper ideal $(x,y)$, since $y\notin(y^2-x^3)$ by degree, so it is not maximal.
:::

<1>4. Q.E.D.
::: {.proof}
Steps <1>1, <1>2, and <1>3 treat parts (a), (b), and (c).
:::
:::
