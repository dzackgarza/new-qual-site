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

On a measure space with $\mu(X)<\infty$, uniform convergence of integrable functions carries the integrals with it, by the estimate $\abs{\int f_n-\int f}\leq\mu(X)\sup_x\abs{f_n(x)-f(x)}$ ([[PR-L7LNZ]]).

::: {.example title="Uniform convergence alone does not commute with the integral"}
On $\RR$ with Lebesgue measure, $f_n\coloneqq\frac1n\chi_{[0,n]}$ converges to $0$ uniformly, since $\sup_x\abs{f_n(x)}=1/n$, every $f_n$ is in [[real-analysis/integration/l1|$L^1$]], and $\int f_n=1$ for every $n$.
So the hypothesis $\mu(X)<\infty$ in [[PR-L7LNZ]] cannot be dropped.
The integral $1$ also survives the pointwise, non-uniform sequences $n\chi_{(0,1/n)}$ and $\chi_{[n,n+1]}$ on $\RR$.
:::

[[T-MN6WQ]]

[[PR-2CZUM]]
