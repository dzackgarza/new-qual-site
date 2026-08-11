---
schema: qual/card@1
id: P-6VF7J
kind: problem
title: "Suppose $f$ is analytic on a region $\\Omega$ such that $\\DD \\subseteq\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
Suppose $f$ is analytic on a region $\Omega$ such that $\DD \subseteq \Omega \subseteq \CC$ and $f(z) = \sum_{n=0}^\infty a_n z^n$ is a power series with radius of convergence exactly 1.

a.
Give an example of such an $f$ that converges at every point of $S^1$.

b.
Give an example of such an $f$ which is analytic at $1$ but $\sum_{n=0}^\infty a_n$ diverges.

c.
Prove that $f$ can not be analytic at *every* point of $S^1$.

:::{.remark}
Missing part (c)
:::
:::{.solution}
\hfill
:::{.concept}
\hfill

:::

a.

- Take $\sum {z^n \over n^2}$
- Then \[\abs{z}\leq 1 \implies \abs{z^n\over n^2} \leq {1\over n^2}\] which is summable
- So the series converges for $\abs{z}\leq 1$.

b.
- Take $\sum {z^n \over n}$; 
- Then $z=1$ yields the harmonic series, which diverges.

- For $z\in S^1\setminus\theset{1}$, we have $z = e^{2\pi it}$ for $0<t<2\pi$. 
- So fix $t$.

- Toward applying the Dirichlet test, set $a_n = 1/n, b_n = z^n$.

- Then for all $N$,
\[
\abs{\sum_{n=1}^N b_n}
= \abs{\sum_{n=1}^N b_n}
= \abs{\sum_{n=1}^N z^n}
= \abs{  {z-z^{N+1} \over \abs{1 - z}} } 
\leq {2 \over 1-z} < \infty
.\]

- Thus $\sum a_n b_n < \infty$ and $\sum z^n/n$ converges.

c. ?

:::
