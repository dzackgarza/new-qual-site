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

::: problem
- Show that every compact metrizable space has a countable basis.
:::

::: {.solution}
<1>1. For each $n \ge 1$, the open balls $\{B(x, 1/n) : x \in X\}$ form an open cover of $X$.
::: {.proof}
every point lies in its own ball.
:::

<1>2. Since $X$ is compact, there is a finite subcover $\{B(x_{n,1}, 1/n), \ldots, B(x_{n,k_n}, 1/n)\}$.
::: {.proof}
compactness.
:::

<1>3. Let $\mathcal B = \{B(x_{n,j}, 1/n) : n \ge 1,\ 1 \le j \le k_n\}$.
::: {.proof}
collect all these balls.
:::

<1>4. $\mathcal B$ is countable.
::: {.proof}
it is a countable union of finite sets.
:::

<1>5. $\mathcal B$ is a basis for the topology of $X$.
<2>1. Let $U$ be open and $x \in U$.
::: {.proof}
take an arbitrary point of an arbitrary open set.
:::
<2>2. There is $\epsilon > 0$ with $B(x, \epsilon) \subseteq U$.
::: {.proof}
$U$ is open.
:::
<2>3. Choose $n$ with $1/n < \epsilon/2$.
::: {.proof}
Archimedean property.
:::
<2>4. Since $\{B(x_{n,j}, 1/n)\}$ covers $X$, there is $j$ with $x \in B(x_{n,j}, 1/n)$.
::: {.proof}
<1>2.
:::
<2>5. Then $B(x_{n,j}, 1/n) \subseteq B(x, \epsilon) \subseteq U$.
::: {.proof}
if $y \in B(x_{n,j}, 1/n)$, then $d(x,y) \le d(x, x_{n,j}) + d(x_{n,j}, y) < 1/n + 1/n = 2/n < \epsilon$.
:::
<2>6. Hence every point of $U$ lies in a member of $\mathcal B$ contained in $U$.
::: {.proof}
<2>1–<2>5.
:::

<1>6. Therefore $\mathcal B$ is a countable basis.
::: {.proof}
<1>4 and <1>5.
:::

<1>7. Q.E.D.
::: {.proof}
<1>6.
:::
:::
