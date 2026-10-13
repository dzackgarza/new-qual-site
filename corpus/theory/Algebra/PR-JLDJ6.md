---
schema: qual/card@1
id: PR-JLDJ6
kind: proposition
title: Computing cyclotomic polynomials $\Phi_n$
slogan: 'Cyclotomic polynomials factor $x^n-1$ over divisors and invert that factorization by Möbius inversion.'
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Polynomials
  - Number Theory
relations: []
review: draft
---

::: {.proposition}
Let $n \geq 1$ and let $\Phi_n$ be the $n$th [[D-BLV6F|cyclotomic polynomial]].
Then
$$
x^{n}-1=\prod_{\substack{d \divides n \\ d > 0}} \Phi_{d}(x),
\qquad\text{so}\qquad
\Phi_n(x) =
\frac{x^n-1}{\displaystyle\prod_{\substack{d \divides n \\ 0 < d < n}} \Phi_{d}(x)},
$$
and
$$
\Phi_{n}(x)=\prod_{\substack{ d \divides n \\  d > 0} }\left(x^{d}-1\right)^{\mu\left(n/d\right)},
$$
where $\mu$ is the [[D-6V3PZ|Möbius function]].
:::

::: {.remark}
The first formula computes $\Phi_n$ recursively: divide $x^n - 1$ by the product of the $\Phi_d$ with $d \divides n$, $d < n$, using polynomial long division.
:::
