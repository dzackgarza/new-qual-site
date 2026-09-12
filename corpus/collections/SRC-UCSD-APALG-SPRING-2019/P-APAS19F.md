---
schema: qual/card@1
id: P-APAS19F
kind: problem
title: Character table of $D_4$ and decomposition of $V\otimes V$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
---

::: problem
Let $D_4=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle$ be the dihedral group of symmetries of the square.

(a) Write down the character table of $D_4$.

(b) Let $V$ be the $2$-dimensional ``defining'' $D_4$-module obtained by centering the square at the origin in the plane and extending symmetries of the square to linear transformations of the plane.
Give the tensor product $V\otimes V$ the structure of a $D_4$-module by setting
\[
g.(v\otimes v'):=(g.v)\otimes(g.v')
\]
for all $g\in D_4$ and $v,v'\in V$.
Calculate the decomposition of $V\otimes V$ into irreducible $D_4$-modules.
:::

::: solution
The conjugacy classes of \(D_4=\langle r,s:r^4=s^2=1,\ srs=r^{-1}
angle\) are
\[
\{1\},\quad \{r^2\},\quad \{r,r^3\},\quad \{s,r^2s\},\quad \{rs,r^3s\}.
\]
There are therefore five irreducible characters. Four are one-dimensional, obtained by choosing independently \(r\mapsto\pm1\) and \(s\mapsto\pm1\). The fifth is the defining two-dimensional representation \(V\). With the classes ordered as above, the character table is
\[
\begin{array}{c|ccccc}
 &1&r^2&\{r,r^3\}&\{s,r^2s\}&\{rs,r^3s\}\\ \hline
\chi_{++}&1&1&1&1&1\\
\chi_{+-}&1&1&1&-1&-1\\
\chi_{-+}&1&1&-1&1&-1\\
\chi_{--}&1&1&-1&-1&1\\
\chi_V&2&-2&0&0&0
\end{array}.
\]
For the tensor product, characters multiply pointwise, so
\[
\chi_{V\otimes V}=\chi_V^2=(4,4,0,0,0).
\]
But the sum of the four linear characters is also
\[
\chi_{++}+\chi_{+-}+\chi_{-+}+\chi_{--}=(4,4,0,0,0).
\]
Hence
\[
V\otimes V\cong
\chi_{++}\oplus\chi_{+-}\oplus\chi_{-+}\oplus\chi_{--}.
\]
:::
