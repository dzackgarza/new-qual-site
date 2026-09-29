---
schema: qual/card@1
id: P-TOPS20H
kind: problem
title: "A simply-connected closed smooth manifold with the homology of S^n is homotopy equivalent to S^n"
classification:
  areas:
  - topology
  topics:
  - Homotopy Type
  - Manifolds
  - Homology
  - Whitehead Theorem
relations: []
review: draft
---

::: {.problem}
Let $X$ be an $n$-dimensional closed smooth manifold.
Suppose $X$ is simply connected and suppose $H_k(X; \mathbb{Z}) = H_k(S^n; \mathbb{Z})$ for all $k \geq 0$.
Show that $X$ is homotopy equivalent to $S^n$.
:::

::: {.solution}

::: pf

::: pf-step
The assumptions imply that $X$ is a simply connected integral homology $n$-sphere.

::: pf-proof
This restates the hypotheses: $H_0(X)=H_n(X)=\mathbb Z$ and all intermediate homology vanishes.
:::

:::

::: {.pf-step #hurewicz-n-minus-1-connected}
The space $X$ is $(n-1)$-connected, and the Hurewicz map
$$\pi_n(X)\xrightarrow{\cong}H_n(X;\mathbb Z)\cong\mathbb Z$$
is an isomorphism.

::: pf-proof
Starting from simple connectivity, apply Hurewicz successively: if $X$ is $(k-1)$-connected for $2\le k<n$, then $\pi_k(X)\cong H_k(X)=0$, so connectivity increases by one. At degree $n$, Hurewicz identifies the first possible nonzero homotopy group with $H_n$.
:::

:::

::: pf-step
Choose $g:S^n\to X$ representing a generator of $\pi_n(X)$. Then $g$ is an integral homology equivalence.

::: pf-proof
By step [](#hurewicz-n-minus-1-connected){.pf-ref}, $g_*$ is an isomorphism on $H_n$. It is also an isomorphism on $H_0$, and all other homology groups of both spaces vanish.
:::

:::

::: pf-step
Therefore
$$\boxed{X\simeq S^n.}$$

::: pf-proof
A smooth closed manifold has the homotopy type of a finite CW complex. Both spaces are simply connected, and a homology equivalence between simply connected CW complexes is a homotopy equivalence by the homological Whitehead theorem.
:::

:::

:::

:::
