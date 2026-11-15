---
schema: qual/card@1
id: E-4PQ1O
kind: problem
title: Coordinatewise convergence of nets in products
classification:
  areas:
  - topology
  topics:
  - Nets
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    No published set for this exercise was located. The sources searched, the pages they
    cover and the conclusion are recorded in COMPLAINTS.md under the entry for the net
    exercises of §29; the card's own proof is kept. The statement was read against Munkres,
    Topology (2000), §29 supplementary exercises on nets, printed pp. 187-188.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Transcribed from dbFin, "Supplementary Exercises*: Nets: Problem 4 Solution",
    https://dbfin.com/topology/munkres/chapter-3/supplementary-exercises-nets/problem-4-solution/,
    read 2026-11-15, text at tmp/sources/dbfin/supplementary-exercises-nets/problem-4.md: a
    neighborhood of x X y contains a basis neighborhood U X V, convergence of the two nets gives
    indices alpha and beta, and directedness gives gamma dominating both; the one correction is
    that dbFin writes "Since J is a net" where the directedness of the index set J is meant. The
    argument also agrees, restricted to two factors and a common index set, with Henno Brandsma's
    answer to Math StackExchange 3373343 (2019-09-28), whose point is that a common upper bound
    replaces the maximum. This supersedes the 2026-11-10 note above.
---

::: {.exercise}

Suppose that

$$
(x_\alpha)_{\alpha \in J} \to x \text{ in } X \quad \text{and} \quad (y_\alpha)_{\alpha \in J} \to y \text{ in } Y.
$$

Show that $(x_\alpha \times y_\alpha) \to x \times y$ in $X \times Y$.
:::

::: {.solution}

::: pf

::: pf-step
Every neighborhood of $x \times y$ in $X \times Y$ contains a set $U \times V$ with $U$ a neighborhood of $x$ in $X$ and $V$ a neighborhood of $y$ in $Y$.

::: pf-proof
The sets $U \times V$, for $U$ open in $X$ and $V$ open in $Y$, form a basis for the product topology, so a neighborhood of $x \times y$ contains such a set with $x \times y \in U \times V$, that is, with $x \in U$ and $y \in V$.
:::

:::

::: pf-step
There is $\gamma \in J$ with $x_\alpha \in U$ and $y_\alpha \in V$ for every $\alpha \succeq \gamma$.

::: pf-proof
By convergence of $(x_\alpha)$ there is $\alpha_0 \in J$ with $x_\alpha \in U$ whenever $\alpha_0 \preceq \alpha$, and by convergence of $(y_\alpha)$ there is $\beta_0 \in J$ with $y_\alpha \in V$ whenever $\beta_0 \preceq \alpha$. Since $J$ is directed, some $\gamma \in J$ satisfies $\alpha_0 \preceq \gamma$ and $\beta_0 \preceq \gamma$; transitivity then gives $x_\alpha \in U$ and $y_\alpha \in V$ for every $\alpha \succeq \gamma$.
:::

:::

::: pf-step
$(x_\alpha \times y_\alpha) \to x \times y$ in $X \times Y$. $\square$

::: pf-proof
Let $W$ be a neighborhood of $x \times y$. By step 1 it contains $U \times V$ with $U$ and $V$ as there, and by step 2 the index $\gamma$ has the property that $\gamma \preceq \alpha$ implies $x_\alpha \times y_\alpha \in U \times V \subset W$. So for each neighborhood $W$ of $x \times y$ such a $\gamma$ exists, which is the definition of convergence of the net $(x_\alpha \times y_\alpha)$ to $x \times y$.
:::

:::

:::

:::
