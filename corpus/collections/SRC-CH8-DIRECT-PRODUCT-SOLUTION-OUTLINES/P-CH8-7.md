---
schema: qual/card@1
id: P-CH8-7
kind: problem
title: Chapter 8 exercise 7
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
Prove that $G _ { 1 } \oplus G _ { 2 }$ is isomorphic to $G _ { 2 } \oplus G _ { 1 }$ . State the general case.
:::

::: {.solution}
Proof.
Define $\phi : G _ { 1 } \oplus G _ { 2 } \to G _ { 2 } \oplus G _ { 1 }$ by $\left( g _ { 1 } , g _ { 2 } \right) \mapsto \left( g _ { 2 } , g _ { 1 } \right)$ . We claim that $\phi$ is an isomorphism.
By construction it is clear that $\phi$ maps from $G _ { 1 } \oplus G _ { 2 }$ to $G _ { 2 } \oplus G _ { 1 }$ . Now $\phi ( ( g _ { 1 } , g _ { 2 } ) ( h _ { 1 } , h _ { 2 } ) ) = \phi ( ( g _ { 1 } h _ { 1 } , g _ { 2 } h _ { 2 } ) ) = ( g _ { 2 } h _ { 2 } , g _ { 1 } h _ { 1 } ) = ( g _ { 2 } , g _ { 1 } ) ( h _ { 2 } , h _ { 1 } ) = \phi ( g _ { 1 } , g _ { 2 } ) \phi ( h _ { 1 } , h _ { 2 } )$ so $\phi$ is indeed a homomorphism.
If we let $\phi ( ( g _ { 1 } , g _ { 2 } ) ) = \phi ( ( h _ { 1 } , h _ { 2 } ) )$ then $\left( g _ { 2 } , g _ { 1 } \right) = \left( h _ { 2 } , h _ { 1 } \right)$ so $g _ { 2 } = h _ { 2 }$ and $g _ { 1 } = h _ { 1 }$ . Thus $\left( g _ { 1 } , g _ { 2 } \right) = \left( h _ { 1 } , h _ { 2 } \right)$ and we know $\phi$ is one to one.
Finally we show $\phi$ is onto.
Let $( g _ { 2 } , g _ { 1 } ) \in G _ { 2 } \oplus G _ { 1 }$ . Then we know that $( g _ { 1 } , g _ { 2 } ) \in G _ { 1 } \oplus G _ { 2 }$ . Moreover, $\phi ( ( g _ { 1 } , g _ { 2 } ) ) = ( g _ { 2 } , g _ { 1 } )$ and $\phi$ is indeed onto.
□

In general, $G _ { 1 } \oplus G _ { 2 } \oplus \cdots \oplus G _ { n } \approx G _ { \sigma ( 1 ) } \oplus G _ { \sigma ( 2 ) } \oplus \cdots \oplus G _ { \sigma ( n ) }$ for $\sigma \in S _ { n }$ .
:::
