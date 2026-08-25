---
schema: qual/card@1
id: E-LQTR7
kind: exercise
title: Schwarz reflection principle on a half-disk
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Reflection
  - Holomorphic Functions
relations: []
review: draft
---

:::{.problem}
Let $S\definedas \theset{z\in \DD\suchthat \Im(z) \geq 0}$.
Suppose $f:S\to \CC$ is continuous on $S$, real on $S\intersect \RR$, and holomorphic on $S^\circ$.

Prove that $f$ is the restriction of a holomorphic function on $\DD$.

:::

:::{.solution}
Define a function
\[
F(z) \da 
\begin{cases}
f(z) & \Im(z)\geq 0 
\\
\bar{f(\bar z)} & \Im(z) < 0
\end{cases}
.\]
Then $F$ is holomorphic on $\tilde S\da \ts{z\in \DD\st \Im(z) < 0}$ -- write $w_0\in \tilde S$ as $w_0 = \bar{z_0}$ for some $z_0\in S$, then
\[
f(z) 
&= \sum_{k\geq 0}c_k (z-z_0)^k \\
\implies \bar{f(\bar z)} 
&= \sum_{k\geq 0}\bar{c_k} \bar{\qty{\bar z - z_0}^k} \\
&= \sum_{k\geq 0}\bar{c_k} \qty{z - \bar{z_0}}^k \\
&= \sum_{k\geq 0}\bar{c_k} \qty{z - w_0}^k
,\]
which yields a power series expansion of $F$ about $w_0$.
So $f$ is analytic at every point in $\tilde S$ and thus holomorphic.
Since $\bar{f(\bar z)} = f(z)$ for $z, f(z)\in \RR$, $F$ is a continuous extension of $f$ to $\DD$.
By the symmetry principle, $F$ is holomorphic, and $\ro{F}{S} = f$.
:::
