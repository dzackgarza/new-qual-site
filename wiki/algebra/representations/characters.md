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

The character is constant on conjugacy classes, its value at the identity is the degree, and it is additive over direct sums and multiplicative over tensor products.

- $\chi_V$ is a class function, since the trace is invariant under conjugation.

- $\chi_V(1) = \dim V$.

- $\chi_{V\oplus W} = \chi_V + \chi_W$ and $\chi_{V\tensor W} = \chi_V\chi_W$.

Because a representation of a finite group splits into irreducibles, the character is a complete invariant once the multiplicities are read off it.

[[T-PIO2B]]

[[T-YHH3M]]

## Orthogonality

The orthogonality relations are the statement that the irreducible characters are orthonormal for the inner product of class functions, and the column form is what determines the last entries of a table.

[[P-ZCY6S]]

## Building a character table

1. The number of irreducible characters equals the number of conjugacy classes, so the character table is square.

2. The degree-one characters are the characters of the abelianization $G/[G,G]$, pulled back to $G$; they include the trivial character, and for $S_n$ the sign character.

3. The degrees $d_i$ of the irreducible characters divide $\size G$ and satisfy $\size G = \sum_i d_i^2$.

4. For an action of $G$ on a finite set $X$, the permutation character is $\chi(g) = \size{\Fix(g)}$; if the action is $2$-transitive, then $\chi-\chi_{\text{triv}}$ is irreducible.

5. The remaining entries are determined by the column orthogonality relations of [[P-ZCY6S]].

[[P-MD6VX]]

[[P-UIXFV]]

[[P-ZVXTG]]

## Permutation characters

::: {.remark title="Permutation characters and Burnside's lemma"}
For the permutation character $\chi(g) = \size{\Fix(g)}$ of an action on $X$, Burnside's lemma states that the number of orbits is $\inner{\chi}{\chi_{\text{triv}}}$; see [[algebra/group-actions/the-class-equation|The class equation]].
:::

[[C-HE5SL]]
