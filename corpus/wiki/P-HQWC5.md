---
schema: qual/card@1
id: P-HQWC5
kind: problem
title: "For $k=1,2,\\cdots, n$, suppose $\\abs{a_k} < 1$ and"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
For $k=1,2,\cdots, n$, suppose $\abs{a_k} < 1$ and
\[
f(z) \da \qty{z - a_1 \over 1 - \bar a_1 z} \qty{z-a_2 \over 1 - \bar a_2 z} \cdots \qty{z - a_n \over 1 - \bar a_n z}
.\]
Show that $f(z) = b$ has $n$ solutions in $\abs{z} < 1$.
:::

:::{.solution}
Note that $f$ is holomorphic on $\DD$ and $S^1$, since the poles are at $1/\bar{a_k}$ and if $\abs{a_l} < 1$ then $\abs{\bar{a_k}} > 1$.
Fix $b$, then define $g_w(z) \da f(z) - w$ and form the solution counting function
\[
F(w) \da {1\over 2\pi i}\oint_{S^1} \logd g_w(z) \dz
= {1\over 2\pi i} \oint_{S^1} {f'(z) \over f(z)-w}\dz
.\]
Start by computing $F(0)$.
\[
F(0) 
&= {1\over 2\pi i }\oint_{S^1} \logd \prod_{1\leq k\leq n} \psi_{a_k}(z) \dz \\
&= {1\over 2\pi i }\oint_{S^1} \sum_{1\leq k\leq n} \logd \psi_{a_k}(z) \dz \\
&= {1\over 2\pi i }\oint_{S^1} \sum_{1\leq k\leq n} \qty{1-\abs{a_k}^2 \over (1-\bar{a_k} z)^2} \qty{z-a_k \over 1-\bar{a_k} z}\inv \dz \\
&= {1\over 2\pi i }\oint_{S^1} \sum_{1\leq k\leq n} {1-\abs{a_k}^2 \over (z-a_k)( 1-\bar{a_k}z) } \dz \\
&= {1\over 2\pi i } \sum_{1\leq k\leq n} \oint_{S^1} {1-\abs{a_k}^2 \over (z-a_k)( 1-\bar{a_k}z) } \dz \\
&= {1\over 2\pi i } \sum_{1\leq k\leq n} 2\pi i \\
&= n
,\]
where we've used that the integrand has a simple pole at $a_k$ since $1/\bar{a_k}\in \DD^c$.
So the equation $f(z) = 0$ has $n$ solutions.
Now use that $F$ is a continuous function of $w$ on $\DD$ and integer valued, thus constant.
So $F(w) = n$ for any $w$, meaning $f(z) = w$ has $n$ solutions in $\DD$ for every $w$.

> Alternative: $F$ continuously depends on the $a_k$, so send them all to zero to get $f(z) = z^n$ which trivially has $n$ zeros.

:::

