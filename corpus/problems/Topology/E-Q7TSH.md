---
schema: qual/card@1
id: E-Q7TSH
kind: problem
title: Every countable discrete space is separable
classification:
  areas:
  - topology
  topics:
  - Countability
  - Density
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}
Show that any countable space with the discrete topology is separable.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Definition of separability:

::: pf-proof

::: pf-step

A topological space $(X, \mathcal{T})$ is **separable** if there exists a subset $D \subseteq X$ such that:
(i) $D$ is at most countable ($|D| \le \aleph_0$), and
(ii) $D$ is dense in $X$ ($\overline{D} = X$).

::: pf-proof

standard definition of separability.

:::

:::

:::

:::

::: {.pf-step #s2}

Verification for a countable discrete space:

::: pf-proof

::: pf-step

Let $X$ be a countable space equipped with the discrete topology $\mathcal{T} = \mathcal{P}(X)$.
Choose the subset $D = X \subseteq X$.

::: pf-proof

choice of $D$.

:::

:::

::: pf-step

$D = X$ is countable by the hypothesis that $X$ is countable.

::: pf-proof

hypothesis.

:::

:::

::: pf-step

The closure of the whole space is $\overline{D} = \overline{X} = X$, so $D$ is dense in $X$.

::: pf-proof

property of topological closure.

:::

:::

:::

:::

::: pf-step

Conclusion:
Since $D = X$ is a countable dense subset of $X$, $(X, \mathcal{T})$ is separable. Q.E.D.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

:::

:::
