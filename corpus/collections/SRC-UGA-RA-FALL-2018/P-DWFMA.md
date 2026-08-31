---
schema: qual/card@1
id: P-DWFMA
kind: problem
title: Every Lebesgue measurable set contains a Borel set of full measure
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: problem
Let $E \subseteq \mathbb{R}$ be a Lebesgue measurable set. Show that there exists a Borel set $B \subseteq E$ such that $m(E \setminus B) = 0$.
:::

::: solution
**Goal:** Prove that every Lebesgue measurable set contains an $F_\sigma$ Borel subset differing by a set of Lebesgue measure zero, using closed approximations on finite-measure pieces.

<1>1. Case 1: $E$ has finite measure ($m(E) < \infty$).
    *Proof:*
    <2>1. By the regularity of Lebesgue measure (or outer regularity applied to $E^c$), for every $\varepsilon > 0$, there exists a closed set $F \subseteq E$ such that $m(E \setminus F) < \varepsilon$.
    <2>2. For each $n \in \mathbb{N}_{\ge 1}$, choose a closed set $F_n \subseteq E$ such that
    $$m(E \setminus F_n) < \frac{1}{n}.$$
    <2>3. Define $B = \bigcup_{n=1}^\infty F_n$.
    <2>4. $B$ is a Borel set: Each $F_n$ is closed in $\mathbb{R}$, so $B$ is an $F_\sigma$ set, hence a Borel set.
    <2>5. $B \subseteq E$: Since each $F_n \subseteq E$, the union satisfies $B = \bigcup_{n=1}^\infty F_n \subseteq E$.
    <2>6. Measure of the difference: For every $n \ge 1$:
    $$E \setminus B = E \setminus \bigcup_{k=1}^\infty F_k \subseteq E \setminus F_n.$$
    <2>7. By monotonicity of Lebesgue measure:
    $$m(E \setminus B) \le m(E \setminus F_n) < \frac{1}{n} \quad \text{for all } n \ge 1.$$
    <2>8. Taking $n \to \infty$ yields $m(E \setminus B) = 0$.

<1>2. Case 2: $E$ has arbitrary (possibly infinite) measure.
    *Proof:*
    <2>1. Partition $\mathbb{R}$ into bounded intervals: $\mathbb{R} = \bigsqcup_{k \in \mathbb{Z}} [k, k+1)$.
    <2>2. For each $k \in \mathbb{Z}$, define the bounded measurable set $E_k = E \cap [k, k+1)$.
    <2>3. Then $E = \bigsqcup_{k \in \mathbb{Z}} E_k$, and $m(E_k) \le m([k, k+1)) = 1 < \infty$.
    <2>4. By Case 1 (<1>1), for each $k \in \mathbb{Z}$, there exists a Borel set $B_k \subseteq E_k$ such that
    $$m(E_k \setminus B_k) = 0.$$
    <2>5. Define $B = \bigcup_{k \in \mathbb{Z}} B_k$.
    <2>6. $B$ is a Borel set as a countable union of Borel sets $B_k$.
    <2>7. $B \subseteq E$ because $B = \bigcup_{k \in \mathbb{Z}} B_k \subseteq \bigcup_{k \in \mathbb{Z}} E_k = E$.
    <2>8. The difference satisfies:
    $$E \setminus B = \left( \bigcup_{k \in \mathbb{Z}} E_k \right) \setminus \left( \bigcup_{j \in \mathbb{Z}} B_j \right) \subseteq \bigcup_{k \in \mathbb{Z}} (E_k \setminus B_k).$$
    <2>9. By countable subadditivity of Lebesgue measure:
    $$m(E \setminus B) \le \sum_{k \in \mathbb{Z}} m(E_k \setminus B_k) = \sum_{k \in \mathbb{Z}} 0 = 0.$$
    <2>10. Thus $m(E \setminus B) = 0$.

<1>3. Conclusion:
    *Proof:*
    Every Lebesgue measurable set $E \subseteq \mathbb{R}$ contains a Borel set $B \subseteq E$ such that $m(E \setminus B) = 0$.
:::

