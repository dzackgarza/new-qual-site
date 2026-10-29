---
schema: qual/card@1
id: P-YACKS
kind: problem
title: Compactness of $\{x\in\QQ \mid 2<x^2<3\}$ in $\QQ$
classification:
  areas:
  - real-analysis
  topics:
  - Compactness
  - Metric Spaces
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Consider the metric space $(\QQ,d)$ where $\QQ$ denotes the rational numbers and $d(x,y)=\abs{x-y}$.
Let $E=\{x\in\QQ:x>0,\,2<x^2<3\}$.
Is $E$ closed and bounded in $\QQ$?
Is $E$ compact in $\QQ$?
:::
::: {.solution}

::: pf

::: {.pf-step #bounded}

$E = \QQ \cap (\sqrt2, \sqrt3)$, in particular $E$ is bounded.

::: pf-proof

$E = \{q \in \QQ : q > 0,\ 2 < q^2 < 3\} = \{q \in \QQ : \sqrt2 < q < \sqrt3\}$, and $\sqrt3 < 2$, so $E \subseteq (0,2)$ is bounded.

:::

:::

::: {.pf-step #closed}

$E$ is closed in $\QQ$.

::: pf-proof

$E = \QQ \cap (\sqrt2, \sqrt3) = \QQ \cap [\sqrt2, \sqrt3]$, since $\sqrt2, \sqrt3 \notin \QQ$.

The set $[\sqrt2, \sqrt3]$ is closed in $\RR$, so its intersection with the subspace $\QQ$ is closed in $\QQ$.

:::

:::

::: {.pf-step #not-compact}

$E$ is not compact.

::: pf-proof

By density of $\QQ$ there are rationals $q_n$ with $\sqrt2 < q_n < \sqrt2 + 1/n$; then $q_n \in E$ for all $n$, and $q_n \to \sqrt2$ in $\RR$.

The sequence $(q_n)$ is Cauchy in the metric space $(\QQ, d)$: $\abs{q_n - q_m} < 1/n + 1/m \to 0$.
But it does not converge in $\QQ$: any limit would have to be $\sqrt2$ (uniqueness of limits in $\RR$), and $\sqrt2 \notin \QQ$.
Hence $E$ is not complete.
In a metric space, compact $\Rightarrow$ complete, so $E$ is not compact.
(Alternatively: compactness implies every sequence has a convergent subsequence, and no subsequence of $(q_n)$ converges in $\QQ$.)

:::

:::

::: pf-qed

By steps [](#bounded){.pf-ref}, [](#closed){.pf-ref} and [](#not-compact){.pf-ref}, $\boxed{E \text{ is closed and bounded in } \QQ \text{ but not compact.}}$ The Heine–Borel theorem fails in $\QQ$ because $\QQ$ is not complete.

:::

:::

:::
