---
schema: qual/card@1
id: P-Y4XPA
kind: problem
title: The ring of arithmetic functions under Dirichlet convolution
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Convolution
  - Number Theory
relations: []
review: draft
---

::: {.problem}
Let $\mathcal A$ be the set of functions $f:\NN\to\CC$, with pointwise addition and Dirichlet convolution
\[
(f*g)(n)=\sum_{d\mid n}f(d)g(n/d).
\]
Show that $\mathcal A$ is a commutative ring. What further structure can be described?
:::

::: {.solution}
Pointwise addition makes $\mathcal A$ an abelian group. We verify the multiplicative axioms for Dirichlet convolution.

Commutativity follows by replacing each divisor $d\mid n$ by its complementary divisor $n/d$:
\[
(f*g)(n)
=\sum_{d\mid n}f(d)g(n/d)
=\sum_{d\mid n}g(d)f(n/d)
=(g*f)(n).
\]

For associativity,
\[
((f*g)*h)(n)
=\sum_{ab\mid n}f(a)g(b)h(n/ab)
=\sum_{abc=n}f(a)g(b)h(c),
\]
and the same triple sum equals
\[
(f*(g*h))(n).
\]

The multiplicative identity is
\[
\delta_1(n)=
\begin{cases}
1,&n=1,\\
0,&n>1.
\end{cases}
\]
Indeed,
\[
(f*\delta_1)(n)=f(n).
\]
Distributivity over pointwise addition follows term-by-term from the defining divisor sum. Hence $\mathcal A$ is a commutative ring.

An arithmetic function $f$ is a unit exactly when
\[
f(1)\ne0.
\]
If $f(1)\ne0$, its inverse is determined recursively by
\[
g(1)=f(1)^{-1},
\]
and for $n>1$,
\[
g(n)
=-\frac1{f(1)}\sum_{\substack{d\mid n\\ d>1}}f(d)g(n/d).
\]

This ring is the classical ring of arithmetic functions under Dirichlet convolution. Formally, Dirichlet series turn convolution into multiplication:
\[
\left(\sum_{n\ge1}\frac{f(n)}{n^s}\right)
\left(\sum_{n\ge1}\frac{g(n)}{n^s}\right)
=
\sum_{n\ge1}\frac{(f*g)(n)}{n^s},
\]
whenever analytic convergence is available, and otherwise as a formal identity of coefficients.
:::
