---
schema: qual/card@1
id: E-AMD-5X2XEHTC
kind: exercise
title: A nilpotent operator is diagonalizable iff it is zero
classification:
  areas:
  - algebra
  topics:
  - nilpotence
  - diagonalization
  - linear-algebra
relations: []
review: draft
solved: true
---

::: {.exercise}
Show that a nilpotent operator is diagonalizable if and only if it is the zero operator.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $V$ be a finite-dimensional vector space over a field $F$, and let $T: V \to V$ be a linear operator.
Suppose $T$ is nilpotent, i.e., $T^k = 0$ for some positive integer $k \ge 1$.
Prove that $T$ is diagonalizable if and only if $T = 0$.

<1>1. Preliminaries on eigenvalues and diagonalizability: <2>1. If $\lambda \in F$ is an eigenvalue of $T$ with non-zero eigenvector $v \in V$, then for every $m \ge 1$, $T^m(v) = \lambda^m v$.
Proof: By mathematical induction: base case $T(v) = \lambda v$ holds by definition of eigenvector.
If $T^m(v) = \lambda^m v$, then $T^{m+1}(v) = T(T^m(v)) = T(\lambda^m v) = \lambda^m T(v) = \lambda^{m+1} v$.
<2>2. If $T$ is nilpotent with $T^k = 0$, then the only eigenvalue of $T$ is $0$.
Proof: Let $\lambda$ be an eigenvalue of $T$ with non-zero eigenvector $v \neq 0$.
By <1>1.<2>1, $0 = T^k(v) = \lambda^k v$.
Since $v \neq 0$, this requires $\lambda^k = 0$ in the field $F$, hence $\lambda = 0$.
<2>3. $T$ is diagonalizable if and only if there exists an ordered basis $\mathcal{B} = \{v_1, \dots, v_n\}$ of $V$ consisting entirely of eigenvectors of $T$.
Proof: Standard definition/characterization of diagonalizable linear operators on finite-dimensional vector spaces.

<1>2. Direction 1 ($\implies$): If $T$ is nilpotent and diagonalizable, then $T = 0$.
<2>1. Assume $T$ is nilpotent and diagonalizable.
Proof: Hypothesis.
<2>2. There exists a basis $\mathcal{B} = \{v_1, \dots, v_n\}$ of $V$ such that each $v_i$ is an eigenvector of $T$.
Proof: By <1>1.<2>3 and diagonalizability of $T$.
<2>3. For each $i \in \{1, \dots, n\}$, the corresponding eigenvalue $\lambda_i = 0$.
Proof: By <1>1.<2>2, every eigenvalue of a nilpotent operator is $0$.
<2>4. For each $i \in \{1, \dots, n\}$, $T(v_i) = 0 \cdot v_i = 0$.
Proof: Since $\lambda_i = 0$ and $T(v_i) = \lambda_i v_i$.
<2>5. For any arbitrary $v \in V$, $T(v) = 0$.
Proof: Since $\mathcal{B}$ is a basis, write $v = \sum_{i=1}^n c_i v_i$ for scalars $c_i \in F$.
By linearity of $T$, $T(v) = \sum_{i=1}^n c_i T(v_i) = \sum_{i=1}^n c_i (0) = 0$.
<2>6. Therefore, $T = 0$ (the zero operator).
Proof: Since $T(v) = 0$ for all $v \in V$.
<2>7. Q.E.D. Proof: Follows from <2>1 through <2>6.

<1>3. Direction 2 ($\impliedby$): If $T = 0$, then $T$ is nilpotent and diagonalizable.
<2>1. The zero operator $T = 0$ satisfies $T^1 = 0$, so $T$ is nilpotent.
Proof: Definition of nilpotent operator with $k = 1$.
<2>2. The matrix representing $T = 0$ with respect to any basis $\mathcal{B}$ of $V$ is the zero matrix $0_{n \times n}$.
Proof: For every basis vector $v_i$, $T(v_i) = 0 = \sum_{j=1}^n 0 \cdot v_j$.
<2>3. The zero matrix $0_{n \times n}$ is a diagonal matrix.
Proof: All off-diagonal entries are 0. <2>4. Therefore, $T = 0$ is diagonalizable.
Proof: A linear operator whose representation with respect to some basis is a diagonal matrix is diagonalizable.
<2>5. Q.E.D. Proof: Follows from <2>1 through <2>4.

<1>4. Conclusion: A nilpotent operator $T$ is diagonalizable if and only if $T = 0$.
Proof: By <1>2 and <1>3.
:::
