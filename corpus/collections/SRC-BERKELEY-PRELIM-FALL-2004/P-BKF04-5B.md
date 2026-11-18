---
schema: qual/card@1
id: P-BKF04-5B
kind: problem
title: Smallest field of characteristic $7$ containing a root of $x^{18}+x^{17}+\cdots+x+1$
classification:
  areas: [prelim]
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's prose proof into numbered steps and re-checked it: the factorization,
    the separability of x^19 - 1 in characteristic 7 (19 not 0 mod 7), the identification of the
    roots with the elements of order 19, the cyclic-group criterion, and the three residues 7, 11,
    1 modulo 19. Nothing was changed mathematically. Not checked against a printed source: the
    Berkeley preliminary examinations are not retained in tmp/sources and the card records no
    page.
---

::: {.problem}
What is the cardinality of the smallest field $F$ of characteristic $7$ such that the equation $x^{18}+x^{17}+\cdots+x+1=0$ has a solution $x\in F$?
:::

::: {.solution}

The argument is the card's own: no solution set for this source is retained in `tmp/sources`, so nothing below is transcribed, and the card's existing solution is restructured into numbered steps. Here a field of characteristic $7$ is a finite extension $\FF_{7^{m}}$ of $\FF_{7}$, so it has $7^{m}$ elements and its multiplicative group is cyclic of order $7^{m}-1$.

::: pf

::: {.pf-step #identity}

$(x-1)(x^{18}+x^{17}+\cdots+x+1)=x^{19}-1$.

::: pf-proof

Expand the product: the intermediate powers cancel.

:::

:::

::: {.pf-step #separable}

$x^{19}-1$ has no repeated root in characteristic $7$.

::: pf-proof

Its derivative is $19x^{18}$, and $19\equiv5\not\equiv0$ in $\FF_{7}$, so the only root of the derivative is $0$, which is not a root of $x^{19}-1$; a repeated root would be a common root of a polynomial and its derivative.

:::

:::

::: {.pf-step #roots}

The roots of $x^{18}+\cdots+x+1$ are exactly the elements of order $19$ in a splitting field.

::: pf-proof

By step [](#identity){.pf-ref} its roots are the roots of $x^{19}-1$ other than $1$; these are the elements $\zeta\neq1$ with $\zeta^{19}=1$, and since $19$ is prime each has order exactly $19$; by step [](#separable){.pf-ref} there are $18$ of them and they are distinct.

:::

:::

::: {.pf-step #criterion}

A field $F$ of characteristic $7$ contains a root if and only if $19\mid(\#F^{\times})$.

::: pf-proof

If $x\in F$ has order $19$ then $19$ divides the order of the group $F^{\times}$ by Lagrange's theorem; conversely, $F^{\times}$ is cyclic, and a cyclic group whose order is divisible by $19$ has an element of order $19$.

:::

:::

::: {.pf-step #least}

$19\mid(7^{m}-1)$ holds first at $m=3$.

::: pf-proof

$7\equiv7$, $7^{2}\equiv49\equiv11$ and $7^{3}\equiv77\equiv1$ modulo $19$, and $1,11\neq1$, so $m=3$ is the least exponent.

:::

:::

::: {.pf-step #done}

The smallest such field has $7^{3}=343$ elements.

::: pf-proof

By steps [](#criterion){.pf-ref} and [](#least){.pf-ref} the least $m$ is $3$, and a finite field of characteristic $7$ has $7^{m}$ elements.

:::

:::

:::

:::
