---
schema: qual/card@1
id: P-IOSZK
kind: problem
title: Jordan form of $\begin{pmatrix}4&1&-1\\-6&-1&2\\2&1&1\end{pmatrix}$, a conjugating
  matrix, and the minimal polynomial
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Eigenvalues and Eigenvectors
  - Minimal and Characteristic Polynomials
relations: []
review: draft
---

::: {.problem}
Let m
\[
A \da 
\begin{bmatrix}
4 & 1 & -1 \\
-6 & -1 & 2 \\
2 & 1 & 1
\end{bmatrix}
\in \Mat(3\times 3, \CC)
.\]

a. 
Find the Jordan canonical form $J$ of $A$.

b. 
Find an invertible matrix $P$ such that $J = P \inv A P$.

c. 
Write down the minimal polynomial of $A$.

> You should not need to compute $P\inv$
:::

::: {.concept}
\envlist

- $\chi_A(t) = t^n - \tr\qty{\Extpower^1 A}t^{n-1} + \tr\qty{\Extpower^2 A}t^{n-2} - \cdots \pm \det(A)$
- Finding generalized eigenvectors: let $B = A-\lambda I$, get eigenvector $v$, solve $Bw_1 = v, Bw_2 = w_1, \cdots$ to get a Jordan block. 
  Repeat with any other usual eigenvectors.
- Convention: construct Jordan blocks in decreasing order of magnitude of eigenvalues.
- Polynomial exponent data:
  - Minimal polynomial exponents: sizes of **largest** Jordan blocks.
  - Characteristic polynomial exponents: **sum of sizes** of Jordan blocks, i.e. how many times $\lambda$ is on the diagonal of $\JCF(A)$.

:::

::: {.solution}
Let $A$ be the matrix in the problem.

<1>1. Its characteristic polynomial is $\chi_A(t)=(t-2)(t-1)^2$.

::: {.proof}
Expansion of $\det(tI-A)$ gives $t^3-4t^2+5t-2=(t-2)(t-1)^2$.
:::

<1>2. The Jordan canonical form and a conjugating matrix are
\[
\boxed{J=\begin{pmatrix}2&0&0\\0&1&1\\0&0&1\end{pmatrix},
\qquad
P=\begin{pmatrix}1&1&0\\-2&-2&1\\0&1&0\end{pmatrix}}.
\]

::: {.proof}
Set $v_1=(1,-2,0)^T$, $v_2=(1,-2,1)^T$, and $v_3=(0,1,0)^T$. Direct multiplication gives
\[
(A-2I)v_1=0,\qquad (A-I)v_2=0,\qquad (A-I)v_3=v_2.
\]
The displayed matrix $P$ has these three columns and determinant $-1$, so it is invertible. The three equations give $AP=PJ$, hence $P^{-1}AP=J$. The Jordan form is therefore the stated one.
:::

<1>3. The minimal polynomial is
\[
\boxed{m_A(t)=(t-2)(t-1)^2}.
\]

::: {.proof}
The minimal polynomial of a Jordan matrix is the least common multiple of the powers $(t-\lambda)^d$ corresponding to its blocks of sizes $d$. By step <1>2, the largest blocks for eigenvalues $2$ and $1$ have sizes one and two, respectively. Similarity preserves the minimal polynomial.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>2 establishes parts (a) and (b), and step <1>3 establishes part (c).
:::

:::

