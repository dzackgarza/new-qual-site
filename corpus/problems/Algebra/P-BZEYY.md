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

::: problem
- Show that every permutation in $S_n$ can be written as a product of pairwise disjoint cycles.
:::


::: {.solution}
Let $\sigma\in S_n$ act on $\{1,\ldots,n\}$.

<1>1. The orbits of the cyclic group $\langle\sigma\rangle$ partition $\{1,\ldots,n\}$.
::: {.proof}
Orbit equivalence under a group action is an equivalence relation, so the orbits are pairwise disjoint and cover the set.
:::

<1>2. Each nontrivial orbit determines a cycle.
::: {.proof}
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

<1>3. The cycles from distinct orbits are disjoint and their product equals $\sigma$.
::: {.proof}
Distinct orbits are disjoint by <1>1, so the corresponding cycles have disjoint supports and commute. Their product agrees with $\sigma$ on every nontrivial orbit and fixes every fixed point of $\sigma$, hence equals $\sigma$.
:::

<1>4. The disjoint-cycle decomposition is unique up to reordering the cycles and cyclically rotating the notation within each cycle.
::: {.proof}
The supports of the cycles are exactly the nontrivial orbits of $\langle\sigma\rangle$, and those orbits are uniquely determined by $\sigma$. On each orbit the cyclic ordering is determined by repeated application of $\sigma$, up to the choice of starting point.
:::
:::
