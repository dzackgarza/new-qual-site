---
schema: qual/card@1
id: E-SS7.PR-2
kind: problem
title: The explicit formula for $\psi_1(x)$ as a sum over zeros of $\zeta$
classification:
  areas:
  - complex-analysis
  topics:
  - Zeta Function
  - Prime Number Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: deepseek-v4.1-flash-free
  date: 2026-10-27
  note: Checked Problem 2 on p.204 against the source PDF. The printed formula has $x^\rho/(\rho(\rho+1))$ and $E=c_1x+c_0+\cdots$; the contour shift of Proposition 2.3 gives $x^{\rho+1}/(\rho(\rho+1))$ and the constant $+c_0$, so the corrected error term is $c_1x-c_0+\cdots$. The erratum records the correction; the solution proves the corrected formula.
---

::: {.exercise}
2. $^\ast$ One of the “explicit formulas” in the theory of primes is as follows: if $\psi _ { 1 }$ is the integrated Tchebychev function considered in Section 2, then

$$
\psi_ {1} (x) = \frac {x ^ {2}}{2} - \sum_ {\rho} \frac {x ^ {\rho + 1}}{\rho (\rho + 1)} - E (x)
$$

where the sum is taken over all zeros $\rho$ of the zeta function in the critical strip.
The error term is given by $E ( x ) = c _ { 1 } x - c _ { 0 } + \sum _ { k = 1 } ^ { \infty } x ^ { 1 - 2 k } / ( 2 k ( 2 k - 1 ) )$ , where $c _ { 1 } = \zeta ^ { \prime } ( 0 ) / \zeta ( 0 )$ and $c _ { 0 } = \zeta ^ { \prime } ( - 1 ) / \zeta ( - 1 )$ . Note that $\textstyle \sum _ { \rho } 1 / | \rho | ^ { 1 + \epsilon } < \infty$ for every $\epsilon > 0$ , because $( 1 - s ) \zeta ( s )$ has order of growth 1. (See Exercise 8.) Also, obviously $E ( x ) = O ( x )$ as $x \to \infty$
:::

::: {.remark title="Erratum"}
The printed source has $x^\rho/(\rho(\rho+1))$ and $E(x)=c_1x+c_0+\cdots$. The contour integral of Proposition 2.3 gives $x^{\rho+1}/(\rho(\rho+1))$ and the constant term $+c_0$, so the corrected formula is the one stated above.
:::
