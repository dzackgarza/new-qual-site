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

For measurable $0\leq f_1\leq f_2\leq\cdots$ with $f_n\to f$ pointwise, $\int f_n\to\int f$ in $[0,\infty]$.
Applied to partial sums, it gives $\int\sum_n g_n = \sum_n\int g_n$ for measurable $g_n\geq0$.

[[T-5K3IO]]

[[FT-5G4Y3]]

## Dominated convergence

If $f_n\to f$ almost everywhere and $\abs{f_n}\leq g$ with $g\in L^1$, then $f\in L^1$ and $\int f_n\to\int f$; applying the theorem to $\abs{f_n-f}\leq 2g$ gives $\norm{f_n-f}_1\to0$.

[[T-IJQQG]]

[[FT-LCR5P]]

[[T-WYX24]]

[[PR-H4ZVI]]

## Fatou's lemma

[[T-LDJNS]]

[[FT-P5UNP]]

::: {.remark title="Relations among the three theorems"}
The monotone convergence theorem and Fatou's lemma can each be proved from the other.
The dominated convergence theorem follows from Fatou's lemma applied to $2g - \abs{f_n - f}\geq0$, which converges to $2g$ and gives $\limsup_n\int\abs{f_n-f}\leq 0$.
For measurable $f_n\geq0$, the inequality $\int\liminf_n f_n\leq\liminf_n\int f_n$ of Fatou's lemma can be strict: $f_n\coloneqq n\chi_{(0,1/n)}$ on $\RR$ gives $0<1$.

:::

## Egorov and Lusin

Egorov's theorem: if $\mu(E)<\infty$ and measurable $f_n\to f$ almost everywhere on $E$ with $f$ finite almost everywhere, then for every $\varepsilon>0$ there is $A\subseteq E$ with $\mu(E\setminus A)<\varepsilon$ and $f_n\to f$ uniformly on $A$.
Lusin's theorem: if $E\subseteq\RR^d$ has finite Lebesgue measure and $f$ is measurable and finite almost everywhere on $E$, then for every $\varepsilon>0$ there is a closed $F\subseteq E$ with $m(E\setminus F)<\varepsilon$ and $f|_F$ continuous.

[[FT-OGS76]]

[[T-CGFCU]]

## Interchanging limits, sums, and integrals

The equality $\lim_n\int f_n=\int\lim_n f_n$ holds when $f_n\to f$ uniformly and all $f_n$ vanish outside one set of finite measure, when $f_n\to f$ almost everywhere with $\abs{f_n}\leq g\in L^1$, and when $0\leq f_n\uparrow f$.
It fails for the pointwise convergent sequences $n\chi_{(0,1/n)}$, $\chi_{[n,n+1]}$, and $\frac1n\chi_{[0,n]}$ on [[real-analysis/integration/l1|$L^1$]], each with limit $0$ and integral $1$.
If $\sum_n\norm{f_n}_1<\infty$, then $\sum_n f_n$ converges absolutely almost everywhere and in $L^1$, and $\int\sum_n f_n = \sum_n\int f_n$.

[[T-MN6WQ]]

[[FS-BM2PV]]

[[PR-EHIXY]]

[[FR-KEWV2]]

[[PR-NKZBT]]

[[PR-YJJSY]]

[[PR-2CZUM]]
