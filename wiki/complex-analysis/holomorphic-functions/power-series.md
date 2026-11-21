---
title: Power series
order: 30
topics:
- Power Series
- Taylor Series
- Radius of Convergence
- Convergence Tests
- Series of Functions
- Series of Numbers
- Sequences of Functions
- Uniform Convergence
---

# Power series

Holomorphic and analytic are equivalent: the Cauchy integral formula gives the power-series expansion, and the coefficient formula gives the Cauchy estimates.

[[D-V6UQJ]]

[[PR-QNDSD]]

## Holomorphic implies analytic

[[T-GROTS]]

[[T-K66DJ]]

[[PR-4BVDD]]

## Abel's theorem

[[T-B7YTE]]

The convergence tests that decide convergence on the boundary circle are on [[complex-analysis/basics/analytic-nt|Summation by parts]].

::: {.example title="The alternating harmonic series"}
Integrating the geometric series $\sum_{k\geq 0}(-z)^k = 1/(1+z)$ term by term gives
$$
\sum_{k\geq 1} {(-1)^{k+1} z^k \over k} = \log(1+z), \qquad \abs z < 1
.$$
The series converges at $z=1$ by the alternating series test, so Abel's theorem gives $\sum_{k\geq1}(-1)^{k+1}/k = \lim_{x\to 1^-}\log(1+x) = \log 2$.

:::

::: {.example title="The converse of Abel's theorem fails"}
Take $f(z) = \sum (-z)^n = 1/(1+z)$.
At $z=1$ the series $1-1+1-\cdots$ diverges, while $\lim_{x\to 1^-} f(x) = 1/2$.
So a radial limit can exist at a point where the series diverges, and the converse of Abel's theorem is false.

:::

The standard series and the factorial notation are collected on [[complex-analysis/basics/series-reference|Series: Reference]].

## Exercises

[[E-EG3W7]] [[P-AZOFF-E07]] [[E-EMISN]] [[E-QLRNW]]
[[E-ZQGR5]] [[E-FS7GZ]] [[E-VWVTY]]
[[FE-LAN3V]] [[FE-VWNUI]] [[FE-EUOB2]]
[[E-BUVLS]] [[P-AZOFF-F01]] [[E-DUMQG]] [[E-AHBVF]] [[E-SQ4GJ]] [[E-ENJAF]] [[E-GMGFS]] [[E-XOCPO]] [[E-QCVGX]]
[[E-XIT36]] [[E-THK2Z]] [[E-ORJPT]]
[[E-TVJFL]] [[P-UGA8150S21-HW1-08]] [[E-SS1.EX-13]] [[E-FMLK2]]
