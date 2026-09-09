---
schema: qual/card@1
id: E-HAT-1.3-2
kind: problem
title: "Product of covering spaces"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Took products of evenly covered neighborhoods and identified the product sheets and their homeomorphisms explicitly.
---

Show that if $p_1: \tilde{X}_1 \to X_1$ and $p_2: \tilde{X}_2 \to X_2$ are covering spaces, so is their product $p_1 \times p_2: \tilde{X}_1 \times \tilde{X}_2 \to X_1 \times X_2$.

::: {.solution}
<1>1. Fix $(x_1,x_2)\in X_1\times X_2$ and choose evenly covered neighborhoods
\[
x_i\in U_i\subseteq X_i
\qquad(i=1,2)
\]
for the coverings $p_i$.
::: {.proof}
For each $i$, the covering-space property gives a decomposition
\[
p_i^{-1}(U_i)=\coprod_{\alpha_i\in A_i}V^i_{\alpha_i},
\]
where each
\[
p_i|_{V^i_{\alpha_i}}:V^i_{\alpha_i}\to U_i
\]
is a homeomorphism.
:::

<1>2. The product $U_1\times U_2$ is an open neighborhood of $(x_1,x_2)$ in $X_1\times X_2$.
::: {.proof}
Products of open sets form a basis for the product topology.
:::

<1>3. The inverse image of this product neighborhood is
\[
(p_1\times p_2)^{-1}(U_1\times U_2)
=
\coprod_{(\alpha_1,\alpha_2)\in A_1\times A_2}
\left(V^1_{\alpha_1}\times V^2_{\alpha_2}\right).
\]
::: {.proof}
One has
\[
(p_1\times p_2)^{-1}(U_1\times U_2)
=p_1^{-1}(U_1)\times p_2^{-1}(U_2).
\]
Substituting the disjoint sheet decompositions from <1>1 and distributing the Cartesian product gives the displayed disjoint union.
Each product sheet is open in $\widetilde X_1\times\widetilde X_2$.
:::

<1>4. On every product sheet,
\[
p_1\times p_2:
V^1_{\alpha_1}\times V^2_{\alpha_2}
\longrightarrow
U_1\times U_2
\]
is a homeomorphism.
::: {.proof}
It is the product of the two homeomorphisms
\[
p_1|_{V^1_{\alpha_1}}
\quad\text{and}\quad
p_2|_{V^2_{\alpha_2}}.
\]
Its inverse is the product of their continuous inverses.
:::

<1>5. Hence $p_1\times p_2$ is a covering map.
::: {.proof}
The point $(x_1,x_2)$ was arbitrary, and <1>2--<1>4 show that it has an evenly covered neighborhood.
:::
:::
