---
schema: qual/card@1
id: E-HAT-3.C-14
kind: problem
title: "Coproduct from the diagonal map"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 14; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that the coproduct in the Hopf algebra $H_*(X; R)$ dual to $H^*(X; R)$ is induced by the diagonal map $X \to X \times X$, $x \mapsto (x, x)$.

::: {.solution}
Assume the degreewise finiteness hypotheses needed to identify homology and cohomology as graded duals. Let
\[
D:X\to X\times X,
\qquad D(x)=(x,x),
\]
be the diagonal map. Under the Künneth identification, write
\[
D_*:H_*(X;R)\to H_*(X;R)\otimes H_*(X;R).
\]

For $z\in H_*(X;R)$ and cohomology classes $\alpha,\beta$, naturality of the Kronecker pairing gives
\[
\langle D_*z,\alpha\times\beta\rangle
=\langle z,D^*(\alpha\times\beta)\rangle.
\]
But by the definition of cup product,
\[
D^*(\alpha\times\beta)=\alpha\smile\beta.
\]
Hence
\[
\langle D_*z,\alpha\times\beta\rangle
=\langle z,\alpha\smile\beta\rangle.
\]
This identity says exactly that $D_*$ is the linear dual of the cup-product multiplication
\[
H^*(X;R)\otimes H^*(X;R)\to H^*(X;R).
\]
Therefore the coproduct in the Hopf algebra $H_*(X;R)$ dual to $H^*(X;R)$ is precisely the map induced by the diagonal.
:::
