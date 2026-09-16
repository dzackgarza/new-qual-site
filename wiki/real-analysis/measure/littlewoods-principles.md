---
title: Littlewood's three principles
order: 20
topics:
- Measure Theory
- Convergence of Functions
---

# Littlewood's three principles

For Lebesgue measure $m$ on $\RR^d$ and $\varepsilon>0$:

| Principle | Theorem |
| --- | --- |
| A measurable set $E$ with $m(E)<\infty$ differs from a finite union of rectangles by a set of measure $<\varepsilon$ | regularity of Lebesgue measure |
| A measurable function finite a.e. on $E$, $m(E)<\infty$, is continuous on a closed $F\subseteq E$ with $m(E\setminus F)<\varepsilon$ | Lusin |
| A sequence converging a.e. on $E$, $m(E)<\infty$, to an a.e. finite limit converges uniformly on a closed $A\subseteq E$ with $m(E\setminus A)<\varepsilon$ | Egorov |

::: {.remark title="Reduction to continuous functions and uniform convergence"}
Lusin's theorem reduces some statements about measurable functions to statements about continuous functions on closed sets, and Egorov's theorem reduces some statements about almost-everywhere convergence to uniform convergence, at the cost of an exceptional set of small measure.

:::

::: {.example title="Egorov's theorem needs finite measure"}
On $\RR$, $f_n\coloneqq\chi_{[n,n+1]}\to0$ pointwise, but $\sup_{A}\abs{f_n}=1$ for all $n$ on any $A$ with $m(\RR\setminus A)<1$, since such $A$ meets every $[n,n+1]$ in positive measure.

:::

The statements and proofs are on [[real-analysis/integration/the-convergence-theorems|The convergence theorems]] and [[real-analysis/measure/littlewood-principles-notes|Littlewood's principles: proofs]].
