---
schema: qual/card@1
id: P-APAS11D
kind: problem
title: Murnaghan–Nakayama on $S_5$, Young-subgroup characters, and restriction of $A^{(4,1)}$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
  - Character Theory
relations: []
review: draft
---

::: {.problem}
As on the exam: if $\lambda=(\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_k)$ is a partition of $n$, let $A^\lambda$ denote the irreducible representation of the symmetric group $S_n$ such that the Frobenius image of $\chi^{A^\lambda}=\chi^\lambda$ is the Schur function $S_\lambda(x_1,\ldots,x_N)$ where $N>n$.

(a) Use the Murnaghan–Nakayama rule to compute the value of the irreducible characters of $S_5$ at the conjugacy class indexed by the partition $(2,3)$.

(b) Find the character table for $S_3\times S_2$ where $S_3\times S_2$ is the Young subgroup of $S_5$ consisting of all permutations $\sigma\in S_5$ such that
\[
\sigma(1),\sigma(2),\sigma(3)\in\{1,2,3\},\qquad
\sigma(4),\sigma(5)\in\{4,5\}.
\]

(c) Find the values of the character of $A^{(4,1)}$ on the conjugacy classes of $S_5$.

(d) Decompose $A^{(4,1)}\downarrow_{S_3\times S_2}^{S_5}$ as a sum of irreducible representations of $S_3\times S_2$.
:::

::: {.solution}
The source prints $A^{(1,4)}$, but under its own convention that partitions are weakly decreasing this is necessarily $A^{(4,1)}$; we use that corrected label below.

For (a), the conjugacy class $(3,2)$ consists of permutations having one $3$-cycle and one $2$-cycle. Applying the Murnaghan--Nakayama rule gives the following values, indexed by the partitions of $5$:
\[
\begin{array}{c|rrrrrrr}
\lambda &(5)&(4,1)&(3,2)&(3,1,1)&(2,2,1)&(2,1,1,1)&(1^5)\\ \hline
\chi^\lambda_{(3,2)}&1&-1&1&0&-1&1&-1.
\end{array}
\]
For example, for $(4,1)$ the only admissible rim-hook removal of length $3$ followed by one of length $2$ has total sign $-1$; the other entries are obtained identically. These values also agree with the ordinary $S_5$ character table.

For (b), write the three irreducible characters of $S_3$ as
\[
1,\quad \varepsilon_3,\quad \rho,
\]
with values on the classes $1,(12),(123)$
\[
\begin{array}{c|rrr}
&1&(12)&(123)\\ \hline
1&1&1&1\\
\varepsilon_3&1&-1&1\\
\rho&2&0&-1
\end{array},
\]
and the two irreducible characters of $S_2$ as $1,\varepsilon_2$, with values on $1,(45)$
\[
\begin{array}{c|rr}
&1&(45)\\ \hline
1&1&1\\
\varepsilon_2&1&-1.
\end{array}
\]
Every irreducible character of $S_3\times S_2$ is an external tensor product $\alpha\boxtimes\beta$, and
\[
(\alpha\boxtimes\beta)(g,h)=\alpha(g)\beta(h).
\]
Thus the complete character table is the Kronecker product of the two displayed tables. Explicitly, on the six classes
\[
(1,1),\ ((12),1),\ ((123),1),\ (1,(45)),\ ((12),(45)),\ ((123),(45))
\]
it is
\[
\begin{array}{c|rrrrrr}
1\boxtimes1&1&1&1&1&1&1\\
\varepsilon_3\boxtimes1&1&-1&1&1&-1&1\\
\rho\boxtimes1&2&0&-1&2&0&-1\\
1\boxtimes\varepsilon_2&1&1&1&-1&-1&-1\\
\varepsilon_3\boxtimes\varepsilon_2&1&-1&1&-1&1&-1\\
\rho\boxtimes\varepsilon_2&2&0&-1&-2&0&1.
\end{array}
\]

For (c), $A^{(4,1)}$ is the standard representation of $S_5$: it is the quotient of the permutation representation on five letters by the invariant line. Hence
\[
\chi^{(4,1)}(\sigma)=\#\operatorname{Fix}(\sigma)-1.
\]
On cycle types
\[
(1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)
\]
this gives respectively
\[
4,\ 2,\ 0,\ 1,\ -1,\ 0,\ -1.
\]

For (d), restrict the permutation representation of $S_5$ to $S_3\times S_2$. The first three letters give the permutation representation of $S_3$, and the last two give the permutation representation of $S_2$. Therefore
\[
\mathbb C^5\downarrow_{S_3\times S_2}
\cong (1\oplus\rho)\boxtimes 1
\oplus 1\boxtimes(1\oplus\varepsilon_2).
\]
Since $A^{(4,1)}$ is obtained by removing one copy of the trivial representation, we obtain
\[
A^{(4,1)}\downarrow_{S_3\times S_2}
\cong
(1\boxtimes1)\oplus(\rho\boxtimes1)\oplus(1\boxtimes\varepsilon_2).
\]
The dimensions $1+2+1=4$ agree with $\dim A^{(4,1)}=4$, so the decomposition is complete.
:::
