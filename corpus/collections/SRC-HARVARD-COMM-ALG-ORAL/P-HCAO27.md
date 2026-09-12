---
schema: qual/card@1
id: P-HCAO27
kind: problem
title: Hilbert functions of ideals in graded polynomial rings
classification:
  areas:
  - algebra
  topics:
  - Hilbert Functions
  - Gröbner Bases
  - Polynomial Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Given an ideal $I$ in a graded polynomial ring, explain how to compute its Hilbert function.
:::

::: solution
Let
\[
S=k[x_1,\ldots,x_n]
\]
with its standard grading, and suppose $I\subseteq S$ is homogeneous. Choose a
term order and compute a Gröbner basis $G$ of $I$.

<1>1. Replace $I$ by its initial monomial ideal
\[
\operatorname{in}(I)
=\langle \operatorname{in}(g):g\in G\rangle.
\]
::: proof
By definition of a Gröbner basis, the leading monomials of the elements of $G$
generate the initial ideal.
:::

<1>2. For every degree $d$,
\[
\dim_k(S/I)_d
=\dim_k(S/\operatorname{in}(I))_d.
\]
::: proof
The monomials not lying in $\operatorname{in}(I)$ are the standard monomials.
Division by the Gröbner basis gives every class in $S/I$ a unique remainder
which is a $k$-linear combination of standard monomials. When $I$ is
homogeneous, this reduction preserves degree. Hence the degree-$d$ standard
monomials form a $k$-basis of $(S/I)_d$.
:::

<1>3. Therefore the Hilbert function of $S/I$ is computed by counting standard
monomials:
\[
H_{S/I}(d)
=\#\{x^\alpha:|\alpha|=d,\ x^\alpha\notin\operatorname{in}(I)\}.
\]
::: proof
This is the basis description from <1>2.
:::

<1>4. If one wants the Hilbert function of the ideal itself, then
\[
H_I(d)=\dim_k I_d
=\binom{n+d-1}{d}-H_{S/I}(d).
\]
::: proof
The degree-$d$ component of
\[
0\longrightarrow I\longrightarrow S\longrightarrow S/I\longrightarrow0
\]
is an exact sequence of finite-dimensional $k$-vector spaces, and
\[
\dim_k S_d=\binom{n+d-1}{d}.
\]
:::
:::
