---
order: 50
---

# Series

## Definitions and Basics

[[D-KM2DV]]

[[D-5NV3N]]

[[D-FYX4I]]

[[T-OSJ5S]]

[[D-T2NZ4]]

::: {.proposition}
If $G$ is *not* simple, then $G$ is an extension of any of its normal subgroups.
I.e. for any $N\normal G$, $G \cong E$ for some extension of the form $N\to E\to G/N$.
:::

[[D-D7L4X]]
> Mnemonic: "lower" because the chain is descending.
> Iterate the adjoint map $[\wait, G]$, if this terminates then the map is nilpotent, so call $G$ nilpotent!

[[D-BGNME]]

[[D-XEDSI]]

[[D-W2QAA]]

## Solvability

::: {.remark}
A useful way to extract normal subgroups: let $G$ act on literally anything by $\phi: G\to \Aut(X)$.
Then $\ker \phi \normal G$ is always a normal subgroup.
Some examples:

- $G\actson G$ by $x\mapsto gx$.

- $G\actson \ts{H\leq G}$ by $H\mapsto gH$ or $H\mapsto gHg\inv$.

- $G\actson \ts{\Syl_p(G)}$ for a fixed $p$ by $S_p \mapsto gS_p g\inv$.

- $G\actson H$ for $H\normal G$ by inner automorphisms $h\mapsto ghg\inv$.
:::

::: {.remark}
A useful way to extract normal subgroups: let $G$ act on literally anything by $\phi: G\to \Aut(X)$.
Then $\ker \phi \normal G$ is always a normal subgroup.
:::

::: {.example title="?"}

- $G\actson G$ by $x\mapsto gx$.

- $G\actson \ts{H\leq G}$ by $H\mapsto gH$ or $H\mapsto gHg\inv$.

- $G\actson \ts{\Syl_p(G)}$ for a fixed $p$ by $S_p \mapsto gS_p g\inv$.

- $G\actson H$ for $H\normal G$ by inner automorphisms $h\mapsto ghg\inv$.
:::

[[D-DFIDP]]

::: {.remark}
If $G = \Gal(L/K)$ is a Galois group corresponding to a polynomial $f$, then $G$ is solvable as a group iff $f$ is solvable in radicals: there is a tower of extensions $K = F_0 \subset F_1 \subset F_2 \subset \cdots \subset F_m = L$ where

1. $F_i = F_{i-1}(\alpha_i)$ where \( \alpha_i^{m_i } \in F_{i-1} \) for some power $m_i \in \ZZ^{\geq 0}$, and

2. $F_m \supseteq \SF(f)$ contains a splitting field for $f$.
:::

[[T-QPMGT]]

[[T-EN5H4]]

::: {.fact}
Some useful facts about solvable groups:

- $G$ is solvable iff $G$ has a terminating *derived series*.

- Solvable groups satisfy the 2 out of 3 property

- Abelian $\implies$ solvable

- Every group of order less than 60 is solvable.
:::

## Series of Groups
