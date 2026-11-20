---
title: Representation theory
order: 2
topics:
- Representation Theory
- Character Theory
- Permutations
---

# Representation theory

The representation theory of finite groups is also treated on [[algebra/representations/index|Representations]]; this page adds induced representations, the representations of the symmetric group, and the Frobenius--Schur indicator.

## Maschke and Schur

By [[T-PIO2B|Maschke's theorem]], every finite-dimensional complex representation of a finite group $G$ is a direct sum of irreducible representations, and by [[T-YHH3M|Schur's lemma]] and the orthogonality relations it implies, the multiplicity of an irreducible representation in a representation with character $\chi$ is the inner product of $\chi$ with the irreducible character.

If $d_1,\ldots,d_r$ are the dimensions of the irreducible representations, then
$$
\size G = \sum_i d_i^2,
$$
because the regular representation is the direct sum of $d_i$ copies of the $i$th irreducible representation, so its character at the identity is $\sum_i d_i^2$, and that character at the identity is $\size G$.
The number $r$ is the number of conjugacy classes of $G$, since the class functions have the irreducible characters as an orthonormal basis and the class functions are spanned by the indicator functions of the classes.

## Building a character table

The table is square, its rows the irreducible characters and its columns the conjugacy classes.

The degree-one characters are the characters of $G/[G,G]$: a character of degree one is a homomorphism $G\to\CC^\times$, and $\CC^\times$ is abelian, so it factors through the abelianization.

The degrees satisfy $\size G = \sum_i d_i^2$, which determines the last degree once the others are known when only one is missing.

For an action of $G$ on a finite set, the permutation character is $\chi(g) = \size{\Fix(g)}$, since the permutation matrix of $g$ has a $1$ on the diagonal exactly at the fixed points.
If the action is $2$-transitive then $\inner{\chi}{\chi} = 2$, as Burnside's lemma counts the orbits of $G$ on $X\times X$: the diagonal and its complement, so $\chi - \chi_{\text{triv}}$ is irreducible.

The remaining entries are then determined by the column orthogonality relations, $\sum_\chi \chi(g)\overline{\chi(h)} = \size{C_G(g)}$ for $g$ and $h$ conjugate and $0$ otherwise.

## Induced representations, the symmetric group, and indicators

For $H\leq G$, a character $\psi$ of $H$, and a character $\chi$ of $G$, [[P-SJBKE|Frobenius reciprocity]], the adjunction $\Hom_{R[G]}(\Indcat_H^GV,W)\cong\Hom_{R[H]}(V,\Res_H^GW)$, gives the character form
$$
\inner{\Indcat_H^G \psi}{\chi}_G = \inner{\psi}{\Res^G_H\chi}_H,
$$
since by [[T-YHH3M|Schur's lemma]] and the orthogonality relations the inner product of a character with an irreducible character is the dimension of the corresponding Hom space, and both sides are linear in $\chi$,
so characters of $G$ are obtained by inducing characters of subgroups and decomposing the result.

The irreducible representations of $S_n$ are indexed by the partitions of $n$, their characters are computed by the Murnaghan--Nakayama rule, and their dimensions by [[T-HOOK|the hook length formula]]; see [[applied-algebra/symmetric-functions/index|Symmetric functions]].

For an irreducible character $\chi$ of $G$, [[T-FSIND|the Frobenius--Schur theorem]] sorts the representation into one of three types: $\chi$ is not real-valued, or it is real-valued and the representation is realizable over $\RR$, or it is real-valued and not realizable over $\RR$, in which case its real form has the quaternions as commuting algebra.
