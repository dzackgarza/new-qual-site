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

::: exercise
Show that any countable space with the discrete topology is separable.
:::

::: {.solution}
<1>1. Definition of separability:
<2>1. A topological space $(X, \mathcal{T})$ is **separable** if there exists a subset $D \subseteq X$ such that:
(i) $D$ is at most countable ($|D| \le \aleph_0$), and
(ii) $D$ is dense in $X$ ($\overline{D} = X$).
::: {.proof}
standard definition of separability.
:::

<1>2. Verification for a countable discrete space:
<2>1. Let $X$ be a countable space equipped with the discrete topology $\mathcal{T} = \mathcal{P}(X)$.
Choose the subset $D = X \subseteq X$.
::: {.proof}
choice of $D$.
:::
<2>2. $D = X$ is countable by the hypothesis that $X$ is countable.
::: {.proof}
hypothesis.
:::
<2>3. The closure of the whole space is $\overline{D} = \overline{X} = X$, so $D$ is dense in $X$.
::: {.proof}
property of topological closure.
:::

<1>3. Conclusion:
Since $D = X$ is a countable dense subset of $X$, $(X, \mathcal{T})$ is separable. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
