---
schema: qual/card@1
id: P-TOPF18D
kind: problem
title: "Euler characteristic of a compact connected closed 3-manifold is zero (orientable and non-orientable)"
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Poincaré Duality
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Provided the sum is finite, the Euler characteristic $\chi(X)$ of a space $X$ is defined to be the alternating sum of the dimensions of the rational homology groups $H_i(X; \mathbb{Q})$.
Use Poincaré duality to show that the Euler characteristic of a compact connected closed orientable $3$-manifold $M^3$ is zero.
Prove that the result still holds even if $M$ is non-orientable.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $M$ is closed, connected, orientable, and $3$-dimensional, then $\chi(M)=0$.

::: pf-proof

Over $\mathbb Q$, Poincaré duality gives $b_i=b_{3-i}$. Hence
$$\chi(M)=b_0-b_1+b_2-b_3=(b_0-b_3)+(b_2-b_1)=0.$$

:::

:::

::: {.pf-step #s2}

If $M$ is nonorientable, let $p:\widetilde M\to M$ be its orientation double cover.

::: pf-proof

The orientation character defines a connected two-sheeted covering, and $\widetilde M$ is orientable.

:::

:::

::: {.pf-step #s3}

Then $\chi(\widetilde M)=2\chi(M)$.

::: pf-proof

Euler characteristic is multiplicative under finite-sheeted coverings of finite CW complexes; closed manifolds admit finite CW structures.

:::

:::

::: pf-step

Since $\widetilde M$ is a closed orientable $3$-manifold, step [](#s1){.pf-ref} gives $\chi(\widetilde M)=0$, so
$$\boxed{\chi(M)=0}.$$

::: pf-proof

Combine steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
