---
schema: qual/card@1
id: P-APASP08J
kind: problem
title: "Pólya enumeration on the cube and Frobenius image"
classification:
  areas:
  - applied-algebra
  topics:
  - Combinatorics
  - Pólya Enumeration
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
Let $\Gamma$ be the group of rotations of the cube.

1. Compute the Pólya enumerator of the action of $\Gamma$ on the edges of the cube.

2. Use the previous result to compute the number of ways to colour the edges of the cube using seven red and five yellow.

3. Show that the polynomial you computed in part 1 is the Frobenius image of the character of a representation of $S_{12}$.
:::

::: solution
The rotation group $\Gamma$ of the cube has order $24$. We classify its elements by rotation axis and angle and record the induced cycle structure on the $12$ edges.

- The identity contributes cycle type $1^{12}$.
- There are $6$ rotations through $90^\circ$ or $270^\circ$ about an axis through opposite faces. Each partitions the edges into three $4$-cycles, so has type $4^3$.
- There are $3$ rotations through $180^\circ$ about an axis through opposite faces. Each pairs all edges, so has type $2^6$.
- There are $8$ rotations through $120^\circ$ or $240^\circ$ about a body diagonal. Each partitions the edges into four $3$-cycles, so has type $3^4$.
- There are $6$ rotations through $180^\circ$ about an axis through the midpoints of a pair of opposite edges. Those two edges are fixed as edge-sets, and the remaining ten edges are paired, so the cycle type is $1^2 2^5$.

Hence the Pólya cycle enumerator is
\[
\boxed{
Z_\Gamma(p_1,p_2,\ldots)
=
\frac1{24}
\left(
 p_1^{12}
+6p_4^3
+3p_2^6
+8p_3^4
+6p_1^2p_2^5
\right).
}
\]

For the two-color problem, substitute
\[
p_k\mapsto r^k+y^k.
\]
The number of orbits with exactly seven red and five yellow edges is the coefficient of $r^7y^5$ in
\[
\frac1{24}
\left[
(r+y)^{12}
+6(r^4+y^4)^3
+3(r^2+y^2)^6
+8(r^3+y^3)^4
+6(r+y)^2(r^2+y^2)^5
\right].
\]
The middle three terms involving only cycle lengths $4$, $2$, and $3$ cannot contribute $r^7y^5$, since their red exponents are respectively divisible by $4$, even, and divisible by $3$.

The identity term contributes
\[
\binom{12}{7}=792.
\]
For the final term, to obtain seven red edges we must choose three of the five $2$-cycles to be red and one of the two fixed edges to be red. Thus its coefficient before the class-size factor is
\[
\binom53\binom21=20.
\]
Therefore Burnside's lemma gives
\[
\frac{792+6\cdot20}{24}
=
\frac{912}{24}
=38.
\]
Hence
\[
\boxed{38}
\]
inequivalent edge colorings use exactly seven red and five yellow edges.

For part 3, regard $\Gamma$ as a subgroup of $S_{12}$ through its action on the edges. Let
\[
M=\operatorname{Ind}_{\Gamma}^{S_{12}}\mathbf1.
\]
The Frobenius characteristic of a representation with character $\chi$ is
\[
\operatorname{ch}(\chi)
=
\sum_{\lambda\vdash12}
\frac{\chi(C_\lambda)}{z_\lambda}p_\lambda.
\]
For an induced trivial character, the standard induced-character formula gives
\[
\operatorname{ch}\left(\operatorname{Ind}_\Gamma^{S_{12}}\mathbf1\right)
=
\frac1{|\Gamma|}\sum_{g\in\Gamma}p_{\lambda(g)},
\]
where $\lambda(g)$ is the cycle type of $g$ in its action on the twelve edges. Using the five classes above, this is exactly
\[
\frac1{24}
\left(
 p_1^{12}
+6p_4^3
+3p_2^6
+8p_3^4
+6p_1^2p_2^5
\right).
\]
Thus the Pólya enumerator from part 1 is precisely the Frobenius image of the character of the $S_{12}$-representation
\[
\boxed{\operatorname{Ind}_\Gamma^{S_{12}}\mathbf1}.
\]
:::
