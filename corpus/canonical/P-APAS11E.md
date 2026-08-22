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
solved: false
---

::: problem
As on the exam: if $\lambda=(\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_k)$ is a partition of $n$, let $A^\lambda$ denote the irreducible representation of the symmetric group $S_n$ such that the Frobenius image of $\chi^{A^\lambda}=\chi^\lambda$ is the Schur function $S_\lambda(x_1,\ldots,x_N)$ where $N>n$.

(a) Let $A^{(1,1,2)}\times A^{(1,2)}$ denote the representation of $S_4\times S_3$ such that for all $(\sigma,\tau)\in S_4\times S_3$
\[
\bigl(A^{(1,1,2)}\times A^{(1,2)}\bigr)(\sigma,\tau)=A^{(1,1,2)}(\sigma)\otimes A^{(1,2)}(\tau)
\]
where for any matrices $A$ and $B$, $A\otimes B$ denotes the tensor product of $A$ and $B$. Decompose
\[
\bigl(A^{(1,1,2)}\times A^{(1,2)}\bigr)\uparrow_{S_4\times S_3}^{S_7}
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

(c) Let $T$ denote the trivial representation. Decompose $T\uparrow_{S_1\times S_3\times S_3}^{S_7}$ as a sum of irreducible representations of $S_7$ where $S_1\times S_3\times S_3$ is the Young subgroup of $S_7$ consisting of all permutations $\sigma\in S_7$ such that
\[
\sigma(1)=1,\qquad
\sigma(2),\sigma(3),\sigma(4)\in\{2,3,4\},\qquad
\sigma(5),\sigma(6),\sigma(7)\in\{5,6,7\}.
\]

(d) Decompose $A^{(2,2)}\otimes A^{(2,2)}$ as a sum of irreducible representations of $S_4$ where $\otimes$ represents the Kronecker product of the representations.
:::
