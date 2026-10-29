---
schema: qual/card@1
id: E-ASWCD
kind: problem
title: Continuity of outer measure on Carathéodory-measurable sets
classification:
  areas:
  - real-analysis
  topics:
  - Continuity of Measure
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
Let $\mu^*$ be an outer measure on $X$ and let $\mathcal M(\mu^*)$ be its Carathéodory $\sigma$-algebra.

(a) Show that the restriction of $\mu^*$ to $\mathcal M(\mu^*)$ is continuous from below, and continuous from above when the first set has finite outer measure.

(b) Give an outer measure for which these continuity statements fail on arbitrary subsets of $X$.
:::

::: {.solution}

::: pf

::: pf-step

(a) $\mu^*$ restricted to $\mathcal M(\mu^*)$ is continuous from below, and continuous from above on sequences whose first set has finite outer measure.

::: pf-proof

::: {.pf-step #cara-measure}

$\mu \coloneqq \mu^*|_{\mathcal M(\mu^*)}$ is a countably additive measure on the $\sigma$-algebra $\mathcal M(\mu^*)$.

::: pf-proof

This is Carathéodory's theorem.

:::

:::

::: {.pf-step #from-below}

If $E_1 \subseteq E_2 \subseteq \cdots$ lie in $\mathcal M(\mu^*)$, then $\mu^*\qty{\bigcup_n E_n} = \lim_{N\to\infty} \mu^*(E_N)$.

::: pf-proof

Set $F_1 = E_1$ and $F_n = E_n \setminus E_{n-1}$ for $n \ge 2$. The $F_n$ are pairwise disjoint and measurable, $\bigcup_{n \le N} F_n = E_N$, and $\bigcup_n F_n = \bigcup_n E_n$. By step [](#cara-measure){.pf-ref},
$$
\mu^*\qty{\bigcup_{n\ge1}E_n}
=\sum_{n\ge1}\mu^*(F_n)
=\lim_{N\to\infty}\sum_{n=1}^N\mu^*(F_n)
=\lim_{N\to\infty}\mu^*(E_N).
$$

:::

:::

::: pf-step

If $E_1 \supseteq E_2 \supseteq \cdots$ lie in $\mathcal M(\mu^*)$ and $\mu^*(E_1) < \infty$, then $\mu^*\qty{\bigcap_n E_n} = \lim_{n\to\infty} \mu^*(E_n)$.

::: pf-proof

Put $F_n = E_1 \setminus E_n$. Then $F_n$ increases to $E_1 \setminus \bigcap_n E_n$, so step [](#from-below){.pf-ref} and finite additivity give
$$
\mu^*(E_1)-\mu^*\qty{\bigcap_nE_n}
=\lim_{n\to\infty}\mu^*(F_n)
=\mu^*(E_1)-\lim_{n\to\infty}\mu^*(E_n).
$$
Since $\mu^*(E_1) < \infty$, every term is finite and $\mu^*(E_1)$ cancels.

:::

:::

:::

:::

::: pf-step

(b) On $X = \NN$, the function $\mu^*(\emptyset) = 0$, $\mu^*(A) = 1$ for $A$ finite and nonempty, and $\mu^*(A) = 2$ for $A$ infinite is an outer measure for which continuity from below and continuity from above both fail on arbitrary subsets.

::: pf-proof

::: pf-step

$\mu^*$ is an outer measure.

::: pf-proof

$\mu^*(\emptyset) = 0$ and monotonicity are immediate. For countable subadditivity, let $A = \bigcup_i A_i$. If $A$ is infinite, then some $A_i$ is infinite or infinitely many $A_i$ are nonempty, so $\sum_i \mu^*(A_i) \ge 2$. If $A$ is finite and nonempty, some $A_i$ is nonempty, so $\sum_i \mu^*(A_i) \ge 1$.

:::

:::

::: pf-step

Continuity from below fails.

::: pf-proof

For $E_n = \theset{1, \ldots, n}$, $\mu^*(E_n) = 1$ for all $n$, while $\mu^*\qty{\bigcup_n E_n} = \mu^*(\NN) = 2$.

:::

:::

::: pf-step

Continuity from above fails although the first set has finite outer measure.

::: pf-proof

For $G_n = \theset{n, n+1, \ldots}$, $\mu^*(G_n) = 2$ for all $n$ and $\mu^*(G_1) = 2 < \infty$, while $\mu^*\qty{\bigcap_n G_n} = \mu^*(\emptyset) = 0$.

:::

:::

:::

:::

:::

:::
