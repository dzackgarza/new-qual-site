---
schema: qual/card@1
id: P-BKS94-6
kind: problem
title: A complex square matrix is similar to its transpose
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 1994 preliminary examination.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the transpose A^t from OCR residue At against Spring94.pdf page 1 problem 6.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Reduced to Jordan normal form and conjugated each Jordan block to its
    transpose by the basis-reversal permutation matrix.
---

::: {.problem}
Prove or disprove: A square complex matrix, $A$, is similar to its transpose, $A^t$.
:::

::: {.solution}
The assertion is true.

<1>1. Every complex square matrix $A$ is similar to a Jordan matrix
$$
J=\bigoplus_\alpha J_{m_\alpha}(\lambda_\alpha).
$$

::: {.proof}
This is the Jordan normal form theorem over $\CC$.
:::

<1>2. For every Jordan block $J_m(\lambda)$,
$$
J_m(\lambda)\sim J_m(\lambda)^t.
$$

::: {.proof}
Let $R_m$ be the permutation matrix that reverses the standard basis:
$$
R_me_j=e_{m+1-j}.
$$
Then
$$
R_m^{-1}=R_m.
$$
Conjugation by $R_m$ reverses both the row and column order. The
superdiagonal $1$'s of $J_m(\lambda)$ become subdiagonal $1$'s, while the
diagonal entries $\lambda$ remain on the diagonal. Therefore
$$
R_mJ_m(\lambda)R_m^{-1}
=
J_m(\lambda)^t.
$$
:::

<1>3. The Jordan matrix $J$ is similar to $J^t$.

::: {.proof}
Let
$$
R\coloneqq\bigoplus_\alpha R_{m_\alpha}.
$$
Applying step <1>2 block by block gives
$$
RJR^{-1}
=
\bigoplus_\alpha J_{m_\alpha}(\lambda_\alpha)^t
=
J^t.
$$
:::

<1>4. The matrices $A$ and $A^t$ are similar.

::: {.proof}
By step <1>1, write
$$
A=PJP^{-1}.
$$
Transposing gives
$$
A^t
=(P^{-1})^tJ^tP^t,
$$
so $A^t$ is similar to $J^t$. Step <1>3 gives $J^t\sim J$, while step
<1>1 gives $J\sim A$. By transitivity of similarity,
$$
A^t\sim A.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 proves the assertion.
:::
:::
