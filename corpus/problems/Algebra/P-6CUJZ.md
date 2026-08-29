---
schema: qual/card@1
id: P-6CUJZ
kind: problem
title: $Z(A_n)=1$ for $n\geq 4$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Prove that the center of the alternating group $A_n$ is trivial for all $n \ge 4$:
$$Z(A_n) = \{e\} \quad \text{for all } n \ge 4.$$
:::

::: solution
**Goal:** Prove that the center $Z(A_n) = \{\sigma \in A_n \mid \sigma \tau = \tau \sigma \ \forall \tau \in A_n\}$ is trivial for $n \ge 4$.

<1>1. Setting and Disjoint Cycle Decomposition of a Non-Identity Element:
    *Proof:*
    <2>1. Let $\sigma \in A_n$ be a non-identity even permutation ($\sigma \ne e$).
    <2>2. We will construct an even permutation $\tau \in A_n$ that does not commute with $\sigma$ ($\sigma \tau \ne \tau \sigma$, or equivalently $\tau \sigma \tau^{-1} \ne \sigma$).
    <2>3. Decompose $\sigma$ into disjoint cycles. Since $\sigma \ne e$, $\sigma$ contains either:
        - A cycle of length $\ge 3$, or
        - At least two disjoint 2-cycles (transpositions), because an odd permutation (single 2-cycle) cannot belong to $A_n$.

<1>2. Case 1: $\sigma$ contains a cycle of length $\ge 3$:
    *Proof:*
    <2>1. Without loss of generality, let $\sigma = (1 \, 2 \, 3 \, \dots) \cdots$.
    <2>2. **Subcase 1A: $\sigma$ moves at least 4 elements, say $\sigma(1)=2, \sigma(2)=3, \sigma(3)=4$ (or $\sigma$ has another cycle moving 4):**
        - Let $\tau = (2 \, 3 \, 4) \in A_n$ (a 3-cycle, which is an even permutation).
        - Then $\tau \sigma \tau^{-1}(1) = \tau \sigma(1) = \tau(2) = 3$.
        - But $\sigma(1) = 2 \ne 3$.
        - Thus $\tau \sigma \tau^{-1} \ne \sigma$, so $\sigma \tau \ne \tau \sigma$.
    <2>3. **Subcase 1B: $\sigma = (1 \, 2 \, 3)$ is a single 3-cycle, fixing all other elements:**
        - Since $n \ge 4$, there exists a 4th element, say $4 \in \{1, \dots, n\}$, which is fixed by $\sigma$ ($\sigma(4) = 4$).
        - Choose $\tau = (2 \, 3 \, 4) \in A_n$.
        - Then $\tau \sigma \tau^{-1}(1) = \tau \sigma(1) = \tau(2) = 3$.
        - But $\sigma(1) = 2 \ne 3$.
        - Thus $\tau \sigma \tau^{-1} \ne \sigma$.

<1>3. Case 2: $\sigma$ consists only of disjoint 2-cycles:
    *Proof:*
    <2>1. Since $\sigma \in A_n$ is even, $\sigma$ must contain at least two disjoint 2-cycles:
        $$\sigma = (1 \, 2)(3 \, 4) \cdots.$$
    <2>2. Choose the 3-cycle $\tau = (1 \, 2 \, 3) \in A_n$.
    <2>3. Compute the conjugate $\tau \sigma \tau^{-1}$:
        $$\tau \sigma \tau^{-1} = (\tau(1) \, \tau(2))(\tau(3) \, \tau(4)) \cdots = (2 \, 3)(1 \, 4) \cdots = (1 \, 4)(2 \, 3) \cdots.$$
    <2>4. Evaluating at $1$:
        - $(\tau \sigma \tau^{-1})(1) = 4$.
        - But $\sigma(1) = 2 \ne 4$.
    <2>5. Therefore $\tau \sigma \tau^{-1} \ne \sigma$, so $\sigma$ does not commute with $\tau \in A_n$.

<1>4. Conclusion:
    In every case, no non-identity element $\sigma \ne e$ can commute with all elements of $A_n$. Thus $Z(A_n) = \{e\}$ for all $n \ge 4$. Q.E.D.
:::
