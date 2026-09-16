---
schema: qual/card@1
id: P-APAS19H
kind: problem
title: Character table of $S_3\times S_2$ and restriction of $S^{(3,2)}$
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
Let $S_n$ be the symmetric group on $n$ letters.

(a) Calculate the character table of the product group $S_3\times S_2$.

(b) Let $\lambda=(3,2)\vdash 5$ and let $S^\lambda$ be the associated irreducible representation of $S_5$.
Calculate the decomposition of the restricted module $S^\lambda\downarrow_{S_3\times S_2}^{S_5}$ into irreducibles.
:::

::: solution
The irreducible characters of a direct product are exactly the external tensor products of irreducible characters of the two factors. For \(S_3\), with conjugacy classes represented by \(1,(12),(123)\), the irreducible characters are
\[
\begin{array}{c|ccc}
&1&(12)&(123)\\ \hline
\mathbf 1&1&1&1\\
\mathrm{sgn}&1&-1&1\\
\mathrm{std}&2&0&-1
\end{array}.
\]
For \(S_2\), with classes \(1,\tau\), the irreducible characters are
\[
\begin{array}{c|cc}
&1&\tau\\ \hline
\mathbf 1&1&1\\
\mathrm{sgn}&1&-1
\end{array}.
\]
Therefore, ordering the six conjugacy classes of \(S_3\times S_2\) as
\[
(1,1),\ ((12),1),\ ((123),1),\ (1,\tau),\ ((12),\tau),\ ((123),\tau),
\]
the character table is
\[
\begin{array}{c|rrrrrr}
& (1,1)&((12),1)&((123),1)&(1,\tau)&((12),\tau)&((123),\tau)\\ \hline
\mathbf 1\boxtimes\mathbf 1&1&1&1&1&1&1\\
\mathrm{sgn}\boxtimes\mathbf 1&1&-1&1&1&-1&1\\
\mathrm{std}\boxtimes\mathbf 1&2&0&-1&2&0&-1\\
\mathbf 1\boxtimes\mathrm{sgn}&1&1&1&-1&-1&-1\\
\mathrm{sgn}\boxtimes\mathrm{sgn}&1&-1&1&-1&1&-1\\
\mathrm{std}\boxtimes\mathrm{sgn}&2&0&-1&-2&0&1
\end{array}.
\]

For the restriction of \(S^{(3,2)}\), the Littlewood--Richardson branching rule gives
\[
\operatorname{Res}^{S_5}_{S_3\times S_2}S^{(3,2)}
\cong \bigoplus_{\alpha\vdash3,\,\beta\vdash2}
c^{(3,2)}_{\alpha,\beta}\,S^\alpha\boxtimes S^\beta.
\]
The only nonzero Littlewood--Richardson coefficients here are
\[
c^{(3,2)}_{(3),(2)}=1,\qquad
c^{(3,2)}_{(2,1),(2)}=1,\qquad
c^{(3,2)}_{(2,1),(1,1)}=1.
\]
Hence
\[
S^{(3,2)}\downarrow_{S_3\times S_2}
\cong
S^{(3)}\boxtimes S^{(2)}
\oplus
S^{(2,1)}\boxtimes S^{(2)}
\oplus
S^{(2,1)}\boxtimes S^{(1,1)}.
\]
The dimensions are \(1+2+2=5=\dim S^{(3,2)}\), providing a check.
:::
