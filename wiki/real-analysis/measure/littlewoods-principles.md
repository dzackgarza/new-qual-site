---
title: Littlewood's three principles
order: 20
topics:
- Measure Theory
- Convergence of Functions
---

# Littlewood's three principles

For Lebesgue measure $m$ on $\RR^d$ and $\varepsilon>0$, the three principles say that a measurable set of finite measure is nearly a finite union of intervals — of boxes, when $d>1$; the precise statement on $\RR$ is Royden--Fitzpatrick, Chapter 2, Theorem 12 — that a measurable function is nearly continuous, and that an almost everywhere convergent sequence on a set of finite measure is nearly uniformly convergent.

## Measurable sets

[[T-IIKSW]]

## Measurable functions

[[T-CGFCU]]

## Almost everywhere convergence

[[FT-OGS76]]

::: {.example title="Egorov's theorem needs finite measure"}
On $\RR$, $f_n\coloneqq\chi_{[n,n+1]}\to0$ pointwise, but $\sup_{A}\abs{f_n}=1$ for all $n$ on any $A$ with $m(\RR\setminus A)<1$, since such $A$ meets every $[n,n+1]$ in positive measure.

The theorem whose hypothesis this example removes is [[FT-OGS76|Egorov's theorem]], and the finiteness of the measure is the hypothesis it needs.
:::

The statements are also on [[real-analysis/measure/littlewood-principles-notes|Egorov and Lusin]] and [[real-analysis/integration/the-convergence-theorems|The convergence theorems]].
