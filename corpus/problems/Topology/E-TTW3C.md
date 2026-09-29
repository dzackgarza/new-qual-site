---
schema: qual/card@1
id: E-TTW3C
kind: problem
title: A continuous map of metric spaces is uniformly continuous on compact subsets
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Uniform Continuity
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
Show that if $f: A\to B$ is a continuous map between metric spaces and $K\subset A$ is compact, then $\restrictionof{f}{K}$ is uniformly continuous.
:::

::: {.solution}
**Goal:** Show that if $f: A \to B$ is a continuous map between metric spaces and $K \subset A$ is compact, then the restriction $\restrictionof{f}{K}$ is uniformly continuous.

::: pf

::: {.pf-step #s1}

Assume, toward a contradiction, that $\restrictionof{f}{K}$ is not uniformly continuous.

::: pf-proof

Then there is $\varepsilon > 0$ and sequences $x_n, y_n \in K$ with $d(x_n, y_n) \to 0$ but $d(f(x_n), f(y_n)) \geq \varepsilon$ for all $n$.

:::

:::

::: {.pf-step #s2}

$K$ is sequentially compact.

::: pf-proof

In metric spaces, compactness implies sequential compactness (every sequence has a convergent subsequence); $K$ is compact by hypothesis.

:::

:::

::: {.pf-step #s3}

$(x_n)$ has a subsequence $(x_{n_j})$ converging to some $x \in K$.

::: pf-proof

Step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

$y_{n_j} \to x$ as well.

::: pf-proof

$d(y_{n_j}, x) \leq d(y_{n_j}, x_{n_j}) + d(x_{n_j}, x) \to 0 + 0 = 0$ using steps [](#s1){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

$f(x_{n_j}) \to f(x)$ and $f(y_{n_j}) \to f(x)$.

::: pf-proof

Continuity of $f$ at $x$, applied to the sequences steps [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s6}

$d(f(x_{n_j}), f(y_{n_j})) \to 0$.

::: pf-proof

Triangle inequality: $d(f(x_{n_j}), f(y_{n_j})) \leq d(f(x_{n_j}), f(x)) + d(f(x), f(y_{n_j})) \to 0$ by step [](#s5){.pf-ref}.

:::

:::

::: pf-step

Contradiction.

::: pf-proof

Step [](#s6){.pf-ref} contradicts $d(f(x_n), f(y_n)) \geq \varepsilon > 0$ from step [](#s1){.pf-ref}.

:::

:::

::: pf-qed

The assumption step [](#s1){.pf-ref} leads to a contradiction, so $\restrictionof{f}{K}$ is uniformly continuous.

:::

:::

:::
