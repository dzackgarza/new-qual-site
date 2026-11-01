---
schema: qual/card@1
id: E-HAT-3.C-14
kind: problem
title: Coproduct from the diagonal map
classification:
  areas:
  - topology
  topics:
  - H-Spaces
  - Hopf Algebras
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
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.C, Exercise 14; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read. The chain is correct and short: naturality of the Kronecker pairing gives
    $\langle D_*z,\alpha\times\beta\rangle=\langle z,D^*(\alpha\times\beta)\rangle$, the definition of the cup product gives $D^*(\alpha\times\beta)=\alpha\smile\beta$, so $D_*$ is the transpose of the cup product. Repaired: the closing sentence now states the two conventions it silently used — that the transpose of the product lives in $H_*\otimes H_*$ only because of the assumed degreewise finiteness and freeness, and that the identification of the dual of a tensor product with the tensor product of duals carries the Koszul sign $(-1)^{|\alpha||\beta|}$, which is why no sign is visible in the displayed identity and where it would appear if the identity is expanded. No statement changed.
---

::: {.problem}
Show that the coproduct in the Hopf algebra $H_*(X; R)$ dual to $H^*(X; R)$ is induced by the diagonal map $X \to X \times X$, $x \mapsto (x, x)$.
:::

::: {.solution}
Assume the degreewise finiteness hypotheses needed to identify homology and cohomology as graded duals. Let
$$
D:X\to X\times X,
\qquad D(x)=(x,x),
$$
be the diagonal map. Under the Künneth identification, write
$$
D_*:H_*(X;R)\to H_*(X;R)\otimes H_*(X;R).
$$

For $z\in H_*(X;R)$ and cohomology classes $\alpha,\beta$, naturality of the Kronecker pairing gives
$$
\langle D_*z,\alpha\times\beta\rangle
=\langle z,D^*(\alpha\times\beta)\rangle.
$$
But by the definition of cup product,
$$
D^*(\alpha\times\beta)=\alpha\smile\beta.
$$
Hence
$$
\langle D_*z,\alpha\times\beta\rangle
=\langle z,\alpha\smile\beta\rangle.
$$
This identity says exactly that $D_*$ is the linear dual of the cup-product multiplication
$$
H^*(X;R)\otimes H^*(X;R)\to H^*(X;R).
$$
Two conventions are being used, and they are the whole content of the last sentence. The expression "the coproduct of the dual Hopf algebra" is the transpose of the cup product under the identification
$$
(H^*(X;R)\otimes H^*(X;R))^*\cong H_*(X;R)\otimes H_*(X;R),
$$
which requires the degreewise finiteness and freeness assumed at the start; without it the right-hand side would be a product, not a tensor product of duals. And in the graded setting that identification carries the Koszul sign $(-1)^{|\alpha||\beta|}$, so the precise form of the last display is
$$
\bigl\langle D_*z,\alpha\times\beta\bigr\rangle=\bigl\langle z,\alpha\smile\beta\bigr\rangle,
$$
read as the statement that $\Delta z=\sum_i z_i'\otimes z_i''$ satisfies $\langle z,\alpha\smile\beta\rangle=\sum_i(-1)^{|z_i'||\beta|}\langle z_i',\alpha\rangle\langle z_i'',\beta\rangle$; the sign is invisible in the display only because it sits in the identification of the duals. Thus the coproduct in the Hopf algebra $H_*(X;R)$ dual to $H^*(X;R)$ is precisely the map induced by the diagonal.
:::
