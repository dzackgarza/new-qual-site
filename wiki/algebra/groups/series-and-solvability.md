---
title: Series and solvability
order: 50
problems:
  topics:
  - Solvable Groups
  - Nilpotent Groups
---

# Series and solvability

[[D-KM2DV]]

[[D-5NV3N]]

[[D-FYX4I]]

[[FD-PLAEO]]

[[T-OSJ5S]]

[[D-T2NZ4]]

[[FD-2UWAQ]]

[[D-D7L4X]]

[[D-BGNME]]

[[D-XEDSI]]

[[D-W2QAA]]

::: {.remark title="The chain of implications"}
\[
\text{cyclic} \implies \text{abelian} \implies \text{nilpotent} \implies \text{solvable}
\]
with none reversing.
A finite group is nilpotent exactly when every Sylow subgroup is normal, equivalently when it is the direct product of its Sylow subgroups, so nilpotence is a Sylow statement and is checked by a Sylow count.

Solvability is what the [[algebra/galois-theory/cyclotomic-and-radical-extensions|Galois theory]] side needs, and $S_n$ is solvable exactly for $n\leq 4$.
:::

## Nilpotent groups

[[D-53JVH]]

> Moral: the adjoint map is nilpotent.

[[T-7PU33]]

[[T-4INET]]

[[T-GM7EB]]

[[T-OHEFT]]

::: {.proposition}
For $G$ a finite group, TFAE:

- $G$ is nilpotent

- Normalizers grow, i.e. if $H < G$ is proper then $H < N_G(H)$.

- Every Sylow-p subgroup is normal

- $G$ is the direct product of its Sylow p-subgroups

- Every maximal subgroup is normal

- $G$ has a terminating *Lower* Central Series

- $G$ has a terminating *Upper* Central Series
:::

::: {.fact}
\envlist

- Nilpotent groups satisfy the 2 out of 3 property.

- $G$ has normal subgroups of order $d$ for *every* $d$ dividing $\abs{G}$
:::

The characterization via normalizers is the most useful for computations: to check nilpotence, pick a proper subgroup $H$ and verify $H < N_G(H)$.
If normalizers always grow, the group is nilpotent.
This is a Sylow-theoretic condition — for finite groups, nilpotence is equivalent to every Sylow subgroup being normal, which is equivalent to $G$ being the direct product of its Sylow subgroups.

The lower central series $G = \gamma_1(G) \geq \gamma_2(G) \geq \cdots$ where $\gamma_{i+1}(G) = [\gamma_i(G), G]$ terminates at the trivial group iff $G$ is nilpotent.
The upper central series $Z_0(G) = 1 \leq Z_1(G) = Z(G) \leq \cdots$ terminates at $G$ iff $G$ is nilpotent.
The class of nilpotency is the length of either series.
