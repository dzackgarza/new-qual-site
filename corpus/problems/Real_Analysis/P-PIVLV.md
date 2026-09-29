---
schema: qual/card@1
id: P-PIVLV
kind: problem
title: $L^q\subseteq L^p$ for $p<q$ implies no sets of arbitrarily large finite measure
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Let $(X, \mathcal{M}, \mu)$ be a measure space and $0 < p < q< \infty$.
Prove that if $L^q(X) \subseteq L^p(X)$, then $X$ does not contain sets of arbitrarily large finite measure.
:::

::: {.solution}
We prove the contrapositive. Assume $X$ contains measurable sets of arbitrarily large finite measure.

::: pf

::: pf-step

There are pairwise disjoint measurable $E_n$, $n \ge 1$, with $2^n \le \mu(E_n) < \infty$.

::: pf-proof

Inductively choose a measurable $B_n$ with $2^n + \sum_{k<n} \mu(E_k) \le \mu(B_n) < \infty$ and put $E_n = B_n \setminus \bigcup_{k<n} E_k$. Then $\mu(E_n) \ge \mu(B_n) - \sum_{k<n}\mu(E_k) \ge 2^n$, and $\mu(E_n) \le \mu(B_n) < \infty$.

:::

:::

::: {.pf-step #s2}

$f = \sum_n \mu(E_n)^{-1/p}\chi_{E_n}$ lies in $L^q \setminus L^p$.

::: pf-proof

The $E_n$ are disjoint, so $\int f^q = \sum_n \mu(E_n)^{1 - q/p} \le \sum_n 2^{n(1-q/p)} < \infty$ because $q/p > 1$, while $\int f^p = \sum_n 1 = \infty$.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} shows $L^q \not\subseteq L^p$.

:::

:::

:::
