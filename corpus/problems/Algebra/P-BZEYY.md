---
schema: qual/card@1
id: P-BZEYY
kind: problem
title: Every permutation in $S_n$ is a product of disjoint cycles
classification:
  areas:
  - algebra
  topics:
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
- Show that every permutation in $S_n$ can be written as a product of pairwise disjoint cycles.
:::

::: {.solution}
Let $\sigma\in S_n$ act on $\{1,\ldots,n\}$.

::: pf

::: {.pf-step #s1}

The orbits of the cyclic group $\langle\sigma\rangle$ partition $\{1,\ldots,n\}$.

::: pf-proof

Orbit equivalence under a group action is an equivalence relation, so the orbits are pairwise disjoint and cover the set.

:::

:::

::: pf-step

Each nontrivial orbit determines a cycle.

::: pf-proof

If
\[
\mathcal O=\{a,\sigma(a),\ldots,\sigma^{r-1}(a)\}
\]
with $r$ minimal such that $\sigma^r(a)=a$, define
\[
c_{\mathcal O}=(a\ \sigma(a)\ \cdots\ \sigma^{r-1}(a)).
\]
On this orbit, $c_{\mathcal O}$ agrees with $\sigma$.

:::

:::

::: pf-step

The cycles from distinct orbits are disjoint and their product equals $\sigma$.

::: pf-proof

Distinct orbits are disjoint by step [](#s1){.pf-ref}, so the corresponding cycles have disjoint supports and commute. Their product agrees with $\sigma$ on every nontrivial orbit and fixes every fixed point of $\sigma$, hence equals $\sigma$.

:::

:::

::: pf-step

The disjoint-cycle decomposition is unique up to reordering the cycles and cyclically rotating the notation within each cycle.

::: pf-proof

The supports of the cycles are exactly the nontrivial orbits of $\langle\sigma\rangle$, and those orbits are uniquely determined by $\sigma$. On each orbit the cyclic ordering is determined by repeated application of $\sigma$, up to the choice of starting point.

:::

:::

:::

:::
