---
schema: qual/card@1
id: P-APAF21G
kind: problem
title: Character table of $S_4$ and decomposition of $\mathbb{C}[X]$ for $2$-subsets
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Write down the character table of the symmetric group $S_4$.
If we let
\[
X:=\{\text{all $2$-element subsets of }\{1,2,3,4\}\},
\]
then $X$ carries a natural permutation action of $S_4$.
Find the decomposition of $\mathbb{C}[X]$ into irreducibles.
:::

::: {.solution}

Order the conjugacy classes of $S_4$ by cycle type
\[
(1^4),\quad(2,1^2),\quad(2^2),\quad(3,1),\quad(4),
\]
with respective sizes
\[
1,6,3,8,6.
\]

::: pf

::: {.pf-step #trivial-and-sign-characters}
The trivial character and the sign character are
\[
\chi^{(4)}=(1,1,1,1,1),
\qquad
\chi^{(1^4)}=(1,-1,1,1,-1).
\]

::: pf-proof
The trivial character is identically $1$. The sign of a transposition and of a $4$-cycle is $-1$, while the identity, a product of two disjoint transpositions, and a $3$-cycle are even.
:::

:::

::: {.pf-step #standard-representation-character}
The standard $3$-dimensional representation has character
\[
\chi^{(3,1)}=(3,1,-1,0,-1).
\]

::: pf-proof
The permutation representation of $S_4$ on $\mathbb C^4$ has character equal to the number of fixed points of the permutation. Its values on the five classes are
\[
4,2,0,1,0.
\]
It decomposes as the trivial line spanned by $(1,1,1,1)$ plus the standard subspace
\[
\{(z_1,z_2,z_3,z_4):z_1+z_2+z_3+z_4=0\}.
\]
Subtracting the trivial character gives the displayed row.
:::

:::

::: pf-step
Tensoring the standard representation with sign gives
\[
\chi^{(2,1,1)}=(3,-1,-1,0,1).
\]

::: pf-proof
Tensoring by the one-dimensional sign representation multiplies character values pointwise by the sign. Multiply the row in step [](#standard-representation-character){.pf-ref} by the sign row in step [](#trivial-and-sign-characters){.pf-ref}.
:::

:::

::: {.pf-step #two-dimensional-irreducible-character}
The remaining $2$-dimensional irreducible character is
\[
\chi^{(2,2)}=(2,0,2,-1,0).
\]

::: pf-proof
Let $S_4$ act on the three partitions of $\{1,2,3,4\}$ into two unordered pairs:
\[
12|34,\qquad13|24,\qquad14|23.
\]
The resulting permutation character counts fixed pairings. The numbers of fixed pairings on the five conjugacy classes are
\[
3,1,3,0,1.
\]
Indeed, a transposition fixes only the pairing containing its transposed pair, a double transposition fixes all three pairings, a $3$-cycle fixes none, and a $4$-cycle fixes exactly the pairing of opposite points.

Subtracting the invariant constant line gives the character
\[
(2,0,2,-1,0).
\]
Its character norm is
\[
\frac1{24}\left(1\cdot2^2+6\cdot0^2+3\cdot2^2+8\cdot(-1)^2+6\cdot0^2\right)
=1,
\]
so this $2$-dimensional representation is irreducible.
:::

:::

::: {.pf-step #s4-character-table}
Therefore the complete character table of $S_4$ is
\[
\begin{array}{c|rrrrr}
& (1^4)&(2,1^2)&(2^2)&(3,1)&(4)\\
\text{class size}&1&6&3&8&6\\ \hline
\chi^{(4)}&1&1&1&1&1\\
\chi^{(3,1)}&3&1&-1&0&-1\\
\chi^{(2,2)}&2&0&2&-1&0\\
\chi^{(2,1,1)}&3&-1&-1&0&1\\
\chi^{(1^4)}&1&-1&1&1&-1
\end{array}.
\]

::: pf-proof
The five displayed characters are irreducible: the one-dimensional rows are irreducible, the standard representation is irreducible, its sign twist is irreducible, and step [](#two-dimensional-irreducible-character){.pf-ref} proves irreducibility of the $2$-dimensional row. Their degree squares sum to
\[
1^2+3^2+2^2+3^2+1^2=24=|S_4|,
\]
so they form the complete set of irreducible characters.
:::

:::

::: {.pf-step #permutation-character-of-2-subsets}
The permutation character of $\mathbb C[X]$, where $X$ is the set of $2$-element subsets, is
\[
\chi_X=(6,2,2,0,0).
\]

::: pf-proof
The character value is the number of $2$-subsets fixed setwise by a representative permutation. The identity fixes all $6$. A transposition fixes its own $2$-set and the complementary $2$-set, hence $2$. A double transposition fixes its two transposition-orbits, hence $2$. A $3$-cycle and a $4$-cycle fix no $2$-subset.
:::

:::

::: pf-step
The decomposition is
\[
\boxed{\mathbb C[X]\cong S^{(4)}\oplus S^{(3,1)}\oplus S^{(2,2)}.}
\]

::: pf-proof
Adding the corresponding character rows from step [](#s4-character-table){.pf-ref} gives
\[
(1,1,1,1,1)+(3,1,-1,0,-1)+(2,0,2,-1,0)
=(6,2,2,0,0),
\]
which is exactly the permutation character from step [](#permutation-character-of-2-subsets){.pf-ref}. Equality of characters over $\mathbb C$ implies isomorphism of representations.
:::

:::

:::

:::
