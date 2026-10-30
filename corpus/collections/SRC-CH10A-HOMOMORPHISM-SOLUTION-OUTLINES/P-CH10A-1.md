---
schema: qual/card@1
id: P-CH10A-1
kind: problem
title: The determinant is a homomorphism $GL(2,\RR)\to\RR^*$
classification:
  areas:
    - algebra
  topics:
    - Group Homomorphisms
relations: []
review: draft
audit:
  - event: source-checked
    by: claude-opus-5
    date: 2026-09-16
    note: Stated the Example 2 map (determinant on GL(2,R)) in the statement, taken from the source's own solution on page 1 of Ch10PtASltns.pdf.
---

::: {.problem}
Prove that the mapping given in Example 2, the map $\phi : GL(2, \RR) \to \RR^*$ defined by $A \mapsto \det(A)$, is a homomorphism.
:::

::: {.solution}
Let $\phi : G L ( 2 , \RR ) \to \RR ^ { * }$ be defined by $A \mapsto d e t ( A )$ . Let $A \in G L ( 2 , \RR )$ . This means that A is invertible thus the $d e t ( A )$ is not zero, hence the $d e t ( A )$ is in $\RR ^ { * }$ . So φ maps to $\RR ^ { * }$ as claimed.
Now let $A , B \in G L ( 2 , \RR )$ . Then $\phi ( A B ) = d e t ( A B ) = d e t ( A ) d e t ( B ) = \phi ( A ) \phi ( B )$ , so $\phi$ is a homomorphism.
:::
