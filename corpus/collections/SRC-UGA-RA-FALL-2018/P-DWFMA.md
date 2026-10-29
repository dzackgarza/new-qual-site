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

::: {.problem}
Let $E \subseteq \RR$ be a Lebesgue measurable set. Show that there exists a Borel set $B \subseteq E$ such that $m(E \setminus B) = 0$.
:::

::: {.solution}
**Goal:** Prove that every Lebesgue measurable set contains an $F_\sigma$ Borel subset differing by a set of Lebesgue measure zero, using closed approximations on finite-measure pieces.

::: pf

::: {.pf-step #s1}

Case 1: $E$ has finite measure ($m(E) < \infty$).

::: pf-proof

::: pf-step

By the regularity of Lebesgue measure (or outer regularity applied to $E^c$), for every $\varepsilon > 0$, there exists a closed set $F \subseteq E$ such that $m(E \setminus F) < \varepsilon$.

:::

::: pf-step

For each $n \in \NN_{\ge 1}$, choose a closed set $F_n \subseteq E$ such that
    $$m(E \setminus F_n) < \frac{1}{n}.$$

:::

::: pf-step

Define $B = \bigcup_{n=1}^\infty F_n$.

:::

::: pf-step

$B$ is a Borel set: Each $F_n$ is closed in $\RR$, so $B$ is an $F_\sigma$ set, hence a Borel set.

:::

::: pf-step

$B \subseteq E$: Since each $F_n \subseteq E$, the union satisfies $B = \bigcup_{n=1}^\infty F_n \subseteq E$.

:::

::: pf-step

Measure of the difference: For every $n \ge 1$:
    $$E \setminus B = E \setminus \bigcup_{k=1}^\infty F_k \subseteq E \setminus F_n.$$

:::

::: pf-step

By monotonicity of Lebesgue measure:
    $$m(E \setminus B) \le m(E \setminus F_n) < \frac{1}{n} \quad \text{for all } n \ge 1.$$

:::

::: pf-step

Taking $n \to \infty$ yields $m(E \setminus B) = 0$.

:::

:::

:::

::: pf-step

Case 2: $E$ has arbitrary (possibly infinite) measure.

::: pf-proof

::: pf-step

Partition $\RR$ into bounded intervals: $\RR = \bigsqcup_{k \in \ZZ} [k, k+1)$.

:::

::: pf-step

For each $k \in \ZZ$, define the bounded measurable set $E_k = E \cap [k, k+1)$.

:::

::: pf-step

Then $E = \bigsqcup_{k \in \ZZ} E_k$, and $m(E_k) \le m([k, k+1)) = 1 < \infty$.

:::

::: pf-step

By Case 1 (step [](#s1){.pf-ref}), for each $k \in \ZZ$, there exists a Borel set $B_k \subseteq E_k$ such that
    $$m(E_k \setminus B_k) = 0.$$

:::

::: pf-step

Define $B = \bigcup_{k \in \ZZ} B_k$.

:::

::: pf-step

$B$ is a Borel set as a countable union of Borel sets $B_k$.

:::

::: pf-step

$B \subseteq E$ because $B = \bigcup_{k \in \ZZ} B_k \subseteq \bigcup_{k \in \ZZ} E_k = E$.

:::

::: pf-step

The difference satisfies:
    $$E \setminus B = \left( \bigcup_{k \in \ZZ} E_k \right) \setminus \left( \bigcup_{j \in \ZZ} B_j \right) \subseteq \bigcup_{k \in \ZZ} (E_k \setminus B_k).$$

:::

::: pf-step

By countable subadditivity of Lebesgue measure:
    $$m(E \setminus B) \le \sum_{k \in \ZZ} m(E_k \setminus B_k) = \sum_{k \in \ZZ} 0 = 0.$$

:::

::: pf-step

Thus $m(E \setminus B) = 0$.

:::

:::

:::

::: pf-step

Conclusion:

::: pf-proof

Every Lebesgue measurable set $E \subseteq \RR$ contains a Borel set $B \subseteq E$ such that $m(E \setminus B) = 0$.

:::

:::

:::

:::
