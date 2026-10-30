---
schema: qual/card@1
id: P-LAFJW
kind: problem
title: Homology of the complement of a knotted solid torus in $S^3$
classification:
  areas:
  - topology
  topics:
  - Mayer-Vietoris
  - Homology
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Let $N$ be a knotted solid torus in $S^3$, let $T$ be its boundary torus, and let $X$ be its exterior, that is the closure of $S^3 - N$.
Use Mayer-Vietoris to compute the homology $H_*(X;\ZZ)$.
:::

::: {.solution}

::: pf

::: {.pf-step #mv}

With $S^3 = N \cup X$ and $N \cap X = T$, the reduced Mayer-Vietoris sequence contains
$$
0 \to H_3(N)\oplus H_3(X) \to H_3(S^3) \xrightarrow{\partial} H_2(T) \to H_2(N)\oplus H_2(X) \to H_2(S^3) \to H_1(T) \to H_1(N)\oplus H_1(X) \to H_1(S^3).
$$

::: pf-proof

$N$ and $X$ are compact 3-manifolds with common boundary $T$, so $T$ has collar neighborhoods on both sides, and Mayer-Vietoris applies to thickenings of $N$ and $X$ that deformation retract to them. The term $H_3(T)$ on the left is zero because $T$ is a surface.

:::

:::

::: {.pf-step #known}

$H_3(N)=H_2(N)=0$, $H_1(N)\cong\ZZ$, $H_2(T)\cong\ZZ$, $H_1(T)\cong\ZZ^2$, $H_3(S^3)\cong\ZZ$, $H_2(S^3)=H_1(S^3)=0$, and $H_3(X) = 0$.

::: pf-proof

$N \simeq S^1$ and $T = S^1\times S^1$. $X$ is a compact connected 3-manifold with nonempty boundary, so $H_3(X)=0$.

:::

:::

::: {.pf-step #h2}

$H_2(X) = 0$.

::: pf-proof

The connecting map $\partial\colon H_3(S^3)\to H_2(T)$ sends the fundamental class $[S^3]$ to $[T]$: a fundamental cycle of $S^3$ is the sum of fundamental cycles of $N$ and $X$, and $\partial$ takes it to the boundary of the $N$-part, which is the fundamental cycle of $T$. So $\partial$ is an isomorphism $\ZZ \to \ZZ$.
By Step [](#mv){.pf-ref} and Step [](#known){.pf-ref} the sequence becomes $\ZZ \xrightarrow{\cong} \ZZ \to H_2(X) \to 0$, so $H_2(X)=0$.

:::

:::

::: {.pf-step #h1}

$H_1(X) \cong \ZZ$.

::: pf-proof

The remaining part of the sequence is $0 \to H_1(T) \to H_1(N)\oplus H_1(X)\to 0$, so $\ZZ^2 \cong \ZZ\oplus H_1(X)$.
$H_1(X)$ is finitely generated because $X$ is a compact manifold, so $H_1(X)\cong\ZZ$ by the structure theorem.

:::

:::

::: pf-qed

$X$ is connected, so $H_*(X;\ZZ) = \ZZ, \ZZ, 0, 0, \ldots$ in degrees $0,1,2,3,\ldots$ by Steps [](#known){.pf-ref}, [](#h2){.pf-ref} and [](#h1){.pf-ref}.

:::

:::

:::
