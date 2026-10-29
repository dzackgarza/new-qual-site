---
schema: qual/card@1
id: P-UCTOP-SU07-4
kind: problem
title: 'Homology of the complement of a knotted torus in $S^4$'
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

::: {.problem}
Let $T \subseteq S^4$ be a (perhaps knotted) subspace homeomorphic to the 2-torus.
Let $N$ be a closed regular neighbourhood of $T$, so that $N$ is homotopy-equivalent to $T$.
Let $X$ be $S^4$ minus the interior of $N$, so that $X$ is a compact 4-manifold with boundary.
By considering the relative cohomology $H^*(S^4, N)$ and applying excision and Lefschetz duality, calculate the homology of $X$.
:::

::: {.solution}

::: pf

::: {.pf-step #excision-identification}
Excision identifies
$$
H^k(S^4,N;\ZZ)\cong H^k(X,\partial X;\ZZ).
$$

::: pf-proof
The decomposition $S^4=N\cup X$ has $N\cap X=\partial N=\partial X$. Excision removes the interior of $N$ from the pair $(S^4,N)$, leaving the pair $(X,\partial X)$.
:::

:::

::: {.pf-step #relative-cohomology-groups}
The relative cohomology groups of $(S^4,N)$ are
$$
H^k(S^4,N)\cong
\begin{cases}
\ZZ^2,&k=2,\\
\ZZ,&k=3,4,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof
Since $N\simeq T^2$,
$$
H^0(N)=\ZZ,\quad H^1(N)=\ZZ^2,\quad H^2(N)=\ZZ,\quad H^{\ge3}(N)=0.
$$
Insert these groups and $H^0(S^4)=H^4(S^4)=\ZZ$, with all intermediate cohomology zero, into the long exact sequence of the pair $(S^4,N)$. The map $H^0(S^4)\to H^0(N)$ is an isomorphism, giving relative groups $0$ in degrees $0,1$; the remaining exact pieces give $H^2\cong\ZZ^2$, $H^3\cong\ZZ$, and $H^4\cong\ZZ$.
:::

:::

::: {.pf-step #lefschetz-duality}
Lefschetz duality gives
$$
H_i(X;\ZZ)\cong H^{4-i}(X,\partial X;\ZZ).
$$

::: pf-proof
The manifold $X$ is a compact orientable $4$-manifold with boundary, since it is a codimension-zero submanifold of the oriented sphere $S^4$. Lefschetz duality therefore applies integrally.
:::

:::

::: pf-step
Consequently
$$
H_i(X;\ZZ)\cong
\begin{cases}
\ZZ,&i=0,1,\\
\ZZ^2,&i=2,\\
0,&i\ge3.
\end{cases}
$$

::: pf-proof
Combine steps [](#excision-identification){.pf-ref}, [](#relative-cohomology-groups){.pf-ref} and [](#lefschetz-duality){.pf-ref} and reverse degrees: $H_0\cong H^4\cong\ZZ$, $H_1\cong H^3\cong\ZZ$, $H_2\cong H^2\cong\ZZ^2$, and $H_3,H_4$ correspond to the vanishing relative groups in degrees $1,0$.
:::

:::

:::

:::

