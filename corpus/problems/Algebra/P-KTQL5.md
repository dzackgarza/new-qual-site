---
schema: qual/card@1
id: P-KTQL5
kind: problem
title: Centre of $S_n$
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
What is the center $Z(S_n)$ of the symmetric group $S_n$? Prove it.
:::

::: solution
**Goal:** Determine and prove the center $Z(S_n)$ for all $n \ge 1$.

<1>1. Cases $n = 1$ and $n = 2$:
    *Proof:*
    <2>1. For $n = 1$, $S_1 = \{e\}$, which is abelian, so $Z(S_1) = S_1 = \{e\}$.
    <2>2. For $n = 2$, $S_2 = \{e, (1\,2)\} \cong \mathbb{Z}_2$, which is abelian, so $Z(S_2) = S_2 \cong \mathbb{Z}_2$.

<1>2. Center is trivial for $n \ge 3$: $Z(S_n) = \{e\}$:
    *Proof:*
    <2>1. Let $n \ge 3$, and let $\sigma \in Z(S_n)$ be a central permutation.
    <2>2. Suppose, for contradiction, that $\sigma \ne e$.
    <2>3. Then there exists some element $a \in \{1, \dots, n\}$ such that $\sigma(a) = b \ne a$.
    <2>4. Since $n \ge 3$, there exists a third distinct element $c \in \{1, \dots, n\} \setminus \{a, b\}$.
    <2>5. Consider the transposition $\tau = (b \ c) \in S_n$.
    <2>6. Compute the action of $\sigma \tau$ and $\tau \sigma$ on the element $a$:
        - $(\sigma \tau)(a) = \sigma(\tau(a)) = \sigma(a) = b$ (since $\tau$ fixes $a$).
        - $(\tau \sigma)(a) = \tau(\sigma(a)) = \tau(b) = c$.
    <2>7. Because $b \ne c$, we have $(\sigma \tau)(a) \ne (\tau \sigma)(a)$, which implies:
        $$\sigma \tau \ne \tau \sigma.$$
    <2>8. This contradicts the assumption that $\sigma$ commutes with all elements of $S_n$ (specifically $\tau \in S_n$).
    <2>9. Therefore, no non-identity permutation can lie in $Z(S_n)$, forcing $Z(S_n) = \{e\}$.

<1>3. Conclusion:
    $$Z(S_n) = \begin{cases} S_1 = \{e\} & \text{if } n = 1, \\ S_2 \cong \mathbb{Z}_2 & \text{if } n = 2, \\ \{e\} & \text{if } n \ge 3. \end{cases}$$
    Q.E.D.
:::
