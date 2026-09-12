---
schema: qual/card@1
id: P-BKS03-4A
kind: problem
title: Chebyshev polynomials with integer coefficients
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
Prove that for every integer $n\ge0$ there is a polynomial $T_n(x)\in\mathbb Z[x]$ such that
\[
2\cos(nz)=T_n(2\cos z)
\]
for every $z$.
:::

::: {.solution}
Put $q = e ^ { i z }$ , so $2 \cos z = q + q ^ { - 1 }$ , and 2 cos $n z = q ^ { n } + q ^ { - n }$ . Then the problem is to find $T _ { n }$ such that $T _ { n } ( q + q ^ { - 1 } ) = q ^ { n } + q ^ { - n }$ . We have

$$
( q + q ^ { - 1 } ) ^ { n } = \sum _ { k = 0 } ^ { n } { \binom { n } { k } } q ^ { 2 k - n } = q ^ { n } + q ^ { - n } + \sum _ { \tiny { n < j < n \atop n - j \mathrm { ~ e v e n } } } { \binom { n } { ( n - j ) / 2 } } ( q ^ { j } + q ^ { - j } ) + \left\{ { \binom { n } { 0 / 2 } } \quad { \mathrm { i f ~ } } n { \mathrm { ~ i s ~ e v e n } } , \atop 0  \right\} .
$$

We can assume we have found $T _ { j }$ for $j < n$ by induction.
Then

$$
T _ { n } ( x ) = x ^ { n } - \sum _ { \stackrel { 0 < j < n } { n - j \mathrm { ~ e v e n } } } { \binom { n } { ( n - j ) / 2 } } ( T _ { j } ( x ) ) - { \left\{ \begin{array} { l l } { { \binom { n } { n / 2 } } } & { { \mathrm { i f ~ } } n { \mathrm { ~ i s ~ e v e n , } } } \\ { { 0 } } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

has the required property.
:::
