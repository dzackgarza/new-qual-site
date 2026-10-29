---
schema: qual/card@1
id: E-BUVLS
kind: problem
title: Laurent series of $\frac{1}{z(z-1)}$ on $0<\abs z<1$ and on $\abs z>1$
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Poles
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source asks for expansions in |z| < 1 and |z| > 1; f has a pole at 0, so the first region is the punctured disc 0 < |z| < 1.
---

::: {.exercise}
Expand $f(z) = \frac{1}{z(z-1)}$ in both

- $0<\abs{z} < 1$
- $\abs{z} > 1$
:::

::: {.solution}

::: pf

::: pf-step
For $0<\abs z<1$, $\boxed{f(z)=-\sum_{k\ge0}z^{k-1}=-\frac1z-1-z-z^2-\cdots}$.

::: pf-proof
For $\abs z<1$, $\frac{1}{1-z}=\sum_{k\ge0}z^k$, and $f(z) = -\frac{1}{z}\cdot\frac{1}{1-z}$.
:::

:::

::: pf-step
For $\abs z>1$, $\boxed{f(z)=\sum_{k\ge2}z^{-k}=\frac1{z^2}+\frac1{z^3}+\cdots}$.

::: pf-proof
For $\abs z>1$, $\frac{1}{1-1/z}=\sum_{k\ge0}z^{-k}$, and $f(z) = \frac{1}{z^2}\cdot\frac{1}{1 - 1/z}$.
:::

:::

:::

:::
