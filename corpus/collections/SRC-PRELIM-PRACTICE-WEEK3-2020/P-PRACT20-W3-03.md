---
schema: qual/card@1
id: P-PRACT20-W3-03
kind: problem
title: The integral $\int_0^\infty\lfloor x\rfloor e^{-x}\,dx$
classification:
  areas:
  - prelim
  topics:
  - Improper Integrals
  - Series
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed OCR junk from the integrand, checked against Week3_solns.pdf page 1 (Problem 3).
---

::: {.problem}
Compute $\int_0^\infty \lfloor x \rfloor e^{-x}\,dx$ where $\lfloor x \rfloor$ denotes the largest integer not exceeding $x$.
:::

::: {.solution}
Split the integral into the intervals $[n,n+1)$ for $n\in\NN_0$ and use $\lfloor x\rfloor=n$ there; the $n=0$ term vanishes:

$$
\begin{aligned}
\int_0^\infty\lfloor x\rfloor e^{-x}\,dx
&=\sum_{n=1}^{\infty}n\int_n^{n+1}e^{-x}\,dx
=\sum_{n=1}^{\infty}n\bigl(e^{-n}-e^{-(n+1)}\bigr)\\
&=\sum_{n=1}^{\infty}ne^{-n}-\sum_{n=2}^{\infty}(n-1)e^{-n}
=\sum_{n=1}^{\infty}e^{-n}.
\end{aligned}
$$

This is a geometric series, so $\displaystyle\int_0^\infty\lfloor x\rfloor e^{-x}\,dx=\frac{e^{-1}}{1-e^{-1}}=\frac{1}{e-1}$.
:::
