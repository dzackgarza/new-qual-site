---
schema: qual/card@1
id: E-66SIM
kind: problem
title: Locally compact Hausdorff spaces are Baire spaces
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that every locally compact Hausdorff space is a Baire space.
:::

::: {.solution}

::: pf

::: pf-step

Reduction:
    Let $X$ be a locally compact Hausdorff space, and let $\{U_n\}_{n=1}^\infty$ be a countable collection of open dense subsets of $X$.
    Let $W \subseteq X$ be an arbitrary non-empty open set.
    It suffices to show that $W \cap \left( \bigcap_{n=1}^\infty U_n \right) \neq \varnothing$.

:::

::: {.pf-step #s2}

Regularity and compact neighborhood property:
    In a locally compact Hausdorff space, for every point $x$ and every open neighborhood $V$ of $x$, there exists an open neighborhood $U$ of $x$ such that $\overline{U}$ is compact and $\overline{U} \subseteq V$.

:::

::: pf-step

Inductive construction of nested compact closures:
    We inductively construct a sequence of non-empty open sets $\{V_n\}_{n=1}^\infty$ such that $\overline{V_1} \subseteq W \cap U_1$, and for each $k \ge 2$, $\overline{V_k}$ is compact with $\overline{V_k} \subseteq V_{k-1} \cap U_k$.
    *Proof:*

::: pf-proof

::: pf-step

**Base step ($k=1$):**
        Since $U_1$ is dense in $X$, the open set $W \cap U_1$ is non-empty. Pick $x_1 \in W \cap U_1$. By step [](#s2){.pf-ref}, choose a non-empty open set $V_1$ such that $\overline{V_1}$ is compact and $\overline{V_1} \subseteq W \cap U_1$.

:::

::: pf-step

**Inductive step ($k \ge 2$):**
        Assume $V_{k-1}$ is a non-empty open set. Since $U_k$ is dense in $X$, $V_{k-1} \cap U_k$ is a non-empty open set. Pick $x_k \in V_{k-1} \cap U_k$. By step [](#s2){.pf-ref}, choose a non-empty open set $V_k$ such that $\overline{V_k}$ is compact and $\overline{V_k} \subseteq V_{k-1} \cap U_k$.

:::

::: pf-step

In particular, $\overline{V_k} \subseteq V_{k-1} \subseteq \overline{V_{k-1}}$ for all $k \ge 2$.

:::

:::

:::

::: pf-step

Non-empty intersection via compactness:
    *Proof:*

::: pf-proof

::: pf-step

The sequence $\{\overline{V_n}\}_{n=1}^\infty$ is a nested sequence of non-empty closed subsets of the compact space $\overline{V_1}$:
        $$\overline{V_1} \supseteq \overline{V_2} \supseteq \overline{V_3} \supseteq \cdots$$

:::

::: pf-step

By the finite intersection property of compact spaces, the total intersection is non-empty:
        $$\bigcap_{n=1}^\infty \overline{V_n} \neq \varnothing.$$

:::

::: pf-step

Choose an element $x \in \bigcap_{n=1}^\infty \overline{V_n}$.

:::

::: pf-step

For every $n \ge 1$, $x \in \overline{V_n} \subseteq U_n$.

:::

::: pf-step

Furthermore, $x \in \overline{V_1} \subseteq W$.

:::

::: pf-step

Thus $x \in W \cap \left( \bigcap_{n=1}^\infty U_n \right)$.

:::

:::

:::

:::

    By step [](#s4){.pf-ref}, $W \cap \left( \bigcap_{n=1}^\infty U_n \right)$ is non-empty for every non-empty open set $W$, so $\bigcap_{n=1}^\infty U_n$ is dense in $X$. Hence $X$ is a Baire space.
:::
