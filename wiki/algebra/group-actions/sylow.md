---
title: Sylow theory
order: 30
topics:
- Sylow Theory
- Sylow Theorems
- p-Groups
---

# Sylow theory

Throughout, $G$ is a finite group, $p$ is a prime, $\size G = p^a m$ with $p\notdivides m$, $\Syl_p(G)$ is the set of Sylow $p$-subgroups of $G$, and $n_p = \size{\Syl_p(G)}$.

[[D-7TQ2M]]

::: {.remark title="Intersections of Sylow subgroups"}
If $a=1$, distinct Sylow $p$-subgroups intersect trivially, so they contain exactly $n_p(p-1)$ elements of order $p$.
For $a>1$, two distinct Sylow $p$-subgroups can intersect nontrivially.
:::

[[L-DJKXL]]

## The Sylow theorems

### Existence

[[T-WRMBM]]

### Conjugacy

[[T-EF2MZ]]

### The number of Sylow subgroups

[[T-S5T5C]]

::: {.remark title="Where the conditions on $n_p$ come from"}
The equality $n_p = [G : N_G(P)]$ is orbit-stabilizer for the transitive conjugation action of $G$ on $\Syl_p(G)$.
The congruence $n_p\equiv1\pmod p$ follows from the conjugation action of $P$ on $\Syl_p(G)$: its only fixed point is $P$, and every other orbit has size divisible by $p$.
:::

## Applications

Arguments producing normal subgroups from Sylow counts are collected on [[algebra/group-actions/show-g-is-not-simple|Show $G$ is not simple]].

- **Classifying groups of a given order.** If $n_p = 1$, then $P\in\Syl_p(G)$ is normal, $\size{G/P} = m$ is coprime to $\size P$, and by the Schur--Zassenhaus theorem $P$ has a complement $H$, so $G \cong P\semidirect H$.

- **Induction on the order.** A normal Sylow subgroup $P$ gives the quotient $G/P$ of order $m < \size G$.

- **Nilpotence.** A finite group is [[D-53JVH|nilpotent]] if and only if every Sylow subgroup is normal, in which case it is the direct product of its Sylow subgroups.

## Exercises

[[E-K3OJW]]
