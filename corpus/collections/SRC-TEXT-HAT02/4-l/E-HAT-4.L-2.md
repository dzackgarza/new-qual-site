---
schema: qual/card@1
id: E-HAT-4.L-2
kind: problem
title: "Cohomology operations distinguish quotients"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.L, Exercise 2 and the current corrections; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Use cohomology operations to show that the spaces $(S^1 \times \mathbb{CP}^\infty) / (S^1 \times \{x_0\})$ and $S^3 \times \mathbb{CP}^\infty$ are not homotopy equivalent.

::: {.solution}
Put
\[
X=(S^1\times\mathbb{CP}^\infty)/(S^1\times\{x_0\}),
\qquad
Y=S^3\times\mathbb{CP}^\infty.
\]
With \(\mathbb Z_2\)-coefficients, the relative Künneth theorem gives
\[
\widetilde H^*(X;\mathbb Z_2)
\cong
H^*(S^1;\mathbb Z_2)\otimes
\widetilde H^*(\mathbb{CP}^\infty;\mathbb Z_2).
\]
Let
\[
a\in H^1(S^1;\mathbb Z_2),
\qquad
x\in H^2(\mathbb{CP}^\infty;\mathbb Z_2)
\]
be the standard generators. Then the unique nonzero class in \(H^3(X;\mathbb Z_2)\) is
\[
u=a\times x.
\]
Using the Cartan formula,
\[
Sq^2(u)
=Sq^2(a\times x)
=a\times Sq^2x,
\]
since \(Sq^1a=a^2=0\) and \(Sq^2a=0\) by instability. For the degree-two generator of \(\mathbb{CP}^\infty\),
\[
Sq^2x=x^2.
\]
Hence
\[
Sq^2(u)=a\times x^2\ne0
\in H^5(X;\mathbb Z_2).
\tag{1}
\]

On the other hand, the unique nonzero class in \(H^3(Y;\mathbb Z_2)\) is the pullback
\[
v=\operatorname{pr}_1^*(\iota_3)
\]
of the fundamental class of \(S^3\). Naturality gives
\[
Sq^2(v)=\operatorname{pr}_1^*(Sq^2\iota_3)=0,
\tag{2}
\]
because \(H^5(S^3;\mathbb Z_2)=0\).

Any homotopy equivalence \(X\simeq Y\) would induce an isomorphism on mod-2 cohomology carrying the unique nonzero degree-three class to the unique nonzero degree-three class and commuting with \(Sq^2\). Equations (1) and (2) contradict this. Therefore
\[
\boxed{X\not\simeq S^3\times\mathbb{CP}^\infty.}
\]
:::
