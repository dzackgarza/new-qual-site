---
title: Sylow theory
order: 30
topics:
- Sylow Theory
- Sylow Theorems
- p-Groups
---

# Sylow theory

The Sylow theorems turn the factorization $|G|=p^km$ with $p\nmid m$ into existence, conjugacy, and counting information for subgroups of order $p^k$.

:::{.remark title="Useful facts"}
\envlist

- If $n_p$ is the number of Sylow $p$-subgroups, then $n_p\mid m$ and $n_p\equiv1\pmod p$.
- A Sylow $p$-subgroup is normal exactly when it is unique, i.e. exactly when $n_p=1$.
- If $k=1$, distinct Sylow $p$-subgroups have trivial intersection, so their nonidentity elements contribute exactly $n_p(p-1)$ distinct elements. For $k>1$, intersections must be analyzed before using such an element count.

:::

:::{.definition}
A **Sylow $p\dash$subgroup** of $G$ is a subgroup of order $p^k$, where $\size G = p^k m$ with $p \nmid m$: a $p\dash$subgroup of maximal possible order.

:::

[[L-354HC]]

## The statements

:::{.remark title="Setup"}
Assume $\size G = p^k m$ with $(p,m)=1$, write $S_p$ for a Sylow $p\dash$subgroup, and $n_p$ for the number of them.

:::

[[FT-ZENUU]]

### Sylow 1: existence

[[T-WRMBM]]

:::{.slogan}
Sylow $p\dash$subgroups exist for every $p$ dividing $\size G$, and more: subgroups of order $p^{\beta}$ exist for every $\beta \leq k$.
Every $p\dash$subgroup is contained in a Sylow $p\dash$subgroup.

:::

### Sylow 2: conjugacy

[[T-EF2MZ]]

:::{.corollary}
$n_p = 1$ if and only if the Sylow $p\dash$subgroup is normal, since conjugation permutes the Sylow $p\dash$subgroups transitively and a single one has nowhere to go.

:::

### Sylow 3: the numerical constraints

[[T-S5T5C]]

:::{.remark title="The two constraints, and where they come from"}
\[
n_p \equiv 1 \pmod p, \qquad n_p \divides m, \qquad n_p = [G : N_G(S_p)]
.\]
The last is orbit-stabilizer for the conjugation action on $\Syl_p(G)$, and it is the form that turns a Sylow count into a statement about an index.
The congruence comes from letting a fixed $S_p$ act on $\Syl_p(G)$: it fixes only itself, and all other orbits have size divisible by $p$.

:::

## Using it

The systematic use is [[algebra/group-actions/show-g-is-not-simple|Show $G$ is not simple]], where a Sylow count is the first thing to try.
The other standard uses:

- **Classifying groups of a given order.** Once $n_p = 1$ for some $p$, that Sylow is normal and $G$ is an extension, usually a semidirect product, of the two Sylow subgroups.

- **Finding a normal subgroup to quotient by**, reducing to a smaller order.

- **Proving nilpotence.** A finite group is nilpotent exactly when every Sylow subgroup is normal, in which case $G$ is their direct product.

## Exercises

[[E-K3OJW]]
