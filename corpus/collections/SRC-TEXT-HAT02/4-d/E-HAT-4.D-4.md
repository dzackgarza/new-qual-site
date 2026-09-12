---
schema: qual/card@1
id: E-HAT-4.D-4
kind: problem
title: "Cohomology of complex flag manifolds"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.D, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

For the flag space $F_n(\mathbb{C}^n)$ show that $H^*(F_n(\mathbb{C}^n); \mathbb{Z}) \approx \mathbb{Z}[x_1, \ldots, x_n]/(\sigma_1, \ldots, \sigma_n)$ where $\sigma_i$ is the $i$th elementary symmetric polynomial.

::: {.solution}
Let \(F_n=F_n(\mathbb C^n)\) be the complete flag manifold, and let
\[
L_1,\ldots,L_n\to F_n
\]
be the tautological line bundles: over a flag their fibers are the successive one-dimensional quotients. Put
\[
x_i=c_1(L_i)\in H^2(F_n;\mathbb Z).
\]
Their direct sum is the trivial bundle \(\underline{\mathbb C}^n\), so
\[
\prod_{i=1}^n(1+x_i)=1.
\]
Equating homogeneous parts gives
\[
\sigma_1(x_1,\ldots,x_n)=\cdots=
\sigma_n(x_1,\ldots,x_n)=0.
\]
Thus there is a graded-ring homomorphism
\[
\Phi:\mathbb Z[x_1,\ldots,x_n]/(\sigma_1,\ldots,\sigma_n)
\longrightarrow H^*(F_n;\mathbb Z).
\]

We show it is an isomorphism by comparing the standard flag tower. Forgetting the last line gives an iterated projective-bundle description, and repeated Leray--Hirsch shows that \(H^*(F_n;\mathbb Z)\) is free abelian with Poincaré polynomial
\[
\prod_{j=1}^n(1+t^2+\cdots+t^{2(j-1)}).
\]
Moreover the classes \(x_i\) generate at each projective-bundle stage, so \(\Phi\) is surjective.

On the algebraic side, the elementary symmetric polynomials form the standard regular sequence of symmetric invariants, and reduction successively by the monic relations gives a free abelian group with basis, for example,
\[
x_1^{a_1}x_2^{a_2}\cdots x_n^{a_n},
\qquad 0\le a_i\le n-i.
\]
Its Poincaré polynomial is the same product above (and its total rank is \(n!\)). Hence the surjection \(\Phi\) is an isomorphism:
\[
\boxed{H^*(F_n(\mathbb C^n);\mathbb Z)
\cong \mathbb Z[x_1,\ldots,x_n]/(\sigma_1,\ldots,\sigma_n).}
\]
:::
