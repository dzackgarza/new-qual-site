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
solved: true
---

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

:::{.concept}
\envlist

- $\chi_A(t) = t^n - \tr\qty{\Extpower^1 A}t^{n-1} + \tr\qty{\Extpower^2 A}t^{n-2} - \cdots \pm \det(A)$
- Finding generalized eigenvectors: let $B = A-\lambda I$, get eigenvector $v$, solve $Bw_1 = v, Bw_2 = w_1, \cdots$ to get a Jordan block. 
  Repeat with any other usual eigenvectors.
- Convention: construct Jordan blocks in decreasing order of magnitude of eigenvalues.
- Polynomial exponent data:
  - Minimal polynomial exponents: sizes of **largest** Jordan blocks.
  - Characteristic polynomial exponents: **sum of sizes** of Jordan blocks, i.e. how many times $\lambda$ is on the diagonal of $\JCF(A)$.

:::

:::{.solution}
\envlist

:::{.proof title="parts a and b"}
\envlist

- Write $\chi_A(t) = t^3 - T_1 t^2 + T_2 t - T_3$ where $T_i \da \tr\qty{\Extpower^i A}$:
  - $T_1 = \tr(A) = 4-1+1=4$.
  - $T_2 = (-1-2) + (4+2) + (-4-6) = 5$.
  - $T_3 = \det(A) = 4(-1-2) -1(-10) + (-1)(-6+2) = 2$.
- So $\chi_A(t) = t^3 - 4t^2 + 5t-2$.
- Try rational roots test: $r \in \ts{\pm 2/1}$, and check that 2 is root.
- By polynomial long division, $\chi_A(t) / (t-2) = t^2-2t+1 = (t-1)^2$.
- So the eigenvalues are $\lambda = 2, 1$.
- $\lambda = 2$:
  - Set $U\da A-\lambda I$, then find $\RREF(U)$ to compute its kernel:
  \[
  U \da
  \begin{bmatrix}
  2 & 1 & -1
  \\
  -6 & -3 & 2
  \\
  2 & 1 & -1
  \end{bmatrix}
  \leadsto
  \begin{bmatrix}
  2 & 1 & 0
  \\
  0 & 0 & 1
  \\
  0 & 0 & 0
  \end{bmatrix}
  ,\]
  which yields $v_1 = [1,-2,0]$.

- $\lambda = 2$:
  - Similarly,
  \[
  U \da 
  \begin{bmatrix}
  3 & 1 & -1 \\
  -6 & -2 & 2 \\
  2 & 1 & 0
  \end{bmatrix}
  \leadsto  
  \begin{bmatrix}
  1 & 0 & -1
  \\
  0 & 1 & 2
  \\
  0 & 0 & 0
  \end{bmatrix}
  ,\]
  which yields $v_2 = [1,-2,1]$.

  - Solve $Uw = v_3$:
  \[
  \begin{bmatrix}
  3 & 1 & -1 & 1 \\
  -6 & -2 & 2 & -2 \\
  2 & 1 & 0 & 1
  \end{bmatrix}
  \leadsto
  \begin{bmatrix}
  1 & 0 & -1 & 0 \\
  0 & 1 & 2 & 1 \\
  0 & 0 & 0 & 0
  \end{bmatrix}
  ,\]
  so take $v_3 = [0,1,0]$.

- Putting things together:
\[
A &= P\inv J P \text{ where } \\
J = J_1(\lambda = 2) \oplus J_2(\lambda = 1) 
&=
\begin{bmatrix}
2 & 0 & 0
\\
0 & 1 & 1
\\
0 & 0 & 1
\end{bmatrix} \\
P = [v_1, v_2, v_3] 
&= 
\begin{bmatrix}
1 & 1 & 0
\\
-2 & -2 & 1
\\
0 & 1 & 0
\end{bmatrix}
.\]

:::

:::{.proof title="part c"}
\envlist

- Write $\min_A(t) = (t-2)(t-1)^{\ell_1}$, then since $\min_A(t)$ divides $\chi_A(t)$ either $\ell_1 = 1, 2$.
- $\ell_1$ is the size of the **largest** block corresponding to $\lambda = 1$, which is size 2, so $\lambda_1=2$.
- Thus 
\[
\min_A(t) = (t-2)(t-1)^2
.\]

:::

:::


