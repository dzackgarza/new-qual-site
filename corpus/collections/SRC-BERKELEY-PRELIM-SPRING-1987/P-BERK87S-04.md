---
schema: qual/card@1
id: P-BERK87S-04
kind: problem
title: Polynomial representation of every function on a finite field
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Used Lagrange interpolation for existence. For uniqueness, the difference
    of two representatives vanishes on every element of F and is therefore
    divisible by the product of the linear factors x-a, which equals x^q-x.
---

::: {.problem}
Let $F$ be a finite field with $q$ elements. For $f\in F[x]$, write
\[
\varphi_f(a)=f(a)
\qquad(a\in F).
\]
Prove that every function $\varphi:F\to F$ equals $\varphi_f$ for some $f\in F[x]$, and that $f$ is determined by $\varphi$ up to addition of a multiple of
\[
x^q-x.
\]
:::

::: {.solution}
::: pf

::: {.pf-step #lagrange-basis}
For each $a\in F$, define
$$
\ell_a(x)
\coloneqq
\prod_{\substack{b\in F\\ b\ne a}}
\frac{x-b}{a-b}.
$$
Then
$$
\ell_a(c)
=
\begin{cases}
1,&c=a,\\
0,&c\ne a,
\end{cases}
$$
for every $c\in F$.

::: pf-proof
Every denominator $a-b$ in the product is nonzero and hence invertible in
the field $F$, so $\ell_a\in F[x]$. If $c=a$, every factor is $1$. If
$c\ne a$, the factor indexed by $b=c$ is $0$.
:::

:::

::: {.pf-step #existence}
Every function $\varphi:F\to F$ is represented by a polynomial in
$F[x]$.

::: pf-proof
Define
$$
f(x)
\coloneqq
\sum_{a\in F}\varphi(a)\ell_a(x).
$$
For any $c\in F$, step [](#lagrange-basis){.pf-ref} gives
$$
f(c)
=
\sum_{a\in F}\varphi(a)\ell_a(c)
=
\varphi(c).
$$
Thus $\varphi=\varphi_f$.
:::

:::

::: {.pf-step #product-identity-boxed}
In $F[x]$ one has
$$
\boxed{\prod_{a\in F}(x-a)=x^q-x}.
$$

::: pf-proof
If $a=0$, then $a^q=a$. If $a\ne0$, then $a\in F^\times$, whose order is
$q-1$. Lagrange's theorem gives
$$
a^{q-1}=1,
$$
and hence again $a^q=a$. Therefore every $a\in F$ is a root of $x^q-x$.

The polynomial
$$
\prod_{a\in F}(x-a)
$$
is monic of degree $q$ and has exactly these $q$ distinct roots. The
polynomial $x^q-x$ is also monic of degree $q$ and has all of them as roots.
Their difference has degree less than $q$ and at least $q$ roots, so it is
zero.
:::

:::

::: {.pf-step #difference-divisible}
If $f,g\in F[x]$ satisfy $\varphi_f=\varphi_g$, then
$$
x^q-x\mid f-g.
$$

::: pf-proof
For every $a\in F$,
$$
(f-g)(a)=0.
$$
By the factor theorem, $x-a$ divides $f-g$ for every $a\in F$. The distinct
linear factors $x-a$ are pairwise coprime, so their product divides $f-g$.
Step [](#product-identity-boxed){.pf-ref} identifies this product with $x^q-x$.
:::

:::

::: {.pf-step #converse-holds}
Conversely, if
$$
f-g=(x^q-x)r
$$
for some $r\in F[x]$, then $\varphi_f=\varphi_g$.

::: pf-proof
For every $a\in F$, step [](#product-identity-boxed){.pf-ref} gives
$$
a^q-a=0.
$$
Hence
$$
f(a)-g(a)
=
(a^q-a)r(a)
=0,
$$
so the two polynomials define the same function on $F$.
:::

:::

::: pf-qed
Step [](#existence){.pf-ref} proves existence. Steps [](#difference-divisible){.pf-ref} and [](#converse-holds){.pf-ref} show that two representing
polynomials define the same function exactly when their difference is a
multiple of $x^q-x$, which is the asserted uniqueness.
:::

:::
:::
