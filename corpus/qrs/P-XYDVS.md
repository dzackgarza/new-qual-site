---
schema: qual/card@1
id: P-XYDVS
kind: problem
title: A normal subgroup of order coprime to its index is unique of its order
classification:
  areas:
  - algebra
  topics:
  - normal-subgroups
  - cosets-and-lagrange
  - subgroups
relations: []
review: draft
solved: true
---
Let $H$ be a normal subgroup of a finite group $G$ where the order of $H$ and the index of $H$ in $G$ are relatively prime.
Prove that no other subgroup of $G$ has the same order as $H$.

:::{.concept}
\envlist

- Division algorithm: $(a,b)= d\implies as+bt =1$ for some $s, t$.
- Coset containment trick: $X\subseteq N \iff xN = N$ for all $x$.
:::

:::{.strategy}
Recognize that it suffices to show $hN = N$.
Context cue: coprimality hints at division algorithm.
Descend to quotient so you can leverage both the order of $h$ *and* the order of cosets simultaneously.
:::

:::{.solution}
\envlist

- For ease of notation, replace $H$ in the problem with $N$ so we remember which one is normal.
- Write $n\da \# N$ and $m \da [G:N] = \#G/N$, where the quotient makes sense since $N$ is normal.
- Let $H \leq G$ with $\# H = n$, we'll show $H=N$.
  - Since $\# H = \# N$ it suffices to show $H \subseteq N$.
  - It further suffices to show $hN = N$ for all $h\in H$.
- Noting $\gcd(m, n)=1$, use the division algorithm to write $1 = ns + mt$ for some $s,t\in \ZZ$.
- The result follows from a computation:
\[
hN 
&= h^1 N \\
&= h^{ns + mt}N \\
&= h^{ns} N \cdot h^{mt}N \\
&= \qty{h^n N}^s \cdot \qty{h^t N}^m \\
&= (eN)^s \cdot N \\
&= N
,\]
  - We've used that $h\in H \implies o(h) \divides \# H = n$ by Lagrange, so $h^n = e$.
  - We've also used that $\# G/N = m$, so $(xH)^m = H$ for any $xH\in G/H$.

:::

