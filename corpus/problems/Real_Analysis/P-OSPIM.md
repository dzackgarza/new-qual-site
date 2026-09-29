---
schema: qual/card@1
id: P-OSPIM
kind: problem
title: Measurability of $\inf_k f_k$ and $\sup_k f_k$, Fatou's lemma, and the monotone
  convergence theorem from Fatou
classification:
  areas:
  - real-analysis
  topics:
  - Fatou
  - Measure Theory
  - Convergence of Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
a. Let $E \subseteq \RR^n$ be bounded.
   Prove that the following are equivalent:

    1. For any $\epsilon>0$ there exist an open set $G$ and a closed set $F$ such that $F \subseteq E \subseteq G$ and $m(G\sm F) < \epsilon$.

    2. There exist a $G_\delta$ set $V$ and an $F_\sigma$ set $H$ such that $m(V\sm H) = 0$.

b. Let $f_k$ be a sequence of extended real-valued Lebesgue measurable function.

    i. Prove that $\inf_k f_k, \sup_k f_k$ are both Lebesgue measurable function.

        *Hint: argue that*
\[
\ts{x \st \inf_k f_k(x) < a} = \Union_k \ts{x \st f_k(x) < a}
.\]

    ii. Carefully state Fatou's Lemma and deduce the Monotone Converge Theorem from it.
:::
::: {.solution}

::: pf

::: pf-step

Part (a), with $H \subseteq E \subseteq V$ in condition 2.

::: pf-proof

This is [[P-7ITXP]]. If (1) holds, take $G_k$ and $F_k$ for $\eps = 1/k$ and put $V = \bigcap_k G_k$, $H = \bigcup_k F_k$; then $m(V \setminus H) \le m(G_k \setminus F_k) < 1/k$. Conversely, intersect $V$ with an open ball containing $E$, write it as a decreasing intersection of open sets of finite measure and $H$ as an increasing union of closed sets, and apply continuity of measure from above and below.

:::

:::

::: pf-step

For measurable $f_k$ with values in $[-\infty, \infty]$, $\sup_k f_k$ and $\inf_k f_k$ are measurable.

::: pf-proof

For every $a \in \RR$, $\theset{\sup_k f_k \le a} = \bigcap_k\theset{f_k \le a}$ and $\theset{\inf_k f_k < a} = \bigcup_k\theset{f_k < a}$ are countable intersections and unions of measurable sets.

:::

:::

::: pf-step

Fatou's lemma: for measurable $f_n \ge 0$, $\int \liminf_n f_n \le \liminf_n \int f_n$.

:::

::: pf-step

If $0 \le f_1 \le f_2 \le \cdots$ are measurable and $f_n \to f$ pointwise, then $\int f_n \to \int f$.

::: pf-proof

$\int f_n$ is nondecreasing, so $\lim_n\int f_n$ exists in $[0,\infty]$. Since $f_n \le f$, $\lim_n \int f_n \le \int f$. Since $f = \liminf_n f_n$, Fatou's lemma gives $\int f \le \liminf_n \int f_n = \lim_n \int f_n$.

:::

:::

:::

:::

::: {.remark}
Condition 2 of part (a) needs $H \subseteq E \subseteq V$; as printed, it holds for every $E$ with $V = H = \emptyset$.
:::
