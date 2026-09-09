---
schema: qual/card@1
id: P-7FMWE
kind: problem
title: The discriminant of a polynomial is a polynomial in the coefficients, via symmetric
  polynomials
classification:
  areas:
  - algebra
  topics:
  - Symmetric Functions
  - Polynomials
  - Galois Theory
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
Is the discriminant of a polynomial always a polynomial in the coefficients?
What does this have to do with symmetric polynomials?
:::


::: {.solution}
Yes. For a fixed degree, the discriminant is a polynomial with integer coefficients in the coefficients of the polynomial.

<1>1. First suppose
\[
f(x)=x^n+c_1x^{n-1}+\cdots+c_n
\]
is monic, with roots $r_1,\ldots,r_n$ in a splitting field. Its discriminant is
\[
\Delta(f)=\prod_{i<j}(r_i-r_j)^2.
\]
::: {.proof}
This is the usual root definition of the discriminant of a monic polynomial.
:::

<1>2. The polynomial
\[
D(r_1,\ldots,r_n)=\prod_{i<j}(r_i-r_j)^2
\]
is symmetric in the roots.
::: {.proof}
Permuting the roots permutes the unordered pairs $\{i,j\}$ and therefore leaves the product unchanged. Equivalently, the unsquared Vandermonde changes by the sign of the permutation, so its square is invariant.
:::

<1>3. Hence $D$ is a polynomial in the elementary symmetric polynomials
\[
e_1(r),\ldots,e_n(r).
\]
::: {.proof}
By the fundamental theorem of symmetric polynomials, every symmetric polynomial with integer coefficients is a polynomial with integer coefficients in the elementary symmetric polynomials. Thus there exists
\[
P\in\ZZ[y_1,\ldots,y_n]
\]
such that
\[
D=P(e_1,\ldots,e_n).
\]
:::

<1>4. Therefore the discriminant is a polynomial in the coefficients $c_i$.
::: {.proof}
Viète's formulas give
\[
e_i(r_1,\ldots,r_n)=(-1)^i c_i.
\]
Substituting these into <1>3 yields
\[
\Delta(f)=P(-c_1,c_2,\ldots,(-1)^n c_n),
\]
a polynomial in the coefficients.
:::

<1>5. For a general degree-$n$ polynomial
\[
f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_0,
\qquad a_n\ne0,
\]
the usual discriminant
\[
\Delta(f)=a_n^{2n-2}\prod_{i<j}(r_i-r_j)^2
\]
is likewise a polynomial with integer coefficients in $a_0,\ldots,a_n$.
::: {.proof}
One equivalent formula is
\[
\Delta(f)=(-1)^{n(n-1)/2}a_n^{-1}\operatorname{Res}(f,f').
\]
The resultant is the determinant of the Sylvester matrix, hence a polynomial with integer coefficients in the coefficients of $f$ and $f'$. For the universal degree-$n$ polynomial, that resultant is divisible by the leading coefficient $a_n$, and the quotient is precisely the displayed discriminant. Equivalently, homogenizing the monic symmetric-polynomial expression in <1>4 by the factor $a_n^{2n-2}$ clears all denominators. Thus $\Delta(f)\in\ZZ[a_0,\ldots,a_n]$.
:::

<1>6. This explains the role of symmetric polynomials.
::: {.proof}
The roots themselves depend on choices and need not lie in the coefficient field, but the squared Vandermonde is invariant under every permutation of the roots. Symmetry is exactly what allows the root expression to descend to a polynomial expression in the elementary symmetric functions, i.e. in the coefficients.
:::
:::
