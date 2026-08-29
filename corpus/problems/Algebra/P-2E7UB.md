---
schema: qual/card@1
id: P-2E7UB
kind: problem
title: Every non-unit lies in a maximal ideal
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Ideals
  - Zorn's Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $R$ be a ring with identity $1 \ne 0$.
Prove that if $x \in R$ is not a left-invertible unit (or non-unit in a commutative ring), then $x$ is contained in some maximal (left) ideal of $R$ (Krull's Theorem).
:::

::: solution
**Goal:** Prove that any proper principal left ideal $(x) = Rx \subsetneq R$ can be extended to a maximal left ideal $\mathfrak{m} \subset R$ containing $x$ using Zorn's Lemma.

<1>1. Setting and the Poset of Proper Left Ideals Containing $x$:
    *Proof:*
    <2>1. Let $R$ be a ring with identity $1 \ne 0$, and let $x \in R$ be a non-unit (not left-invertible, so $1 \notin Rx$).
    <2>2. The principal left ideal $I_0 \coloneqq Rx = \{rx \mid r \in R\}$ is a **proper left ideal** of $R$, because if $1 \in Rx$, there would exist $r \in R$ with $rx = 1$, making $x$ left-invertible, contrary to hypothesis.
    <2>3. Define the partially ordered set:
        $$\mathcal{P} \coloneqq \{I \subseteq R \mid I \text{ is a left ideal of } R, \; x \in I, \text{ and } I \subsetneq R\},$$
        ordered by set inclusion $\subseteq$.
    <2>4. $\mathcal{P}$ is **non-empty** since $I_0 = Rx \in \mathcal{P}$.

<1>2. Verification of Chain Condition for Zorn's Lemma:
    *Proof:*
    <2>1. Let $\mathcal{C} = \{I_\alpha\}_{\alpha \in A}$ be a non-empty totally ordered chain in $\mathcal{P}$ (so for any $\alpha, \beta \in A$, either $I_\alpha \subseteq I_\beta$ or $I_\beta \subseteq I_\alpha$).
    <2>2. Define the union of the chain:
        $$U \coloneqq \bigcup_{\alpha \in A} I_\alpha.$$
    <2>3. We verify that $U$ is a left ideal:
        - Since each $I_\alpha$ contains $x$ and $0$, $x \in U$ and $0 \in U$.
        - If $a, b \in U$, then $a \in I_\alpha$ and $b \in I_\beta$ for some $\alpha, \beta \in A$.
          Since $\mathcal{C}$ is a chain, without loss of generality $I_\alpha \subseteq I_\beta$, so $a, b \in I_\beta$.
          Since $I_\beta$ is a left ideal, $a - b \in I_\beta \subseteq U$.
        - For any $r \in R$ and $a \in U$ (with $a \in I_\alpha$), $ra \in I_\alpha \subseteq U$.
        - Thus $U$ is a left ideal containing $x$.
    <2>4. We verify that $U$ is a **proper** left ideal ($U \subsetneq R$):
        - A left ideal $I \subseteq R$ is proper if and only if $1 \notin I$.
        - Since each $I_\alpha \in \mathcal{P}$ is proper, $1 \notin I_\alpha$ for every $\alpha \in A$.
        - Therefore, $1 \notin \bigcup_{\alpha \in A} I_\alpha = U$.
        - Thus $U \subsetneq R$, so $U \in \mathcal{P}$.
    <2>5. Clearly $I_\alpha \subseteq U$ for all $\alpha \in A$, so $U$ is an **upper bound** for the chain $\mathcal{C}$ in $\mathcal{P}$.

<1>3. Application of Zorn's Lemma:
    *Proof:*
    <2>1. By **Zorn's Lemma**, the poset $\mathcal{P}$ has at least one **maximal element**, say $\mathfrak{m} \in \mathcal{P}$.
    <2>2. By definition of $\mathcal{P}$, $\mathfrak{m}$ is a proper left ideal of $R$ containing $x$.
    <2>3. If $J$ is any proper left ideal of $R$ with $\mathfrak{m} \subseteq J \subsetneq R$:
        - Since $x \in \mathfrak{m} \subseteq J$, we have $J \in \mathcal{P}$.
        - By the maximality of $\mathfrak{m}$ in $\mathcal{P}$, we must have $J = \mathfrak{m}$.
    <2>4. Therefore, $\mathfrak{m}$ is a **maximal left ideal** of $R$.

<1>4. Conclusion:
    Every non-unit $x \in R$ is contained in a maximal left ideal $\mathfrak{m} \subset R$. Q.E.D.
:::
