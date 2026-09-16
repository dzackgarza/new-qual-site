---
schema: qual/card@1
id: P-APAS11E
kind: problem
title: Induction from Young subgroups of $S_7$ and a Kronecker product on $S_4$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
relations: []
review: draft
---

::: {.problem}
As on the exam: if $\lambda=(\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_k)$ is a partition of $n$, let $A^\lambda$ denote the irreducible representation of the symmetric group $S_n$ such that the Frobenius image of $\chi^{A^\lambda}=\chi^\lambda$ is the Schur function $S_\lambda(x_1,\ldots,x_N)$ where $N>n$.

(a) Let $A^{(2,1,1)}\times A^{(2,1)}$ denote the representation of $S_4\times S_3$ such that for all $(\sigma,\tau)\in S_4\times S_3$
\[
\bigl(A^{(2,1,1)}\times A^{(2,1)}\bigr)(\sigma,\tau)=A^{(2,1,1)}(\sigma)\otimes A^{(2,1)}(\tau)
\]
where for any matrices $A$ and $B$, $A\otimes B$ denotes the tensor product of $A$ and $B$.
Decompose
\[
\bigl(A^{(2,1,1)}\times A^{(2,1)}\bigr)\uparrow_{S_4\times S_3}^{S_7}
\]
as a sum of irreducible representations of $S_7$.

(b) Show that $\{A^\lambda\times A^\mu:\lambda\vdash 4\text{ and }\mu\vdash 3\}$ is a complete set of representatives of the irreducible representations of $S_4\times S_4$ where
\[
\bigl(A^\lambda\times A^\mu\bigr)(\sigma,\tau)=A^\lambda(\sigma)\otimes A^\mu(\tau).
\]

Note: For parts (a) and (b) above, regard $S_4\times S_3$ as a subgroup of $S_7$ by letting
\[
S_4\times S_4=\{\sigma\in S_7:\sigma(1),\sigma(2),\sigma(3),\sigma(4)\in\{1,2,3,4\},\ \sigma(5),\sigma(6),\sigma(7)\in\{5,6,7\}\}.
\]

(c) Let $T$ denote the trivial representation.
Decompose $T\uparrow_{S_1\times S_3\times S_3}^{S_7}$ as a sum of irreducible representations of $S_7$ where $S_1\times S_3\times S_3$ is the Young subgroup of $S_7$ consisting of all permutations $\sigma\in S_7$ such that
\[
\sigma(1)=1,\qquad
\sigma(2),\sigma(3),\sigma(4)\in\{2,3,4\},\qquad
\sigma(5),\sigma(6),\sigma(7)\in\{5,6,7\}.
\]

(d) Decompose $A^{(2,2)}\otimes A^{(2,2)}$ as a sum of irreducible representations of $S_4$ where $\otimes$ represents the Kronecker product of the representations.
:::

::: {.solution}
The source contains three forced notation corrections: under its decreasing-partition convention, $(1,1,2)$ and $(1,2)$ mean $(2,1,1)$ and $(2,1)$, and the product group in part (b) and the displayed embedding is $S_4\times S_3$.

For (a), Frobenius characteristic converts induction from a Young subgroup into multiplication of Schur functions:
\[
\operatorname{ch}\operatorname{Ind}_{S_4\times S_3}^{S_7}
(A^{(2,1,1)}\boxtimes A^{(2,1)})
=s_{(2,1,1)}s_{(2,1)}.
\]
The Littlewood--Richardson rule gives
\[
\begin{aligned}
s_{(2,1,1)}s_{(2,1)}={}&s_{(2,2,1,1,1)}+s_{(2,2,2,1)}+s_{(3,1,1,1,1)}\\
&+2s_{(3,2,1,1)}+s_{(3,2,2)}+s_{(3,3,1)}+s_{(4,1,1,1)}+s_{(4,2,1)}.
\end{aligned}
\]
Hence the induced representation is the corresponding direct sum, with $A^{(3,2,1,1)}$ appearing twice and all other listed constituents once.

For (b), if $U$ and $V$ are irreducible representations of finite groups $G$ and $H$, then $U\boxtimes V$ is irreducible for $G\times H$; moreover every irreducible representation of $G\times H$ is of this form. Applying this with $G=S_4$ and $H=S_3$ gives precisely
\[
\{A^\lambda\boxtimes A^\mu:\lambda\vdash4,\ \mu\vdash3\}.
\]

For (c), the Frobenius characteristic of the induced trivial representation is
\[
h_1h_3h_3=s_{(3,3,1)}+s_{(4,2,1)}+2s_{(4,3)}+s_{(5,1,1)}+2s_{(5,2)}+2s_{(6,1)}+s_{(7)}.
\]
Therefore
\[
T\uparrow_{S_1\times S_3\times S_3}^{S_7}
\cong A^{(7)}\oplus2A^{(6,1)}\oplus2A^{(5,2)}\oplus A^{(5,1,1)}
\oplus2A^{(4,3)}\oplus A^{(4,2,1)}\oplus A^{(3,3,1)}.
\]

For (d), the character of $A^{(2,2)}$ on the five conjugacy classes of $S_4$, of cycle types
\[
(1^4),(2,1^2),(2^2),(3,1),(4),
\]
is
\[
(2,0,2,-1,0).
\]
Thus the Kronecker square has character
\[
(4,0,4,1,0).
\]
Taking inner products with the irreducible characters of $S_4$ yields multiplicity one for $(4)$, $(2,2)$, and $(1^4)$, and zero for the other two partitions. Hence
\[
A^{(2,2)}\otimes A^{(2,2)}\cong A^{(4)}\oplus A^{(2,2)}\oplus A^{(1^4)}.
\]
:::
