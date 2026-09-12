---
schema: qual/card@1
id: P-APAS18D
kind: problem
title: $D_8$-orbits on diagonals of a regular octogon; rank of the Reynolds operator
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Permutations
  - Invariant Theory
relations: []
review: draft
---

::: problem
Let $X$ be the set of the $20$ diagonals in a regular octogon.
The dihedral group $D_8$ of octogon symmetries acts on $X$; let $V=\mathbb{C}[X]$ be the associated permutation representation of $D_8$.

(a) How many orbits are there in the action of $D_8$ on $X$?

(b) The Reynolds operator $R_{D_8}\colon V\to V$ is given by
\[
R_{D_8}(v)=\frac{1}{|G|}\sum_{g\in D_8}g\cdot v.
\]
What is the rank of $R_{D_8}$?
:::

::: solution
Label the vertices of the regular octagon by the elements of \(\mathbb Z/8\mathbb Z\). An unordered pair of distinct vertices is determined up to the dihedral action by its cyclic distance
\[
d=\min(|i-j|,8-|i-j|).
\]
Edges have \(d=1\), so the diagonals have \(d=2,3,4\). The dihedral group preserves \(d\), and it acts transitively on the diagonals of each fixed distance. Therefore \(X\) has exactly three \(D_8\)-orbits.

For a permutation representation \(\mathbb C[X]\), the invariant subspace consists exactly of functions on \(X\) that are constant on each orbit. Hence
\[
\dim V^{D_8}=3.
\]
The Reynolds operator is the projection of \(V\) onto \(V^{D_8}\): it fixes every invariant vector, and its image is invariant because for \(h\in D_8\),
\[
hR_{D_8}(v)=\frac1{|D_8|}\sum_{g\in D_8}hg\cdot v=R_{D_8}(v).
\]
Thus
\[
\operatorname{rank}R_{D_8}=\dim V^{D_8}=3.
\]
:::
