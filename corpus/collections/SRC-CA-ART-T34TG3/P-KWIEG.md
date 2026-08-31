---
schema: qual/card@1
id: P-KWIEG
kind: problem
title: Number of roots of $4z^4-6z+3$ in $|z|<1$ and $1<|z|<2$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
Find the number of roots of $p(z) = 4z^4 - 6z + 3$ in $\abs{z} < 1$ and $1 < \abs{z} < 2$ respectively.
:::

::: {.solution}
**Goal:** Find the number of roots of $p(z) = 4z^4 - 6z + 3$ in $|z| < 1$ and in $1 < |z| < 2$ respectively.

<1>1. $p$ has exactly 4 roots in $|z| < 2$.
::: {.proof}
Rouch\'e's theorem on $|z| = 2$: $|4z^4| = 64$ and $|{-6z} + 3| \le 12 + 3 = 15 < 64$, so $p = 4z^4 + (-6z + 3)$ has as many zeros in $|z| < 2$ as $4z^4$, namely 4.
:::

<1>2. $p$ has exactly 2 real roots, both in the interval $(0, 1)$.
<2>1. $p'$ has a single real root $x_0 = \qty{\tfrac38}^{1/3} \approx 0.72$, and $p$ decreases on $(-\infty, x_0)$, increases on $(x_0, \infty)$.
::: {.proof}
$p'(x) = 16x^3 - 6$, which vanishes exactly at $x_0$; $p' < 0$ for $x < x_0$ and $p' > 0$ for $x > x_0$.
:::
<2>2. $p$ has exactly two real zeros, both in $(0, 1)$.
::: {.proof}
$p(0) = 3 > 0$ and $p(x_0) = 4x_0^4 - 6x_0 + 3 = \qty{\tfrac38}^{1/3}\qty{-\tfrac92} + 3 < 0$ (as $x_0 < 2/3$), and $p(1) = 1 > 0$; so by the intermediate value theorem and monotonicity (<2>1) there is exactly one root in $(0, x_0)$ and one in $(x_0, 1)$, and none elsewhere on $\RR$ (for $x < 0$, $p(x) > p(0) > 0$; for $x \ge 1$, $p(x) \ge p(1) > 0$).
:::

<1>3. The remaining two roots form a conjugate pair $z, \bar z$ with $1 < |z| < 2$.
<2>1. $p$ has exactly 2 roots in $|z| < 1$: the two real roots of <1>2.
::: {.proof}
the real roots lie in $(0,1) \subset |z| < 1$; the other two roots are non-real (real coefficients), and their product with the real roots equals $3/4$ (constant term), so $|z|^2\,r_1r_2 = \tfrac34$.
:::
<2>2. $r_1r_2 \in (\tfrac38, \tfrac34)$, hence $|z|^2 = \frac{3/4}{r_1r_2} \in (1, 2)$.
::: {.proof}
pin the roots: $x_0 = \qty{\tfrac38}^{1/3} \in (\tfrac12, \tfrac34)$ (as $\tfrac18 < \tfrac38 < \tfrac{27}{64}$); $p(\tfrac12) = \tfrac14 > 0$ and $p$ decreases on $(0, x_0)$, so the smaller root satisfies $r_1 \in (\tfrac12, x_0) \subset (\tfrac12, \tfrac34)$; and $p(\tfrac34) = 4\qty{\tfrac{81}{256}} - \tfrac92 + 3 = -\tfrac{15}{64} < 0$ while $p$ increases on $(x_0, 1)$ with $p(1) = 1 > 0$, so $r_2 \in (\tfrac34, 1)$.
:::
Hence $r_1r_2 \in (\tfrac38, \tfrac34)$, and $|z|^2 = \tfrac{3/4}{r_1r_2} \in \qty{\tfrac{3/4}{3/4}, \tfrac{3/4}{3/8}} = (1, 2)$.

<1>4. Counts: 2 roots in $|z| < 1$ and $4 - 2 = 2$ roots in $1 < |z| < 2$.
::: {.proof}
<1>2–<1>3 give exactly 2 roots in $|z| < 1$ and show the other 2 satisfy $1 < |z| < 2$; <1>1 shows no roots lie in $|z| \ge 2$.
:::

<1>5. Q.E.D.
::: {.proof}
<1>1–<1>4 answer the question.
:::
:::
