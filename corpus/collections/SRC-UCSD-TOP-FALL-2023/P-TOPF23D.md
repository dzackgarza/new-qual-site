---
schema: qual/card@1
id: P-TOPF23D
kind: problem
title: "Fixed-point-free map on S^n is antipodal; free finite group action on S^{2n} is Z/2"
classification:
  areas:
  - topology
  topics:
  - Fixed Point Theory
  - Antipodal Map
  - Group Actions
  - Spheres
relations: []
review: draft
---

::: problem
Show that a map $f : S^n \to S^n$ which has no fixed points must be homotopic to the antipodal map.
Use this to deduce that a non-trivial finite group acting freely on $S^{2n}$ must be isomorphic to $\mathbb{Z}_2$.
:::

::: {.solution}
<1>1. If $f:S^n\to S^n$ has no fixed point, then
$$H(x,t)=\frac{(1-t)f(x)-tx}{\|(1-t)f(x)-tx\|}$$
defines a homotopy from $f$ to the antipodal map $x\mapsto-x$.
::: {.proof}
The denominator could vanish only if $(1-t)f(x)=tx$. Since both $f(x)$ and $x$ have norm $1$, this forces $t=1/2$ and $f(x)=x$, contrary to the fixed-point-free hypothesis.
:::

<1>2. Therefore every fixed-point-free self-map of $S^n$ has degree
$$(-1)^{n+1}.$$
::: {.proof}
Homotopic maps have the same degree, and the antipodal map on $S^n$ has degree $(-1)^{n+1}$.
:::

<1>3. Now let a nontrivial finite group $G$ act freely on $S^{2n}$. Every $g\ne e$ is fixed-point-free, hence
$$\deg g=-1.$$
::: {.proof}
Apply <1>2 with even sphere dimension $2n$.
:::

<1>4. There can be at most one nonidentity element of $G$.
::: {.proof}
If $g,h\ne e$ are distinct, then $gh\ne e$ unless $h=g^{-1}$. But degree is multiplicative, so $\deg(gh)=(-1)(-1)=+1$. If $gh\ne e$, this contradicts <1>3. Hence every pair of nonidentity elements must be inverses; in particular choosing $h=g$ shows $g^2=e$, and there cannot be a second nonidentity element distinct from $g$.
:::

<1>5. Consequently
$$\boxed{G\cong\mathbb Z/2.}$$
::: {.proof}
The action is nontrivial, so $G$ has exactly two elements by <1>4.
:::
:::
