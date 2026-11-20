---
title: The convergence theorems
order: 20
topics:
- Convergence of Integrals
- Convergence of Functions
---

# The convergence theorems

[[real-analysis/integration/which-convergence-theorem|Which convergence theorem?]] compares the hypotheses of these theorems.

## Monotone convergence

[[T-5K3IO]]

## Dominated convergence

[[T-IJQQG]]

[[T-WYX24]]

[[PR-H4ZVI]]

## Fatou's lemma

[[T-LDJNS]]

::: {.example title="Strictness in Fatou's lemma"}
For measurable $f_n\geq0$, the inequality $\int\liminf_n f_n\leq\liminf_n\int f_n$ of Fatou's lemma can be strict: $f_n\coloneqq n\chi_{(0,1/n)}$ on $\RR$ gives $0<1$.

:::

## Egorov and Lusin

[[FT-OGS76]]

[[T-CGFCU]]

## Interchanging limits, sums, and integrals

The equality $\lim_n\int f_n=\int\lim_n f_n$ holds when $f_n\to f$ uniformly and the $f_n$ and $f$ are integrable: choosing $N$ with $\abs{f_n-f}\leq1$ for $n\geq N$, the integrable $g\coloneqq\max\qty{\abs{f_1},\dots,\abs{f_N},\abs f+1}$ dominates every $f_n$, so the [[T-IJQQG|dominated convergence theorem]] applies.
It fails for the pointwise convergent sequences $n\chi_{(0,1/n)}$, $\chi_{[n,n+1]}$, and $\frac1n\chi_{[0,n]}$ on $\RR$, all in [[real-analysis/integration/l1|$L^1$]], each with limit $0$ and integral $1$.

[[T-MN6WQ]]

[[PR-2CZUM]]
