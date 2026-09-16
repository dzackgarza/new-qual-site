---
schema: qual/card@1
id: PR-JLDJ6
kind: proposition
title: Computing cyclotomic polynomials $\Phi_n$
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
\Phi_n(x) = \qty{x^n-1} \qty{\prod_{\substack{d \divides n \\ 0 < d < n}} \Phi_{d}(x)}\inv,
$$
and
$$
\Phi_{n}(x)=\prod_{\substack{ d \divides n \\  d > 0} }\left(x^{d}-1\right)^{\mu\left(n/d\right)},
$$
where $\mu$ is the Möbius function:
$$
\mu(m) =
\begin{cases}
1 & \text{if } m = 1, \\
(-1)^{k} & \text{if } m \text{ is a product of } k \text{ distinct primes}, \\
0 & \text{if } p^2 \divides m \text{ for some prime } p.
\end{cases}
$$
:::

::: {.remark}
The first formula computes $\Phi_n$ recursively: divide $x^n - 1$ by the product of the $\Phi_d$ with $d \divides n$, $d < n$, using polynomial long division.
:::
