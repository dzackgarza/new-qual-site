---
schema: qual/card@1
id: E-HAT-4.L-3
kind: problem
title: "No bundle $S^4 \\to \\mathbb{HP}^5 \\to \\mathbb{OP}^2$ exists"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.L, Exercise 3 and the current corrections; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Since there is a fiber bundle $S^2 \to \mathbb{CP}^5 \to \mathbb{HP}^2$ by Exercise 35 in §4.2, one might ask whether there is an analogous bundle $S^4 \to \mathbb{HP}^5 \to \mathbb{OP}^2$.
Use Steenrod powers for the prime 3 to show that such a bundle cannot exist.

::: {.solution}
Assume there were a fiber bundle
\[
S^4\longrightarrow\mathbb{HP}^5
\xrightarrow{p}\mathbb{OP}^2.
\]
Write
\[
H^*(\mathbb{HP}^5;\mathbb Z_3)=\mathbb Z_3[x]/(x^6),
\qquad |x|=4,
\]
and
\[
H^*(\mathbb{OP}^2;\mathbb Z_3)=\mathbb Z_3[y]/(y^3),
\qquad |y|=8.
\]

The Gysin sequence of the \(S^4\)-bundle shows that
\[
p^*:H^8(\mathbb{OP}^2;\mathbb Z_3)
\longrightarrow H^8(\mathbb{HP}^5;\mathbb Z_3)
\]
is an isomorphism: the adjacent base cohomology groups in degrees \(3\) and \(4\) vanish. Hence, after rescaling \(y\),
\[
p^*y=x^2.
\tag{1}
\]

At the prime \(3\), the reduced power \(P^1\) raises degree by \(4\). Since
\[
H^{12}(\mathbb{OP}^2;\mathbb Z_3)=0,
\]
we have
\[
P^1y=0.
\tag{2}
\]
For the generator \(x\in H^4(\mathbb{HP}^\infty;\mathbb Z_3)\), the splitting-principle calculation gives
\[
P^1x=x^2.
\]
Indeed, after restriction to \(\mathbb{CP}^\infty\) one has \(x=-u^2\), and
\[
P^1(-u^2)=-2u^4=u^4=x^2\quad\text{in }\mathbb Z_3.
\]
The Cartan formula therefore yields
\[
P^1(x^2)=2x^3\ne0.
\tag{3}
\]

Naturality applied to (1), together with (2), would give
\[
0=p^*(P^1y)=P^1(p^*y)=P^1(x^2),
\]
contradicting (3). Hence
\[
\boxed{\text{no bundle }S^4\to\mathbb{HP}^5\to\mathbb{OP}^2\text{ exists}.}
\]
:::
