---
schema: qual/card@1
id: P-AGXGATHPULLBACK
kind: problem
title: Morphisms of affine varieties against the induced maps of coordinate rings
classification:
  areas:
  - algebraic-geometry
  topics:
  - Morphisms of Varieties
  - Coordinate Rings
  - Automorphisms
relations: []
review: draft
---

::: {.problem}
Let $f:X\to Y$ be a morphism of affine varieties and $f^*: A(Y) \to A(X)$ the induced map on coordinate rings.
Determine whether the following statements are true or false:

a. $f$ is surjective $\iff$ $f^*$ is injective.

b. $f$ is injective $\iff$ $f^*$ is surjective.

c. If $f:\AA^1\to\AA^1$ is an isomorphism, then $f$ is *affine linear*, i.e. $f(x) = ax+b$ for some $a, b\in k$.

d. If $f:\AA^2\to\AA^2$ is an isomorphism, then $f$ is *affine linear*, i.e. $f(x) = Ax+b$ for some $A \in \Mat(2\times 2, k)$ and $b\in k^2$.
:::

::: {.solution}
**Part a**: true.
If $p, q\in A(Y)$, then
\[
f^* p &= f^* q \\
&\implies (p\circ f) = (q\circ f) \\
&\implies p = q
,\]
where in the last implication we used that $f$ is surjective iff $f$ admits a right inverse.
:::

::: {.remark}
Erratum: the answer "true" in part a is wrong, and the argument above proves only one direction.
It shows that $f$ surjective implies $f^*$ injective; that step needs only that a surjective map can be cancelled on the right, $p \circ f = q \circ f \Rightarrow p = q$.
The converse fails: the projection $f: V(xy-1) \to \AA^1$, $(x,y) \mapsto x$, has image $\AA^1 \sm \ts{0}$, yet $f^*: k[x] \to k[x, y]/\gens{xy-1}$ is injective.
In general $f^*$ is injective exactly when $f$ is dominant.
:::
