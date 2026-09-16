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
(1) Prove that the set of diagonalizable $N \times N$ matrices over $\mathbb{C}$ is **dense** in $M_N(\mathbb{C})$ in the standard Euclidean/metric topology.
(2) Prove that over any algebraically closed field $K$, the set of diagonalizable matrices is **Zariski dense** in $M_N(K) \cong \mathbb{A}^{N^2}$.
:::

::: {.solution}
Let $A\in M_N(K)$. If the characteristic polynomial $\chi_A(t)$ has $N$ distinct roots, then $A$ is diagonalizable. The discriminant
\[
\Delta(A)=\operatorname{Disc}(\chi_A)
\]
is a polynomial in the $N^2$ entries of $A$, and
\[
\Delta(A)\ne0
\]
exactly when $\chi_A$ has distinct roots.

This polynomial is not identically zero. Indeed, over any algebraically closed field $K$ one can choose $N$ distinct scalars $a_1,\dots,a_N\in K$; then for
\[
D=\operatorname{diag}(a_1,\dots,a_N)
\]
we have
\[
\Delta(D)=\prod_{i<j}(a_i-a_j)^2\ne0.
\]
Thus the principal open set
\[
U_\Delta=\{A:\Delta(A)\ne0\}
\]
is nonempty and consists of diagonalizable matrices. Since affine space $M_N(K)\cong\mathbb A^{N^2}$ is irreducible, every nonempty Zariski-open subset is dense. Hence diagonalizable matrices are Zariski dense in $M_N(K)$.

For the ordinary topology over $\mathbb C$, let $A=UTU^*$ be a Schur triangularization, with diagonal entries $\lambda_1,\dots,\lambda_N$. Given $\varepsilon>0$, choose $\delta_1,\dots,\delta_N$ with
\[
|\delta_i|<\varepsilon
\]
such that the numbers $\lambda_i+\delta_i$ are pairwise distinct, and set
\[
T_\varepsilon=T+\operatorname{diag}(\delta_1,\dots,\delta_N),
\qquad
A_\varepsilon=UT_\varepsilon U^*.
\]
Then $A_\varepsilon$ has distinct eigenvalues and is therefore diagonalizable, while
\[
\|A_\varepsilon-A\|=\max_i|\delta_i|<\varepsilon
\]
for the operator norm. Thus diagonalizable complex matrices are Euclidean-dense as well.
:::
