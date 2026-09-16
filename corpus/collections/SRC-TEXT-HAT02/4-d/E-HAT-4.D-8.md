---
schema: qual/card@1
id: E-HAT-4.D-8
kind: problem
title: "Thom space of a product bundle"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.D, Exercise 8; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
If $E$ is the product bundle $B \times D^n$ with $B$ a CW complex, show that the Thom space $T(E)$ is the $n$-fold reduced suspension $\Sigma^n(B_+)$, where $B_+$ is the union of $B$ with a disjoint basepoint, and that the Thom isomorphism specializes to the suspension isomorphism $\tilde{H}^i(B; R) \approx \tilde{H}^{n+i}(\Sigma^n B; R)$ given by the reduced cross product in §3.2.
:::

::: {.solution}
For the product disk bundle
\[
E=B\times D^n,
\qquad E'=B\times S^{n-1},
\]
the Thom space is
\[
T(E)=\frac{B\times D^n}{B\times S^{n-1}}.
\]
Adjoining a disjoint basepoint to \(B\), this quotient is naturally
\[
B_+\wedge(D^n/S^{n-1})
\cong B_+\wedge S^n
=\Sigma^n(B_+).
\]
Hence
\[
\boxed{T(E)\cong\Sigma^n(B_+).}
\]

Let \(u\in H^n(D^n,S^{n-1};R)\) be the fiber orientation class. The Thom class of the product bundle is
\[
1\times u\in H^n(B\times D^n,B\times S^{n-1};R).
\]
The Thom isomorphism sends
\[
a\in H^i(B;R)
\]
to the relative cross product
\[
a\times u.
\]
Under the quotient identification above this is exactly the reduced suspension isomorphism
\[
\widetilde H^i(B_+;R)
\xrightarrow{\cong}
\widetilde H^{i+n}(\Sigma^nB_+;R).
\]
Restricting to reduced cohomology of \(B\) gives the usual
\[
\boxed{\widetilde H^i(B;R)\cong\widetilde H^{i+n}(\Sigma^nB;R)}
\]
induced by the reduced cross product.
:::
