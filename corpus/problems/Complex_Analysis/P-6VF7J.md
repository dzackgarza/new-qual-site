---
schema: qual/card@1
id: P-6VF7J
kind: problem
title: 'Power series of radius $1$: convergence on the circle versus analyticity on
  the circle'
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

Suppose $f$ is analytic on a region $\Omega$ such that $\DD \subseteq \Omega \subseteq \CC$ and $f(z) = \sum_{n=0}^\infty a_n z^n$ is a power series with radius of convergence exactly 1.

a. Give an example of such an $f$ that converges at every point of $S^1$.

b. Give an example of such an $f$ which is analytic at $1$ but $\sum_{n=0}^\infty a_n$ diverges.

c. Prove that $f$ can not be analytic at *every* point of $S^1$.

::: {.solution}
For (a), take
\[
f(z)=\sum_{n=1}^\infty {z^n\over n^2}.
\]
Its radius of convergence is $1$, since
\[
\limsup_{n\to\infty}\left({1\over n^2}\right)^{1/n}=1.
\]
For every $|z|=1$ the series converges absolutely by comparison with $\sum n^{-2}$.

For (b), take
\[
f(z)={1\over1+z}=\sum_{n=0}^\infty(-1)^nz^n.
\]
The Taylor series at $0$ has radius exactly $1$, because the nearest singularity is at $z=-1$.
But $f$ is holomorphic in a neighborhood of $z=1$, while
\[
\sum_{n=0}^\infty a_n
=\sum_{n=0}^\infty(-1)^n
\]
diverges.

For (c), suppose instead that $f$ were analytic at every point of $S^1$ as well as on $\DD$.
Then the closed unit disk $\overline\DD$ would be a compact subset of the open domain of analyticity.
Hence there is $\varepsilon>0$ such that
\[
\{z:|z|<1+\varepsilon\}
\]
is still contained in that domain.
The Taylor series of $f$ at $0$ would therefore have radius of convergence at least $1+\varepsilon$, contradicting the hypothesis that its radius is exactly $1$.
:::
