---
schema: qual/card@1
id: P-APAF17B
kind: problem
title: Frobenius-norm bound by eigenvalues forces normality
classification:
  areas:
  - applied-algebra
  topics:
  - Norms
  - Normal Operators
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $A\in\mathbb{C}^{n\times n}$ be a matrix with eigenvalues $\lambda_1,\dots,\lambda_n\in\mathbb{C}$.
If
\[
\|A\|_F^2\leq|\lambda_1|^2+\cdots+|\lambda_n|^2,
\]
show that $A$ is normal, i.e., $AA^*=A^*A$.
:::

::: {.solution}
<1>1. Schur Decomposition and unitary invariance of Frobenius norm:
<2>1. By Schur’s Triangularization Theorem, there exists a unitary matrix $U \in U(n)$ and an upper triangular matrix $T \in \mathbb{C}^{n \times n}$ such that:
\[
A = U T U^*,
\]
where the diagonal entries of $T$ are the eigenvalues of $A$: $t_{ii} = \lambda_i$ for $i = 1, \dots, n$.
Proof: Schur's Theorem.
<2>2. The Frobenius norm is unitarily invariant:
\[
\|A\|_F^2 = \operatorname{tr}(A^* A) = \operatorname{tr}\big((U T U^*)^*(U T U^*)\big) = \operatorname{tr}(U T^* T U^*) = \operatorname{tr}(T^* T) = \|T\|_F^2.
\]
Proof: cyclic property of trace and $U^* U = I$.

<1>2. Expansion of $\|T\|_F^2$ and vanishing of strictly upper triangular entries:
<2>1. Decompose the sum of squares of entries of the upper triangular matrix $T = (t_{ij})$:
\[
\|T\|_F^2 = \sum_{i=1}^n |t_{ii}|^2 + \sum_{1 \le i < j \le n} |t_{ij}|^2 = \sum_{i=1}^n |\lambda_i|^2 + \sum_{1 \le i < j \le n} |t_{ij}|^2.
\]
Proof: $t_{ij} = 0$ for $i > j$ and $t_{ii} = \lambda_i$.
<2>2. By the given hypothesis $\|A\|_F^2 \le \sum_{i=1}^n |\lambda_i|^2$:
\[
\sum_{i=1}^n |\lambda_i|^2 + \sum_{1 \le i < j \le n} |t_{ij}|^2 \le \sum_{i=1}^n |\lambda_i|^2.
\]
Proof: substituting <2>1 into hypothesis.
<2>3. Subtracting $\sum_{i=1}^n |\lambda_i|^2$ from both sides yields:
\[
\sum_{1 \le i < j \le n} |t_{ij}|^2 \le 0.
\]
Since $|t_{ij}|^2 \ge 0$ for all pairs $(i, j)$, we must have $t_{ij} = 0$ for all $1 \le i < j \le n$.
Proof: non-negativity of real squares.

<1>3. Prove that $A$ is normal:
<2>1. Since all off-diagonal entries of $T$ vanish ($t_{ij} = 0$ for $i \neq j$), $T = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ is a diagonal matrix.
Proof: <1>2.
<2>2. Any complex diagonal matrix commutes with its conjugate transpose:
\[
T T^* = \operatorname{diag}(|\lambda_1|^2, \dots, |\lambda_n|^2) = T^* T.
\]
Proof: diagonal matrix multiplication.
<2>3. Conjugating by the unitary matrix $U$:
\[
A A^* = (U T U^*)(U T^* U^*) = U (T T^*) U^* = U (T^* T) U^* = (U T^* U^*)(U T U^*) = A^* A.
\]
Thus $A$ is normal.
Proof: unitary conjugation preserves matrix products and commutativity.

<1>4. Conclusion:
$A$ is a normal matrix ($A A^* = A^* A$). Q.E.D.
Proof: <1>1 through <1>3.
:::
