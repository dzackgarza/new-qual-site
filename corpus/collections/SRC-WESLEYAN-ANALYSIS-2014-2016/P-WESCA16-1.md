---
schema: qual/card@1
id: P-WESCA16-1
kind: problem
title: 'Analytic continuation and an example'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
State the principle of analytic continuation for holomorphic functions and give a specific example of how it is used in complex analysis.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $D$ is connected and open and $f,g:D\to\CC$ are holomorphic,
then agreement on a subset of $D$ having an accumulation point in $D$ implies
$$
\boxed{f=g\text{ on }D}.
$$


::: pf-proof

This is the identity theorem. Equivalently, analytic continuation through
overlapping connected domains is unique wherever two continuations overlap.

:::

:::

::: {.pf-step #s1-2}

A concrete example is
$$
\sum_{n=0}^{\infty}z^n=\frac1{1-z}\qquad(\abs{z}<1).
$$
Thus the power-series function continues uniquely as $(1-z)^{-1}$ on
$\CC\setminus\{1\}$.


::: pf-proof

For $\abs{z}<1$, the finite geometric-sum identity gives
$$
\sum_{n=0}^{N}z^n=\frac{1-z^{N+1}}{1-z}.
$$
Letting $N\to\infty$ gives the displayed identity. The function
$(1-z)^{-1}$ is holomorphic on $\CC\setminus\{1\}$ and agrees with the
series on the unit disk. Step [](#s1-1){.pf-ref} gives uniqueness of any analytic
continuation from that germ to a connected overlapping domain.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} states the principle and step [](#s1-2){.pf-ref} gives a specific application.

:::

:::

:::
