---
schema: qual/card@1
id: E-AMD-J2G54GWY
kind: exercise
title: Composition factors of finite solvable groups have prime order
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Subgroup Series
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that if $G$ is finite and solvable, then every composition factor of $G$ has prime order.
:::

::: solution
**Goal:** Prove that every composition factor of a finite solvable group $G$ is a cyclic group of prime order $\mathbb{Z}_p$.

<1>1. Solvability of composition factors:
    *Proof:*
    <2>1. Let $\{e\} = G_0 \trianglelefteq G_1 \trianglelefteq \dots \trianglelefteq G_n = G$ be a composition series of $G$.
    <2>2. By definition of a composition series, each factor $S_i = G_{i+1} / G_i$ is a non-trivial simple group.
    <2>3. Because subgroups and quotient groups of solvable groups are solvable, each $G_{i+1}$ is solvable, and therefore each quotient factor $S_i = G_{i+1} / G_i$ is a solvable group.

<1>2. Simple solvable groups are abelian:
    *Proof:*
    <2>1. Let $S$ be a finite group that is both simple and solvable.
    <2>2. The derived subgroup $[S, S]$ is a characteristic (and hence normal) subgroup of $S$.
    <2>3. Because $S$ is solvable, $[S, S] \neq S$ (the derived series must terminate at $\{e\}$).
    <2>4. Since $S$ is simple and $[S, S] \trianglelefteq S$, the only possibilities for $[S, S]$ are $\{e\}$ and $S$.
    <2>5. Since $[S, S] \neq S$, we must have $[S, S] = \{e\}$.
    <2>6. Thus $S$ is abelian.

<1>3. Simple abelian groups have prime order:
    *Proof:*
    <2>1. In an abelian group $S$, every subgroup is normal.
    <2>2. Since $S$ is simple, $S$ has no proper non-trivial subgroups.
    <2>3. Let $p$ be a prime dividing $|S|$. By Cauchy's Theorem, $S$ contains an element $x$ of order $p$.
    <2>4. The cyclic subgroup $\langle x \rangle \le S$ has order $p$.
    <2>5. Because $S$ has no proper non-trivial subgroups, we must have $\langle x \rangle = S$.
    <2>6. Therefore $|S| = p$ is prime, and $S \cong \mathbb{Z}_p$.

<1>4. Conclusion:
    Every composition factor of $G$ is simple and solvable, hence isomorphic to $\mathbb{Z}_p$ for some prime $p$. Q.E.D.
:::
