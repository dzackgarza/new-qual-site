---
schema: qual/card@1
id: P-7IYBS
kind: problem
title: "Note that if $A = 0$ or $I$ then $A$ is patently diagonal, so suppose\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
Note that if $A = 0$ or $I$ then $A$ is patently diagonal, so suppose otherwise. 
Since $A^2 = A$, we have $A^2 - A = 0$ and thus $A$ satisfies the polynomial $p(x) = x^2 - 1 = x(x-1)$.
Moreover, since $A\neq 0, I$, the minimal polynomial is at least degree -- since $p$ is monic, it must in fact be the minimal polynomial.

We can immediately deduce that the size of the largest Jordan block corresponding to $\lambda = 0$ is exactly 1, as is the size of the largest Jordan block corresponding to $\lambda = 1$. 
But this says that *all* Jordan blocks must be size 1, so $JNF(A)$ has no off-diagonal entries and is thus diagonal.

If $k$ is the multiplicity of $\lambda = 0$ as an eigenvalue, we have

\begin{align*}
A \sim 
\left[\begin{array}{ccc|cccc}
0 & 0 & 0     & 0 & 0 & 0 & 0 \\
0 & \ddots & 0     & 0 & 0 & 0 & 0 \\
0 & 0 & 0     & 0 & 0 & 0 & 0 \\ 
\hline
0 & 0 & 0     & 1 & 0 & 0 & 0 \\
0 & 0 & 0     & 0 & 1 & 0 & 0 \\
0 & 0 & 0     & 0 & 0 & \ddots & 0 \\
0 & 0 & 0     & 0 & 0 & 0 & 1
\end{array}\right]
,\end{align*}

which has a $k\times k$ block of zeros and an $(n-k)\times(n-k)$ block of 1s.

