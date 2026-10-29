---
schema: qual/card@1
id: P-TC2PJ
kind: problem
title: Every compact metrizable space has a countable basis
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
  - Countability
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Show that every compact metrizable space has a countable basis.
:::

::: {.solution}
Let $X$ be compact with a metric $d$ inducing its topology, and write $B(x,r)$ for the open ball of radius $r$ about $x$.

::: pf

::: {.pf-step #finite}
For each $n \geq 1$ there are finitely many points $x_{n,1}, \ldots, x_{n,k_n}$ with $X = \bigcup_{j} B(x_{n,j}, 1/n)$.

::: pf-proof
The balls $B(x, 1/n)$, $x \in X$, form an open cover of $X$, which has a finite subcover because $X$ is compact.
:::

:::

::: pf-step
The countable family $\mathcal B = \{B(x_{n,j}, 1/n) : n \ge 1,\ 1 \le j \le k_n\}$ is a basis for the topology of $X$.

::: pf-proof
$\mathcal B$ is a countable union of finite sets of open sets.
Let $U$ be open and $x \in U$, and choose $\varepsilon > 0$ with $B(x,\varepsilon) \subseteq U$ and $n$ with $2/n < \varepsilon$.
By step [](#finite){.pf-ref} there is $j$ with $x \in B(x_{n,j}, 1/n)$.
For $y \in B(x_{n,j}, 1/n)$ we have $d(x,y) \le d(x, x_{n,j}) + d(x_{n,j}, y) < 2/n < \varepsilon$, so $x \in B(x_{n,j},1/n) \subseteq U$.
:::

:::

:::

:::
