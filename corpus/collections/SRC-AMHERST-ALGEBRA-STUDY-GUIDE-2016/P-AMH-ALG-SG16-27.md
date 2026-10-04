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
(March 2009) Let $F$ be a field, let $R=F[x]$ be the ring of polynomials in one variable with coefficients in $F$, and let $f(x)\in R$ be a polynomial of degree $2009$.
Let
\[
I=\{g(x)f(x)\mid g\in R\}
\]
be the set of all polynomials which are multiples of $f(x)$.
It is a fact, which you may assume, that $I$ is an ideal of $R$.
(a) For any $g,h\in R$, prove that $I+g=I+h$ if and only if $g-h$ is divisible by $f$.
(b) Prove that for any $g\in R$, there is a unique polynomial $h\in R$ with $\deg h<2009$ such that $I+g=I+h$.
:::

::: {.solution}
<1>1. For $g,h\in R$,
$$
I+g=I+h
\iff
g-h\in I.
$$

::: {.proof}
This is the standard equality criterion for cosets of the additive subgroup
$I$: two cosets are equal exactly when the difference of their representatives
lies in $I$.
:::

<1>2. For $g,h\in R$,
$$
I+g=I+h
\iff
f\mid(g-h).
$$

::: {.proof}
By definition,
$$
I=\{qf:q\in R\}.
$$
Hence $g-h\in I$ exactly when $g-h=qf$ for some $q\in R$, which is exactly
the condition that $f$ divide $g-h$.  Combine this with step <1>1.
:::

<1>3. Part (a) follows.

::: {.proof}
Step <1>2 is precisely the assertion of part (a).
:::

<1>4. For every $g\in R$, there exists $h\in R$ with
$$
\deg h<2009
$$
and
$$
I+g=I+h.
$$

::: {.proof}
By the division algorithm in $F[x]$, there are unique polynomials $q,h\in R$
such that
$$
g=qf+h
$$
with either $h=0$ or $\deg h<\deg f=2009$.  Then
$$
g-h=qf\in I,
$$
so step <1>1 gives $I+g=I+h$.
:::

<1>5. The polynomial $h$ in step <1>4 is unique among polynomials of degree
less than $2009$ representing the coset $I+g$.

::: {.proof}
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
Then $I+h=I+h'$, so by step <1>2 there exists $k\in R$ such that
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

<1>6. Part (b) follows.

::: {.proof}
Step <1>4 proves existence and step <1>5 proves uniqueness.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>3 and <1>6 establish parts (a) and (b), respectively.
:::
:::
