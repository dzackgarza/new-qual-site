---
schema: qual/card@1
id: P-AMH-ALG-SG16-28
kind: problem
title: Cubic polynomials over a field are irreducible exactly when rootless
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
(January 1999) Let $k$ be a field. Show that a cubic polynomial $f(x)\in k[x]$ is irreducible in $k[x]$ if and only if $f(x)$ has no roots in $k$.
:::

::: {.solution}
<1>1. If the cubic polynomial $f$ is reducible, then $f$ has a root in $k$.

::: {.proof}
Since $f$ is reducible, there exist nonconstant polynomials $g,h\in k[x]$ such
that
$$
f=gh
$$
and
$$
\deg g<3,
\qquad
\deg h<3.
$$
Because
$$
\deg g+\deg h=\deg f=3
$$
and both degrees are positive integers, one factor has degree $1$ and the other
has degree $2$.  Without loss of generality, write
$$
g(x)=ax+b
$$
with $a\neq0$.  Since $k$ is a field,
$$
c=-\frac ba\in k.
$$
Then $g(c)=0$, and hence
$$
f(c)=g(c)h(c)=0.
$$
Thus $c$ is a root of $f$ in $k$.
:::

<1>2. If $f$ has a root in $k$, then $f$ is reducible.

::: {.proof}
Let $c\in k$ satisfy $f(c)=0$.  Divide $f(x)$ by $x-c$.  The division
algorithm gives polynomials $q,r\in k[x]$ such that
$$
f(x)=q(x)(x-c)+r(x)
$$
with either $r=0$ or $\deg r<1$.  Thus $r$ is a constant.  Evaluating at
$x=c$ gives
$$
0=f(c)=r,
$$
so in fact
$$
f(x)=q(x)(x-c).
$$
Since $\deg f=3$ and $\deg(x-c)=1$,
$$
\deg q=2.
$$
Thus $f$ factors as a product of two nonconstant polynomials of smaller degree,
so $f$ is reducible.
:::

<1>3. A cubic polynomial is reducible if and only if it has a root in $k$.

::: {.proof}
Step <1>1 proves the forward implication and step <1>2 proves the reverse
implication.
:::

<1>4. Therefore a cubic polynomial $f\in k[x]$ is irreducible if and only if
it has no roots in $k$.

::: {.proof}
Negating both equivalent conditions in step <1>3 gives
$$
f\text{ irreducible}
\iff
f\text{ has no root in }k.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required equivalence.
:::
:::
