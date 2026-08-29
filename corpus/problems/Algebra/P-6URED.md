---
schema: qual/card@1
id: P-6URED
kind: problem
title: $S_4$ is solvable and nonabelian
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Permutations
  - Subgroup Series
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.problem}
Prove that the symmetric group $S_4$ is a **non-abelian** and **solvable** group.
:::

::: solution
**Goal:** Prove that $S_4$ is non-abelian and construct an explicit subnormal series with abelian factor groups (solvable series).

<1>1. Proof that $S_4$ is Non-Abelian:
    *Proof:*
    <2>1. Consider the transpositions $(1 \, 2)$ and $(2 \, 3)$ in $S_4$:
        $$(1 \, 2)(2 \, 3) = (1 \, 2 \, 3), \qquad (2 \, 3)(1 \, 2) = (1 \, 3 \, 2).$$
    <2>2. Since $(1 \, 2 \, 3) \ne (1 \, 3 \, 2)$, $(1 \, 2)$ and $(2 \, 3)$ do not commute.
    <2>3. Thus $S_4$ is **non-abelian**.

<1>2. The Derived Series / Subnormal Series of $S_4$:
    *Proof:*
    <2>1. Consider the following chain of subgroups of $S_4$:
        $$\{e\} \triangleleft V_4 \triangleleft A_4 \triangleleft S_4$$
        where:
        - $A_4$ is the alternating group on 4 letters (order 12).
        - $V_4 = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}$ is the Klein 4-group (order 4).

<1>3. Verification of Normality and Abelian Factors:
    *Proof:*
    <2>1. **$A_4 \triangleleft S_4$:**
        $[S_4 : A_4] = 24/12 = 2$.
        Every subgroup of index 2 is normal, and the quotient:
        $$S_4 / A_4 \cong \mathbb{Z}_2 \quad \text{is abelian}.$$
    <2>2. **$V_4 \triangleleft A_4$ (and $V_4 \trianglelefteq S_4$):**
        $V_4$ consists of the identity and all three elements of cycle type $(2, 2)$ in $S_4$.
        Since conjugation in $S_4$ preserves cycle types, $g V_4 g^{-1} = V_4$ for all $g \in S_4$.
        Thus $V_4$ is normal in $S_4$ (hence normal in $A_4$).
        The quotient has order $[A_4 : V_4] = 12/4 = 3$:
        $$A_4 / V_4 \cong \mathbb{Z}_3 \quad \text{is abelian (cyclic of prime order 3)}.$$
    <2>3. **$\{e\} \triangleleft V_4$:**
        $V_4 \cong \mathbb{Z}_2 \times \mathbb{Z}_2$, which is an **abelian group**.
        Thus $V_4 / \{e\} \cong V_4$ is abelian.

<1>4. Refinement to Composition Series:
    *Proof:*
    <2>1. Choosing any order-2 subgroup $H = \{e, (1\,2)(3\,4)\} \le V_4$, we have the composition series:
        $$\{e\} \triangleleft \mathbb{Z}_2 \triangleleft V_4 \triangleleft A_4 \triangleleft S_4$$
        with composition factors $\mathbb{Z}_2, \mathbb{Z}_2, \mathbb{Z}_3, \mathbb{Z}_2$, all of prime cyclic order.

<1>5. Conclusion:
    $S_4$ is non-abelian, and the series $\{e\} \triangleleft V_4 \triangleleft A_4 \triangleleft S_4$ has abelian factors $\mathbb{Z}_2, \mathbb{Z}_3, V_4$, proving $S_4$ is solvable. Q.E.D.
:::
