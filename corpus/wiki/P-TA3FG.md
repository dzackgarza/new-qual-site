---
schema: qual/card@1
id: P-TA3FG
kind: problem
title: "Suppose $f$ is analytic on a region $\\Omega$ such that $\\DD \\subseteq \\Omega \\subseteq \\CC$ and $f(z) = \\sum_{n=0}^\\infty a_n z^n$ is a power\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
Suppose $f$ is analytic on a region $\Omega$ such that $\DD \subseteq \Omega \subseteq \CC$ and $f(z) = \sum_{n=0}^\infty a_n z^n$ is a power series with radius of convergence exactly 1.

a. 
Give an example of such an $f$ that converges at every point of $S^1$.

b.  
Give an example of such an $f$ which is analytic at $1$ but $\sum_{n=0}^\infty a_n$ diverges.

c.  
Prove that $f$ can not be analytic at *every* point of $S^1$.

:::

:::{.solution}
\envlist

**Part a**:
Take $f(z) \da \displaystyle\sum n^{-2}z^n$, which converges absolutely for $\abs{z}=1$ by the comparison test.

**Part b**:
Take $f(z) \da {1\over 1+z} = \sum_{k\geq 0} (-1)^k z^k$, then $f(1) = 2$ by analytic continuation of the series at $z=1$.
Then $a_k = (-1)^k$,

**Part c**:
??? Not clear if this is true, take $f(z) = \sum z^n/n^2$.

:::

