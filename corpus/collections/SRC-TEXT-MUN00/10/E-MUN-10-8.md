---
schema: qual/card@1
id: E-MUN-10-8
kind: problem
title: Well-ordering unions of disjoint well-ordered sets
classification:
  areas:
  - topology
  topics:
  - Well-Ordered Sets
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.exercise}
(a) Let $A_{1}$ and $A_{2}$ be disjoint sets, well-ordered by $<_{1}$ and $<_{2}$, respectively.
Define an order relation on $A_{1} \cup A_{2}$ by letting $a < b$ either if $a, b \in A_{1}$ and $a <_{1} b$, or if $a, b \in A_{2}$ and $a <_{2} b$, or if $a \in A_{1}$ and $b \in A_{2}$. Show that this is a **well-ordering**.

(b) Generalize (a) to an arbitrary family of pairwise disjoint well-ordered sets $\{A_\alpha\}_{\alpha \in J}$, indexed by a well-ordered set $J$.
:::

::: solution
**Goal:** Prove that the ordinal sum (lexicographic / concatenation order) of well-ordered sets indexed by a well-ordered set produces a well-ordering.

<1>1. Proof of Part (b) (Arbitrary Disjoint Family Indexed by a Well-Ordered Set):
    *Proof:*
    <2>1. Let $(J, <_J)$ be a well-ordered indexing set.
    <2>2. For each $\alpha \in J$, let $(A_\alpha, <_\alpha)$ be a well-ordered set, with $A_\alpha \cap A_\beta = \emptyset$ for $\alpha \ne \beta$.
    <2>3. Let $A = \bigcup_{\alpha \in J} A_\alpha$.
    <2>4. Define a binary relation $<$ on $A$ as follows: for $a, b \in A$, let $\alpha, \beta \in J$ be the unique indices such that $a \in A_\alpha$ and $b \in A_\beta$. We define:
        $$a < b \iff (\alpha <_J \beta) \quad \text{or} \quad (\alpha = \beta \text{ and } a <_\alpha b).$$

<1>2. Verification that $<$ is a Strict Simple (Linear) Order:
    *Proof:*
    <2>1. **Trichotomy:** For any $a, b \in A$ with $a \in A_\alpha, b \in A_\beta$:
        - If $\alpha \ne \beta$: since $<_J$ is a linear order on $J$, exactly one of $\alpha <_J \beta$ or $\beta <_J \alpha$ holds, so exactly one of $a < b$ or $b < a$ holds.
        - If $\alpha = \beta$: then $a, b \in A_\alpha$. Since $<_\alpha$ is a linear order, exactly one of $a <_\alpha b$, $b <_\alpha a$, or $a = b$ holds.
        - Thus exactly one of $a < b$, $b < a$, or $a = b$ holds.
    <2>2. **Transitivity:** Let $a < b$ and $b < c$, with $a \in A_\alpha, b \in A_\beta, c \in A_\gamma$.
        - If $\alpha <_J \beta$ and $\beta <_J \gamma$: by transitivity of $<_J$, $\alpha <_J \gamma \implies a < c$.
        - If $\alpha <_J \beta$ and $\beta = \gamma$: $\alpha <_J \gamma \implies a < c$.
        - If $\alpha = \beta$ and $\beta <_J \gamma$: $\alpha <_J \gamma \implies a < c$.
        - If $\alpha = \beta = \gamma$: then $a <_\alpha b <_\alpha c$, so by transitivity of $<_\alpha$, $a <_\alpha c \implies a < c$.
    <2>3. Thus $(A, <)$ is a linearly ordered set.

<1>3. Proof of the Well-Ordering Property (Every Non-Empty Subset Has a Smallest Element):
    *Proof:*
    <2>1. Let $S \subseteq A$ be any non-empty subset.
    <2>2. Define the set of index values occupied by elements of $S$:
        $$J_0 \coloneqq \{ \alpha \in J \mid S \cap A_\alpha \ne \emptyset \}.$$
    <2>3. Since $S$ is non-empty, $J_0$ is a non-empty subset of the well-ordered set $J$.
    <2>4. Since $J$ is well-ordered, $J_0$ has a **unique least element** $\alpha_0 = \min(J_0) \in J$.
    <2>5. Consider the non-empty subset $S \cap A_{\alpha_0} \subseteq A_{\alpha_0}$.
    <2>6. Since $(A_{\alpha_0}, <_{\alpha_0})$ is well-ordered, $S \cap A_{\alpha_0}$ has a **unique least element** $m_0 \coloneqq \min_{<_{\alpha_0}}(S \cap A_{\alpha_0})$.
    <2>7. We claim that $m_0$ is the **smallest element of $S$** under $<$:
        - Let $s \in S$ be any element, with $s \in A_\beta$ for some $\beta \in J_0$.
        - By definition of $\alpha_0 = \min(J_0)$, we have $\alpha_0 \le_J \beta$.
        - Case 1 ($\alpha_0 <_J \beta$): By definition of $<$, $m_0 < s$ because $\alpha_0 <_J \beta$.
        - Case 2 ($\alpha_0 = \beta$): Then $s \in S \cap A_{\alpha_0}$. By definition of $m_0 = \min(S \cap A_{\alpha_0})$, we have $m_0 \le_{\alpha_0} s \implies m_0 \le s$.
    <2>8. Thus $m_0 \le s$ for all $s \in S$, confirming that $m_0$ is the minimum element of $S$.

<1>4. Part (a) as a Special Case:
    *Proof:*
    <2>1. Set the indexing set $J = \{1, 2\}$ with the standard well-ordering $1 <_J 2$.
    <2>2. Applying Part (b) directly proves that the concatenated order on $A_1 \cup A_2$ is a well-ordering.

<1>5. Conclusion:
    The concatenated / ordinal sum order on the union of any well-ordered collection of disjoint well-ordered sets is a well-ordering. Q.E.D.
:::
