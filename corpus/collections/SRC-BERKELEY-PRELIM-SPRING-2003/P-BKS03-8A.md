---
schema: qual/card@1
id: P-BKS03-8A
kind: problem
title: Evaluate $\int_0^\infty e^{-x^2}\cos(x^2)\,dx$
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Evaluate
\[
\int_0^{\infty}e^{-x^2}\cos(x^2)\,dx.
\]
:::

::: {.solution}
It is the real part of

$$
I : = \int _ { 0 } ^ { \infty } e ^ { - ( 1 + i ) x ^ { 2 } } d x = \int _ { 0 } ^ { \infty } e ^ { - { \sqrt { 2 } } e ^ { i \pi / 4 } x ^ { 2 } } d x = \int _ { 0 } ^ { \infty } e ^ { - { \sqrt { 2 } } ( e ^ { i \pi / 8 } x ) ^ { 2 } } d x .
$$

Let C denote the wedge-shaped closed contour consisting of the straight path from 0 to $R > 0$ , the arc γ given by $e ^ { i t } R$ as t goes from 0 to $\pi / 8$ , and the straight path from $e ^ { i \pi / 8 } R$ to 0. By Cauchy’s Theorem, $\textstyle \int _ { C } e ^ { - { \sqrt { 2 } } z ^ { 2 } } d z = 0$ . But $\textstyle \int _ { \gamma } e ^ { - { \sqrt { 2 } } z ^ { 2 } } d z \to 0$ as $R \to \infty$ , since the integrand is bounded in absolute value by $\vert e ^ { - \sqrt { 2 } e ^ { i \pi / 4 } R ^ { 2 } } \vert = e ^ { - R ^ { 2 } }$ along $\gamma ,$ , while the length of $\gamma$ is $O ( R )$ . Thus $\textstyle \int _ { C } e ^ { - { \sqrt { 2 } } z ^ { 2 } } d z = 0$ implies

$$
0 = \int _ { 0 } ^ { \infty } e ^ { - \sqrt { 2 } z ^ { 2 } } d z - \int _ { 0 } ^ { \infty } e ^ { - \sqrt { 2 } ( e ^ { i \pi / 8 } x ) ^ { 2 } } d ( e ^ { i \pi / 8 } x )
$$

or equivalently,

$$
0 = 2 ^ { - 1 / 4 } \int _ { 0 } ^ { \infty } e ^ { - u ^ { 2 } } d u - e ^ { i \pi / 8 } I ,
$$

so $I = 2 ^ { - 1 / 4 } e ^ { - i \pi / 8 } \frac { \sqrt { \pi } } { 2 }$ . Thus the answer, which is the real part of I, is

$$
2 ^ { - 5 / 4 } ( \cos \pi / 8 ) { \sqrt { \pi } } .
$$
:::
