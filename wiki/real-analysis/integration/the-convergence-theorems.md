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

::: {.remark title="Relations among the three theorems"}
The monotone convergence theorem and Fatou's lemma can each be proved from the other.
The dominated convergence theorem follows from Fatou's lemma applied to $2g - \abs{f_n - f}\geq0$, which converges to $2g$ and gives $\limsup_n\int\abs{f_n-f}\leq 0$.
For measurable $f_n\geq0$, the inequality $\int\liminf_n f_n\leq\liminf_n\int f_n$ of Fatou's lemma can be strict: $f_n\coloneqq n\chi_{(0,1/n)}$ on $\RR$ gives $0<1$.

:::

## Egorov and Lusin

[[FT-OGS76]]

[[T-CGFCU]]

## Interchanging limits, sums, and integrals

The equality $\lim_n\int f_n=\int\lim_n f_n$ holds when $f_n\to f$ uniformly and all $f_n$ vanish outside one set of finite measure.
It fails for the pointwise convergent sequences $n\chi_{(0,1/n)}$, $\chi_{[n,n+1]}$, and $\frac1n\chi_{[0,n]}$ on $\RR$, all in [[real-analysis/integration/l1|$L^1$]], each with limit $0$ and integral $1$.

[[T-MN6WQ]]

[[PR-2CZUM]]
