---
schema: qual/card@1
id: P-7IGID
kind: problem
title: Two non-homeomorphic connected double covers of $\RP^2\vee\RP^3$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Homotopy
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 5 of the official UGA Fall 2017 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Replaced the invalid free-product calculation for pi_2 with explicit two-sheeted coverings and an integral H_2 distinction.
---

::: problem
Describe, as explicitly as you can, two different (non-homeomorphic) connected two-sheeted covering spaces of $\RP^2\vee\RP^3$, and prove that they are not homeomorphic.
:::

::: {.solution}
Let
\[
X=\RP^2\vee\RP^3,
\]
and write $x_0$ for the wedge point.

<1>1. There is a connected double cover $p_2:Y_2\to X$ whose restriction over the $\RP^2$ summand is the universal double cover $S^2\to\RP^2$ and whose restriction over the $\RP^3$ summand is the trivial double cover.
::: {.proof}
Let
\[
q_2:S^2\longrightarrow\RP^2
\]
be the antipodal quotient, and let
\[
q_2^{-1}(x_0)=\{u_0,u_1\}.
\]
Take two copies $R_0,R_1$ of $\RP^3$ and attach the base point of $R_i$ to $u_i$.
Thus
\[
Y_2=S^2\cup_{u_0}R_0\cup_{u_1}R_1.
\]
Define $p_2$ to be $q_2$ on $S^2$ and the identity map onto the $\RP^3$ summand on each $R_i$.

Away from the wedge point this is visibly two-sheeted.
For a sufficiently small wedge neighborhood
\[
U=U_2\vee U_3
\]
of $x_0$, where each $U_j$ is evenly covered in its summand, the inverse image $p_2^{-1}(U)$ is the disjoint union of two neighborhoods of $u_0,u_1$, each mapped homeomorphically onto $U$.
Hence $p_2$ is a two-sheeted covering map.
The space $Y_2$ is connected because the sphere $S^2$ contains both $u_0$ and $u_1$ and each $R_i$ is attached to it.
:::

<1>2. There is a connected double cover $p_3:Y_3\to X$ whose restriction over the $\RP^3$ summand is the universal double cover $S^3\to\RP^3$ and whose restriction over the $\RP^2$ summand is the trivial double cover.
::: {.proof}
Let
\[
q_3:S^3\longrightarrow\RP^3
\]
be the antipodal quotient, with
\[
q_3^{-1}(x_0)=\{v_0,v_1\}.
\]
Take two copies $P_0,P_1$ of $\RP^2$ and attach the base point of $P_i$ to $v_i$.
Set
\[
Y_3=S^3\cup_{v_0}P_0\cup_{v_1}P_1.
\]
Define $p_3$ to be $q_3$ on $S^3$ and the identity map onto the $\RP^2$ summand on each $P_i$.
The same evenly-covered-neighborhood argument as in <1>1 shows that $p_3$ is a two-sheeted covering map, and $Y_3$ is connected because $S^3$ contains both attachment points.
:::

<1>3. The covering spaces $Y_2$ and $Y_3$ are not homeomorphic.
::: {.proof}
Attaching a path-connected space to another path-connected space at one point gives, in every positive degree, the direct sum of their reduced homology groups by the reduced Mayer--Vietoris sequence.
Applying this twice gives
\[
H_2(Y_2;\ZZ)
\cong
H_2(S^2;\ZZ)
\oplus H_2(\RP^3;\ZZ)
\oplus H_2(\RP^3;\ZZ)
\cong\ZZ,
\]
whereas
\[
H_2(Y_3;\ZZ)
\cong
H_2(S^3;\ZZ)
\oplus H_2(\RP^2;\ZZ)
\oplus H_2(\RP^2;\ZZ)
=0.
\]
Therefore $H_2(Y_2;\ZZ)$ and $H_2(Y_3;\ZZ)$ are not isomorphic.
Since homeomorphic spaces have isomorphic homology groups, $Y_2$ and $Y_3$ are not homeomorphic.
:::
:::
