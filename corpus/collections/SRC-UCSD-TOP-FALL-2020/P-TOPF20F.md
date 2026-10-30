---
schema: qual/card@1
id: P-TOPF20F
kind: problem
title: "A map of nonzero degree induces injection on rational cohomology"
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Degree
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Let $M, N$ be two connected, closed, oriented $n$-dimensional manifolds ($n \geq 1$). Consider a continuous map $f : M \to N$ that has nonzero mapping degree.
Show that the induced map $f^* : H^k(N; \QQ) \to H^k(M; \QQ)$ is injective for any $k$.
:::

::: {.solution}

::: pf

::: {.pf-step #pairing}

For every nonzero $\alpha\in H^k(N;\QQ)$ there is $\beta\in H^{n-k}(N;\QQ)$ with $\langle \alpha\smile\beta,[N]\rangle\ne0$.

::: pf-proof

For a closed connected oriented $n$-manifold, Poincaré duality over the field $\QQ$ makes the cup-product pairing
$$
H^k(N;\QQ)\times H^{n-k}(N;\QQ)\longrightarrow \QQ,
\qquad (u,v)\longmapsto\langle u\smile v,[N]\rangle
$$
nondegenerate.

:::

:::

::: {.pf-step #naturality}

For such $\alpha,\beta$,
$$
\langle f^*\alpha\smile f^*\beta,[M]\rangle=(\deg f)\,\langle \alpha\smile\beta,[N]\rangle.
$$

::: pf-proof

By naturality of the cup product and of the Kronecker pairing,
$$
\langle f^*\alpha\smile f^*\beta,[M]\rangle
=\langle f^*(\alpha\smile\beta),[M]\rangle
=\langle \alpha\smile\beta,f_*[M]\rangle,
$$
and $f_*[M]=(\deg f)[N]$.

:::

:::

::: pf-qed

Let $\alpha\ne0$ in $H^k(N;\QQ)$ and choose $\beta$ by Step [](#pairing){.pf-ref}. The right side of Step [](#naturality){.pf-ref} is a product of two nonzero rational numbers, so it is nonzero. Hence $f^*\alpha\ne0$, and $f^*$ is injective in every degree $k$.

:::

:::

:::
