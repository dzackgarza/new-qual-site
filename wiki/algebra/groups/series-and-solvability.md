---
title: Series and solvability
order: 50
topics:
- Solvable Groups
- Nilpotent Groups
---

# Series and solvability

## Normal and composition series

A [[D-FYX4I|composition series]] of $G$ is a chain $1=G_0\normal G_1\normal\cdots\normal G_n=G$ whose factors $G_{i+1}/G_i$ are [[D-T2NZ4|simple groups]].
By the Jordan--Hölder theorem, any two composition series of a finite group have the same length and the same composition factors, counted with multiplicity and up to isomorphism.

[[D-KM2DV]]

[[D-5NV3N]]

[[D-FYX4I]]

[[FD-PLAEO]]

[[T-OSJ5S]]

[[D-T2NZ4]]

[[FD-2UWAQ]]

## Central and derived series

The [[D-D7L4X|lower central series]] $\gamma_1(G)=G$, $\gamma_{i+1}(G)=[\gamma_i(G),G]$ and the [[D-XEDSI|upper central series]] $Z_0(G)=1$, $Z_{i+1}(G)/Z_i(G)=Z(G/Z_i(G))$ reach $1$ and $G$ respectively if and only if $G$ is [[D-53JVH|nilpotent]], and in that case they have the same length, the nilpotency class of $G$.
The [[D-W2QAA|derived series]] $G^{(0)}=G$, $G^{(i+1)}=[G^{(i)},G^{(i)}]$ reaches $1$ if and only if $G$ is [[D-DFIDP|solvable]].
Each of these series is determined by $G$.

[[D-D7L4X]]

[[D-BGNME]]

[[D-XEDSI]]

[[D-W2QAA]]

::: {.remark title="Implications among the classes"}
$$
\text{cyclic} \implies \text{abelian} \implies \text{nilpotent} \implies \text{solvable},
$$
and no implication reverses: $\ZZ/2\times\ZZ/2$ is abelian and not cyclic, $Q_8$ is nilpotent and not abelian, and $S_3$ is solvable and not nilpotent.
The symmetric group $S_n$ is solvable if and only if $n\leq 4$.
Over a field of characteristic $0$, a polynomial is solvable by radicals if and only if its Galois group is solvable; see [[algebra/galois-theory/cyclotomic-and-radical-extensions|Cyclotomic and radical extensions]].
:::

## Nilpotent groups

[[D-53JVH]]

[[T-7PU33]]

[[T-4INET]]

[[T-GM7EB]]

[[T-OHEFT]]

::: {.proposition}
For a finite group $G$, the following are equivalent.

- $G$ is nilpotent.

- For every proper subgroup $H < G$, $H < N_G(H)$.

- Every Sylow subgroup of $G$ is normal.

- $G$ is the direct product of its Sylow subgroups.

- Every maximal subgroup of $G$ is normal.

- The lower central series of $G$ reaches $1$.

- The upper central series of $G$ reaches $G$.
:::

::: {.fact}
\envlist

- Subgroups and quotients of nilpotent groups are nilpotent.

- An extension of nilpotent groups need not be nilpotent: $S_3$ has the normal subgroup $A_3 \cong C_3$ with quotient $S_3/A_3 \cong C_2$, both nilpotent, and $S_3$ is not nilpotent.

- For $N \normal G$, $G$ is solvable if and only if both $N$ and $G/N$ are solvable.

- A finite nilpotent group $G$ has a normal subgroup of order $d$ for every $d$ dividing $\abs{G}$.
:::
