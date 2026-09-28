---
schema: qual/card@1
id: P-FKAJJ
kind: problem
title: Orbit-stabilizer bijection $G/G_x\simeq G\cdot x$, and nontriviality of $Z(G)$
  for finite $p$-groups
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Group Actions
  - p-Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $G$ be a finite group acting on a set $X$.
For $x\in X$, let $G_x$ be the stabilizer of $x$ and $G\cdot x$ be the orbit of $x$.

a. Prove that there is a bijection between the left cosets $G/G_x$ and $G\cdot x$.

b. Prove that the center of every finite $p\dash$group $G$ is nontrivial by considering that action of $G$ on $X=G$ by conjugation.
:::

::: {.solution}
For (a), define
\[
\Phi:G/G_x\longrightarrow G\cdot x,
\qquad
\Phi(gG_x)=g\cdot x.
\]
If $gG_x=hG_x$, then $h^{-1}g\in G_x$, so $(h^{-1}g)\cdot x=x$ and therefore $g\cdot x=h\cdot x$. Thus $\Phi$ is well defined. It is surjective by the definition of the orbit. If $g\cdot x=h\cdot x$, then $h^{-1}g\in G_x$, so $gG_x=hG_x$; hence $\Phi$ is injective. Therefore it is a bijection, and in particular
\[
|G\cdot x|=[G:G_x].
\]

For (b), let the finite $p$-group $G$ act on itself by conjugation. The fixed points are exactly the elements of $Z(G)$. For any $x\in G$, the stabilizer is the centralizer $C_G(x)$, so by part (a) the conjugacy class of $x$ has size
\[
[G:C_G(x)],
\]
a power of $p$. Hence every non-singleton conjugacy class has size divisible by $p$. The class equation therefore gives
\[
|G|=|Z(G)|+\sum_i |\mathcal C_i|,
\]
where every term in the sum is divisible by $p$. Since $p\mid |G|$, it follows that $p\mid |Z(G)|$. The identity lies in $Z(G)$, so $|Z(G)|\ge p$, and in particular $Z(G)$ is nontrivial.
:::
