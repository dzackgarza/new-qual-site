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

::: {.remark title="Egorov's theorem and bounded convergence"}
Egorov's theorem proves the bounded convergence theorem.
Let $\abs{f_n}\leq M$ vanish outside $E$, $m(E)<\infty$, and $f_n\to f$ almost everywhere.
For $\varepsilon>0$ take a closed $A\subseteq E$ with $m(E\setminus A)<\varepsilon$ on which $f_n\to f$ uniformly.
Then $\int_E\abs{f_n-f}\leq m(E)\sup_A\abs{f_n-f}+2M\varepsilon$, so $\limsup_n\int\abs{f_n-f}\leq2M\varepsilon$ for every $\varepsilon>0$.

:::

::: {.example title="Egorov's theorem needs finite measure"}
On $\RR$, $f_n\coloneqq\chi_{[n,n+1]}\to0$ pointwise, but $\sup_{A}\abs{f_n}=1$ for all $n$ on any $A$ with $m(\RR\setminus A)<1$, since such $A$ meets every $[n,n+1]$ in positive measure.

:::

The statements and proofs are on [[real-analysis/integration/the-convergence-theorems|The convergence theorems]] and [[real-analysis/measure/littlewood-principles-notes|Littlewood's principles: proofs]].
