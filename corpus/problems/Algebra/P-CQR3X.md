---
schema: qual/card@1
id: P-CQR3X
kind: problem
title: A finite group is solvable iff its composition factors have prime order
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Subgroup Series
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $G$ be a finite group.
Prove that $G$ is solvable if and only if all of its composition factors are of prime order (i.e. cyclic groups $\mathbb{Z}_p$).
:::

::: solution
**Goal:** Prove the equivalence: $G$ is finite solvable $\iff$ every composition factor of $G$ is isomorphic to $\mathbb{Z}_p$ for some prime $p$.

<1>1. Definition of Composition Series and Factors:
    *Proof:*
    <2>1. A **composition series** of a finite group $G$ is a subnormal series:
        $$\{e\} = G_0 \triangleleft G_1 \triangleleft G_2 \triangleleft \cdots \triangleleft G_k = G$$
        such that each factor group $G_{i+1}/G_i$ is a **simple group** (has no non-trivial proper normal subgroups).
    <2>2. The Jordan–Hölder Theorem guarantees that any two composition series for $G$ have the same length and the same composition factors up to isomorphism and permutation.

<1>2. Direction $(\implies)$: $G$ solvable $\implies$ composition factors are prime cyclic $\mathbb{Z}_p$:
    *Proof:*
    <2>1. If $G$ is solvable, $G$ has a subnormal series with **abelian** factor groups.
    <2>2. By refining this abelian series to a composition series (by inserting maximal normal subgroups between each step), the resulting composition factors $S = G_{i+1}/G_i$ are both **simple** and **abelian** (subquotients of abelian groups are abelian).
    <2>3. Let $S$ be an abelian simple group.
    <2>4. Take any non-identity element $x \in S \setminus \{e\}$.
    <2>5. The cyclic subgroup $\langle x \rangle \le S$ is normal in $S$ because $S$ is abelian.
    <2>6. Since $S$ is simple and $\langle x \rangle \ne \{e\}$, we must have $\langle x \rangle = S$, so $S$ is cyclic.
    <2>7. If $|S| = n$ is composite with a proper divisor $d \mid n$, then the cyclic group $\mathbb{Z}_n$ has a non-trivial proper subgroup of order $d$, contradicting simplicity.
    <2>8. Therefore, $|S| = p$ must be a **prime integer**, so $S \cong \mathbb{Z}_p$.
    <2>9. By Jordan–Hölder, *all* composition series of $G$ have composition factors of prime order.

<1>3. Direction $(\impliedby)$: All composition factors have prime order $\implies G$ is solvable:
    *Proof:*
    <2>1. Suppose $G$ has a composition series $\{e\} = G_0 \triangleleft G_1 \triangleleft \cdots \triangleleft G_k = G$ where each factor $G_{i+1}/G_i \cong \mathbb{Z}_{p_i}$ has prime order $p_i$.
    <2>2. Since every group of prime order is cyclic, and every cyclic group is **abelian**, each quotient $G_{i+1}/G_i$ is abelian.
    <2>3. A subnormal series with abelian factors is, by definition, a **solvable series** for $G$.
    <2>4. Therefore, $G$ is a solvable group.

<1>4. Conclusion:
    A finite group $G$ is solvable if and only if all of its composition factors are cyclic of prime order $\mathbb{Z}_p$. Q.E.D.
:::
