---
schema: qual/card@1
id: E-DUMQG
kind: exercise
title: Laurent expansions on annuli
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Poles
  - Principal Parts
  - Residues
relations: []
review: draft
---

:::{.exercise}
Find a Laurent expansion for $f(z) \da {1\over (z-3)(z-1)}$ on the 3 annular regions centered at $0$ where $f$ is holomorphic.

![](../../assets/Complex_Analysis/010_Basics/figures/2021-12-19_22-39-19.png)

:::

:::{.solution}
The three regions are 

- $0 \leq \abs{z} < 1$
- $1 < \abs{z} < 3$
- $3 < \abs{z} < \infty$

Write $f$ in terms of its principal parts at $z=1$ and $z=3$ by computing the residues:

- $\Res_{z=1}f(z) = (z-1)f(z)\evalfrom_{z=1} = {1\over z-3}\evalfrom_{z=1} = -{1\over 2}$
- $\Res_{z=3}f(z) = (z-3)f(z)\evalfrom_{z=3} = {1\over z-1}\evalfrom_{z=3} = {1\over 2}$

Thus
\[
f(z) = {-1/2 \over z-1} + {1/2 \over z-3}
.\]

Now find the two expansions for each term:

\[
{-1/2 \over z-1} &= {1/2 \over 1-z} = {1\over 2}\sum_{k\geq 0} z^k 
&& 0 < \abs{z} < 1 \\
{-1/2 \over z-1} &= -{1\over 2}{z\inv \over z\inv - 1} = -{1\over 2z}{1\over 1-z\inv} = -{1\over 2}\sum_{k\geq 0}z^{-k-1} 
&& 1 < \abs{z} < \infty \\
{1/2\over z-3} &= -{1\over 2}{1\over 3-z} = -{1\over 6}{1\over 1-{z\over 3}} = -{1\over 6}\sum_{k\geq 0}3^{-k} z^k 
&& 0 < \abs{z} < 3 \\
{1/2\over z-3} &= {1\over 2z}{1\over 1-3z\inv} = {1\over 2z} \sum_{k\geq 0}3^kz^{-k} = {1\over 2}\sum_{k\geq 0}3^k z^{-k-1}
&& 3 < \abs{z} < \infty
.\]

Now, just combinatorics to pick the various series that converge on the desired regions:
\[
0 \leq \abs{z} < 1 
\qquad & f(z) = {1\over 2}\sum_{k\geq 0}z^k - {1\over 6}\sum_{k\geq 0} 3^{-k}z^k \\
1 \leq \abs{z} < 3 
\qquad & f(z) = -{1\over 2}\sum_{k\geq 0}z^{-k-1} - {1\over 6}\sum_{k\geq 0} 3^{-k}z^k \\
3 \leq \abs{z} < \infty 
\qquad & f(z) = - {1\over 2}\sum_{k\geq 0}z^{-k-1} + {1\over 2}\sum_{k\geq 0} 3^{k}z^{-k-1}
.\]
:::

