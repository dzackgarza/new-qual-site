---
schema: qual/card@1
id: P-BKF16-1B
kind: problem
title: The Gaussian integral and surface areas of spheres via $\Gamma$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Statement checked against F16_Exam.pdf problem 1B, which prints S_3 = 4 pi/3; kept with an erratum remark.
---

::: {.problem}
Let $C = \int_{-\infty}^{\infty} e^{-x^2}\,dx$ and let $S_n$ be the $(n-1)$-dimensional "surface area" of the unit sphere in $\mathbb{R}^n$ (so $S_2 = 2\pi$, $S_3 = 4\pi/3$).

(a) Prove that $C^n = S_n \Gamma(n/2)/2$, where $\Gamma(s) = \int_0^\infty e^{-t} t^{s-1}\,dt$.
(Evaluate the integral of $e^{-(x_1^2 + \cdots + x_n^2)}$ over $\mathbb{R}^n$ in rectangular and polar coordinates.)

(b) Show that $s\Gamma(s) = \Gamma(s+1)$ and $\Gamma(1) = 1$.

(c) Evaluate $C$.
(Hint: $S_2 = 2\pi$.)

(d) Evaluate $S_4$.
:::

::: {.remark}
The source's parenthetical value $S_3 = 4\pi/3$ is an erratum: the surface area of the unit sphere in $\mathbb{R}^3$ is $S_3 = 4\pi$, and $4\pi/3$ is the volume of the unit ball.
The formula in (a) gives $S_3 = 2C^3/\Gamma(3/2) = 2\pi^{3/2}/(\sqrt{\pi}/2) = 4\pi$.
:::
