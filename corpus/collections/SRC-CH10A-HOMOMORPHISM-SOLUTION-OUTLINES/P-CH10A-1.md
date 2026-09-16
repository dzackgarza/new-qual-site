---
schema: qual/card@1
id: P-CH10A-1
kind: problem
title: The determinant is a homomorphism $GL(2,\mathbb R)\to\mathbb R^*$
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
Prove that the mapping given in Example 2 is a homomorphism.
:::

::: {.solution}
Let $\phi : G L ( 2 , \mathbb { R } ) \to \mathbb { R } ^ { * }$ be defined by $A \mapsto d e t ( A )$ . Let $A \in G L ( 2 , \mathbb { R } )$ . This means that A is invertible thus the $d e t ( A )$ is not zero, hence the $d e t ( A )$ is in $\mathbb { R } ^ { * }$ . So φ maps to $\mathbb { R } ^ { * }$ as claimed.
Now let $A , B \in G L ( 2 , \mathbb { R } )$ . Then $\phi ( A B ) = d e t ( A B ) = d e t ( A ) d e t ( B ) = \phi ( A ) \phi ( B )$ , so $\phi$ is a homomorphism.
:::
