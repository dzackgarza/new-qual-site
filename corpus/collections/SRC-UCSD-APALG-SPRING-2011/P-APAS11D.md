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
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-31
  note: The exam prints A^(1,4); under its own decreasing convention this is A^(4,1).
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2, with (a)-(c) as steps and (d) as the QED step.
    Re-checked the numbers: the column of $\chi^\lambda$ at cycle type $(3,2)$ is
    $1,-1,1,0,-1,1,-1$, whose squares sum to $6$, the centraliser order $3\cdot2$, as column
    orthogonality requires; the $S_3$ and $S_2$ tables are the standard ones and their Kronecker
    products give the six rows listed, with $\sum(\dim)^2=6\cdot2=12$; $A^{(4,1)}$ is the standard
    representation with character $\Fix-1$, giving $4,2,0,1,-1,0,-1$ on the seven cycle types; and
    the restriction of $\CC^5$ is $(1\oplus\rho)\boxtimes1\oplus1\boxtimes(1\oplus\varepsilon_2)$,
    from which one copy of $1\boxtimes1$ is removed, matching dimensions $1+2+1=4$. Added: the
    column-orthogonality check in (a), the dimension check in (b), and the fixed-point counts in (c),
    none of which the prose gave. Presentation repairs: `\mathrm{sign}` and `\operatorname{Fix}` are
    written `\sgn` and `\Fix`, the vocabulary macros (STYLE-03/04). The collection's provenance is the
    Spring 2011 examination paper, so no retained solution set covers the problem.
---

::: {.problem}
If $\lambda=(\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_k)$ is a partition of $n$, let $A^\lambda$ denote the irreducible representation of the symmetric group $S_n$ such that the Frobenius image of $\chi^{A^\lambda}=\chi^\lambda$ is the Schur function $S_\lambda(x_1,\ldots,x_N)$ where $N>n$.

(a) Use the Murnaghan–Nakayama rule to compute the value of the irreducible characters of $S_5$ at the conjugacy class indexed by the partition $(2,3)$.

(b) Find the character table for $S_3\times S_2$ where $S_3\times S_2$ is the Young subgroup of $S_5$ consisting of all permutations $\sigma\in S_5$ such that
$$
\sigma(1),\sigma(2),\sigma(3)\in\{1,2,3\},\qquad
\sigma(4),\sigma(5)\in\{4,5\}.
$$

(c) Find the values of the character of $A^{(4,1)}$ on the conjugacy classes of $S_5$.

(d) Decompose $A^{(4,1)}\downarrow_{S_3\times S_2}^{S_5}$ as a sum of irreducible representations of $S_3\times S_2$.
:::

::: {.solution}
The collection's provenance is the examination paper, so no retained solution set covers the problem; the computation is the card's own, checked against the Murnaghan--Nakayama rule and the tables of $S_3$ and $S_2$. The paper prints $A^{(1,4)}$; under its own convention that partitions are weakly decreasing this is $A^{(4,1)}$, the label used below.

::: pf

