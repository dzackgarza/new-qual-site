---
schema: qual/card@1
id: P-VAK32
kind: problem
title: A nilpotent operator is diagonalizable iff it is zero
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Diagonalization
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Show that a nilpotent operator is diagonalizable if and only if it is the zero operator.
:::

::: {.solution}
Let $T$ be a nilpotent operator on a vector space $V$, with $T^k=0$.

::: pf

::: {.pf-step #eig}

Every eigenvalue of $T$ is $0$.

::: pf-proof

If $Tv=\lambda v$ with $v\ne0$, then $0=T^kv=\lambda^k v$, so $\lambda^k=0$ and $\lambda=0$.

:::

:::

::: {.pf-step #forward}

If $T$ is diagonalizable, then $T=0$.

::: pf-proof

$V$ has a basis of eigenvectors of $T$, and by step [](#eig){.pf-ref} $T$ sends each of them to $0$. So $T$ vanishes on a basis.

:::

:::

::: pf-qed

Conversely, the zero operator is nilpotent and its matrix in every basis is diagonal. With step [](#forward){.pf-ref},
$$
\boxed{T\text{ nilpotent and diagonalizable}\iff T=0}.
$$

:::

:::

:::
