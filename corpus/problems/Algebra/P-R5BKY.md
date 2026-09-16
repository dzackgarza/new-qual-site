---
schema: qual/card@1
id: P-R5BKY
kind: problem
title: $(\RR,+)\cong(\RR_{>0},\times)$, but not for $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Homomorphisms
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
Is $(\RR,+)$ isomorphic to $(\RR_{>0},\times)$? Is the analogous statement true for $\QQ$ and $\QQ_{>0}$?
:::

::: {.solution}
For the reals, yes. The exponential map
\[
\exp:(\RR,+)\longrightarrow(\RR_{>0},\times)
\]
is a group isomorphism, with inverse $\log$.

For the rationals, no. The additive group $(\QQ,+)$ is divisible: for every $q\in\QQ$ and every positive integer $n$, there exists $x=q/n$ with
\[
nx=q.
\]

The multiplicative group $(\QQ_{>0},\times)$ is not divisible. For example, $2$ has no square root in $\QQ_{>0}$. Divisibility is preserved by group isomorphism, so
\[
(\QQ,+)\not\cong(\QQ_{>0},\times).
\]
:::