::: {.pf-step #part-a}
(a) On the class of cycle type $(3,2)$ the irreducible characters of $S_5$ take the values
$$
\begin{array}{c|rrrrrrr}
\lambda &(5)&(4,1)&(3,2)&(3,1,1)&(2,2,1)&(2,1,1,1)&(1^5)\\ \hline
\chi^\lambda_{(3,2)}&1&-1&1&0&-1&1&-1
\end{array}
$$

::: pf-proof
The Murnaghan--Nakayama rule computes $\chi^\lambda_\mu$ as the signed sum, over all ways of removing border strips of lengths $\mu_1,\mu_2,\ldots$ from the diagram of $\lambda$, of $(-1)^{\text{height}}$. For $\lambda=(4,1)$ and $\mu=(3,2)$ the only admissible removal is a strip of length $3$ from the first row followed by one of length $2$ spanning the two rows, of total height $1$, giving $-1$. The other rows are computed identically: $(5)$ and $(1^5)$ give the trivial and sign values $1$ and $-1$; $(4,1)$, $(2,2,1)$ and $(2,1,1,1)=(1^5)\otimes\sgn$ give $-1,-1,1$; $(3,1,1)$ and $(3,2)$ give $0$ and $1$. As a check, the sum of squares down the column is $1+1+1+0+1+1+1=6$, the order of the centraliser of a permutation of cycle type $(3,2)$, which is $3\cdot2$; column orthogonality requires exactly this.
:::

:::

::: {.pf-step #part-b}
(b) The character table of $S_3\times S_2$ on the six classes $(1,1)$, $((12),1)$, $((123),1)$, $(1,(45))$, $((12),(45))$, $((123),(45))$ is
$$
\begin{array}{c|rrrrrr}
1\boxtimes1&1&1&1&1&1&1\\
\varepsilon_3\boxtimes1&1&-1&1&1&-1&1\\
\rho\boxtimes1&2&0&-1&2&0&-1\\
1\boxtimes\varepsilon_2&1&1&1&-1&-1&-1\\
\varepsilon_3\boxtimes\varepsilon_2&1&-1&1&-1&1&-1\\
\rho\boxtimes\varepsilon_2&2&0&-1&-2&0&1
\end{array}
$$

::: pf-proof
The irreducible characters of $S_3$ are $1,\varepsilon_3,\rho$ with values $1,1,2$ at $1$; $1,-1,0$ at $(12)$; and $1,1,-1$ at $(123)$; those of $S_2$ are $1,\varepsilon_2$ with values $1,1$ at $1$ and $1,-1$ at $(45)$. The irreducible representations of a direct product are exactly the external tensor products $\alpha\boxtimes\beta$, with character $(\alpha\boxtimes\beta)(g,h)=\alpha(g)\beta(h)$, so the table is the Kronecker product of the two, six rows, and the entries are the products read off class by class. The six rows have the orthogonality relations of a table of six irreducible characters of a group of order $6\cdot2=12$, since $1^2+1^2+2^2=6$ and $1^2+1^2=2$ multiply to $12$.
:::

:::

::: {.pf-step #part-c}
(c) $A^{(4,1)}$ is the standard representation, and $\chi^{(4,1)}(\sigma)=\#\Fix(\sigma)-1$; on the cycle types $(1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)$ the values are $4,2,0,1,-1,0,-1$.

::: pf-proof
The permutation representation of $S_5$ on $\CC^5$ splits as the trivial representation spanned by the all-ones vector together with its orthogonal complement, and that complement is the irreducible representation indexed by the partition $(4,1)$; its character is the permutation character $\#\Fix$ minus the trivial character. A permutation of $S_5$ fixes a basis vector exactly when the corresponding point is a fixed point, which gives the count: a $5$-cycle or a $(3,2)$-type permutation fixes nothing, a transposition or a $(4,1)$-type fixes one point, a $(2,2,1)$ fixes one, a $(3,1,1)$ fixes two, a $(2,1,1,1)$ fixes three, and the identity fixes five. Subtracting $1$ gives the listed values.
:::

:::

::: {.pf-step}
(d) $\restrictionof{A^{(4,1)}}{S_3\times S_2}\cong(1\boxtimes1)\oplus(\rho\boxtimes1)\oplus(1\boxtimes\varepsilon_2)$.

::: pf-proof
Restricting the permutation module $\CC^5$ to the Young subgroup, the first three letters give the permutation module of $S_3$, which is $1\oplus\rho$, and the last two give that of $S_2$, which is $1\oplus\varepsilon_2$; so $\restrictionof{\CC^5}{S_3\times S_2}\cong(1\oplus\rho)\boxtimes1\oplus1\boxtimes(1\oplus\varepsilon_2)$. The standard representation is $\CC^5$ with one copy of the trivial representation removed, and the trivial representation of the subgroup is $1\boxtimes1$, which occurs once in that restriction; removing it leaves $(1\boxtimes1)\oplus(\rho\boxtimes1)\oplus(1\boxtimes\varepsilon_2)$. The dimensions $1+2+1=4$ equal $\dim A^{(4,1)}=4$, so this is the complete decomposition. Parts (a), (b) and (c) are steps [](#part-a){.pf-ref}, [](#part-b){.pf-ref} and [](#part-c){.pf-ref}.
:::

:::

:::
:::
