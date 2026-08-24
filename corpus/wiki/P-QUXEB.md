---
schema: qual/card@1
id: P-QUXEB
kind: problem
title: Convergence of $\sum nz^n$, $\sum z^n/n^2$, and $\sum z^n/n$ on $S^1$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Convergence Tests
  - Series of Functions
relations: []
review: draft
---

:::{.problem title="?"}
Prove the following:

a. $\sum_{n} nz^n$ does not converge at any point of $S^1$

b. $\sum_n {z^n \over n^2}$ converges at every point of $S^1$.

c. $\sum_n {z^n \over n}$ converges at every point of $S^1$ except $z=1$.

:::

:::{.concept}
\envlist

- Summation by parts:
  Set $B_0 \da 0, B_n \da \sum_{k\leq n} b_k$, then
\[
\sum_{n=M}^{N} a_{n} b_{n}=a_{N} B_{N}-a_{M} B_{M-1}-\sum_{n=M}^{N-1}\left(a_{n+1}-a_{n}\right) B_{n}
.\]

- Summing a geometric series:
\[
\sum_{1\leq k \leq N} z^k = {1 - z^{N+1}\over 1-z}
.\]

:::

:::{.solution}
**Part 1**:
This series does not have small tails: writing $c_n \da n z^n$ we have $\abs{c_n} = \abs{nz^n} = \abs{n}\to \infty$ when $\abs{z} = 1$.

**Part 2**:
This converges absolutely and absolute convergence implies convergence:
\[
\abs{\sum n^{-2} z^n} \leq \sum \abs{n^{-2}z^n} = \sum n^{-2} < \infty
.\]


**Part 3**:
Write $f(z) = \sum_{k\geq 1} k\inv z^k$.
The value $f(1)$ is the harmonic series, which we know diverges from undergraduate Calculus.
For $z\neq 1$, apply summation by parts with $a_k \da k\inv$ and $b_k \da z^k$, so 

- $a_N = N\inv$
- $a_M = M\inv$
- $B_N = \sum_{k\leq N} z^k = {1-z^{N+1} \over 1-z}$
- $B_M = \sum_{k\leq M} z^k$
- $a_{n+1} - a_n = (n+1)\inv + n\inv = - (n(n+1))\inv$

Note that $\abs{B_N} \leq C_z \da {2\over \abs{1-z} }$ for any $N$, since $\abs{z} = 1$ is on $S^1$ and the maximum distance between two points on $S^1$ is 2.
Moreover $C_z < \infty$ when $z\neq 1$.

Applying the formula:

\[
\abs{\sum_{n=M}^N n\inv z^n }
&\leq
\abs{
N\inv B_N - M\inv B_{M-1} - \sum_{n=M}^{N-1} \left[
-(n(n+1))\inv B_n 
\right] }\\
&\leq N\inv C_z + M\inv C_z + \sum_{M\leq n \leq N-1} C_z \qty{1\over n^2 + n}\\
&\leq C_z\qty{N\inv + M\inv + \sum_{M\leq n \leq N-1} n^{-2}} \\
&\convergesto{M, N\to\infty} 0
,\]

where we've used the triangle inequality and convergence of $\sum n^{-2}$.
By the Cauchy criterion for sums, $f(z)$ converges pointwise for $z\neq 1$.

:::

