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
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the four containers state why their subclaims suffice, and the 15
    leaf steps that asserted a claim with no justification each carry a sentence deriving it. The Goal
    paragraph before the proof was removed, the concluding summary was turned from a pf-qed into an
    ordinary step with its own justification, and the singular value is boxed where it is established.
    The mathematics is unchanged: AA^T = diag(r_1,...,r_m) because one-hot columns give the rows
    disjoint supports, the singular values sqrt(r_i) for r_i > 0, the left vectors e_i, the right
    vectors r_i^{-1/2} times the indicator of S_i, orthonormality from the disjointness of the S_i, and
    the grouping of equal singular values into one space on each side. Checked against the statement on
    the card, from the UCSD Spring 2026 applied algebra qualifying exam. No published solution is cited,
    so the argument is the card's own. Nothing in the statement was changed.
---

::: {.problem}
Let $A$ be an $m \times n$ matrix whose columns are one-hot binary vectors: each column contains exactly one entry equal to $1$ and all other entries are equal to $0$.
Let $r_i$ denote the sum of the entries in row $i$ of $A$ (the number of columns with a 1 in row $i$).
Determine the **nonzero singular values** of $A$, and give explicit **orthonormal bases** for each of the corresponding left and right singular spaces.
:::

::: {.solution}

::: pf

::: pf-step
Computation of $A A^H$ and $A^H A$:

::: pf-proof
The subclaims show that the rows are pairwise orthogonal and compute the product, which is what makes the singular values readable.

::: pf-step
Let the columns of $A$ be $c_1, c_2, \dots, c_n \in \RR^m$, where each $c_j = e_{k(j)}$ for some row index $k(j) \in \{1, \dots, m\}$.

::: pf-proof
A one-hot column has its unique $1$ in some row $k(j)$, so it is the standard basis vector belonging to that row.
:::

:::

::: pf-step
The rows of $A$ are pairwise orthogonal: row $i$ and row $j$ ($i \ne j$) have disjoint supports since each column has a 1 in only one row.

::: pf-proof
A column lying in the support of both rows would need a $1$ in row $i$ and a $1$ in row $j$, which a one-hot column cannot have; so no column lies in both supports.
:::

:::

::: pf-step
Thus the $m \times m$ matrix $A A^T$ is **diagonal**:
$$(A A^T)_{ij} = \sum_{k=1}^n A_{ik} A_{jk} = \begin{cases} r_i & \text{if } i = j, \\ 0 & \text{if } i \ne j. \end{cases}$$

::: pf-proof
The $(i,j)$ entry is the inner product of row $i$ with row $j$: for $i=j$ it counts the columns with a $1$ in row $i$, which is $r_i$, and for $i\neq j$ it vanishes by the orthogonality of the preceding subclaim.
:::

:::

::: pf-step
Therefore:
$$A A^T = \operatorname{diag}(r_1, r_2, \dots, r_m) \in M_m(\RR).$$

::: pf-proof
A matrix whose off-diagonal entries vanish and whose diagonal entries are $r_i$ is by definition the diagonal matrix with those entries.
:::

:::

:::

:::

::: pf-step
Non-Zero Singular Values of $A$:

::: pf-proof
The subclaims read the singular values off the diagonal form of $AA^T$.

::: pf-step
The singular values of $A$ are the square roots of the eigenvalues of $A A^T$.

::: pf-proof
For a real matrix the singular values are the square roots of the eigenvalues of $AA^T$, which is positive semidefinite, so those eigenvalues are non-negative and their square roots are real.
:::

:::

::: pf-step
The eigenvalues of $A A^T = \operatorname{diag}(r_1, \dots, r_m)$ are precisely the row sums $r_1, r_2, \dots, r_m$.

::: pf-proof
Each standard basis vector $e_i$ satisfies $AA^Te_i=r_ie_i$, so the $r_i$ are eigenvalues; an $m\times m$ matrix has exactly $m$ eigenvalues counted with multiplicity, so these are all of them.
:::

:::

::: pf-step
Therefore, the **non-zero singular values** of $A$ are:
$$\sigma_i = \boxed{\sqrt{r_i}} \quad \text{for all rows } i \in \{1, \dots, m\} \text{ with } r_i > 0.$$

::: pf-proof
Taking square roots of the eigenvalues listed in the preceding subclaim and discarding those equal to $0$ leaves $\sqrt{r_i}$ for the rows with $r_i>0$, and no others.
:::

:::

:::

:::

::: pf-step
Left Singular Vectors (Orthonormal Basis):

::: pf-proof
The subclaims show that the standard basis vectors are the left singular vectors and that they are orthonormal.

::: pf-step
The left singular vectors $u_i \in \RR^m$ are eigenvectors of $A A^T = \operatorname{diag}(r_1, \dots, r_m)$.

::: pf-proof
In a singular value decomposition the left vector belonging to $\sigma_i$ satisfies $AA^Tu_i=\sigma_i^2u_i$, so it is an eigenvector of $AA^T$.
:::

