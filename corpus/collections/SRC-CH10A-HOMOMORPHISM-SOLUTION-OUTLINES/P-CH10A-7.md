---
schema: qual/card@1
id: P-CH10A-7
kind: problem
title: Chapter 10A exercise 7
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
If φ is a homomorphism from G to H and $\sigma$ is a homomorphism from H to K, show that σφ is a homomorphism from G to K. How are Kerφ and Kerσφ related?
:::

::: {.solution}
Let $\phi : G \to H$ be a homomorphism and $\sigma : H \to K$ also be a group homomorphism.
Then $\sigma \phi : G \to K$ and $\sigma \phi ( x y ) = \sigma ( \phi ( x ) \phi ( y ) ) = \sigma ( \phi ( x ) ) \sigma ( \phi ( y ) ) = \sigma \phi ( x ) \sigma \phi ( y )$ so the composition is a homomorphism.

Notice that $\sigma$ is a homomorphism so the ker $\phi$ maps to the identity in H. Since $\sigma$ is also a homomorphism, it maps this identity to the identity in K. Thus, $K e r \phi \subseteq K e r \sigma \phi$ . Note that more things from H could map to the identity in K so we do not know that the $K e r \phi = K e r \sigma \phi$
:::
