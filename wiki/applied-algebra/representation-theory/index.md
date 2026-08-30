---
title: Representation theory
order: 2
problems:
  topics:
  - Representation Theory
  - Character Theory
  - Permutations
---

# Representation theory

The same subject as [[Algebra/representations/index|the algebra qual's representations chapter]], asked in more detail: this paper expects character tables to be built, not just used.

## The framework

Maschke makes every complex representation of a finite group a sum of irreducibles, Schur makes the multiplicities inner products of characters, and together they give
\[
\size G = \sum_i d_i^2
,\]
with the number of irreducibles equal to the number of conjugacy classes.

## Building a character table

1. Count conjugacy classes; the table is square.
2. Write the trivial character, and the degree-one characters, which are the characters of $G/[G,G]$.
3. Use $\size G = \sum d_i^2$ to pin the remaining degrees.
4. Take the permutation character of an action, $\chi(g) = \size{\Fix(g)}$, and subtract the trivial character.
5. Finish with column orthogonality.

## What this paper adds

- **Induced and restricted representations,** with Frobenius reciprocity $\inner{\Ind_H^G \psi}{\chi}_G = \inner{\psi}{\Res^G_H\chi}_H$, which is the tool for building characters of a large group from a subgroup.
- **The symmetric group specifically:** irreducibles are indexed by partitions of $n$, characters are computed by the Murnaghan--Nakayama rule, and dimensions by the hook length formula.
  That connects directly to [[Applied_Algebra/symmetric-functions/index|symmetric functions]].
- **Real and quaternionic types,** detected by the Frobenius--Schur indicator.
