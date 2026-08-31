---
schema: qual/card@1
id: P-APAS13F
kind: problem
title: Character $\chi^{(1,2^2)}$ on $S_5$; character table of $S_3\times S_2$; restriction
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
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Suppose that $\lambda=(\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_k)$ is a partition of $n$.
Then $A^\lambda$ denotes the irreducible representation of the symmetric group $S_n$ such that the Frobenius image of $\chi^{A^\lambda}=\chi^\lambda$ is the Schur function $S_\lambda(x_1,\ldots,x_N)$ where $N>n$, and $S_{\lambda_1}\times\cdots\times S_{\lambda_k}$ denotes the Young subgroup of $S_n$ corresponding to $\lambda$.

(a) Compute the values of the character $\chi^{(1,2^2)}$ on the conjugacy classes of $S_5$.

(b) Find the character table of $S_3\times S_2$.

(c) Decompose $A^{(1,2^2)}\downarrow_{S_3\times S_2}^{S_5}$ as a sum of irreducible characters of $S_3\times S_2$.
:::

::: {.solution}
**Part (a).**

<1>1. The conjugacy classes of $S_5$ are indexed by cycle types $1^5, 2\cdot 1^3, 2^2\cdot 1, 3\cdot 1^2, 3\cdot 2, 4\cdot 1, 5$, with sizes $1, 10, 15, 20, 20, 30, 24$.
::: {.proof}
standard count of permutations by cycle type.
:::

<1>2. The values of $\chi^{(2,2,1)}$ on these classes are
$$\chi^{(2,2,1)} = (5,\ -1,\ 1,\ -1,\ -1,\ 1,\ 0).$$
::: {.proof}
computed by the Murnaghan–Nakayama rule (or the hook-length formula for the degree $5$ and the standard character table of $S_5$).
:::

<1>3. Verification: $\sum_{\mu} |C_\mu|\, \chi^{(2,2,1)}(\mu)^2 = 25 + 10 + 15 + 20 + 20 + 30 + 0 = 120 = |S_5|$.
::: {.proof}
first orthogonality relation, confirming <1>2.
:::

**Part (b).**

<1>1. The character table of $S_3$ is
$$\begin{array}{c|ccc}
& 1^3 & 2\cdot 1 & 3 \\ \hline
(3) & 1 & 1 & 1 \\
(2,1) & 2 & 0 & -1 \\
(1^3) & 1 & -1 & 1
\end{array}$$
and of $S_2$ is
$$\begin{array}{c|cc}
& 1^2 & 2 \\ \hline
(2) & 1 & 1 \\
(1,1) & 1 & -1
\end{array}.$$
::: {.proof}
standard character tables.
:::

<1>2. The irreps of $S_3 \times S_2$ are the tensor products $\chi^{\nu} \otimes \chi^{\rho}$, giving the character table
$$\begin{array}{c|cccccc}
& (1^3,1^2) & (2\cdot1,1^2) & (3,1^2) & (1^3,2) & (2\cdot1,2) & (3,2) \\ \hline
(3)\otimes(2) & 1 & 1 & 1 & 1 & 1 & 1 \\
(3)\otimes(1,1) & 1 & 1 & 1 & -1 & -1 & -1 \\
(2,1)\otimes(2) & 2 & 0 & -1 & 2 & 0 & -1 \\
(2,1)\otimes(1,1) & 2 & 0 & -1 & -2 & 0 & 1 \\
(1^3)\otimes(2) & 1 & -1 & 1 & 1 & -1 & 1 \\
(1^3)\otimes(1,1) & 1 & -1 & 1 & -1 & 1 & -1
\end{array}.$$
::: {.proof}
the character of a tensor product is the product of the characters.
:::

**Part (c).**

<1>1. The Young subgroup $S_3 \times S_2 \le S_5$ embeds with $S_3$ acting on $\{1,2,3\}$ and $S_2$ on $\{4,5\}$.
::: {.proof}
definition of the Young subgroup for $\lambda = (3,2)$.
:::

<1>2. The restriction of $\chi^{(2,2,1)}$ to $S_3 \times S_2$ has values
$$(5,\ -1,\ -1,\ -1,\ 1,\ -1)$$
on the six classes of <1>2.
::: {.proof}
evaluate <1>2 on the embedded classes: identity $\mapsto 1^5$ (value $5$); a transposition in $S_3$ or in $S_2$ $\mapsto 2\cdot 1^3$ (value $-1$); a $3$-cycle $\mapsto 3\cdot 1^2$ (value $-1$); a transposition in $S_3$ times one in $S_2$ $\mapsto 2^2\cdot 1$ (value $1$); a $3$-cycle times a transposition $\mapsto 3\cdot 2$ (value $-1$).
:::

<1>3. Decomposing <1>2 against the table of <1>2 gives
$$A^{(2,2,1)}\downarrow_{S_3\times S_2}^{S_5} = \left(A^{(2,1)} \boxtimes A^{(2)}\right) \oplus \left(A^{(2,1)} \boxtimes A^{(1,1)}\right) \oplus \left(A^{(1,1,1)} \boxtimes A^{(1,1)}\right).$$
::: {.proof}
the Littlewood–Richardson rule (equivalently, solving the linear system for the multiplicities); the multiplicities are $1$ for $(2,1)\otimes(2)$, $(2,1)\otimes(1,1)$, and $(1^3)\otimes(1,1)$, and $0$ otherwise.
:::

<1>4. Dimension check: $2\cdot 1 + 2\cdot 1 + 1\cdot 1 = 5 = \dim A^{(2,2,1)}$.
::: {.proof}
<1>3 and the hook-length formula.
:::

<1>5. Q.E.D.
::: {.proof}
<1>2 (part (a)), <1>2 (part (b)), and <1>3 (part (c)).
:::
:::
