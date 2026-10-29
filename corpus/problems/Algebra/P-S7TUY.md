---
schema: qual/card@1
id: P-S7TUY
kind: problem
title: Irreducible varieties
classification:
  areas:
  - algebra
  topics:
  - Geometry
  - Prime Ideals
  - Commutative Algebra
relations: []
review: draft
---

::: {.problem}
What is an irreducible variety? Give an example of a reducible one.
:::

::: {.solution}

A nonempty topological space $X$ is irreducible if $X=Y\cup Z$ with $Y,Z$ closed implies $X=Y$ or $X=Z$; a variety is irreducible when its Zariski topology is. Let $k$ be algebraically closed, and for an affine algebraic set $V\subseteq\AA^n_k$ let $I(V)$ be the ideal of polynomials vanishing on $V$.

::: pf

::: pf-step

A nonempty affine algebraic set $V$ is irreducible if and only if $I(V)$ is prime.

::: pf-proof

Suppose $I(V)$ is prime and $V=Y\cup Z$ with $Y,Z$ closed. If $Y\neq V$ and $Z\neq V$, choose $f\in I(Y)\setminus I(V)$ and $g\in I(Z)\setminus I(V)$. Then $fg$ vanishes on $Y\cup Z=V$, so $fg\in I(V)$, contradicting primality. Conversely, suppose $V$ is irreducible. Then $I(V)\neq k[x_1,\ldots,x_n]$ because $V\neq\varnothing$. If $fg\in I(V)$, then $V=(V\cap V(f))\cup(V\cap V(g))$, so $V\subseteq V(f)$ or $V\subseteq V(g)$, that is, $f\in I(V)$ or $g\in I(V)$.

:::

:::

::: pf-qed

The algebraic set $V(xy)\subseteq\AA^2_k$ is reducible: $V(xy)=V(x)\cup V(y)$ is the union of the two coordinate axes, each a proper closed subset. Equivalently, $I(V(xy))=(xy)$ is not prime, since $x,y\notin(xy)$.

:::

:::

:::
