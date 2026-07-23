---
schema: qual/card@1
id: E-7PAHX
kind: exercise
title: "Let $P, Q$ be polynomials with no common zeros. Assume $a$ is a root o\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
Let $P, Q$ be polynomials with no common zeros. Assume $a$ is a root of
$Q$.
Find the principal part of $P/Q$ at $z=a$ in terms of $P$ and $Q$ if $a$ is 

(1) a simple root, and 
(2) a double root.

:::

:::{.solution}
Write 
\[
P(z) &= \prod_{k\leq n} (z-a_k) \\
Q(z) &= \prod_{k\leq m}(z-b_k) \\
Q_j(z) &= \prod_{k\neq j}(z-b_k) = {Q(z) \over z-z_j}
.\]

For $b_\ell$ a simple pole,
\[
{P(z) \over Q(z) } = {1\over z-b_\ell} {P(z) \over Q_\ell(z)} 
&= {1\over z-b_\ell}\qty{c_0 + c_1(z-b_\ell) + c_2(z-b_\ell)^2 + \cdots} \\
&= {c_0 \over z-b_\ell} + c_1 + \bigo(z-b_\ell) \\
& \da {P_{b_\ell}(z)} + c_1 + \bigo(z-b_\ell) 
,\]
so the principal part at $z=z_\ell$ is given by
\[
P_{z_\ell}(z) = {c_0 \over z-b_\ell} = {P(z) \over Q_\ell(z)}\evalfrom_{z=b_\ell} = \lim_{z\to z_\ell} {(z-b_\ell) P(z) \over Q(z)}
.\]

For $b_\ell$ a double pole,
\[
{P(z) \over Q(z) } 
&= {1\over (z-b_\ell)^2 } {(z-z_\ell)^2P(z) \over Q(z) } \\
&= {1\over (z-b_\ell)^2}\qty{ d_0 + d_1(z-b_\ell) + d_2(z-b_\ell)^2 } \\
&= {d_0 \over (z-b_\ell)^2} + {d_1\over z-z_\ell} + d_2 + \bigo(z-b_\ell) \\
&\da P_{b_\ell}(z) + d_2 + \bigo(z-b_\ell)
.\]
To extract the $d_1$ coefficient, note that
\[
{(z-b_\ell)^2 P(z) \over Q(z)}
&= d_0 + d_1(z-b_\ell) + \cdots \\
\implies 
\dd{}{z} {(z-b_\ell)^2 P(z) \over Q(z)}
&= d_1 + 2d_2(z-b_\ell) + \cdots
,\]
so
\[
d_0 &= \lim_{z\to b_\ell} { (z-b_\ell)^2 P(z) \over Q(z) } \\
d_1 &= \lim_{z\to b_\ell} \dd{}{z} {(z-b_\ell)^2 P(z) \over Q(z) } \\
P_{b_\ell} 
&= {d_0 \over (z-b_\ell)^2} + {d_1\over z-b_\ell}
.\]
:::

