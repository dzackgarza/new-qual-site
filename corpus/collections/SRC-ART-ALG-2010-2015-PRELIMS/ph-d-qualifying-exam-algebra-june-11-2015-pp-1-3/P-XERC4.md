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

a. $R = \CC[x]$, $I = (x^2+1)$.

b. $R = \ZZ[x]$, $I = (6, x)$.

c. $R = \CC[x,y]$, $I = (y^2 - x^3)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

In part (a), $I=(x^2+1)$ is neither prime nor maximal in
$\CC[x]$.

::: pf-proof

Over $\CC$,
$$
x^2+1=(x-i)(x+i).
$$
Neither factor belongs to $(x^2+1)$, since each has smaller degree than
$x^2+1$, but their product does. Hence $(x^2+1)$ is not prime.

Moreover,
$$
(x^2+1)\subsetneq(x-i)\subsetneq\CC[x].
$$
The first containment is strict because $x-i\notin(x^2+1)$, and the second
is strict because $(x-i)$ is a proper ideal. Therefore $(x^2+1)$ is not
maximal.

:::

:::

::: {.pf-step #s2}

In part (b), $I=(6,x)$ is neither prime nor maximal in $\ZZ[x]$.

::: pf-proof

Evaluation at $x=0$ followed by reduction modulo $6$ defines a surjective
homomorphism
$$
\ZZ[x]\longrightarrow\ZZ/6\ZZ
$$
whose kernel is $(6,x)$. Hence
$$
\ZZ[x]/(6,x)\cong\ZZ/6\ZZ.
$$
The quotient is not an integral domain because
$\overline2\,\overline3=\overline0$ with
$\overline2,\overline3\ne\overline0$, so $(6,x)$ is not prime. It is
also not a field, so $(6,x)$ is not maximal.

:::

:::

::: {.pf-step #s3}

In part (c), $I=(y^2-x^3)$ is prime but not maximal in
$\CC[x,y]$.

::: pf-proof

Regard $y^2-x^3$ as a polynomial in $y$ over the UFD $\CC[x]$. It is
primitive. Over the fraction field $\CC(x)$, a quadratic polynomial
$y^2-x^3$ is reducible only if $x^3$ is a square in $\CC(x)$. This is
impossible: the valuation at the irreducible polynomial $x$ of a square is
even, whereas the valuation of $x^3$ is $3$. Thus $y^2-x^3$ is irreducible
in $\CC(x)[y]$, and Gauss's lemma implies that it is irreducible in
$\CC[x,y]$.

Since $\CC[x,y]$ is a UFD, every irreducible element is prime. Hence
$(y^2-x^3)$ is a prime ideal.

It is not maximal because
$$
(y^2-x^3)\subsetneq(x,y)\subsetneq\CC[x,y].
$$
Indeed, $y^2-x^3\in(x,y)$, while
$x\notin(y^2-x^3)$: if
$x=(y^2-x^3)g(x,y)$ with $g\ne0$, then the degree in $y$ of the right-hand
side would be at least $2$, whereas the degree in $y$ of $x$ is $0$.
Finally, $(x,y)$ is proper because evaluation at $(0,0)$ has kernel
$(x,y)$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} show, respectively, that the three ideals are neither,
neither, and prime but not maximal.

:::

:::

:::
