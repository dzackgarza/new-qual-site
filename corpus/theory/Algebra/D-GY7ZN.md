---
schema: qual/card@1
id: D-GY7ZN
kind: definition
title: Special orthogonal group $\SO_n(F)$
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
relations: []
review: draft
---

::: {.definition}
Let $F$ be a field and $n\geq 1$.
The \dfn{special orthogonal group} is
$$
\SO_n(F) \coloneqq \theset{ A\in\Mat_{n\times n}(F) \st AA^t = I \text{ and } \det A = 1} = \Orth_n(F) \cap \SL_n(F).
$$
:::

::: {.remark}
Every $A\in\Orth_n(\RR)$ satisfies $\det A = \pm 1$, and $\SO_n(\RR)$ is the kernel of $\det\colon\Orth_n(\RR)\to\theset{\pm1}$, of index $2$ in $\Orth_n(\RR)$.
For $n\geq 2$, $\SO_n(\RR)$ is a proper subgroup of $\SL_n(\RR)$: the matrix $\operatorname{diag}(2, 1/2, 1, \ldots, 1)$ lies in $\SL_n(\RR)$ but not in $\Orth_n(\RR)$.
:::
