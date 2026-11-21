---
title: Characters
order: 20
topics:
- Character Theory
---

# Characters

Throughout, $G$ is a finite group and representations are finite-dimensional over $\CC$.

[[D-CTAKB]]

## Characters and their arithmetic

::: {.proposition}
Let $V$ and $W$ be finite-dimensional representations of $G$ over $\CC$, with characters $\chi_V$ and $\chi_W$.

- $\chi_V$ is a class function, since the trace is invariant under conjugation.

- $\chi_V(1) = \dim V$.

- $\chi_{V\oplus W} = \chi_V + \chi_W$ and $\chi_{V\tensor W} = \chi_V\chi_W$.
:::

::: {.proposition}
A finite-dimensional representation of $G$ over $\CC$ splits into irreducibles, so its character is a complete invariant of it once the multiplicities of the irreducible characters are read off.
:::

[[T-PIO2B]]

[[T-YHH3M]]

## Orthogonality

::: {.proposition}
The irreducible characters are orthonormal for the inner product of class functions, and the column form of the same relations determines the last entries of a character table.
:::

[[P-ZCY6S]]

## Building a character table

::: {.proposition}

1. The number of irreducible characters equals the number of conjugacy classes, so the character table is square.

2. The degree-one characters are the characters of the abelianization $G/[G,G]$, pulled back to $G$; they include the trivial character, and for $S_n$ the sign character.

3. The degrees $d_i$ of the irreducible characters divide $\size G$ and satisfy $\size G = \sum_i d_i^2$.

4. For an action of $G$ on a finite set $X$, the permutation character is $\chi(g) = \size{\Fix(g)}$; if the action is $2$-transitive, then $\chi-\chi_{\text{triv}}$ is irreducible.

5. The remaining entries are determined by [[P-ZCY6S|the column orthogonality relations]].
:::

[[P-MD6VX]]

[[P-UIXFV]]

[[P-ZVXTG]]

## Permutation characters

::: {.remark title="Permutation characters and Burnside's lemma"}
For the permutation character $\chi(g) = \size{\Fix(g)}$ of an action on $X$, Burnside's lemma states that the number of orbits is $\inner{\chi}{\chi_{\text{triv}}}$; see [[algebra/group-actions/the-class-equation|The class equation]].
:::

[[C-HE5SL]]
