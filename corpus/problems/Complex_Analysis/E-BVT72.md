---
schema: qual/card@1
id: E-BVT72
kind: problem
title: A nonzero analytic function on the disk with infinitely many zeros
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Identity Theorem
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
(1) Explicitly write down an example of a non-zero analytic function in $|z|<1$ which has infinitely zeros in $|z|<1$.

(2) Why does not the phenomenon in (1) contradict the uniqueness theorem?
:::

::: {.solution}
Take
\[
f(z)=\sin\!\left(\frac{1}{1-z}\right).
\]
The function $z\mapsto(1-z)^{-1}$ is holomorphic on the unit disk, since its
only pole is at the boundary point $z=1$. Hence $f$ is holomorphic on
$|z|<1$, and it is not identically zero.

For every sufficiently large positive integer $n$,
\[
z_n=1-\frac{1}{n\pi}
\]
lies in the unit disk and satisfies
\[
f(z_n)=\sin(n\pi)=0.
\]
Thus $f$ has infinitely many zeros in $\mathbb D$.

This does not contradict the identity theorem. The zeros $z_n$ converge to
$1$, but $1\notin\mathbb D$. Hence the zero set has no accumulation point in
the domain of holomorphy. The identity theorem forces a holomorphic function
to vanish identically only when its zeros have an accumulation point inside
the domain.
:::
