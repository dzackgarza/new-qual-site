---
schema: qual/card@1
id: P-J2XEL
kind: problem
title: Diagonalizable matrices are dense over $\CC$ and Zariski-dense over an algebraically
  closed field
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Matrices
  - Geometry
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
(a) Prove that the set of diagonalizable $N \times N$ matrices over $\CC$ is dense in $M_N(\CC)$ in the standard Euclidean/metric topology.

(b) Prove that over any algebraically closed field $K$, the set of diagonalizable matrices is Zariski dense in $M_N(K) \cong \AA^{N^2}$.
:::

::: {.solution}
A matrix whose characteristic polynomial has $N$ distinct roots is diagonalizable.

::: pf

::: pf-step

(a) Diagonalizable matrices are dense in $M_N(\CC)$ for the Euclidean topology.

::: pf-proof

Let $A\in M_N(\CC)$ and $\varepsilon>0$. Write $A=UTU^*$ with $U$ unitary and $T$ upper triangular (Schur triangularization), with diagonal entries $\lambda_1,\ldots,\lambda_N$. Choose $\delta_1,\ldots,\delta_N\in\CC$ with $\abs{\delta_i}<\varepsilon$ such that the numbers $\lambda_i+\delta_i$ are pairwise distinct, and set
$$
A_\varepsilon=U\bigl(T+\diag(\delta_1,\ldots,\delta_N)\bigr)U^*.
$$
The eigenvalues of $A_\varepsilon$ are the distinct numbers $\lambda_i+\delta_i$, so $A_\varepsilon$ is diagonalizable, and in the operator norm
$$
\norm{A_\varepsilon-A}=\norm{\diag(\delta_1,\ldots,\delta_N)}=\max_i\abs{\delta_i}<\varepsilon.
$$

:::

:::

::: pf-step

(b) Diagonalizable matrices are Zariski dense in $M_N(K)$.

::: pf-proof

The discriminant $\Delta(A)$ of the characteristic polynomial $\chi_A$ is a polynomial in the $N^2$ entries of $A$, and $\Delta(A)\ne0$ exactly when $\chi_A$ has distinct roots. It is not identically zero: $K$ is infinite, so there are distinct $a_1,\ldots,a_N\in K$, and $D=\diag(a_1,\ldots,a_N)$ has
$$
\Delta(D)=\prod_{i<j}(a_i-a_j)^2\ne0.
$$
Hence the principal open set $U_\Delta=\{A:\Delta(A)\ne0\}$ is nonempty and consists of diagonalizable matrices. Since $\AA^{N^2}$ is irreducible, every nonempty Zariski-open subset is dense.

:::

:::

:::

:::
