---
schema: qual/card@1
id: P-J77EG
kind: problem
title: "Let $M$ be an $n \\times n$ matrix such that $M_{ij} = 1$ for all $i, j$, and consider the\u2026"
classification:
  areas:
  - algebra
  topics:
  - eigenvalues-and-eigenvectors
  - diagonalization
  - matrices
relations: []
review: draft
---

::: problem
Let $M$ be an $n \times n$ matrix such that $M_{ij} = 1$ for all $i, j$, and consider the possible eigenvectors of $M$.

We have 
$$
M [1,1, \cdots, 1]^t = [n, n, \cdots, n]^t = n[1,1,\cdots, 1]^t,
$$

which exhibits $\vector x = [1,1,\cdots, 1]$ as an eigenvector with eigenvalue $\lambda = n$.

Now consider 
$$
\vector x_j \definedas \vector e_1 - \vector e_j = [1, 0,0, \cdots, 0,-1,0,\cdots, 0]
$$ 
which has a $1$ in the $1$st coordinate and a $-1$ in the $j$th coordinate.

Then

\begin{align*}
M \vector x_j = 
\left[\begin{array}{c} 
1 + 0 + \cdots + 0 + (-1) + 0 + \cdots + 0 \\ 
1 + 0 + \cdots + 0 + (-1) + 0 + \cdots + 0 \\ 
\vdots 
\end{array}\right]
= [0,0,\cdots, 0]^t
,\end{align*}


which exhibits each $\vector x_j$ as an eigenvector with eigenvalue $\lambda = 0$.

But the set $\theset{ \vector x_j \mid 2 \leq j \leq n}$ with eigenvalue $0$ contains $n-1$ distinct eigenvectors, and we have an additional 1 eigenvector with eigenvalue $1$, which yields $n$ distinct eigenvectors. 

So $M$ is fact diagonalizable and given by
$$
JCF(M) = (n-1)J_0^{1} \oplus J_n^1 =
\left[\begin{array}{ccccc}
0 & 0 & 0 & \cdots & 0 \\
0 & 0 & 0 & \cdots & 0 \\
0 & 0 & 0 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & n \\
\end{array}\right]
$$
:::
