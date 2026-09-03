---
schema: qual/card@1
id: E-3SU0X
kind: problem
title: Quotient topology on a three-point image of the line
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Check the details of Example 3 of §22: for the map $p: \mathbb{R} \to A = \ts{a, b, c}$ defined by

$$
p(x) =
\begin{cases}
a & \text{if } x > 0, \\
b & \text{if } x < 0, \\
c & \text{if } x = 0,
\end{cases}
$$

determine the quotient topology on $A$ induced by $p$.
:::

::: solution
**Goal:** Determine the quotient topology $\mathcal{T}_A$ on the 3-point set $A = \{a, b, c\}$ induced by the sign partition map $p: \mathbb{R} \to A$.

<1>1. Definition of quotient topology:
    A subset $U \subseteq A$ is open in the quotient topology $\mathcal{T}_A$ if and only if its preimage $p^{-1}(U)$ is an open subset of $\mathbb{R}$ in the standard Euclidean topology.

<1>2. Preimages of all subsets of $A$:
    *Proof:*
    <2>1. $\emptyset$: $p^{-1}(\emptyset) = \emptyset$, which is open in $\mathbb{R}$.
    <2>2. $\{a\}$: $p^{-1}(\{a\}) = (0, \infty)$, which is open in $\mathbb{R}$.
    <2>3. $\{b\}$: $p^{-1}(\{b\}) = (-\infty, 0)$, which is open in $\mathbb{R}$.
    <2>4. $\{c\}$: $p^{-1}(\{c\}) = \{0\}$, which is closed and not open in $\mathbb{R}$.
    <2>5. $\{a, b\}$: $p^{-1}(\{a, b\}) = (-\infty, 0) \cup (0, \infty) = \mathbb{R} \setminus \{0\}$, which is open in $\mathbb{R}$.
    <2>6. $\{a, c\}$: $p^{-1}(\{a, c\}) = [0, \infty)$, which is not open in $\mathbb{R}$ because it contains no open neighborhood around $0$.
    <2>7. $\{b, c\}$: $p^{-1}(\{b, c\}) = (-\infty, 0]$, which is not open in $\mathbb{R}$ because it contains no open neighborhood around $0$.
    <2>8. $\{a, b, c\}$: $p^{-1}(\{a, b, c\}) = \mathbb{R}$, which is open in $\mathbb{R}$.

<1>3. Conclusion:
    The quotient topology consists precisely of the subsets whose preimages are open:
    $$\mathcal{T}_A = \big\{\emptyset, \{a\}, \{b\}, \{a, b\}, \{a, b, c\}\big\}.$$
    *(Note: $A$ is non-Hausdorff and non-$T_1$, since the only open neighborhood of $c$ is the whole space $A$.)* Q.E.D.
:::
