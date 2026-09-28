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

::: {.problem}
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
The natural action on $\FF_q^2$ is a representation over the field $\FF_q$; it is **not** a complex representation, since a finite field of characteristic $p$ does not embed as a field in $\CC$.

Complex representations can instead be constructed from honest $G$-sets and complex group-algebra operations. For example, the action on the projective line
\[
\PP^1(\FF_q)
\]
with $q+1$ points gives a permutation representation on
\[
\CC[\PP^1(\FF_q)].
\]
Other standard constructions include the regular representation, induction from the Borel subgroup or from split and nonsplit tori, tensor products and duals, and irreducible constituents of these representations. The permutation representation on $\PP^1(\FF_q)$ contains the trivial representation and the $q$-dimensional Steinberg representation.

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
