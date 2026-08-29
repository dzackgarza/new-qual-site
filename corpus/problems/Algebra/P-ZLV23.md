---
schema: qual/card@1
id: P-ZLV23
kind: problem
title: No simple group of order $160$, and the structure of groups of that order
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Simple Groups
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Prove that there is no simple group of order 160. What can you say about the structure of groups of that order?
:::

::: solution
**Goal:** Prove that no group of order $160 = 2^5 \cdot 5 = 32 \cdot 5$ is simple, and describe the structure of such groups.

<1>1. Sylow analysis:
    *Proof:*
    <2>1. The order of $G$ is $|G| = 160 = 2^5 \cdot 5$.
    <2>2. **Sylow 5-subgroups:** By the Sylow theorems:
        $$n_5 \equiv 1 \pmod 5 \quad \text{and} \quad n_5 \mid 32.$$
    <2>3. The divisors of 32 are $1, 2, 4, 8, 16, 32$.
    <2>4. Checking modulo 5:
        - $1 \equiv 1 \pmod 5$ ✓
        - $2 \equiv 2 \pmod 5$
        - $4 \equiv 4 \pmod 5$
        - $8 \equiv 3 \pmod 5$
        - $16 \equiv 1 \pmod 5$ ✓
        - $32 \equiv 2 \pmod 5$
    <2>5. Thus $n_5 \in \{1, 16\}$.

<1>2. Case $n_5 = 1$:
    *Proof:*
    <2>1. If $n_5 = 1$, the unique Sylow 5-subgroup $P_5 \cong \mathbb{Z}_5$ is normal in $G$: $P_5 \trianglelefteq G$.
    <2>2. Since $1 < |P_5| = 5 < 160$, $P_5$ is a proper, non-trivial normal subgroup, so $G$ is not simple.

<1>3. Case $n_5 = 16$: Sylow 2-subgroup index and action:
    *Proof:*
    <2>1. **Sylow 2-subgroups:** Let $P_2$ be a Sylow 2-subgroup of order $|P_2| = 32$.
    <2>2. The index of $P_2$ in $G$ is $[G : P_2] = \frac{160}{32} = 5$.
    <2>3. Consider the action of $G$ on the 5 left cosets $G/P_2$ by left multiplication:
        $$\rho: G \to S_5.$$
    <2>4. The kernel $K = \ker\rho$ is the core of $P_2$ in $G$: $K = \bigcap_{g \in G} g P_2 g^{-1} \trianglelefteq G$.
    <2>5. If $G$ were simple, $\ker\rho$ would have to be trivial, so $\rho: G \hookrightarrow S_5$ would be injective.
    <2>6. But $|G| = 160$ and $|S_5| = 120$.
    <2>7. Since $160 > 120$, no injective homomorphism $G \hookrightarrow S_5$ can exist.
    <2>8. Thus $\ker\rho$ is a non-trivial proper normal subgroup of $G$ (in fact, $|K| \ge 160 / 120 > 1$, so $K \ne \{e\}$ and $K \subseteq P_2 \subsetneq G$).
    <2>9. Therefore, $G$ cannot be simple in this case either.

<1>4. Structure of groups of order 160:
    *Proof:*
    <2>1. **Solvability:**
        - If $n_5 = 1$, $G / P_5$ has order 32 ($p$-group, hence nilpotent and solvable). Since $P_5 \cong \mathbb{Z}_5$ is solvable and $G/P_5$ is solvable, $G$ is **solvable** (by Burnside's $p^a q^b$ theorem, any group of order $p^a q^b$ is solvable).
        - If $n_5 = 16$, the normal subgroup $K \trianglelefteq G$ is a 2-group, and $G/K$ embeds into $S_5$. Since $K$ is a 2-group and $G/K$ is a subgroup of $S_5$ of order dividing 160 (specifically order 20, 40, or 80), $G$ is solvable.
    <2>2. **Semidirect product structure:** When $n_5 = 1$, $G \cong \mathbb{Z}_5 \rtimes_\theta P_2$, where $P_2$ is a group of order 32 and $\theta: P_2 \to \operatorname{Aut}(\mathbb{Z}_5) \cong \mathbb{Z}_4$.
    <2>3. The action $\theta$ factors through a cyclic quotient of $P_2$ of order dividing 4.

<1>5. Conclusion:
    There is no simple group of order 160 (by Sylow 5 counting or the coset permutation representation in $S_5$), and every group of order 160 is solvable by Burnside's $p^a q^b$ Theorem. Q.E.D.
:::
