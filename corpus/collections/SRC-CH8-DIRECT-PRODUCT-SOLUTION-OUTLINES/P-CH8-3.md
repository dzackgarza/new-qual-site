---
schema: qual/card@1
id: P-CH8-3
kind: problem
title: $G\cong G\oplus\{e_H\}$
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
Let G be a group with identity $e _ { G }$ and let H be a group with identity $e _ { H }$ . Prove that G is isomorphic to $G \oplus \{ e _ { H } \}$ and that H is isomorphic to $\{ e _ { G } \} \oplus H .$
:::

::: {.solution}
Proof.
Define $\phi : G \to G \oplus \{ e _ { H } \}$ by $g \mapsto \left( g , e _ { H } \right)$ . Since $\phi ( g h ) = ( g h , e _ { H } ) = ( g h , e _ { H } e _ { H } ) = ( g , e _ { H } ) ( h , e _ { H } ) = \phi ( g ) \phi ( h )$ , the map $\phi$ is a homomorphism.
The kernel of $\phi$ is simply $\{ g \mid \phi ( g ) = ( e _ { G } , e _ { H } ) \} = \{ g \mid ( g , e _ { H } ) = ( e _ { G } , e _ { H } ) \} = \{ g \mid g = e _ { G } \} = \{ e _ { G } \}$ so $\phi$ is one-to-one.
Finally, let $y \in G \oplus \{ e _ { H } \}$ . Then $y = \left( g , e _ { H } \right)$ for some $g \in G$ by definition of the external direct product.
Hence $\phi ( g ) = y$ and the map is also onto.
Since $\phi$ is an isomorphism, $G \approx G \oplus \{ e _ { H } \}$ . Using a similar argument, it is clear that $H \approx \{ e _ { G } \} \oplus H$ .
:::
