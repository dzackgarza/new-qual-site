---
title: Sylow theory
order: 30
problems:
  topics:
  - Sylow Theory
  - Sylow Theorems
  - p-Groups
---

# Sylow theory

Sylow is where the counting arguments of this chapter are pointed at a specific question: which subgroups of prime power order exist, how many, and how they sit relative to each other.
It is filed here rather than as a chapter of its own because all three statements are conjugation counts.

:::{.remark title="Useful facts"}
\envlist

- Counting contributions to $\size G$ from $\Syl_p(G)$: writing $\size G = p^k m$ so that $\size{S_p} = p^k$, and using that every element of order $p$ lies in some $S_p$, one gets at least $n_p(\ell - 1)$ for some constant $\ell > 1$.

  - **Warning**: every $S_p$ is the same size, so it is tempting to take $\ell \da \size{S_p} = p^k$.
    That only works if the $S_p$ intersect trivially, for instance if $k=1$.
    Otherwise the best available without more information is $\ell = p$, meaning the $S_p$ intersect trivially or in subgroups of order $p$.

  - **Warning**: this is not quite a count of elements of order $p$, since elements of $S_p$ can have order $p^{k'}$ for $k' \leq k$.

- When counting: leave the identity out of every calculation and add it back as a $+1$ at the end.

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

The systematic use is [[Algebra/group-actions/show-g-is-not-simple|Show $G$ is not simple]], where a Sylow count is the first thing to try.
The other standard uses:

- **Classifying groups of a given order.** Once $n_p = 1$ for some $p$, that Sylow is normal and $G$ is an extension, usually a semidirect product, of the two Sylow subgroups.

- **Finding a normal subgroup to quotient by**, reducing to a smaller order.

- **Proving nilpotence.** A finite group is nilpotent exactly when every Sylow subgroup is normal, in which case $G$ is their direct product.

## Exercises

[[E-K3OJW]]
