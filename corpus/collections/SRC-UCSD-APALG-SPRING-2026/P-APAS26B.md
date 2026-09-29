---
schema: qual/card@1
id: P-APAS26B
kind: problem
title: Nonzero singular values of a one-hot column matrix
classification:
  areas:
  - applied-algebra
  topics:
  - Singular Values
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.problem}
Let $A$ be an $m \times n$ matrix whose columns are one-hot binary vectors: each column contains exactly one entry equal to $1$ and all other entries are equal to $0$.
Let $r_i$ denote the sum of the entries in row $i$ of $A$ (the number of columns with a 1 in row $i$).
Determine the **nonzero singular values** of $A$, and give explicit **orthonormal bases** for each of the corresponding left and right singular spaces.
:::

::: {.solution}
**Goal:** Compute the singular value decomposition of a one-hot column matrix $A$, finding $\sigma_i = \sqrt{r_i}$ and explicit left and right singular vectors.

::: pf

::: pf-step
Computation of $A A^H$ and $A^H A$:

::: pf-proof

::: pf-step
Let the columns of $A$ be $c_1, c_2, \dots, c_n \in \mathbb{R}^m$, where each $c_j = e_{k(j)}$ for some row index $k(j) \in \{1, \dots, m\}$.
:::

::: pf-step
The rows of $A$ are pairwise orthogonal: row $i$ and row $j$ ($i \ne j$) have disjoint supports since each column has a 1 in only one row.
:::

::: pf-step
Thus the $m \times m$ matrix $A A^T$ is **diagonal**:
$$(A A^T)_{ij} = \sum_{k=1}^n A_{ik} A_{jk} = \begin{cases} r_i & \text{if } i = j, \\ 0 & \text{if } i \ne j. \end{cases}$$
:::

::: pf-step
Therefore:
$$A A^T = \operatorname{diag}(r_1, r_2, \dots, r_m) \in M_m(\mathbb{R}).$$
:::

:::

:::

::: pf-step
Non-Zero Singular Values of $A$:

::: pf-proof

::: pf-step
The singular values of $A$ are the square roots of the eigenvalues of $A A^T$.
:::

::: pf-step
The eigenvalues of $A A^T = \operatorname{diag}(r_1, \dots, r_m)$ are precisely the row sums $r_1, r_2, \dots, r_m$.
:::

::: pf-step
Therefore, the **non-zero singular values** of $A$ are:
$$\sigma_i = \sqrt{r_i} \quad \text{for all rows } i \in \{1, \dots, m\} \text{ with } r_i > 0.$$
:::

:::

:::

::: pf-step
Left Singular Vectors (Orthonormal Basis):

::: pf-proof

::: pf-step
The left singular vectors $u_i \in \mathbb{R}^m$ are eigenvectors of $A A^T = \operatorname{diag}(r_1, \dots, r_m)$.
:::

::: pf-step
For each row $i$ with $r_i > 0$, the corresponding left singular vector is the standard basis vector:
$$u_i = e_i = (0, \dots, 0, \underbrace{1}_{i\text{-th}}, 0, \dots, 0)^T \in \mathbb{R}^m.$$
:::

::: pf-step
Since $\{e_i\}_{i: r_i > 0}$ are standard basis vectors, they form an **orthonormal basis** for the left singular space corresponding to $\sigma_i = \sqrt{r_i}$.
:::

:::

:::

::: pf-step
Right Singular Vectors (Orthonormal Basis):

::: pf-proof

::: pf-step
For each row $i$ with $r_i > 0$, let $S_i = \{j \in \{1, \dots, n\} \mid A_{ij} = 1\}$ be the set of column indices having their non-zero entry in row $i$, so $|S_i| = r_i$.
:::

::: pf-step
The right singular vector $v_i \in \mathbb{R}^n$ associated with the singular value $\sigma_i = \sqrt{r_i}$ and left vector $u_i = e_i$ satisfies $A^T u_i = \sigma_i v_i$:
$$A^T e_i = \text{the } i\text{-th row of } A \text{ as a column vector in } \mathbb{R}^n = \sum_{j \in S_i} \hat{e}_j.$$
:::

::: pf-step
Normalizing by $\sigma_i = \sqrt{r_i}$:
$$v_i = \frac{1}{\sqrt{r_i}} A^T e_i = \frac{1}{\sqrt{r_i}} \sum_{j \in S_i} \hat{e}_j = \frac{1}{\sqrt{r_i}} (\underbrace{0, \dots, 0, 1, \dots, 1, 0, \dots}_{\text{1s at indices in } S_i})^T.$$
:::

::: pf-step
**Orthonormality:**

- $\|v_i\|_2^2 = \frac{1}{r_i} \sum_{j \in S_i} 1 = \frac{r_i}{r_i} = 1$.

- For $i \ne k$, the index sets $S_i \cap S_k = \varnothing$ are disjoint, so $v_i^T v_k = 0$.
:::

::: pf-step
Thus $\{v_i\}_{i: r_i > 0}$ form an orthonormal set of right singular vectors for the non-zero singular values.
:::

:::

:::

::: pf-qed
Conclusion:
The non-zero singular values are $\sigma_i = \sqrt{r_i}$ for $r_i > 0$; the left singular vectors are standard basis vectors $e_i \in \mathbb{R}^m$, and the right singular vectors are normalized indicator vectors $v_i = \frac{1}{\sqrt{r_i}} \sum_{j \in S_i} \hat{e}_j \in \mathbb{R}^n$.
:::

:::
:::
