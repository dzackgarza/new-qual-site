---
schema: qual/card@1
id: P-QJ7MD
kind: problem
title: A subgroup of index $2$ is normal; the same for index the smallest prime dividing
  $|G|$
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
---

::: {.problem}
1. Prove that every subgroup of index $2$ is normal.
2. More generally, let $G$ be finite and let $p$ be the smallest prime dividing $|G|$. Prove that every subgroup of index $p$ is normal.
:::

::: {.solution}
<1>1. Index $2$.
::: {.proof}
If $H\le G$ has index $2$, then there are exactly two left cosets and two right cosets. For $g\notin H$, both $gH$ and $Hg$ are the complement $G\setminus H$. Hence
\[
gH=Hg
\]
for every $g\in G$, so $H\trianglelefteq G$.
:::

<1>2. Index equal to the smallest prime divisor.
::: {.proof}
Let $[G:H]=p$ and let $G$ act on the left cosets $G/H$. This gives
\[
\rho:G\to S_p.
\]
The image is transitive, so $p\mid |\rho(G)|$. Also $|\rho(G)|$ divides both $|G|$ and $p!$.

Every prime divisor of $|G|$ is at least $p$, while every prime divisor of $p!$ is at most $p$. Therefore the only possible prime divisor of $|\rho(G)|$ is $p$. Since $p^2\nmid p!$, we get
\[
|\rho(G)|=p.
\]
A transitive group of prime order acts regularly, so the stabilizer of the coset $H$ in $\rho(G)$ is trivial. But the stabilizer upstairs is $H$, hence
\[
H=\ker\rho.
\]
Therefore $H$ is normal in $G$.
:::
:::
