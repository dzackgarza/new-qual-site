---
schema: qual/card@1
id: P-UCTOP-SU14-2
kind: problem
title: Homology of complement of knotted solid torus inside solid torus
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

Let $K \subseteq V$ be a knotted solid torus $S^1 \times B^2$ inside a larger solid torus $V = S^1 \times B^2$, and let $X = V - \overset{\circ}{K}$ be the complement, obtained by removing the interior of $K$.
Compute $H_*(X; \mathbb{Z})$.

::: {.solution}
<1>1. Embed the ambient solid torus $V$ in $S^3$ as the complement of the interior of a tubular neighborhood $N(U)$ of an unknot $U$.
::: {.proof}
Every standard solid torus is homeomorphic to the exterior of an unknot in $S^3$.
:::

<1>2. Then
$$
X=V\setminus\operatorname{int}K
$$
is the exterior in $S^3$ of the two-component link consisting of the core knot of $K$ together with $U$.
::: {.proof}
Removing the interior of the knotted solid torus $K$ from $V=S^3\setminus\operatorname{int}N(U)$ is the same as removing disjoint tubular neighborhoods of the two knot components from $S^3$.
:::

<1>3. Alexander duality for a two-component link $L\subset S^3$ gives
$$
\widetilde H_i(S^3\setminus L;\mathbb Z)\cong \widetilde H^{2-i}(L;\mathbb Z).
$$
::: {.proof}
This is Alexander duality for the compact locally contractible subset $L\subset S^3$.
:::

<1>4. Since $L=S^1\sqcup S^1$,
$$
\widetilde H^0(L)\cong\mathbb Z,
\qquad H^1(L)\cong\mathbb Z^2,
$$
and all other reduced cohomology vanishes.
::: {.proof}
The reduced degree-zero cohomology of two components is $\mathbb Z$, and each circle contributes one degree-one generator.
:::

<1>5. Hence
$$
\boxed{H_i(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,2,\\
\mathbb Z^2,&i=1,\\
0,&i\ge3.
\end{cases}}
$$
::: {.proof}
The link exterior $X$ deformation-retracts onto the link complement $S^3\setminus L$. Apply <1>3--<1>4.
:::
:::
