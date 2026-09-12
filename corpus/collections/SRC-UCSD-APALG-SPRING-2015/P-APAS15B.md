---
schema: qual/card@1
id: P-APAS15B
kind: problem
title: Character table of $S_3 \times S_2$ and restriction of $S^{(2,2,1)}$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
  - Symmetric Functions
relations: []
review: draft
---

::: problem
(1) Write down the character table of the product of symmetric groups $S_3 \times S_2$.

(2) Let $S^{(2,2,1)}$ be the irreducible representation of $S_5$ indexed by the partition $(2,2,1) \vdash 5$.
Determine the decomposition of the restriction $S^{(2,2,1)} \downarrow_{S_3 \times S_2}$ into irreducible $S_3 \times S_2$-representations.
:::

::: solution
The irreducible characters of a direct product are exactly the external products of irreducible characters of the two factors.

For \(S_3\), write
\[
\mathbf 1,\quad \varepsilon,\quad \rho
\]
for the trivial, sign, and standard two-dimensional characters. On the three conjugacy classes
\[
1,\quad (12),\quad (123)
\]
their values are
\[
\begin{array}{c|rrr}
&1&(12)&(123)\\ \hline
\mathbf 1&1&1&1\\
\varepsilon&1&-1&1\\
\rho&2&0&-1
\end{array}.
\]
For \(S_2\), write \(\mathbf 1\) and \(\delta\) for the trivial and sign characters, with values
\[
\begin{array}{c|rr}
&1&(12)\\ \hline
\mathbf 1&1&1\\
\delta&1&-1.
\end{array}
\]

Thus \(S_3\times S_2\) has six conjugacy classes, represented by
\[
(1,1),\ ((12),1),\ ((123),1),\ (1,(12)),\ ((12),(12)),\ ((123),(12)),
\]
and six irreducible characters. Since an external product satisfies
\[
(\chi\boxtimes\psi)(g,h)=\chi(g)\psi(h),
\]
the full character table is
\[
\begin{array}{c|rrrrrr}
&(1,1)&((12),1)&((123),1)&(1,(12))&((12),(12))&((123),(12))\\ \hline
\mathbf1\boxtimes\mathbf1&1&1&1&1&1&1\\
\varepsilon\boxtimes\mathbf1&1&-1&1&1&-1&1\\
\rho\boxtimes\mathbf1&2&0&-1&2&0&-1\\
\mathbf1\boxtimes\delta&1&1&1&-1&-1&-1\\
\varepsilon\boxtimes\delta&1&-1&1&-1&1&-1\\
\rho\boxtimes\delta&2&0&-1&-2&0&1
\end{array}.
\]

For part (2), restriction from \(S_5\) to the Young subgroup \(S_3\times S_2\) is governed by the Littlewood--Richardson coefficients:
\[
\operatorname{Res}^{S_5}_{S_3\times S_2}S^\lambda
\cong
\bigoplus_{\mu\vdash3,\,\nu\vdash2}
 c_{\mu,\nu}^{\lambda}\,
 S^\mu\boxtimes S^\nu.
\]
For \(\lambda=(2,2,1)\), the nonzero coefficients with \(|\mu|=3\), \(|\nu|=2\) are
\[
c_{(1,1,1),(1,1)}^{(2,2,1)}=1,
\qquad
c_{(2,1),(1,1)}^{(2,2,1)}=1,
\qquad
c_{(2,1),(2)}^{(2,2,1)}=1,
\]
and all others are zero. Hence
\[
\boxed{
\operatorname{Res}^{S_5}_{S_3\times S_2}S^{(2,2,1)}
\cong
S^{(1,1,1)}\boxtimes S^{(1,1)}
\oplus
S^{(2,1)}\boxtimes S^{(1,1)}
\oplus
S^{(2,1)}\boxtimes S^{(2)}.}
\]
The dimensions are \(1+2+2=5\), agreeing with \(\dim S^{(2,2,1)}=5\).
:::
