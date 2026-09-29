---
schema: qual/card@1
id: P-TOPF07D
kind: problem
title: "Homology of the complement of a knotted S^3 in S^5 via duality"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Lefschetz Duality
  - Knot Theory
relations: []
review: draft
---

::: {.problem}
Let $K$ be a (perhaps knotted) subspace of $S^5$ which is homeomorphic to the $3$-sphere.
Let $N$ be a closed regular neighbourhood of $K$, so that $N$ is homotopy equivalent to $K$.
Let $X$ be $S^5$ minus the interior of $N$, so that $X$ is a compact $5$-manifold with boundary.
By considering the relative cohomology $H^*(S^5, N)$ and applying excision and Lefschetz duality, calculate the homology of $X$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Excision identifies
$$
H^k(S^5,N;\mathbb Z)\cong H^k(X,\partial X;\mathbb Z).
$$

::: pf-proof

In the decomposition $S^5=N\cup X$, the intersection is the common boundary. Excision removes the interior of $N$ from the pair $(S^5,N)$.

:::

:::

::: {.pf-step #s2}

Since $N\simeq S^3$, the long exact sequence of $(S^5,N)$ gives
$$
H^k(S^5,N)\cong
\begin{cases}
\mathbb Z,&k=4,5,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof

The only nonzero cohomology groups of $N$ are $H^0(N)=H^3(N)=\mathbb Z$, while those of $S^5$ are in degrees $0,5$. The map in degree zero is an isomorphism; exactness gives the displayed relative groups.

:::

:::

::: {.pf-step #s3}

Lefschetz duality gives
$$
H_i(X;\mathbb Z)\cong H^{5-i}(X,\partial X;\mathbb Z).
$$

::: pf-proof

The exterior $X$ is a compact orientable $5$-manifold with boundary, as a codimension-zero submanifold of the oriented sphere.

:::

:::

::: pf-step

Therefore
$$
\boxed{H_i(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,1,\\
0,&i\ge2.
\end{cases}}
$$

::: pf-proof

Reverse degrees in step [](#s2){.pf-ref} using steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
