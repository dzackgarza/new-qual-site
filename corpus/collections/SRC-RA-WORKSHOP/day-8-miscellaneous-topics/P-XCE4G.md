---
schema: qual/card@1
id: P-XCE4G
kind: problem
title: Pointwise and locally uniform convergence of $\sum\frac{x^k}{1+x^k}$ on $[0,1)$,
  and differentiability of the sum
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
  - Uniform Convergence
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against the Lamport standard and checked. (a) comparison with the geometric series, since
    0 <= x^k/(1+x^k) <= x^k on [0,1); (b) the same bound gives uniform convergence on [0,a] by the
    M-test with sum a^k; (c) term-by-term differentiation: g_k'(x) = k x^{k-1}/(1+x^k)^2 and, for
    0 <= x <= a < 1, the denominator is at least 1, so |g_k'| <= k a^{k-1}, whose sum converges by
    the ratio test; the M-test then gives uniform convergence of the derivative series on [0,a], and
    the differentiation theorem applies because the partial sums converge at 0. The point 1 is
    genuinely excluded, since the terms tend to 1/2 there and the series diverges, which the card
    notes. All three parts are right.
---

::: {.problem}
Let $f_n \colon [0,1) \to \RR$ be the function defined by $$f_n(x)\coloneqq \sum_{k=1}^n \frac{x^k}{1+x^k}.$$

(a) Prove that $f_n$ converges to a function $f \colon [0,1) \to \RR$.

(b) Prove that for every $0 < a < 1$ the convergence is uniform on $[0,a]$.

(c) Prove that $f$ is differentiable on $(0,1)$.
:::

::: {.solution}
For $k\ge1$, let $g_k(x)\coloneqq x^k/(1+x^k)$ on $[0,1)$.

::: pf

::: pf-step

The series $\sum_{k=1}^\infty g_k(x)$ converges for every $x\in[0,1)$ and defines $f:[0,1)\to\RR$.

::: pf-proof

For each $x\in[0,1)$ and $k\ge1$,
$$
0\le g_k(x)=\frac{x^k}{1+x^k}\le x^k.
$$
The geometric series $\sum_{k\ge1}x^k$ converges, so comparison proves convergence of $\sum g_k(x)$.

:::

:::

::: pf-step

For every $0<a<1$, the sequence $f_n=\sum_{k=1}^n g_k$ converges uniformly to $f$ on $[0,a]$.

::: pf-proof

For all $x\in[0,a]$, $\abs{g_k(x)}\le a^k$.
Since $\sum_{k\ge1}a^k$ converges, the Weierstrass M-test gives uniform convergence of the series on $[0,a]$.

:::

:::

::: pf-step

$f$ is differentiable on $(0,1)$, with $f'(x)=\sum_{k=1}^\infty\dfrac{kx^{k-1}}{(1+x^k)^2}$.

::: pf-proof

::: {.pf-step #s3}

For every $0<a<1$, the series of derivatives $\sum_{k=1}^\infty g_k'$ converges uniformly on $[0,a]$.

::: pf-proof

The quotient rule gives
$$
g_k'(x)=\frac{kx^{k-1}}{(1+x^k)^2}.
$$
For $0\le x\le a$, the denominator is at least $1$, hence $\abs{g_k'(x)}\le ka^{k-1}$.
The numerical series $\sum_{k\ge1}ka^{k-1}$ converges by the ratio test, since the ratio of consecutive terms tends to $a<1$.
The M-test proves uniform convergence of the derivative series.

:::

:::

::: pf-qed

Fix $x\in(0,1)$ and some $a$ with $x<a<1$.
The partial sums $f_n$ converge at $0$ (indeed $f_n(0)=0$), and by step [](#s3){.pf-ref} their derivatives converge uniformly on $[0,a]$.
The term-by-term differentiation theorem therefore gives differentiability of $f$ on $(0,a)$ and the displayed formula at $x$.
Since $x$ was arbitrary, the result holds throughout $(0,1)$.

:::

:::

:::

:::

:::
