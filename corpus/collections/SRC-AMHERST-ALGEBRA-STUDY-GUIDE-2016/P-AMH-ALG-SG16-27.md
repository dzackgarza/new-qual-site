---
schema: qual/card@1
id: P-AMH-ALG-SG16-27
kind: problem
title: Cosets of a principal ideal in $F[x]$ and remainder representatives
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
Let $F$ be a field, let $R=F[x]$ be the ring of polynomials in one variable with coefficients in $F$, and let $f(x)\in R$ be a polynomial of degree $2009$.
Let
$$
I=\{g(x)f(x)\mid g\in R\}
$$
be the set of all polynomials which are multiples of $f(x)$.
It is a fact, which you may assume, that $I$ is an ideal of $R$.
(a) For any $g,h\in R$, prove that $I+g=I+h$ if and only if $g-h$ is divisible by $f$.
(b) Prove that for any $g\in R$, there is a unique polynomial $h\in R$ with $\deg h<2009$ such that $I+g=I+h$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}
For $g,h\in R$,
$$
I+g=I+h
\iff
g-h\in I.
$$

::: pf-proof
This is the standard equality criterion for cosets of the additive subgroup
$I$: two cosets are equal exactly when the difference of their representatives
lies in $I$.
:::

:::

::: {.pf-step #s1-2}
For $g,h\in R$,
$$
I+g=I+h
\iff
f\mid(g-h).
$$

::: pf-proof
By definition,
$$
I=\{qf:q\in R\}.
$$
Hence $g-h\in I$ exactly when $g-h=qf$ for some $q\in R$, which is exactly
the condition that $f$ divide $g-h$.  Combine this with step [](#s1-1){.pf-ref}.
:::

:::

::: pf-step
Part (a) follows.

::: pf-proof
Step [](#s1-2){.pf-ref} is precisely the assertion of part (a).
:::

:::

::: {.pf-step #s1-4}
For every $g\in R$, there exists $h\in R$ with
$$
\deg h<2009
$$
and
$$
I+g=I+h.
$$

::: pf-proof
By the division algorithm in $F[x]$, there are unique polynomials $q,h\in R$
such that
$$
g=qf+h
$$
with either $h=0$ or $\deg h<\deg f=2009$.  Then
$$
g-h=qf\in I,
$$
so step [](#s1-1){.pf-ref} gives $I+g=I+h$.
:::

:::

::: {.pf-step #s1-5}
The polynomial $h$ in step [](#s1-4){.pf-ref} is unique among polynomials of degree
less than $2009$ representing the coset $I+g$.

::: pf-proof
Suppose $h,h'\in R$ satisfy
$$
\deg h<2009,
\qquad
\deg h'<2009,
$$
and
$$
I+g=I+h=I+h'.
$$
Then $I+h=I+h'$, so by step [](#s1-2){.pf-ref} there exists $k\in R$ such that
$$
h-h'=kf.
$$
If $k\neq0$, then
$$
\deg(h-h')
=\deg(kf)
=\deg k+\deg f
\geq2009.
$$
But either $h-h'=0$ or
$$
\deg(h-h')\leq\max\{\deg h,\deg h'\}<2009,
$$
a contradiction.  Hence $k=0$, so $h-h'=0$ and therefore $h=h'$.
:::

:::

::: pf-step
Part (b) follows.

::: pf-proof
Step [](#s1-4){.pf-ref} proves existence and step [](#s1-5){.pf-ref} proves uniqueness.
:::

:::

:::

:::
