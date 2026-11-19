---
title: Basics
order: 10
topics:
- Groups
- Group Theory
- Subgroups
- Normal Subgroups
- Homomorphisms
---

# Basics

Throughout, $G$ is a group with identity $e$, and $H$ and $K$ are subgroups of $G$.

## Subgroups

Recall that $\generators S$ is the smallest subgroup containing $S$ ([[D-D36IY]]), so an inclusion $\generators S\leq H$ is checked on $S$ alone, and that membership in a subset is decided by one closure condition rather than three ([[PR-U5CHT]]).

[[D-IQ4OX]]

[[PR-U5CHT]]

[[D-D36IY]]

[[E-MSDCC]]

## Order and presentations

The order of an element is the order of the cyclic subgroup it generates, which is why Lagrange's theorem applies to it.

[[D-ZTPHF]]

[[P-SVM3O]]

[[D-V6UJ7]]

## Commutators and the derived series

$[x,y]=e$ exactly when $x$ and $y$ commute, and iterating the commutator subgroup gives the [[D-W2QAA|derived series]].

[[D-BQ4BQ]]

[[D-W2QAA]]

[[T-QPMGT]]

## Conjugacy

Conjugation by $g$ is an automorphism of $G$, so conjugate elements have the same order.

[[D-HLDEY]]

[[D-ES7MP]]

[[E-47X7Y]]

[[P-ALGS08A]]

## Normal subgroups

Normality is the condition under which the cosets of $H$ carry a group structure, and it is weaker than being characteristic: see [[algebra/groups/characteristic-subgroups|Characteristic subgroups]].

[[D-EKE4Q]]

[[E-BSGSM]]

[[P-67U4W]]

[[P-AMD-5H2CPVWT]]

[[T-I5N43]]

## Centralizers, normalizers, and the center

The centralizer of a subset fixes its elements under conjugation and the normalizer permutes them, so $C_G(H)\leq N_G(H)$; the center is the centralizer of $G$, and also the intersection of the centralizers of its elements.

[[D-PX64W]]

[[FD-HRCTL]]

[[D-NK7G7]]

[[E-AMD-YBSKHIZ3]]

[[P-JUZ6G]]

[[E-O73XQ]]

## Cosets and the index

A map of sets is injective exactly when it has a left inverse and surjective exactly when it has a right inverse; the coset $gH$ is the image of $H$ under the bijection $h\mapsto gh$, so all cosets of $H$ have $\size{H}$ elements and the index counts them.

[[FD-JI2RH]]

[[FD-BWVRA]]

[[PR-VUKHO]]

[[T-5KGVV]]

[[D-VJGH5]]

[[PR-SF6ZE]]

[[PR-YY3JG]]

[[T-WR7CD]]

The tower law makes the index multiplicative down a chain of subgroups, and Lagrange's theorem is the tower law with $K$ trivial.

[[E-NNTQB]]

## Exercises

[[E-BAOST]]
