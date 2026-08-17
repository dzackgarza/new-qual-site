---
schema: qual/card@1
id: E-AMD-5LBXBRCH
kind: exercise
title: Show if $G$ is finite, then $G$ is solvable $\iff$ all of its…
classification:
  areas:
  - algebra
  topics:
  - solvable-groups
  - subgroup-series
  - classification
relations: []
review: draft
solved: true
---

::: {.exercise}
Show that a finite group $G$ is solvable if and only if all of its composition factors are cyclic groups of prime order.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Let $G$ be a finite group. Recall that a **composition series** of $G$ is a subnormal series:
$$
1 = G_0 \normal G_1 \normal G_2 \normal \cdots \normal G_n = G
$$
such that each composition factor $G_{i+1}/G_i$ is a **simple group** for $i = 0, \ldots, n-1$.
By the Jordan-Hölder Theorem, the composition factors of $G$ are unique up to permutation and isomorphism.

**$(\Longrightarrow)$ Suppose $G$ is solvable:**
1. Since $G$ is solvable, $G$ has a subnormal series with abelian factor groups.
2. By refining this series (inserting intermediate normal subgroups), we obtain a composition series:
   $$
   1 = G_0 \normal G_1 \normal \cdots \normal G_n = G.
   $$
3. Each composition factor $S_i = G_{i+1}/G_i$ is a simple group.
   Since $G$ is solvable, every subgroup and every quotient of $G$ is solvable; in particular, the simple factor $S_i$ is a solvable simple group.
4. The only non-trivial proper subgroup of a simple group is the trivial group, so the derived subgroup $[S_i, S_i]$ must be either $1$ or $S_i$.
   Since $S_i$ is solvable, $[S_i, S_i] \neq S_i$, which forces $[S_i, S_i] = 1$.
   Thus $S_i$ is **abelian**.
5. The only abelian simple groups are cyclic groups of prime order $\ZZ_p$ (since any proper non-trivial subgroup $\langle x \rangle$ is normal in an abelian group).
   Therefore, every composition factor $G_{i+1}/G_i \cong \ZZ_p$ has prime order.

**$(\Longleftarrow)$ Suppose all composition factors of $G$ are of prime order:**
1. Let $1 = G_0 \normal G_1 \normal \cdots \normal G_n = G$ be a composition series of $G$.
2. By assumption, each quotient group $G_{i+1}/G_i \cong \ZZ_{p_i}$ is a cyclic group of prime order $p_i$.
3. Since cyclic groups are abelian, each factor $G_{i+1}/G_i$ is abelian.
4. By definition, a group possessing a subnormal series with abelian factor groups is **solvable**.

Thus, a finite group $G$ is solvable if and only if all of its composition factors are isomorphic to $\ZZ_p$ for various primes $p$.
:::
