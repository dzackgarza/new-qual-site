---
schema: qual/card@1
id: E-AKPMH
kind: problem
title: The irrationals are a Baire space
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that the irrationals are a Baire space.
:::

::: solution
**Goal:** Prove that the subspace of irrational numbers $\mathbb{P} = \mathbb{R} \setminus \mathbb{Q}$ equipped with the subspace topology from $\mathbb{R}$ is a Baire space.

<1>1. Representation of $\mathbb{P}$ as a $G_\delta$ subset of $\mathbb{R}$:
    *Proof:*
    <2>1. Enumerate the countable set of rational numbers as $\mathbb{Q} = \{q_n\}_{n=1}^\infty$.
    <2>2. For each $n \ge 1$, the singleton $\{q_n\}$ is closed in $\mathbb{R}$, so $U_n = \mathbb{R} \setminus \{q_n\}$ is an open and dense subset of $\mathbb{R}$.
    <2>3. The subspace of irrational numbers is:
        $$\mathbb{P} = \mathbb{R} \setminus \mathbb{Q} = \bigcap_{n=1}^\infty U_n.$$

<1>2. Verification of the dense open intersection condition:
    *Proof:*
    <2>1. Let $\{V_k\}_{k=1}^\infty$ be a countable sequence of dense open subsets of the subspace $\mathbb{P}$.
    <2>2. Since each $V_k$ is open in $\mathbb{P}$, there exists an open set $W_k \subseteq \mathbb{R}$ such that $V_k = W_k \cap \mathbb{P}$.
    <2>3. Because $V_k$ is dense in $\mathbb{P}$ and $\mathbb{P}$ is dense in $\mathbb{R}$, the open set $W_k$ is dense in $\mathbb{R}$ for each $k \ge 1$.
    <2>4. The combined collection $\{W_k\}_{k=1}^\infty \cup \{U_n\}_{n=1}^\infty$ is a countable family of open and dense subsets of $\mathbb{R}$.
    <2>5. By the Baire Category Theorem (Theorem 48.2), the complete metric space $\mathbb{R}$ is a Baire space, so the countable intersection:
        $$\bigcap_{k=1}^\infty W_k \cap \bigcap_{n=1}^\infty U_n = \left(\bigcap_{k=1}^\infty W_k\right) \cap \mathbb{P} = \bigcap_{k=1}^\infty V_k$$
        is dense in $\mathbb{R}$.
    <2>6. Since this intersection lies in $\mathbb{P}$ and is dense in $\mathbb{R}$, it is dense in the subspace $\mathbb{P}$.

<1>3. Conclusion:
    Every countable intersection of dense open subsets of $\mathbb{P}$ is dense in $\mathbb{P}$, so $\mathbb{P}$ is a Baire space. Q.E.D.
:::
