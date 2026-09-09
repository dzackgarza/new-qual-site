---
schema: qual/card@1
id: P-GLKAB
kind: problem
title: Discriminant of a polynomial
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Polynomials
  - Symmetric Functions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
What is the discriminant of a polynomial?
:::


::: {.solution}
Let
\[
f(x)=a_n\prod_{i=1}^n(x-r_i)
\]
in a splitting field, with $a_n\ne0$. The discriminant of $f$ is
\[
\operatorname{Disc}(f)
=
a_n^{2n-2}\prod_{1\le i<j\le n}(r_i-r_j)^2.
\]

Equivalently,
\[
\operatorname{Disc}(f)
=
(-1)^{n(n-1)/2}a_n^{-1}\operatorname{Res}(f,f').
\]
Because the product of squared root differences is symmetric in the roots, the fundamental theorem of symmetric polynomials shows that the discriminant is a polynomial in the coefficients of $f$.

Over a field, one has
\[
\operatorname{Disc}(f)=0
\iff
f\text{ has a repeated root}
\iff
\gcd(f,f')\ne1.
\]
For a monic quadratic $x^2+bx+c$, this recovers the familiar discriminant $b^2-4c$.
:::
