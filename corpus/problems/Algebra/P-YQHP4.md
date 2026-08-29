---
schema: qual/card@1
id: P-YQHP4
kind: problem
title: An ideal containing a unit is the whole ring
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Rings
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
(1) Let $R$ be a ring with identity $1 \ne 0$, and let $I \trianglelefteq R$ be an ideal of $R$.
Prove that if $I$ contains a unit $u \in R^\times$, then $I = R$.
(2) Prove that the group of units $R^\times$ need not be closed under addition, and provide concrete examples in standard rings.
:::

::: solution
**Goal:** Prove that an ideal containing a unit equals the whole ring, and demonstrate that units do not form an additive subgroup.

<1>1. Part 1: An Ideal Containing a Unit is the Whole Ring:
    *Proof:*
    <2>1. Let $I \subseteq R$ be a (left, right, or two-sided) ideal of $R$.
    <2>2. Suppose $I$ contains an invertible element (unit) $u \in R^\times$.
    <2>3. By definition of a unit, there exists an element $u^{-1} \in R$ such that $u^{-1} u = u u^{-1} = 1$.
    <2>4. By the absorption property of ideals:
        - If $I$ is a left ideal: since $u \in I$ and $u^{-1} \in R$, we have $1 = u^{-1} u \in I$.
        - If $I$ is a right ideal: since $u \in I$ and $u^{-1} \in R$, we have $1 = u u^{-1} \in I$.
    <2>5. Once $1 \in I$, for every element $r \in R$, the product $r \cdot 1 = r$ must belong to $I$ by ideal absorption.
    <2>6. Therefore, $R \subseteq I$, which forces:
        $$I = R.$$

<1>2. Part 2: $R^\times$ Need Not Be Closed Under Addition:
    *Proof:*
    <2>1. The set of units $R^\times$ is a group under **multiplication**, but is almost never closed under addition.
    <2>2. **Counterexample 1 (In $\mathbb{Z}$):**
        - The units of $\mathbb{Z}$ are $\mathbb{Z}^\times = \{1, -1\}$.
        - Taking $u = 1 \in \mathbb{Z}^\times$ and $v = 1 \in \mathbb{Z}^\times$:
          $$u + v = 1 + 1 = 2 \notin \mathbb{Z}^\times \quad (\text{since } 1/2 \notin \mathbb{Z}).$$
        - Taking $u = 1$ and $v = -1$:
          $$u + v = 1 + (-1) = 0 \notin \mathbb{Z}^\times.$$
    <2>3. **Counterexample 2 (In a Field $k$):**
        - In any field $k$, $k^\times = k \setminus \{0\}$.
        - For any $u \in k^\times$, $-u \in k^\times$ is also a unit.
        - Their sum is $u + (-u) = 0 \notin k^\times$.
        - Thus in any non-zero ring, the sum of two units can equal $0$, which is never a unit (since $1 \ne 0$).

<1>3. Conclusion:
    $u \in I \implies 1 = u^{-1} u \in I \implies I = R$, and $R^\times$ is not closed under addition as $1 + (-1) = 0 \notin R^\times$. Q.E.D.
:::
