---
schema: qual/card@1
id: P-F5ZKB
kind: problem
title: A finite field has $p^n$ elements; subfields of a field of size $3^{12}$; an
  infinite field of characteristic $3$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Fields
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.problem}
a. Show that a finite field must have exactly $p^n$ elements for some prime $p$ and some positive integer $n$.

b. List all the subfields of the field of size $3^{12}$.

c. Give an example of an infinite field of characteristic $3$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

In part (a), a finite field $F$ has $p^n$ elements for a prime $p$ and an integer $n\ge1$.

::: pf-proof

The characteristic of a field is $0$ or a prime.
In characteristic $0$ the prime subfield is isomorphic to $\QQ$, which is infinite, so $F$ has prime characteristic $p$ and prime subfield $\FF_p=\ZZ/p\ZZ$.
Field addition and multiplication by elements of $\FF_p$ make $F$ an $\FF_p$-vector space, which is finite-dimensional because $F$ is finite.
If $n=\dim_{\FF_p}F$, then $n\ge1$ and $F\cong\FF_p^n$ as vector spaces, so $\abs{F}=p^n$.

:::

:::

::: {.pf-step #s2}

In part (b), the subfields of $\FF_{3^{12}}$ are its unique subfields of orders
$$
3,\quad 3^2=9,\quad 3^3=27,\quad 3^4=81,\quad 3^6=729,\quad 3^{12}=531441.
$$

::: pf-proof

A subfield $K$ of $\FF_{p^m}$ contains $\FF_p$, and by the tower law $d=[K:\FF_p]$ divides $m=[\FF_{p^m}:\FF_p]$.
Conversely, for each positive divisor $d$ of $m$, the polynomial $x^{p^d}-x$ divides $x^{p^m}-x$ in $\FF_p[x]$, and its roots in $\FF_{p^m}$ form the unique subfield of order $p^d$ [@DF04].
Here $p=3$, $m=12$, and the positive divisors of $12$ are $1,2,3,4,6,12$.

:::

:::

::: {.pf-step #s3}

In part (c), $\FF_3(t)$, the field of rational functions in one indeterminate $t$ over $\FF_3$, is an infinite field of characteristic $3$.

::: pf-proof

$\FF_3(t)$ is the field of fractions of the integral domain $\FF_3[t]$, so it is a field.
Its characteristic is $3$, since $1+1+1=0$ in $\FF_3\subseteq\FF_3(t)$.
The monomials $t^k$, $k\ge0$, are pairwise distinct elements, so $\FF_3(t)$ is infinite.
An algebraic closure $\overline{\FF}_3=\bigcup_{n\ge1}\FF_{3^n}$ is another infinite field of characteristic $3$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} answer parts (a), (b), and (c).

:::

:::

:::
