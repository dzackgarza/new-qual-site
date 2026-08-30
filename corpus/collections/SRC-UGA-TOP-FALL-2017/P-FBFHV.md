---
schema: qual/card@1
id: P-FBFHV
kind: problem
title: Fundamental group and homology of two $2$-spheres glued by a two-sheeted covering
  of equators
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homology
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Compute, by any means available, the fundamental group and all the homology groups of the space obtained by gluing one copy $A$ of $S^2$ to another copy $B$ of $S^2$ via a two-sheeted covering space map from the equator of $A$ onto the equator of $B$.
:::

::: {.solution}
<1>1. Computation of the fundamental group $\pi_1(X)$:
<2>1. Decompose $X$ into two open sets $U$ and $V$, where $U$ is a regular neighborhood of $S_A^2$ and $V$ is a regular neighborhood of $S_B^2$ in $X$.
Then $U \simeq S_A^2 \cong S^2$ and $V \simeq S_B^2 \cong S^2$ deformation retract onto 2-spheres, so:
\[
\pi_1(U) \cong \{0\}, \qquad \pi_1(V) \cong \{0\}.
\]
Proof: spheres of dimension $\ge 2$ are simply connected.
<2>2. The intersection $U \cap V$ deformation retracts onto the circle $S_B^1$, which is path-connected.
By the Seifert–van Kampen Theorem:
\[
\pi_1(X) \cong \pi_1(U) *_{\pi_1(U \cap V)} \pi_1(V) \cong \{0\} *_{\mathbb{Z}} \{0\} \cong \{0\}.
\]
Thus $X$ is simply connected.
Proof: Seifert–van Kampen Theorem.

<1>2. Computation of homology groups via the Mayer–Vietoris sequence:
<2>1. Consider the Mayer–Vietoris sequence associated to the decomposition $(U, V)$ with $U \cap V \simeq S^1$:
\[
\cdots \to H_2(U \cap V) \to H_2(U) \oplus H_2(V) \to H_2(X) \xrightarrow{\partial_*} H_1(U \cap V) \to H_1(U) \oplus H_1(V) \to \cdots
\]
Proof: Mayer–Vietoris exact sequence.
<2>2. Substitute the known homology groups $H_*(S^2)$ and $H_*(S^1)$:
- $H_2(U \cap V) \cong H_2(S^1) = 0$,
- $H_2(U) \oplus H_2(V) \cong H_2(S^2) \oplus H_2(S^2) \cong \mathbb{Z} \oplus \mathbb{Z}$,
- $H_1(U \cap V) \cong H_1(S^1) \cong \mathbb{Z}$,
- $H_1(U) \oplus H_1(V) \cong 0 \oplus 0 = 0$.
Proof: homology of spheres.
<2>3. The sequence in low degrees becomes:
\[
0 \longrightarrow \mathbb{Z}^2 \longrightarrow H_2(X) \xrightarrow{\;\partial_*\;} \mathbb{Z} \longrightarrow 0 \longrightarrow H_1(X) \longrightarrow 0.
\]
From the exact sequence:
- $H_1(X) = 0$.
- The short exact sequence $0 \to \mathbb{Z}^2 \to H_2(X) \to \mathbb{Z} \to 0$ splits because the quotient $\mathbb{Z}$ is free abelian, yielding:
\[
H_2(X) \cong \mathbb{Z}^2 \oplus \mathbb{Z} \cong \mathbb{Z}^3.
\]
Proof: splitting lemma for free abelian groups.

<1>3. Higher homology groups:
<2>1. For $n \ge 3$, $H_n(U) = 0$, $H_n(V) = 0$, and $H_{n-1}(U \cap V) = 0$, so $H_n(X) = 0$.
For $n = 0$, since $X$ is path-connected, $H_0(X) \cong \mathbb{Z}$.
Proof: dimension of CW complex is 2 and path-connectedness.

<1>4. Conclusion:
$\pi_1(X) = 0$, and the homology groups are $H_0(X) \cong \mathbb{Z}$, $H_1(X) = 0$, $H_2(X) \cong \mathbb{Z}^3$, and $H_n(X) = 0$ for all $n \ge 3$. Q.E.D.
Proof: <1>1 through <1>3.
:::
