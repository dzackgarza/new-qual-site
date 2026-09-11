---
schema: qual/card@1
id: P-AGH2410CHOW
kind: problem
title: Chow's lemma
classification:
  areas:
  - algebraic-geometry
  topics:
  - Proper Morphisms
  - Projective Morphisms
  - Birational Geometry
relations: []
review: draft
---

::: problem
This result says that proper morphisms are fairly close to projective morphisms.

Let $X$ be proper over a noetherian scheme $S$.
Then there is a scheme $X'$ and a morphism $g: X' \to X$ such that $X'$ is projective over $S$, and there is an open dense subset $U \subseteq X$ such that $g$ induces an isomorphism of $g\inv(U)$ onto $U$.
Prove this in the following steps.

a. Reduce to the case $X$ irreducible.

b. Show that $X$ can be covered by finitely many open subsets $U_i$, $i = 1, \ldots, n$, each of which is quasi-projective over $S$.
Let $U_i \injects P_i$ be an open immersion of $U_i$ into a scheme $P_i$ which is projective over $S$.

c. Let $U = \bigcap_i U_i$, and consider the map
\[
f: U \to X \fiberproduct{S} P_1 \fiberproduct{S} \cdots \fiberproduct{S} P_n
\]
deduced from the given maps $U \to X$ and $U \to P_i$.
Let $X'$ be the closed image subscheme structure on $\cl_X f(U)$.
Let $g: X' \to X$ be the projection onto the first factor, and let $h: X' \to P = P_1 \fiberproduct{S} \cdots \fiberproduct{S} P_n$ be the projection onto the product of the remaining factors.
Show that $h$ is a closed immersion, hence $X'$ is projective over $S$.

d. Show that $g\inv(U) \to U$ is an isomorphism, completing the proof.
:::
