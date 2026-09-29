---
schema: qual/card@1
id: P-NYZMD
kind: problem
title: Best linear approximation to $x^2$ in $L^2([0,1])$ by projection onto $1$ and
  $\sqrt3(2x-1)$
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - L²
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Consider $L^2([0, 1])$ and define
\[
e_0(x) &= 1 \\
e_1(x) &= \sqrt{3}(2x-1)
.\]

a. Show that $\ts{e_0, e_1}$ is an orthonormal system.

b. Show that the polynomial $p(x)$ where $\deg(p) = 1$ which is closest to $f(x) = x^2$ in $L^2([0, 1])$ is given by
\[
h(x) = x - {1\over 6}
.\]

Compute $\norm{f - g}_2$.
:::
::: {.solution}

::: pf

::: {.pf-step #s1}

$\theset{e_0, e_1}$ is orthonormal in $L^2([0,1])$.

::: pf-proof

$\|e_0\|_2^2 = \int_0^1 1\,dx = 1$. $\|e_1\|_2^2 = 3\int_0^1(4x^2 - 4x + 1)\,dx = 3\left(\frac43 - 2 + 1\right) = 1$. $\inner{e_0}{e_1} = \sqrt 3\int_0^1 (2x-1)\,dx = \sqrt3(1 - 1) = 0$.

:::

:::

::: pf-step

The polynomial of degree at most $1$ closest to $f(x) = x^2$ is $h = \inner{f}{e_0}e_0 + \inner{f}{e_1}e_1 = x - \frac16$.

::: pf-proof

The polynomials of degree at most $1$ form the span of $e_0$ and $e_1$, and the closest point of a closed subspace is the orthogonal projection, which for an orthonormal basis $e_0, e_1$ is $\inner{f}{e_0}e_0 + \inner{f}{e_1}e_1$ by step [](#s1){.pf-ref}. Here $\inner{f}{e_0} = \int_0^1 x^2\,dx = \frac13$ and $\inner{f}{e_1} = \sqrt 3\int_0^1 (2x^3 - x^2)\,dx = \sqrt 3\left(\frac12 - \frac13\right) = \frac{\sqrt 3}{6}$, so $h(x) = \frac13 + \frac12(2x - 1) = x - \frac16$.

:::

:::

::: pf-step

$\|f - h\|_2 = \boxed{\frac{1}{6\sqrt 5}}$.

::: pf-proof

$f - h$ is orthogonal to $h$, so $\|f - h\|_2^2 = \|f\|_2^2 - \|h\|_2^2$. Here $\|f\|_2^2 = \int_0^1 x^4\,dx = \frac15$ and $\|h\|_2^2 = \frac19 + \frac{3}{36} = \frac{7}{36}$, so $\|f - h\|_2^2 = \frac15 - \frac7{36} = \frac1{180}$ and $\sqrt{180} = 6\sqrt5$.

:::

:::

:::

:::

::: {.remark}
In the last line of the statement, $g$ is read as $h$.
:::
