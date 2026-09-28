---
schema: qual/card@1
id: E-7ZCKU
kind: problem
title: No conformal bijection from the punctured disk onto the annulus $1<\abs z<2$
classification:
  areas:
  - complex-analysis
  topics:
  - Biholomorphisms
  - Conformal Maps
  - Removable Singularities
  - Open Mapping Theorem
relations: []
review: draft
---

::: {.exercise}
Show that there is no bijective conformal map from $A\da \ts{0< \abs{z} < 1}$ to $B\da \ts{1<\abs{z} < 2}$.
:::

::: {.solution}
Suppose toward a contradiction that $f: A\to B$ is a bijective conformal map.
Since $f(A) \subseteq B$, which is bounded, the isolated singularity of $f$ at $0$ is removable.
So $f$ extends holomorphically to $F: \DD\to \bar{B}$. As $F$ is nonconstant, it is an open map, so $F(\DD)$ is open and contained in $\bar B$, hence $F(\DD) \subseteq B$.
Write $w_0 \da F(0) \in B$. By surjectivity there is a $z_0\in A$ such that $f(z_0) = w_0$.
Choose disjoint open disks $U\ni z_0$ and $V\ni0$ in $\DD$ with $0\notin U$.
Since $F$ is open, $F(U)\intersect F(V)$ is an open set containing $w_0$, so it contains a point $w\neq w_0$.
Then $w=F(v)$ for some $v\in V$ with $v\neq0$ (as $F(0)=w_0$), and $w=F(u)$ for some $u\in U$. Both $u$ and $v$ lie in $A$ and $u\neq v$ since $U\intersect V$ is empty, so $f(u)=f(v)$ contradicts injectivity of $f$.
:::
