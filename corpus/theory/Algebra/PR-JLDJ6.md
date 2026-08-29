---
schema: qual/card@1
id: PR-JLDJ6
kind: proposition
title: Computing Cyclotomic Polynomials
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

:::{.proposition}
**Computing $\Phi_n$:**

$$
\Phi_{n}(z)=\prod_{\substack{ d \divides n \\  d > 0} }\left(z^{d}-1\right)^{\mu\left(\frac{n}{d}\right)}
$$
where
$$
\mu(n) \equiv\left\{ \begin{array}{ll}{0} & {\text { if } n \text { has one or more repeated prime factors }} \\ {1} & {\text { if } n=1} \\ {(-1)^{k}} & {\text { if } n \text { is a product of } k \text { distinct primes, }}\end{array}\right.
$$

\[
x^{n}-1=\prod_{d | n} \Phi_{d}(x) \implies \Phi_n(x) = \qty{x^n-1} \qty{\prod_{d | n \atop d < n} \Phi_{d}(x)}\inv,
\]
so just use polynomial long division.

:::
