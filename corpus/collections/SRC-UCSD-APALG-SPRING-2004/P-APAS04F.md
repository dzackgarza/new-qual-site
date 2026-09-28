---
schema: qual/card@1
id: P-APAS04F
kind: problem
title: Murnaghan–Nakayama values of $A^{(4,1)}$ and restriction to $S_3\times S_2$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
  - Character Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
  note: The official UCSD source prints A^(1,4) and S_6 in part (b); these are corrected to the partition (4,1) and subgroup of S_5.
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
If $\lambda=(\lambda_1\ge\lambda_2\ge\dots\ge\lambda_k)$ is a partition of $n$, let $A^\lambda$ denote the irreducible representation of the symmetric group $S_n$ such that the Frobenius image of $\chi^{A^\lambda}$ is the Schur function $S_\lambda(x_1,\ldots,x_N)$ where $N>n$.

(a) Use the Murnaghnam-Nakayama rule to compute the values of the character $A^{(4,1)}$ on the conjugacy classes of $S_5$.

(b) Express $\chi^{A^{(1,4)}\downarrow^{S_5}_{S_3\times S_2}}$ as a sum of irreducible characters of $S_3\times S_2$.
Here $S_3\times S_2$ is the Young subgroup of $S_5$ consisting of all permutations $\sigma\in S_5$ such that
\[
\sigma(1),\sigma(2),\sigma(3)\in\{1,2,3\},\qquad \sigma(4),\sigma(5)\in\{4,5\}.
\]
:::


::: {.solution}
Write \(\chi=\chi^{(4,1)}\).

<1>1. The values of \(\chi\) on the conjugacy classes of \(S_5\), ordered by cycle type
\[
(1^5),\ (2,1^3),\ (2^2,1),\ (3,1^2),\ (3,2),\ (4,1),\ (5),
\]
are
\[
\boxed{4,\ 2,\ 0,\ 1,\ -1,\ 0,\ -1}.
\]
::: {.proof}
The Specht module \(S^{(4,1)}\) is the standard representation of \(S_5\), obtained from the permutation representation \(\mathbb C^5\) by removing the one-dimensional invariant line spanned by \(e_1+\cdots+e_5\). Hence for every \(\sigma\in S_5\),
\[
\chi^{(4,1)}(\sigma)=\#\operatorname{Fix}(\sigma)-1.
\]
The numbers of fixed points for the seven cycle types above are respectively
\[
5,\ 3,\ 1,\ 2,\ 0,\ 1,\ 0,
\]
which yields the displayed row.

This agrees with the Murnaghan--Nakayama rule: removing rim hooks from the hook diagram \((4,1)\) gives exactly the same signed contributions for each cycle type.
:::

<1>2. The restriction of \(S^{(4,1)}\) to the Young subgroup \(S_3\times S_2\) decomposes as
\[
\boxed{
S^{(4,1)}\!\downarrow_{S_3\times S_2}^{S_5}
\cong
(S^{(3)}\boxtimes S^{(2)})
\oplus
(S^{(2,1)}\boxtimes S^{(2)})
\oplus
(S^{(3)}\boxtimes S^{(1,1)}).
}
\]
::: {.proof}
Restrict first the permutation representation \(\mathbb C^5\). Under \(S_3\times S_2\), the first three basis vectors and the last two basis vectors span invariant subspaces, so
\[
\mathbb C^5\!\downarrow_{S_3\times S_2}
\cong
\mathbb C^3\boxtimes \mathbf 1
\oplus
\mathbf 1\boxtimes \mathbb C^2.
\]
The permutation modules decompose as
\[
\mathbb C^3\cong S^{(3)}\oplus S^{(2,1)},
\qquad
\mathbb C^2\cong S^{(2)}\oplus S^{(1,1)}.
\]
Therefore
\[
\mathbb C^5\!\downarrow_{S_3\times S_2}
\cong
2(S^{(3)}\boxtimes S^{(2)})
\oplus
(S^{(2,1)}\boxtimes S^{(2)})
\oplus
(S^{(3)}\boxtimes S^{(1,1)}).
\]
Finally,
\[
\mathbb C^5\cong S^{(5)}\oplus S^{(4,1)},
\]
and the restricted trivial representation \(S^{(5)}\) is one copy of \(S^{(3)}\boxtimes S^{(2)}\). Subtracting that copy gives the asserted decomposition.
:::
:::
