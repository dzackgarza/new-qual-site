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
- Show that every compact metrizable space has a countable basis.
:::

::: {.solution}

::: pf

::: pf-step

For each $n \ge 1$, the open balls $\{B(x, 1/n) : x \in X\}$ form an open cover of $X$.

::: pf-proof

every point lies in its own ball.

:::

:::

::: {.pf-step #s2}

Since $X$ is compact, there is a finite subcover $\{B(x_{n,1}, 1/n), \ldots, B(x_{n,k_n}, 1/n)\}$.

::: pf-proof

compactness.

:::

:::

::: pf-step

Let $\mathcal B = \{B(x_{n,j}, 1/n) : n \ge 1,\ 1 \le j \le k_n\}$.

::: pf-proof

collect all these balls.

:::

:::

::: {.pf-step #s4}

$\mathcal B$ is countable.

::: pf-proof

it is a countable union of finite sets.

:::

:::

::: {.pf-step #s5}

$\mathcal B$ is a basis for the topology of $X$.

::: pf-proof

::: {.pf-step #s5-1}

Let $U$ be open and $x \in U$.

::: pf-proof

take an arbitrary point of an arbitrary open set.

:::

:::

::: {.pf-step #s5-2}

There is $\epsilon > 0$ with $B(x, \epsilon) \subseteq U$.

::: pf-proof

$U$ is open.

:::

:::

::: {.pf-step #s5-3}

Choose $n$ with $1/n < \epsilon/2$.

::: pf-proof

Archimedean property.

:::

:::

::: {.pf-step #s5-4}

Since $\{B(x_{n,j}, 1/n)\}$ covers $X$, there is $j$ with $x \in B(x_{n,j}, 1/n)$.

::: pf-proof

Step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s5-5}

Then $B(x_{n,j}, 1/n) \subseteq B(x, \epsilon) \subseteq U$.

::: pf-proof

if $y \in B(x_{n,j}, 1/n)$, then $d(x,y) \le d(x, x_{n,j}) + d(x_{n,j}, y) < 1/n + 1/n = 2/n < \epsilon$.

:::

:::

::: pf-step

Hence every point of $U$ lies in a member of $\mathcal B$ contained in $U$.

::: pf-proof

Steps [](#s5-1){.pf-ref}, [](#s5-2){.pf-ref}, [](#s5-3){.pf-ref}, [](#s5-4){.pf-ref} and [](#s5-5){.pf-ref}.

:::

:::

:::

:::

::: {.pf-step #s6}

Therefore $\mathcal B$ is a countable basis.

::: pf-proof

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref}.

:::

:::

:::
