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
Show that there is no bijective conformal map from $A\coloneqq \theset{0< \abs{z} < 1}$ to $B\coloneqq \theset{1<\abs{z} < 2}$.
:::

::: {.solution}
Suppose toward a contradiction that $f: A\to B$ is a bijective conformal map.

::: pf

::: {.pf-step #extend}
$f$ extends to a holomorphic map $F:\DD\to B$.

::: pf-proof
Since $f$ is bounded near $0$, its isolated singularity at $0$ is removable, and the extension $F$ maps $\DD$ into $\overline B$.
As $F$ is nonconstant, it is an open map, so $F(\DD)$ is an open subset of $\overline B$, hence contained in the interior $B$.
:::

:::

::: pf-step
$f$ is not injective.

::: pf-proof
Let $w_0\coloneqq F(0)\in B$; by surjectivity of $f$ there is $z_0\in A$ with $f(z_0)=w_0$.
Choose disjoint open discs $U\ni z_0$ and $V\ni0$ in $\DD$ with $0\notin U$.
Since $F$ is open (step [](#extend){.pf-ref}), $F(U)\intersect F(V)$ is an open set containing $w_0$, so it contains a point $w\neq w_0$.
Then $w=F(v)$ for some $v\in V$ with $v\neq0$, because $F(0)=w_0$, and $w=F(u)$ for some $u\in U$.
Both $u$ and $v$ lie in $A$, and $u\neq v$ because $U\intersect V$ is empty, so $f(u)=f(v)$ with $u\neq v$.
:::

:::

:::

:::
