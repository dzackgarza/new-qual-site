---
title: Representation theory
order: 2
topics:
- Representation Theory
- Character Theory
- Permutations
---

# Representation theory

The representation theory of finite groups is also treated on [[algebra/representations/index|Representations]]; this page adds induced representations, representations of the symmetric group, and the Frobenius--Schur indicator.

## Maschke and Schur

By [[T-PIO2B|Maschke's theorem]], every finite-dimensional complex representation of a finite group $G$ is a direct sum of irreducible representations, and by [[T-YHH3M|Schur's lemma]] the multiplicities are inner products of characters.
If $d_1,\ldots,d_r$ are the dimensions of the irreducible representations, then
$$
\size G = \sum_i d_i^2,
$$
and $r$ is the number of conjugacy classes of $G$.

## Building a character table

1. The number of irreducible characters equals the number of conjugacy classes, so the table is square.

2. The degree-one characters are the characters of $G/[G,G]$; they include the trivial character.

3. The degrees satisfy $\size G = \sum_i d_i^2$ and divide $\size G$.

4. For an action of $G$ on a finite set, the permutation character is $\chi(g) = \size{\Fix(g)}$; if the action is $2$-transitive, $\chi-\chi_{\text{triv}}$ is irreducible.

5. The remaining entries are determined by the column orthogonality relations.

## Induced representations, the symmetric group, and indicators

- **Induced and restricted representations.** For $H\le G$, a character $\psi$ of $H$, and a character $\chi$ of $G$, Frobenius reciprocity gives $\inner{\Ind_H^G \psi}{\chi}_G = \inner{\psi}{\Res^G_H\chi}_H$; characters of $G$ are obtained by inducing characters of subgroups and decomposing.

- **The symmetric group.** The irreducible representations of $S_n$ are indexed by the partitions of $n$, their characters are computed by the Murnaghan--Nakayama rule, and their dimensions by the hook length formula; see [[applied-algebra/symmetric-functions/index|Symmetric functions]].

- **Real and quaternionic representations.** The Frobenius--Schur indicator ${1\over\size G}\sum_{g\in G}\chi(g^2)$ of an irreducible character $\chi$ is $1$, $0$, or $-1$ according as the representation is realizable over $\RR$, has a non-real character, or is quaternionic.
