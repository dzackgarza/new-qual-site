---
schema: qual/card@1
id: D-GY7ZN
kind: definition
title: Special orthogonal group $\SO_n(\RR)$
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
relations: []
review: draft
---

::: {.definition}
Let $n\geq 1$.
The \dfn{special orthogonal group} is
$$
\SO_n(\RR) \coloneqq \theset{ A\in\Mat_{n\times n}(\RR) \st AA^t = I \text{ and } \det A = 1} = \Orth_n(\RR) \cap \SL_n(\RR).
$$
:::

::: {.remark}
Every $A\in\Orth_n(\RR)$ satisfies $\det A = \pm 1$, and $\SO_n(\RR)$ is the kernel of $\det\colon\Orth_n(\RR)\to\theset{\pm1}$, of index $2$ in $\Orth_n(\RR)$.
For $n\geq 2$, the matrix $\operatorname{diag}(2, 1/2, 1, \ldots, 1)$ lies in $\SL_n(\RR)$ but not in $\Orth_n(\RR)$.
:::
