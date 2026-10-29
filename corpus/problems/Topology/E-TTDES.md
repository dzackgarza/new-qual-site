---
schema: qual/card@1
id: E-TTDES
kind: problem
title: Compact, limit-point compact, and sequentially compact coincide for second-countable
  Hausdorff or metric spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Countability
  - Convergence
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that if $X$ is second-countable and Hausdorff (or a metric space), then the following are equivalent:
(1) $X$ is compact (every open cover has a finite subcover).
(2) $X$ is limit-point compact (every infinite subset $A \subseteq X$ has a limit point in $X$).
(3) $X$ is sequentially compact (every sequence in $X$ has a convergent subsequence in $X$).
:::

::: {.solution}

A metric space is first-countable and Hausdorff; a second-countable space is first-countable. The arguments for (1)$\Rightarrow$(2) and (2)$\Rightarrow$(3) use only that $X$ is first-countable and Hausdorff.

::: pf

::: pf-step

(1)$\Rightarrow$(2).

::: pf-proof

Suppose $X$ is compact and $A\subseteq X$ is infinite with no limit point. Then every $x\in X$ has an open neighborhood $U_x$ with $U_x\cap A\subseteq\{x\}$. A finite subcover $U_{x_1},\ldots,U_{x_m}$ gives $A\subseteq\{x_1,\ldots,x_m\}$, contradicting that $A$ is infinite.

:::

:::

::: pf-step

(2)$\Rightarrow$(3).

::: pf-proof

::: pf-step

Let $(x_n)$ be a sequence. If its range is finite, it has a convergent subsequence.

::: pf-proof

Some value occurs infinitely often and gives a constant subsequence.

:::

:::

::: {.pf-step #limit}

If the range $S$ is infinite, it has a limit point $x$, and every neighborhood of $x$ contains infinitely many points of $S$.

::: pf-proof

The limit point exists by (2). If a neighborhood $U$ of $x$ contained only finitely many points of $S\setminus\{x\}$, then removing them, which is possible because points are closed in a Hausdorff space, would give a neighborhood of $x$ meeting $S$ in at most $\{x\}$.

:::

:::

::: pf-step

If the range is infinite, $(x_n)$ has a subsequence converging to $x$.

::: pf-proof

Choose a decreasing countable neighborhood basis $B_1\supseteq B_2\supseteq\cdots$ at $x$. By step [](#limit){.pf-ref}, each $B_k$ contains $x_n$ for infinitely many $n$, so we may choose $n_1<n_2<\cdots$ with $x_{n_k}\in B_k$. Then $x_{n_k}\to x$.

:::

:::

:::

:::

::: pf-step

(3)$\Rightarrow$(1) when $X$ is second-countable.

::: pf-proof

::: {.pf-step #countable}

Every open cover of $X$ has a countable subcover.

::: pf-proof

Let $\mathcal B$ be a countable basis. For each $B\in\mathcal B$ contained in some member of the cover, choose one such member. These countably many chosen sets cover $X$, since each point lies in a basis element inside some member of the cover.

:::

:::

::: pf-step

Every open cover of $X$ has a finite subcover.

::: pf-proof

By step [](#countable){.pf-ref}, it suffices to treat a countable open cover $U_1,U_2,\ldots$. Suppose it has no finite subcover, and choose $x_N\in X\setminus(U_1\cup\cdots\cup U_N)$ for each $N$. By (3), a subsequence $x_{N_k}$ converges to some $x$. Choose $m$ with $x\in U_m$. Then $x_{N_k}\in U_m$ for all large $k$, while $N_k\ge m$ for all large $k$ forces $x_{N_k}\notin U_m$, a contradiction.

:::

:::

:::

:::

::: pf-step

(3)$\Rightarrow$(1) when $X$ is a metric space.

::: pf-proof

A sequentially compact metric space is complete and totally bounded, and a complete totally bounded metric space is compact.

:::

:::

:::

:::
