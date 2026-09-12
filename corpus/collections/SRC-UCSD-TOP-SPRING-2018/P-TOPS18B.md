---
schema: qual/card@1
id: P-TOPS18B
kind: problem
title: "Mayer-Vietoris computation of a closed 4-manifold from gluing two copies of B^2 x S^2"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
  - Manifolds
  - Intersection Theory
  - Homotopy Type
relations: []
review: draft
---

::: problem
Let $S^2$ be the standard unit sphere, and let $R_\theta : S^2 \to S^2$ be the operation of rotation through angle $\theta$ anticlockwise about the $z$-axis.
Let $M$ be the closed $4$-manifold obtained by gluing together two copies $A_1, A_2$ of $B^2 \times S^2$ along their common boundary $S^1 \times S^2$; specifically, identify
$$
(e^{i\theta}, v) \in \partial A_1 \sim (e^{i\theta}, R_\theta(v)) \in \partial A_2 \quad \text{for all } e^{i\theta} \in S^1, v \in S^2.
$$
Use Mayer-Vietoris to compute $H_*(M; \mathbb{Z})$.
Give an example of another closed $4$-manifold $N$ with the same homology, and use intersection theory to show that $M$ and $N$ are not homotopy-equivalent.
:::

::: {.solution}
<1>1. In the Mayer--Vietoris decomposition $M=A_1\cup A_2$, each $A_i\simeq S^2$ and $A_1\cap A_2\simeq S^1\times S^2$.
::: {.proof}
Each $A_i=B^2\times S^2$ deformation retracts onto the $S^2$ factor, while the common boundary is $S^1\times S^2$.
:::

<1>2. The Mayer--Vietoris sequence gives
$$\boxed{H_k(M;\mathbb Z)\cong\begin{cases}
\mathbb Z,&k=0,4,\\
\mathbb Z^2,&k=2,\\
0,&\text{otherwise.}
\end{cases}}$$
::: {.proof}
The only nonzero homology of the overlap is $H_0=H_1=H_2=H_3=\mathbb Z$. The maps $H_2(S^1\times S^2)\to H_2(A_1)\oplus H_2(A_2)$ are $(1,-1)$ up to orientation conventions, because each boundary inclusion preserves the $S^2$ fiber class (the rotation $R_\theta$ has degree $1$ on $S^2$). Thus its cokernel is $\mathbb Z$, while exactness at the adjacent $H_1$ term contributes one further free generator to $H_2(M)$; the $H_3$ overlap produces $H_4(M)\cong\mathbb Z$, and all odd-dimensional homology vanishes. Equivalently, this is the standard homology calculation for an oriented $S^2$-bundle over $S^2$.
:::

<1>3. The clutching loop $\theta\mapsto R_\theta$ represents the nontrivial element of
$$\pi_1(SO(3))\cong\mathbb Z/2,$$
so $M$ is the nontrivial oriented $S^2$-bundle over $S^2$.
::: {.proof}
The construction glues two trivial bundles over the hemispheres of the base $S^2$ by exactly this loop of fiber rotations along the equator. A full $2\pi$ rotation is the nontrivial loop in $SO(3)$.
:::

<1>4. This nontrivial bundle is diffeomorphic to $\mathbb{CP}^2\#\overline{\mathbb{CP}}^{\,2}$ and has intersection form
$$Q_M\cong\begin{pmatrix}1&0\\0&-1\end{pmatrix},$$
which is odd.
::: {.proof}
The two oriented $S^2$-bundles over $S^2$ are classified by $\pi_1(SO(3))\cong\mathbb Z/2$. The nontrivial bundle is the first Hirzebruch surface, diffeomorphic to $\mathbb{CP}^2\#\overline{\mathbb{CP}}^{\,2}$; its standard exceptional and hyperplane classes give the displayed form.
:::

<1>5. Take $N=S^2\times S^2$. It has the same integral homology groups as $M$, but its intersection form is
$$Q_N\cong\begin{pmatrix}0&1\\1&0\end{pmatrix},$$
which is even.
::: {.proof}
The two factor classes generate $H_2(S^2\times S^2)$, have self-intersection $0$, and intersect each other once.
:::

<1>6. Hence $M$ and $N$ are not homotopy equivalent.
::: {.proof}
An orientation-preserving homotopy equivalence of closed oriented $4$-manifolds preserves the integral intersection form up to isomorphism (and orientation reversal changes only its overall sign). Parity is invariant under either operation, while $Q_M$ is odd and $Q_N$ is even.
:::
:::
