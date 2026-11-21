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

::: {.fact title="A subgroup containing $S$ contains $\generators S$"}
If $S\subseteq H$, then $\generators S\leq H$: the subgroup $\generators S$ is the intersection of all the subgroups of $G$ that contain $S$, and $H$ is one of them.
:::

[[D-IQ4OX]]

[[PR-U5CHT]]

[[D-D36IY]]

[[E-MSDCC]]

## Order and presentations

Lagrange's theorem applies to an element through the cyclic subgroup it generates.

[[D-ZTPHF]]

[[P-SVM3O]]

[[D-V6UJ7]]

## Commutators and the derived series

::: {.fact title="The commutator measures noncommutation"}
$[x,y]=x y \inverseof{x} \inverseof{y}$, so $[x,y]=e$ exactly when $xy=yx$, and the commutator is trivial on every pair exactly when $G$ is abelian.
:::

[[D-BQ4BQ]]

[[D-W2QAA]]

[[T-QPMGT]]

## Conjugacy

::: {.fact title="Conjugation preserves order"}
For $g\in G$, $c_g\colon x\mapsto gx\inverseof{g}$ is an automorphism with inverse $c_{\inverseof{g}}$, so conjugate elements have the same order.
:::

[[D-HLDEY]]

[[D-ES7MP]]

[[E-47X7Y]]

[[P-ALGS08A]]

## Normal subgroups

Normality is weaker than being characteristic: see [[algebra/groups/characteristic-subgroups|Characteristic subgroups]].

[[D-EKE4Q]]

[[E-BSGSM]]

[[P-67U4W]]

[[P-AMD-5H2CPVWT]]

[[T-I5N43]]

## Centralizers, normalizers, and the center

[[D-PX64W]]

[[FD-HRCTL]]

[[D-NK7G7]]

[[E-AMD-YBSKHIZ3]]

[[P-JUZ6G]]

[[E-O73XQ]]

## Cosets and the index

::: {.fact title="All cosets of $H$ have $\size H$ elements"}
Left multiplication by $g$ is a bijection $H\to gH$ with inverse left multiplication by $\inverseof{g}$, so $\size{gH}=\size H$, and $G$ is the disjoint union of the $\size{G}/\size{H}$ left cosets when $G$ is finite.
:::

[[FD-JI2RH]]

[[FD-BWVRA]]

[[PR-VUKHO]]

[[T-5KGVV]]

[[D-VJGH5]]

[[PR-SF6ZE]]

[[PR-YY3JG]]

[[T-WR7CD]]

Lagrange's theorem is the tower law with $K$ trivial.

[[E-NNTQB]]

## Exercises

[[E-BAOST]]
