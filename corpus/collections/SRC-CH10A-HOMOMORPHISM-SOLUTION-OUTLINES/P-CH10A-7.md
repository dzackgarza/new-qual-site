---
schema: qual/card@1
id: P-CH10A-7
kind: problem
title: Composition of homomorphisms and their kernels
classification:
  areas:
    - algebra
  topics:
    - Group Homomorphisms
relations: []
review: draft
---

::: {.problem}
If $\phi$ is a homomorphism from $G$ to $H$ and $\sigma$ is a homomorphism from $H$ to $K$, show that $\sigma\phi$ is a homomorphism from $G$ to $K$. How are $\ker \phi$ and $\ker \sigma\phi$ related?
:::

::: {.solution}
Let $\phi : G \to H$ be a homomorphism and $\sigma : H \to K$ also be a group homomorphism.
Then $\sigma \phi : G \to K$ and $\sigma \phi ( x y ) = \sigma ( \phi ( x ) \phi ( y ) ) = \sigma ( \phi ( x ) ) \sigma ( \phi ( y ) ) = \sigma \phi ( x ) \sigma \phi ( y )$ so the composition is a homomorphism.

By definition, $\phi$ maps $\ker \phi$ to the identity in H. Since $\sigma$ is a homomorphism, it maps this identity to the identity in K. Thus, $\ker \phi \subseteq \ker \sigma\phi$. More precisely, $\ker \sigma\phi = \phi^{-1}(\ker\sigma)$, so the inclusion is strict exactly when $\ker\sigma$ contains a nonidentity element of $\phi(G)$.
:::
