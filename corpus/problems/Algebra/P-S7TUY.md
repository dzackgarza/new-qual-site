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

::: problem
What is an irreducible variety? Give an example of a reducible one.
:::

::: solution
A nonempty topological space $X$ is **irreducible** if whenever
\[
X=Y\cup Z
\]
with $Y,Z$ closed in $X$, then $X=Y$ or $X=Z$. Thus an algebraic variety is irreducible when it cannot be written as the union of two proper closed subvarieties.

For an affine algebraic set $V(I)\subseteq k^n$, over an algebraically closed field $k$, one has
\[
V(I)\text{ irreducible}\iff I(V(I))=\sqrt I\text{ is prime}.
\]
Indeed, if $\sqrt I$ is prime and
\[
V(I)=V(J)\cup V(K)=V(JK),
\]
then $JK\subseteq\sqrt I$, so primality gives $J\subseteq\sqrt I$ or $K\subseteq\sqrt I$, hence one of the two closed subsets is all of $V(I)$. The converse is obtained by applying irreducibility to $V(I+(fg))=V(I+(f))\cup V(I+(g))$.

A basic reducible example is
\[
V(xy)\subseteq\mathbb A_k^2.
\]
Since
\[
V(xy)=V(x)\cup V(y),
\]
it is the union of the two coordinate axes, both proper closed subsets. Equivalently, $(xy)$ is not a prime ideal.
:::
