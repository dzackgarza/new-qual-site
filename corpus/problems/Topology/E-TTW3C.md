---
schema: qual/card@1
id: E-TTW3C
kind: exercise
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

::: exercise
Show that if $f: A\to B$ is a continuous map between metric spaces and $K\subset A$ is compact, then $\restrictionof{f}{K}$ is uniformly continuous.
:::

::: {.solution}
**Goal:** Show that if $f: A \to B$ is a continuous map between metric spaces and $K \subset A$ is compact, then the restriction $\restrictionof{f}{K}$ is uniformly continuous.

<1>1. Assume, toward a contradiction, that $\restrictionof{f}{K}$ is not uniformly continuous.
::: {.proof}
Then there is $\varepsilon > 0$ and sequences $x_n, y_n \in K$ with $d(x_n, y_n) \to 0$ but $d(f(x_n), f(y_n)) \geq \varepsilon$ for all $n$.
:::

<1>2. $K$ is sequentially compact.
::: {.proof}
In metric spaces, compactness implies sequential compactness (every sequence has a convergent subsequence); $K$ is compact by hypothesis.
:::

<1>3. $(x_n)$ has a subsequence $(x_{n_j})$ converging to some $x \in K$.
::: {.proof}
<1>2.
:::

<1>4. $y_{n_j} \to x$ as well.
::: {.proof}
$d(y_{n_j}, x) \leq d(y_{n_j}, x_{n_j}) + d(x_{n_j}, x) \to 0 + 0 = 0$ using <1>1 and <1>3.
:::

<1>5. $f(x_{n_j}) \to f(x)$ and $f(y_{n_j}) \to f(x)$.
::: {.proof}
Continuity of $f$ at $x$, applied to the sequences <1>3 and <1>4.
:::

<1>6. $d(f(x_{n_j}), f(y_{n_j})) \to 0$.
::: {.proof}
Triangle inequality: $d(f(x_{n_j}), f(y_{n_j})) \leq d(f(x_{n_j}), f(x)) + d(f(x), f(y_{n_j})) \to 0$ by <1>5.
:::

<1>7. Contradiction.
::: {.proof}
<1>6 contradicts $d(f(x_n), f(y_n)) \geq \varepsilon > 0$ from <1>1.
:::

<1>8. Q.E.D.
::: {.proof}
The assumption <1>1 leads to a contradiction, so $\restrictionof{f}{K}$ is uniformly continuous.
:::
:::
