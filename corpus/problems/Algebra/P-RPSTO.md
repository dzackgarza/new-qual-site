---
schema: qual/card@1
id: P-RPSTO
kind: problem
title: Solvable groups have a nontrivial normal subgroup
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Normal Subgroups
  - Commutators
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
- Show that if $G$ is solvable, then $G$ contains a nontrivial normal subroup.

  - What does this mean on the Galois theory side?

> Hint: consider the derived series.
:::

::: {.solution}
**Goal.** Show a solvable group has a nontrivial normal subgroup, and interpret this in Galois theory.

<1>1. $G$ solvable means the derived series $G = G^{(0)} \supseteq G^{(1)} \supseteq G^{(2)} \supseteq \cdots$ terminates at $\theset{1}$.
::: {.proof}
definition of solvable (the derived series reaches the trivial group).
:::

<1>2. If $G \neq \theset{1}$, then $G^{(1)} = [G, G]$ is a proper subgroup of $G$.
::: {.proof}
if $[G,G] = G$, then the derived series never descends, so $G$ would not be solvable (unless $G = \theset{1}$).
:::

<1>3. $G^{(1)} = [G, G]$ is normal in $G$.
::: {.proof}
the commutator subgroup is characteristic, hence normal.
:::

<1>4. $G^{(1)}$ is nontrivial unless $G$ is abelian.
<2>1. If $G$ is nonabelian, then $[G,G] \neq \theset{1}$.
::: {.proof}
$[G,G] = \theset{1}$ iff $G$ is abelian.
:::
<2>2. If $G$ is abelian and nontrivial, then $G$ itself is a nontrivial normal subgroup (or any nontrivial element generates a normal subgroup).
::: {.proof}
in an abelian group, every subgroup is normal.
:::

<1>5. Hence $G$ has a nontrivial normal subgroup.
<2>1. If $G$ is nonabelian, take $[G,G]$ (nontrivial and normal).
::: {.proof}
<1>3 and <1>4.1. <2>2. If $G$ is abelian and nontrivial, take $G$ itself (or a nontrivial cyclic subgroup).
:::
::: {.proof}
<1>4.2.
:::

<1>6. Galois-theoretic interpretation.
<2>1. A solvable Galois group corresponds to a tower of fields $F = F_0 \subseteq F_1 \subseteq \cdots \subseteq F_k = E$ with each $F_{i+1}/F_i$ abelian (or cyclic of prime order).
::: {.proof}
the derived series of the Galois group corresponds, via the Galois correspondence, to a tower of intermediate fields with abelian (or cyclic) successive extensions.
:::
<2>2. The nontrivial normal subgroup corresponds to a nontrivial intermediate field $F \subsetneq K \subsetneq E$ that is Galois over $F$.
::: {.proof}
a normal subgroup $H \normal G$ corresponds to a Galois intermediate field $E^H$ (Galois over $F$ since $H$ is normal).
:::

<1>7. Q.E.D.
::: {.proof}
<1>5 proves the group statement; <1>6 gives the Galois interpretation.
:::
:::
