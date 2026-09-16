---
title: Sylow theory
order: 30
topics:
- Sylow Theory
- Sylow Theorems
- p-Groups
---

# Sylow theory

Throughout, $G$ is a finite group, $p$ is a prime, $\size G = p^k m$ with $p\notdivides m$, $\Syl_p(G)$ is the set of Sylow $p$-subgroups of $G$, and $n_p = \size{\Syl_p(G)}$.

[[D-7TQ2M]]

::: {.remark title="Counting Sylow subgroups"}
\envlist

- $n_p\divides m$ and $n_p\equiv1\pmod p$.
- A Sylow $p$-subgroup is normal if and only if $n_p=1$.
- If $k=1$, distinct Sylow $p$-subgroups intersect trivially, so they contain exactly $n_p(p-1)$ elements of order $p$. For $k>1$, two distinct Sylow $p$-subgroups can intersect nontrivially.
:::

[[L-354HC]]

## The Sylow theorems

[[FT-ZENUU]]

### Existence

[[T-WRMBM]]

::: {.slogan}
For every $\beta \leq k$, $G$ has a subgroup of order $p^{\beta}$; in particular Sylow $p$-subgroups exist.
Every $p$-subgroup of $G$ is contained in a Sylow $p$-subgroup.
:::

### Conjugacy

[[T-EF2MZ]]

::: {.corollary}
A Sylow $p$-subgroup $P$ is normal if and only if $n_p = 1$.
:::

::: {.proof}
Every Sylow $p$-subgroup is conjugate to $P$, so $\Syl_p(G) = \ts{gPg\inv \st g\in G}$, and this set is $\ts P$ if and only if $P\normal G$.
:::

### The number of Sylow subgroups

[[T-S5T5C]]

::: {.remark title="The conditions on $n_p$"}
For $P\in\Syl_p(G)$,
$$
n_p \equiv 1 \pmod p, \qquad n_p \divides m, \qquad n_p = [G : N_G(P)].
$$
The equality $n_p = [G : N_G(P)]$ is orbit-stabilizer for the transitive conjugation action of $G$ on $\Syl_p(G)$, and it expresses $n_p$ as the index of a subgroup.
The congruence follows from the conjugation action of $P$ on $\Syl_p(G)$: its only fixed point is $P$, and every other orbit has size divisible by $p$.
:::

## Applications

Arguments producing normal subgroups from Sylow counts are collected on [[algebra/group-actions/show-g-is-not-simple|Show $G$ is not simple]].

- **Classifying groups of a given order.** If $n_p = 1$, then $P\in\Syl_p(G)$ is normal, $\size{G/P} = m$ is coprime to $\size P$, and by the Schur--Zassenhaus theorem $P$ has a complement $H$, so $G \cong P\semidirect H$.

- **Induction on the order.** A normal Sylow subgroup $P$ gives the quotient $G/P$ of order $m < \size G$.

- **Nilpotence.** A finite group is [[D-53JVH|nilpotent]] if and only if every Sylow subgroup is normal, in which case it is the direct product of its Sylow subgroups.

## Exercises

[[E-K3OJW]]
