---
schema: qual/card@1
id: P-ASHJM
kind: problem
title: Classification of compact surfaces, with $H_1$ and Euler characteristic
classification:
  areas:
  - topology
  topics:
  - Classification
  - Surfaces
  - Homology
  - Euler Characteristic
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 7 of the official UGA Fall 2005 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the orientable and nonorientable cellular homology computations and the genus-two identifications.
---

::: problem
State the classification theorem for surfaces (compact, without boundary, but not necessarily orientable).
For each surface in the classification, indicate the structure of the first homology group and the value of the Euler characteristic.

Also, explain briefly how the 2-holed torus and the connected sum $\RP^2 \# \RP^2$ fit into the classification.
:::

::: {.solution}
<1>1. Every compact connected surface without boundary is homeomorphic to exactly one surface of one of the following two types:
\[
M_g=\mathop{\#}_{i=1}^{g}T^2
\qquad(g\ge0),
\]
where $M_0=S^2$, or
\[
N_k=\mathop{\#}_{i=1}^{k}\RP^2
\qquad(k\ge1).
\]
The surfaces $M_g$ are orientable and the surfaces $N_k$ are nonorientable.
::: {.proof}
This is the classification theorem for compact connected surfaces.
The orientability and the integer $g$ or $k$ determine the homeomorphism type uniquely.
If disconnected surfaces are allowed, each connected component is one of these surfaces.
:::

<1>2. For the orientable surface $M_g$,
\[
H_1(M_g;\ZZ)\cong\ZZ^{2g},
\qquad
\chi(M_g)=2-2g.
\]
::: {.proof}
Use the standard CW structure with one $0$-cell, $2g$ oriented $1$-cells
\[
a_1,b_1,\ldots,a_g,b_g,
\]
and one $2$-cell attached by the word
\[
[a_1,b_1]\cdots[a_g,b_g].
\]
Thus
\[
C_2\cong\ZZ,
\qquad
C_1\cong\ZZ^{2g},
\qquad
C_0\cong\ZZ.
\]
Since there is one vertex, $\partial_1=0$.
The cellular boundary $\partial_2$ records the total exponent of each $1$-cell in the attaching word.
Every commutator has exponent sum zero in each generator, so $\partial_2=0$.
Therefore
\[
H_1(M_g;\ZZ)=\ker\partial_1/\operatorname{im}\partial_2\cong\ZZ^{2g}.
\]
The same CW structure gives
\[
\chi(M_g)=1-2g+1=2-2g.
\]
:::

<1>3. For the nonorientable surface $N_k$,
\[
H_1(N_k;\ZZ)\cong\ZZ^{k-1}\oplus\ZZ/2\ZZ,
\qquad
\chi(N_k)=2-k.
\]
::: {.proof}
Use the standard CW structure with one $0$-cell, $k$ oriented $1$-cells
\[
a_1,\ldots,a_k,
\]
and one $2$-cell attached by
\[
a_1^2a_2^2\cdots a_k^2.
\]
Again $\partial_1=0$, while the exponent sums give
\[
\partial_2(1)=2(a_1+\cdots+a_k).
\]
Hence
\[
H_1(N_k;\ZZ)
\cong
\ZZ^k/\langle2(1,\ldots,1)\rangle.
\]
The vector $(1,\ldots,1)$ is primitive, so it can be completed to a basis of $\ZZ^k$.
In such a basis the single relation is $2e_1=0$.
Therefore
\[
H_1(N_k;\ZZ)\cong\ZZ^{k-1}\oplus\ZZ/2\ZZ.
\]
The CW structure has one $0$-cell, $k$ $1$-cells, and one $2$-cell, so
\[
\chi(N_k)=1-k+1=2-k.
\]
:::

<1>4. The 2-holed torus is the orientable genus-two surface
\[
M_2=T^2\#T^2,
\]
so
\[
H_1(M_2;\ZZ)\cong\ZZ^4,
\qquad
\chi(M_2)=-2.
\]
::: {.proof}
By definition, a closed orientable surface with two handles is the connected sum of two tori, hence is $M_2$ in the orientable branch of the classification.
The displayed invariants follow from <1>2 with $g=2$.
:::

<1>5. The connected sum
\[
\RP^2\#\RP^2
\]
is $N_2$, equivalently the Klein bottle, and therefore
\[
H_1(\RP^2\#\RP^2;\ZZ)\cong\ZZ\oplus\ZZ/2\ZZ,
\qquad
\chi(\RP^2\#\RP^2)=0.
\]
::: {.proof}
By the definition of the nonorientable family,
\[
N_2=\RP^2\#\RP^2.
\]
The standard polygon presentations show that $N_2$ is homeomorphic to the Klein bottle.
The displayed invariants are the case $k=2$ of <1>3.
:::
:::
