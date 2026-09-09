---
schema: qual/card@1
id: P-WVWEP
kind: problem
title: $|\mathrm{GL}_2(\FF_q)|$ and its representations
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Finite Fields
  - Representation Theory
relations: []
review: draft
---

::: problem
Let $G=\GL_2(\FF_q)$.

1. Compute $|G|$.
2. Describe standard ways to construct finite-dimensional complex representations of $G$.
3. Determine the one-dimensional complex representations of $G$.
4. State the corresponding simplicity theorem for $\PSL_2(\FF_q)$.
:::

::: {.solution}
<1>1. Count invertible matrices.
The first column can be any nonzero vector of $\FF_q^2$, giving $q^2-1$ choices. The second column can be any vector not in the span of the first, giving $q^2-q$ choices. Hence
\[
|\GL_2(\FF_q)|=(q^2-1)(q^2-q)=q(q-1)^2(q+1).
\]

<1>2. Standard representation constructions.
The defining representation is the natural action on $\FF_q^2$; after choosing an embedding of the relevant character values into $\CC$, one obtains complex representations by the usual finite-group constructions: permutation representations from actions on finite $G$-sets, induction from subgroups, tensor products, duals, symmetric/exterior powers, and decomposition of the regular representation.

A particularly important permutation representation comes from the action on the projective line
\[
\PP^1(\FF_q),
\]
which has $q+1$ points.

<1>3. One-dimensional complex representations.
For $q>2$, the commutator subgroup of $\GL_2(\FF_q)$ is $\SL_2(\FF_q)$, so the abelianization is
\[
\GL_2(\FF_q)^{\mathrm{ab}}
\cong
\FF_q^\times
\]
via the determinant. Therefore every one-dimensional complex character has the form
\[
\chi\circ\det
\]
for a multiplicative character
\[
\chi:\FF_q^\times\to\CC^\times.
\]
Since $\FF_q^\times$ is cyclic of order $q-1$, there are exactly $q-1$ such characters. For $q=2$, $\GL_2(\FF_2)\cong S_3$ and its abelianization is $C_2$, giving two one-dimensional complex characters.

<1>4. Simplicity of the projective special linear group.
The classical theorem is
\[
\PSL_2(\FF_q)\text{ is simple for }q\ge4,
\]
with the small exceptions
\[
\PSL_2(\FF_2)\cong S_3,
\qquad
\PSL_2(\FF_3)\cong A_4.
\]
For example,
\[
\PSL_2(\FF_4)\cong A_5
\]
is simple.
:::
