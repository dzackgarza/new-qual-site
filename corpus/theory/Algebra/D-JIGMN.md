---
schema: qual/card@1
id: D-JIGMN
kind: definition
title: Similar matrices
classification:
  areas:
  - algebra
  topics:
  - Matrices
  - Canonical Forms
  - Jordan Canonical Form
relations: []
review: draft
---

::: {.definition}
Let $k$ be a field and $n\geq 1$.
Matrices $A,B\in\Mat_{n\times n}(k)$ are \dfn{similar} if there exists $P\in\GL_n(k)$ such that $A = PBP^{-1}$.
:::

::: {.proposition}
Let $k$ be an algebraically closed field and $A,B\in\Mat_{n\times n}(k)$.
Then $A$ and $B$ are similar if and only if they have the same Jordan canonical form, up to the order of the Jordan blocks.
:::

::: {.proof}
Every matrix over $k$ is similar to a Jordan canonical form, and similarity is an equivalence relation, so matrices with the same Jordan form are similar.
Conversely, for $\lambda\in k$ and $j\geq 1$, the number of Jordan blocks of $A$ with eigenvalue $\lambda$ and size at least $j$ is $\dim\ker(A-\lambda I)^j-\dim\ker(A-\lambda I)^{j-1}$.
If $A=PBP^{-1}$, then $(A-\lambda I)^j=P(B-\lambda I)^jP^{-1}$, so these dimensions agree for $A$ and $B$, and hence so do their Jordan blocks.
:::
