---
schema: qual/card@1
id: P-JPTMN
kind: problem
title: The center of $S_n$ is trivial for $n \geq 3$
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
Prove that the center of the symmetric group $S_n$ is trivial for all $n \ge 3$:
$$Z(S_n) = \{e\} \quad \text{for all } n \ge 3.$$
:::

::: solution
**Goal:** Prove that if $\sigma \in S_n$ satisfies $\sigma \tau = \tau \sigma$ for all $\tau \in S_n$, then $\sigma = e$.

<1>1. Setting:
    *Proof:*
    <2>1. Let $n \ge 3$, and let $\sigma \in Z(S_n)$.
    <2>2. We will show that $\sigma(i) = i$ for every $i \in \{1, 2, \dots, n\}$.

<1>2. Proof by Contradiction (Non-Identity Element):
    *Proof:*
    <2>1. Suppose, for contradiction, that $\sigma \ne e$.
    <2>2. Then there exists some element $i \in \{1, 2, \dots, n\}$ such that:
        $$\sigma(i) = j \ne i.$$
    <2>3. Since $n \ge 3$, there exists a third element $k \in \{1, 2, \dots, n\}$ distinct from both $i$ and $j$:
        $$k \notin \{i, j\}.$$
    <2>4. Consider the transposition:
        $$\tau = (j \, k) \in S_n.$$
    <2>5. We evaluate the products $\sigma \tau$ and $\tau \sigma$ at the element $i$:
        - $(\sigma \tau)(i) = \sigma(\tau(i)) = \sigma(i) = j$ (since $\tau$ fixes $i$).
        - $(\tau \sigma)(i) = \tau(\sigma(i)) = \tau(j) = k$ (since $\tau$ swaps $j$ and $k$).
    <2>6. Since $j \ne k$, we have:
        $$(\sigma \tau)(i) = j \ne k = (\tau \sigma)(i).$$
    <2>7. Therefore:
        $$\sigma \tau \ne \tau \sigma.$$
    <2>8. This contradicts the assumption that $\sigma \in Z(S_n)$ commutes with all elements of $S_n$.

<1>3. Conclusion:
    No non-identity permutation can commute with all transpositions in $S_n$ when $n \ge 3$. Thus $Z(S_n) = \{e\}$ for all $n \ge 3$. Q.E.D.
:::
