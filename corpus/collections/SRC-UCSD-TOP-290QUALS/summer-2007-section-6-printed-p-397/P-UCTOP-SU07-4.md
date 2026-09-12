---
schema: qual/card@1
id: P-UCTOP-SU07-4
kind: problem
title: Homology of S^4 minus knotted torus
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

Let $T \subseteq S^4$ be a (perhaps knotted) subspace homeomorphic to the 2-torus.
Let $N$ be a closed regular neighbourhood of $T$, so that $N$ is homotopy-equivalent to $T$.
Let $X$ be $S^4$ minus the interior of $N$, so that $X$ is a compact 4-manifold with boundary.
By considering the relative cohomology $H^*(S^4, N)$ and applying excision and Lefschetz duality, calculate the homology of $X$.

::: {.solution}
<1>1. Excision identifies
$$
H^k(S^4,N;\mathbb Z)\cong H^k(X,\partial X;\mathbb Z).
$$
:::
::: {.proof}
The decomposition $S^4=N\cup X$ has $N\cap X=\partial N=\partial X$. Excision removes the interior of $N$ from the pair $(S^4,N)$, leaving the pair $(X,\partial X)$.
:::

<1>2. The relative cohomology groups of $(S^4,N)$ are
$$
H^k(S^4,N)\cong
\begin{cases}
\mathbb Z^2,&k=2,\\
\mathbb Z,&k=3,4,\\
0,&\text{otherwise}.
\end{cases}
$$
:::
::: {.proof}
Since $N\simeq T^2$,
$$
H^0(N)=\mathbb Z,\quad H^1(N)=\mathbb Z^2,\quad H^2(N)=\mathbb Z,\quad H^{\ge3}(N)=0.
$$
Insert these groups and $H^0(S^4)=H^4(S^4)=\mathbb Z$, with all intermediate cohomology zero, into the long exact sequence of the pair $(S^4,N)$. The map $H^0(S^4)\to H^0(N)$ is an isomorphism, giving relative groups $0$ in degrees $0,1$; the remaining exact pieces give $H^2\cong\mathbb Z^2$, $H^3\cong\mathbb Z$, and $H^4\cong\mathbb Z$.
:::

<1>3. Lefschetz duality gives
$$
H_i(X;\mathbb Z)\cong H^{4-i}(X,\partial X;\mathbb Z).
$$
:::
::: {.proof}
The manifold $X$ is a compact orientable $4$-manifold with boundary, since it is a codimension-zero submanifold of the oriented sphere $S^4$. Lefschetz duality therefore applies integrally.
:::

<1>4. Consequently
$$
H_i(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,1,\\
\mathbb Z^2,&i=2,\\
0,&i\ge3.
\end{cases}
$$
:::
::: {.proof}
Combine <1>1--<1>3 and reverse degrees: $H_0\cong H^4\cong\mathbb Z$, $H_1\cong H^3\cong\mathbb Z$, $H_2\cong H^2\cong\mathbb Z^2$, and $H_3,H_4$ correspond to the vanishing relative groups in degrees $1,0$.
:::
:::

