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
Let
$$
A \coloneqq
\begin{bmatrix}
4 & 1 & -1 \\
-6 & -1 & 2 \\
2 & 1 & 1
\end{bmatrix}
\in \Mat(3\times 3, \CC)
.$$

a. 
Find the Jordan canonical form $J$ of $A$.

b. 
Find an invertible matrix $P$ such that $J = \inverseof{P} A P$.

c. 
Write down the minimal polynomial of $A$.

> You should not need to compute $\inverseof{P}$
:::

::: {.concept}
\envlist

- $\chi_A(t) = t^n - \tr\qty{\Wedgepower^1 A}t^{n-1} + \tr\qty{\Wedgepower^2 A}t^{n-2} - \cdots \pm \det(A)$

- Finding generalized eigenvectors: let $B = A-\lambda I$, get eigenvector $v$, solve $Bw_1 = v, Bw_2 = w_1, \cdots$ to get a Jordan block.
  Repeat with any other usual eigenvectors.

- Convention: construct Jordan blocks in decreasing order of magnitude of eigenvalues.

- Polynomial exponent data:

  - Minimal polynomial exponents: sizes of **largest** Jordan blocks.

  - Characteristic polynomial exponents: **sum of sizes** of Jordan blocks, i.e. how many times $\lambda$ is on the diagonal of $\JCF(A)$.

:::


::: {.solution}

::: pf

::: {.pf-step #char}

$\chi_A(t)=(t-2)(t-1)^2$.

::: pf-proof

$\operatorname{tr}A=4$, the sum of the principal $2\times2$ minors is $2+6-3=5$, and $\det A=4(-3)-1(-10)+(-1)(-4)=2$. Hence $\chi_A(t)=t^3-4t^2+5t-2$. Since $\chi_A(2)=0$, division gives $\chi_A(t)=(t-2)(t^2-2t+1)$.

:::

:::

::: {.pf-step #eig}

$v_1=(1,-2,0)^T$ spans $\ker(A-2I)$, and $v_2=(1,-2,1)^T$ spans $\ker(A-I)$.

::: pf-proof

Direct multiplication gives $(A-2I)v_1=0$ and $(A-I)v_2=0$. The matrix
$$
A-I=\begin{bmatrix}3&1&-1\\-6&-2&2\\2&1&0\end{bmatrix}
$$
has rank $2$, because its first and third rows are independent and the second row is $-2$ times the first. So $\ker(A-I)$ has dimension $1$. The eigenvalue $2$ has algebraic multiplicity $1$, so $\ker(A-2I)$ also has dimension $1$.

:::

:::

::: {.pf-step #jcf}

$$
\boxed{J=\begin{bmatrix}2&0&0\\0&1&1\\0&0&1\end{bmatrix}}
$$

::: pf-proof

By Step [](#char){.pf-ref}, the eigenvalue $1$ has algebraic multiplicity $2$. By Step [](#eig){.pf-ref}, it has geometric multiplicity $1$, so it has a single Jordan block of size $2$. The eigenvalue $2$ has one block of size $1$.

:::

:::

::: {.pf-step #conj}

With $v_3=(0,1,0)^T$,
$$
\boxed{P=[v_1\mid v_2\mid v_3]=\begin{bmatrix}1&1&0\\-2&-2&1\\0&1&0\end{bmatrix}}
$$
satisfies $P^{-1}AP=J$.

::: pf-proof

$(A-I)v_3=(1,-2,1)^T=v_2$, so $Av_3=v_2+v_3$. Also $Av_1=2v_1$ and $Av_2=v_2$, so $AP=PJ$. Expansion along the third row gives $\det P=-(1\cdot1-0\cdot(-2))=-1\neq0$, so $P$ is invertible.

:::

:::

::: {.pf-step #min}

$$
\boxed{m_A(t)=(t-2)(t-1)^2}
$$

::: pf-proof

The exponent of each factor of the minimal polynomial is the size of the largest Jordan block for that eigenvalue. By Step [](#jcf){.pf-ref}, these sizes are $1$ for the eigenvalue $2$ and $2$ for the eigenvalue $1$.

:::

:::

::: pf-qed

Steps [](#jcf){.pf-ref}, [](#conj){.pf-ref} and [](#min){.pf-ref} prove parts (a), (b) and (c).

:::

:::

:::
