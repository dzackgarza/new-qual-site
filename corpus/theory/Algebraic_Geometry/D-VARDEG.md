---
schema: qual/card@1
id: D-VARDEG
kind: definition
title: Degree as an intersection count
classification:
  areas:
  - algebraic-geometry
  topics:
  - Degree
  - Intersection Theory
  - Hilbert Polynomial
relations:
- kind: uses
  target: D-L6ERW
- kind: related-to
  target: PR-JR7TS
review: draft
prompts:
- What is the degree of a projective variety?
- Why do the two definitions of degree agree?
---

::: {.definition title="Degree"}
Let $X \subseteq \PP^N$ be projective of dimension $n$.
The \dfn{degree} of $X$ is the number of points of
$$
X \intersect H_1 \intersect \cdots \intersect H_n
$$
for $H_1, \ldots, H_n$ general hyperplanes.
:::

::: {.proposition}
This number is finite, independent of the general hyperplanes chosen, and equals $n!$ times the leading coefficient of the Hilbert polynomial $P_X$.
:::

::: {.remark}
If a hyperplane $H$ contains no irreducible component of $X$, the sequence $0\to\OO_X(-1)\to\OO_X\to\OO_{X\cap H}\to0$ is exact, so $P_{X\cap H}(r)=P_X(r)-P_X(r-1)$.
If $P_X$ has leading term $\frac{d}{n!}r^n$, then $P_{X\cap H}$ has leading term $\frac{d}{(n-1)!}r^{n-1}$, so $X\cap H$ has dimension $n-1$ and the same degree $d$.
After $n$ such cuts, $X\cap H_1\cap\cdots\cap H_n$ is a finite scheme of length $d$; for general hyperplanes it is reduced, so it consists of $d$ points.

For hyperplanes that are not general, the intersection can have fewer points: a line tangent to a smooth conic meets it in one point, of intersection multiplicity $2$, as Bézout's theorem requires.
Degree depends on the embedding: the twisted cubic and a line are both isomorphic to $\PP^1$ but have degrees $3$ and $1$ in their respective embeddings.
:::
