---
schema: qual/card@1
id: E-MUN-6-6
kind: problem
title: Bijection between $\mathcal{P}(A)$ and $X^n$
classification:
  areas:
  - topology
  topics:
  - Finite Sets
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

(a) Let $A = \{1, \ldots, n\}$ . Show there is a bijection of $\mathcal{P}(A)$ with the cartesian product $X^n$, where $X$ is the two-element set $X = \{0, 1\}$ .

(b) Show that if $A$ is finite, then $\mathcal{P}(A)$ is finite.
:::

::: {.solution}
<1>1. Map $\mathcal P(A)\to X^n$ by $S\mapsto (\chi_S(1),\dots,\chi_S(n))$ where $\chi_S$ characteristic.
::: {.proof}
bijection, inverse $(x_i)\mapsto\{i:x_i=1\}$.
:::

<1>2. Hence $|\mathcal P(A)|=2^n$ finite.
::: {.proof}
$X^n$ has $2^n$ elements.
:::

<1>3. Q.E.D.
::: {.proof}
<1>2.
:::
:::
