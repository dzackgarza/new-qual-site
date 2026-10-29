---
schema: qual/card@1
id: D-J5AAX
kind: definition
title: General linear group $\GL_n(F)$
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Linear Algebra
relations: []
review: draft
---

::: {.definition}
Let $F$ be a field and $n\geq 1$.
The \dfn{general linear group} is
$$
\GL_n(F) \coloneqq \theset{ A \in \Mat_{n\times n}(F) \st \det A \neq 0 },
$$
a group under matrix multiplication.
:::

::: {.remark}
A matrix $A\in\Mat_{n\times n}(F)$ lies in $\GL_n(F)$ if and only if there exists $B\in\Mat_{n\times n}(F)$ with $AB=BA=I_n$.
If $AB=I_n$, then $\det A\det B=1$, so $\det A\neq 0$; conversely, if $\det A\neq0$, then $B=(\det A)^{-1}\operatorname{adj}(A)$ satisfies $AB=BA=I_n$.
:::
