---
schema: qual/card@1
id: P-TOPF03D
kind: problem
title: "Homology of the exterior of a thickened torus in S^3 via Mayer-Vietoris"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
  - Knot Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $N$ be a submanifold of $S^3$ which is homeomorphic to a thickened torus $T^2 \times I$.
Let $X$ be its exterior, that is the closure of $S^3 \setminus N$.
Use Mayer-Vietoris to compute the homology $H_*(X; \mathbb{Z})$.
:::

::: {.solution}
<1>1. Setup the Mayer–Vietoris sequence for $S^3 = X \cup N$.
<2>1. $N \cong T^2 \times [0, 1]$ is a thickened torus, so $N$ deformation retracts onto $T^2$.
Proof: $[0, 1]$ is contractible.
<2>2. The intersection $A = X \cap N = \partial N = T_0^2 \sqcup T_1^2$ is the disjoint union of two 2-dimensional tori.
Proof: $\partial(T^2 \times [0, 1]) = (T^2 \times \{0\}) \cup (T^2 \times \{1\})$.
<2>3. The homology groups of $N$ and $A$ are:
\[
H_k(N) \cong \begin{cases} \mathbb{Z} & k = 0, 2, \\ \mathbb{Z}^2 & k = 1, \\ 0 & k \ge 3, \end{cases}
\qquad
H_k(A) \cong \begin{cases} \mathbb{Z}^2 & k = 0, 2, \\ \mathbb{Z}^4 & k = 1, \\ 0 & k \ge 3. \end{cases}
\]
Proof: homology of $T^2$ and disjoint union $H_k(T^2 \sqcup T^2) \cong H_k(T^2) \oplus H_k(T^2)$.
<2>4. The reduced Mayer–Vietoris sequence for $(S^3, X, N)$ is:
\[
0 \to \widetilde{H}_3(S^3) \xrightarrow{\partial_3} H_2(A) \to H_2(X) \oplus H_2(N) \to \widetilde{H}_2(S^3) \to H_1(A) \to H_1(X) \oplus H_1(N) \to \widetilde{H}_1(S^3) \to \widetilde{H}_0(A) \to \widetilde{H}_0(X) \oplus \widetilde{H}_0(N) \to \widetilde{H}_0(S^3) \to 0.
\]
Proof: Mayer–Vietoris theorem for open regular neighborhoods in manifolds.

<1>2. Compute $H_0(X)$ and path components:
<2>1. $\widetilde{H}_0(S^3) = 0$, $\widetilde{H}_0(N) = 0$ (since $N$ is path-connected), and $\widetilde{H}_0(A) \cong \mathbb{Z}$ (since $A = T_0^2 \sqcup T_1^2$ has two path components).
Proof: path connectivity of $S^3, N$ and two components of $A$.
<2>2. The tail of the Mayer–Vietoris sequence gives $0 \to \widetilde{H}_0(A) \xrightarrow{i_*} \widetilde{H}_0(X) \to 0$.
Proof: $\widetilde{H}_1(S^3) = 0$ and $\widetilde{H}_0(N) = 0$.
<2>3. Thus $\widetilde{H}_0(X) \cong \widetilde{H}_0(A) \cong \mathbb{Z}$, so $H_0(X) \cong \mathbb{Z}^2$ ($X$ has two path components).
Proof: $H_0(X) \cong \widetilde{H}_0(X) \oplus \mathbb{Z}$.

<1>3. Compute $H_2(X)$ and $H_k(X)$ for $k \ge 3$:
<2>1. $X$ is a compact 3-manifold with non-empty boundary $\partial X = T^2 \sqcup T^2$, so $H_k(X) = 0$ for all $k \ge 3$.
Proof: homology of non-closed 3-manifolds vanishes in dimension $\ge 3$.
<2>2. The sequence at degree 3 to 2 is:
\[
0 \to \mathbb{Z} \xrightarrow{\partial_3} \mathbb{Z}^2 \xrightarrow{\Phi_2} H_2(X) \oplus \mathbb{Z} \to 0.
\]
Proof: $\widetilde{H}_3(S^3) \cong \mathbb{Z}$, $H_2(A) \cong \mathbb{Z}^2$, $H_2(N) \cong \mathbb{Z}$, and $\widetilde{H}_2(S^3) = 0$.
<2>3. The boundary map $\partial_3: H_3(S^3) \to H_2(A)$ sends $[S^3]$ to $([T_0^2], -[T_1^2])$, which is a primitive vector in $H_2(A) \cong \mathbb{Z}^2$.
Proof: orientation of the boundary $\partial N$.
<2>4. Thus $\operatorname{coker}(\partial_3) \cong \mathbb{Z}^2 / \mathbb{Z} \cong \mathbb{Z}$.
Proof: quotient of $\mathbb{Z}^2$ by a rank-1 primitive submodule.
<2>5. By exactness, $H_2(X) \oplus \mathbb{Z} \cong \operatorname{coker}(\partial_3) \cong \mathbb{Z}$, which implies $H_2(X) \cong 0$.
Proof: <2>2 and <2>4.

<1>4. Compute $H_1(X)$:
<2>1. Since $\widetilde{H}_2(S^3) = 0$ and $\widetilde{H}_1(S^3) = 0$, the sequence at degree 1 is an isomorphism:
\[
0 \to H_1(A) \xrightarrow{(i_{X*}, i_{N*})} H_1(X) \oplus H_1(N) \to 0.
\]
Proof: Mayer–Vietoris exactness.
<2>2. Thus $H_1(X) \oplus H_1(N) \cong H_1(A) \cong \mathbb{Z}^4$.
Proof: <2>1 and <1>1.
<2>3. Since $H_1(N) \cong \mathbb{Z}^2$ is a free abelian group of rank 2, $H_1(X) \cong \mathbb{Z}^4 / \mathbb{Z}^2 \cong \mathbb{Z}^2$.
Proof: classification of finitely generated free abelian groups.

<1>5. Conclusion:
\[
H_k(X; \mathbb{Z}) \cong \begin{cases}
\mathbb{Z}^2 & k = 0, \\
\mathbb{Z}^2 & k = 1, \\
0 & k \ge 2.
\end{cases}
\]
Q.E.D.
Proof: <1>2, <1>3, and <1>4.
:::
