---
schema: qual/card@1
id: P-TRIV-DE34
kind: problem
title: $\int_{-\infty}^\infty \delta''(x-2)\frac{dx}{1+x^2}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 34, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Compute $\int _ { - \infty } ^ { \infty } \delta ^ { \prime \prime } ( x - 2 ) \frac { 1 } { 1 + x ^ { 2 } } \mathrm { d } x$
:::

Set
\[
f(x)=\frac1{1+x^2}.
\]

::: pf

::: pf-step

The distributional derivative identity gives
\[
\int_{-\infty}^{\infty}\delta''(x-2)f(x)\,dx=f''(2).
\]


::: pf-proof

For a smooth test function $f$,
\[
\langle\delta_a^{(n)},f\rangle=(-1)^nf^{(n)}(a).
\]
Here $n=2$ and $a=2$, so the sign is positive.

:::

:::

::: pf-step

The second derivative of $f$ is
\[
f''(x)=\frac{6x^2-2}{(1+x^2)^3}.
\]


::: pf-proof

Differentiate twice:
\[
f'(x)=-\frac{2x}{(1+x^2)^2},
\]
and hence
\[
f''(x)=-\frac2{(1+x^2)^2}+\frac{8x^2}{(1+x^2)^3}
=\frac{6x^2-2}{(1+x^2)^3}.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
\int_{-\infty}^{\infty}\delta''(x-2)\frac{dx}{1+x^2}
=\frac{22}{125}}.
\]


::: pf-proof

By steps <1>1--<1>2,
\[
f''(2)=\frac{6\cdot4-2}{(1+4)^3}
=\frac{22}{125}.
\]

:::

:::

::: pf-qed

Step <1>3 gives the requested value.

:::

:::