:::

::: pf-step
For each row $i$ with $r_i > 0$, the corresponding left singular vector is the standard basis vector:
$$u_i = e_i = (0, \dots, 0, \underbrace{1}_{i\text{-th}}, 0, \dots, 0)^T \in \RR^m.$$

::: pf-proof
Since $AA^T$ is diagonal, $AA^Te_i=r_ie_i$, so $e_i$ is a unit eigenvector with eigenvalue $r_i$; for $r_i>0$ it belongs to the singular value $\sigma_i=\sqrt{r_i}$.
:::

:::

::: pf-step
Since $\{e_i\}_{i: r_i > 0}$ are standard basis vectors, they form an **orthonormal basis** for the left singular space corresponding to $\sigma_i = \sqrt{r_i}$.

::: pf-proof
The standard basis vectors of $\RR^m$ are orthonormal, and the ones indexed by rows with $r_i>0$ are eigenvectors with those eigenvalues, so they span the corresponding left singular space.
:::

:::

:::

:::

::: pf-step
Right Singular Vectors (Orthonormal Basis):

::: pf-proof
The subclaims compute $v_i$ from $u_i$ and check that the resulting vectors are orthonormal.

::: pf-step
For each row $i$ with $r_i > 0$, let $S_i = \{j \in \{1, \dots, n\} \mid A_{ij} = 1\}$ be the set of column indices having their non-zero entry in row $i$, so $\cardinality{S_i} = r_i$.

::: pf-proof
The row sum $r_i$ counts the columns whose unique $1$ lies in row $i$, and those are exactly the members of $S_i$.
:::

:::

::: pf-step
The right singular vector $v_i \in \RR^n$ associated with the singular value $\sigma_i = \sqrt{r_i}$ and left vector $u_i = e_i$ satisfies $A^T u_i = \sigma_i v_i$:
$$A^T e_i = \text{the } i\text{-th row of } A \text{ as a column vector in } \RR^n = \sum_{j \in S_i} \hat{e}_j.$$

::: pf-proof
Multiplying on the left by $e_i^T$ selects the $i$-th row, and that row has entry $1$ exactly in the columns of $S_i$ and $0$ elsewhere.
:::

:::

::: pf-step
Normalizing by $\sigma_i = \sqrt{r_i}$:
$$v_i = \frac{1}{\sqrt{r_i}} A^T e_i = \frac{1}{\sqrt{r_i}} \sum_{j \in S_i} \hat{e}_j = \frac{1}{\sqrt{r_i}} (\underbrace{0, \dots, 0, 1, \dots, 1, 0, \dots}_{\text{1s at indices in } S_i})^T.$$

::: pf-proof
The defining relation $A^Tu_i=\sigma_iv_i$ with $\sigma_i=\sqrt{r_i}>0$ gives the first equality, and the preceding subclaim gives the second.
:::

:::

::: pf-step
**Orthonormality:**

- $\norm{v_i}_2^2 = \frac{1}{r_i} \sum_{j \in S_i} 1 = \frac{r_i}{r_i} = 1$.

- For $i \ne k$, the index sets $S_i \cap S_k = \varnothing$ are disjoint, so $v_i^T v_k = 0$.

::: pf-proof
The squared norm is the number of indices in $S_i$, namely $r_i$, divided by $r_i$. For $i\neq k$ the sets $S_i$ and $S_k$ are disjoint because a column has its $1$ in one row only, so the inner product is a sum of products of a $1$ with a $0$.
:::

:::

::: pf-step
Thus $\{v_i\}_{i: r_i > 0}$ form an orthonormal set of right singular vectors for the non-zero singular values.

::: pf-proof
The preceding subclaim verifies unit length and pairwise orthogonality, and each $v_i$ satisfies $A^Tu_i=\sigma_iv_i$ with $\sigma_i=\sqrt{r_i}$, which is what makes it a right singular vector for that value.
:::

:::

:::

:::

::: pf-step
Conclusion:
The non-zero singular values are $\sigma_i = \sqrt{r_i}$ for $r_i > 0$; the left singular vectors are standard basis vectors $e_i \in \RR^m$, and the right singular vectors are normalized indicator vectors $v_i = \frac{1}{\sqrt{r_i}} \sum_{j \in S_i} \hat{e}_j \in \RR^n$.
Several rows can have the same sum, so for each nonzero singular value $s$ the left singular space is $\operatorname{span}\{e_i : r_i = s^2\}$, with orthonormal basis $\{e_i : r_i = s^2\}$, and the right singular space is $\operatorname{span}\{v_i : r_i = s^2\}$, with orthonormal basis $\{v_i : r_i = s^2\}$.

::: pf-proof
The four containers compute the values, the left vectors and the right vectors, and verify their orthonormality. Grouping the indices $i$ with $r_i=s^2$ collects exactly the vectors belonging to the single singular value $s$, which is the description of the left and right singular spaces; a singular value repeated $k$ times has a $k$-dimensional space on each side.
:::

:::

:::

:::
