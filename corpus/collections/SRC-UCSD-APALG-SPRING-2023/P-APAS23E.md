---
schema: qual/card@1
id: P-APAS23E
kind: problem
title: Isomorphism $D_6 \cong S_3 \times C_2$ and the character table of $D_6$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
  - Group Theory
relations: []
review: draft
---

::: problem
Let $D_6$ be the group of symmetries of a regular hexagon, let $S_3$ be the symmetric group on three objects, and let $C_2$ be the cyclic group of order $2$.

(1) Prove that $D_6$ is isomorphic to the direct product $S_3 \times C_2$.

(2) Calculate the character table of $D_6$.
:::


::: solution
Write
\[
D_6=\langle r,s\mid r^6=s^2=1,\ srs=r^{-1}\rangle.
\]
Let
\[
z=r^3,
\qquad
H=\langle r^2,s\rangle.
\]
Then $z$ has order $2$ and is central, while $r^2$ has order $3$ and
\[
sr^2s=r^{-2}=(r^2)^{-1}.
\]
Hence
\[
H\cong D_3\cong S_3.
\]
Also $H$ has order $6$, $\langle z\rangle$ has order $2$, and $H\cap\langle z\rangle=\{1\}$ because $z=r^3\notin H$. Since $z$ is central,
\[
H\langle z\rangle\cong H\times\langle z\rangle.
\]
Its order is $6\cdot2=12=|D_6|$, so it is all of $D_6$. Therefore
\[
\boxed{D_6\cong S_3\times C_2.}
\]

For the character table, use the conjugacy classes
\[
C_1=\{1\},\quad
C_2=\{r^3\},\quad
C_3=\{r^2,r^4\},\quad
C_4=\{r,r^5\},
\]
\[
C_5=\{s,r^2s,r^4s\},\quad
C_6=\{rs,r^3s,r^5s\}.
\]
Under $D_6\cong S_3\times C_2$, these correspond respectively to
\[
(e,+),\ (e,-),\ (\text{$3$-cycle},+),\ (\text{$3$-cycle},-),\
(\text{transposition},+),\ (\text{transposition},-).
\]
Let $1,\varepsilon,\tau$ be the irreducible characters of $S_3$, where $\tau$ is the standard $2$-dimensional character, and let $1,\delta$ be the two characters of $C_2$. Taking external tensor products gives all six irreducibles of $D_6$:
\[
\begin{array}{c|rrrrrr}
& C_1&C_2&C_3&C_4&C_5&C_6\\
\hline
1\boxtimes1          &1& 1& 1& 1& 1& 1\\
1\boxtimes\delta    &1&-1& 1&-1& 1&-1\\
\varepsilon\boxtimes1       &1& 1& 1& 1&-1&-1\\
\varepsilon\boxtimes\delta &1&-1& 1&-1&-1& 1\\
\tau\boxtimes1      &2& 2&-1&-1& 0& 0\\
\tau\boxtimes\delta&2&-2&-1& 1& 0& 0
\end{array}
\]
The degree squares are
\[
1+1+1+1+4+4=12=|D_6|,
\]
so this is the complete character table.
:::
