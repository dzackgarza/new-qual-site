---
schema: qual/card@1
id: P-QVCO4
kind: problem
title: $F[x]\oplus F$ as the cokernel of a $2\times 2$ Smith normal form matrix
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Smith Normal Form
  - Modules
relations: []
review: draft
---

::: {.problem}
Construct a $2\times2$ matrix $A$ over $F[x]$ whose cokernel is
$$
F[x]\oplus F.
$$
:::

::: {.solution}
::: pf

::: pf-step
The matrix
$$
\boxed{A=\begin{pmatrix}x+1&0\\0&0\end{pmatrix}}
$$
has $\operatorname{coker}(A)\cong F[x]\oplus F$.

::: pf-proof
The image of $A:F[x]^2\to F[x]^2$ is $(x+1)F[x]\oplus 0$, so
$$
\operatorname{coker}(A)\cong F[x]/(x+1)\oplus F[x]/(0)\cong F\oplus F[x],
$$
where $F[x]/(x+1)\cong F$ by evaluation at $-1$.
:::

:::

:::
:::
