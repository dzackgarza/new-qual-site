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

::: problem
- Show that a nilpotent operator is diagonalizable if and only if it is the zero operator.
:::

::: {.solution}
If $T$ is nilpotent and $Tv=\lambda v$ with $v\ne0$, then for some $k$,
\[
0=T^kv=\lambda^k v,
\]
so $\lambda=0$. Thus a nilpotent operator has only the eigenvalue $0$.

If $T$ is also diagonalizable, it has a basis of eigenvectors, and every basis vector has eigenvalue $0$. Therefore $T$ vanishes on a basis and hence
\[
T=0.
\]
Conversely, the zero operator is nilpotent and its matrix in every basis is diagonal. Hence
\[
\boxed{T\text{ nilpotent and diagonalizable}\iff T=0}.
\]
:::
