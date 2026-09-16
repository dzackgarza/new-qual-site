---
schema: qual/card@1
id: D-J5AAX
kind: definition
title: General linear group $\GL_n(\RR)$
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
Let $n\geq 1$.
The \dfn{general linear group} is
$$
\GL_n(\RR) \coloneqq \theset{ A \in \Mat_{n\times n}(\RR) \st \det A \neq 0 },
$$
a group under matrix multiplication.
:::

::: {.remark}
A matrix $A\in\Mat_{n\times n}(\RR)$ lies in $\GL_n(\RR)$ if and only if there exists $B\in\Mat_{n\times n}(\RR)$ with $AB=BA=I_n$.
If $AB=I_n$, then $\det A\det B=1$, so $\det A\neq 0$; conversely, if $\det A\neq0$, then $B=(\det A)^{-1}\operatorname{adj}(A)$ satisfies $AB=BA=I_n$.
:::
