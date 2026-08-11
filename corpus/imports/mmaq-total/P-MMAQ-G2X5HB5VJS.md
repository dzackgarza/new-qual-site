---
schema: qual/card@1
id: P-MMAQ-G2X5HB5VJS
kind: problem
title: Let $A$ be a commutative ring and $M$ a finitely generated $A$-module.
classification:
  areas:
  - algebra
  topics:
  - commutative-algebra
  - modules
  - ideals
  - localization
relations: []
review: draft
---

::: problem
Let $A$ be a commutative ring and $M$ a finitely generated $A$-module.
Define
`\begin{align*}
  \Ann(M) = \{a \in A: am = 0 \text{ for all } m \in M\}
.\end{align*}`{=tex}
Show that for a prime ideal $\mathfrak p \subset A$, the following are equivalent:

-   $\Ann(M) \not\subset \mathfrak p$

-   The localization of $M$ at the prime ideal $\mathfrak p$ is $0$.

-   $M \otimes_A k(\mathfrak p) = 0$, where $k(\mathfrak p) = A_{\mathfrak p}/\mathfrak p A_{\mathfrak p}$ is the residue field of $A$ at $\mathfrak p$.
:::
