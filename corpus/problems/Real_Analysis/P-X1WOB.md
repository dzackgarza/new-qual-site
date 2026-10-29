---
schema: qual/card@1
id: P-X1WOB
kind: problem
title: "Convergence of series: small tails and the standard convergence tests"
classification:
  areas:
  - real-analysis
  topics:
  - Series of Numbers
  - Convergence Tests
  - Small Tails
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source wrote "convergent sequences have small tails" and "find a sequence that converges but not absolutely" for series, and wrote sum a_n < infinity for a possibly signed series; the statement now says series and drops the inequality.'
---

::: {.exercise}

(a) What does it mean for a series to converge? How can you check this?

(b) What does it mean for a series to converge *uniformly*? What do you have to show to prove it does *not* converge uniformly?

(c) Show that if $\sum_{n\in \NN} a_n$ converges, then $a_n \ctz{n}$.

(d) Show that convergent series *have small tails* in the following sense: $\sum_{n > N} a_n \ctz{N}$. Is this a necessary and sufficient condition for convergence?

(e) State the ratio, root, integral, and alternating series tests.

(f) Prove that the harmonic series diverges.

(g) Derive a formula for the sum of a geometric series.

(h) State and prove the $p$-test.

(i) What does it mean for a series to converge absolutely? Find a series that converges but not absolutely.

:::

::: {.solution}

::: pf

::: pf-step

(a) What convergence of a series means, and how to check it.

::: pf-proof

$\sum_{n\ge 1}a_n$ converges iff the sequence of partial sums $s_N = \sum_{n\le N}a_n$ converges (to a finite limit). Practical checks: (i) necessary: $a_n \to 0$; (ii) Cauchy criterion: for every $\eps > 0$ there is $N$ with $|\sum_{n=M+1}^{K}a_n| < \eps$ for all $K > M \ge N$; (iii) tests: comparison, ratio, root, integral, alternating series, and absolute convergence.

:::

:::

::: pf-step

(b) Uniform convergence of a series, and how to disprove it.

::: pf-proof

$\sum f_n$ converges uniformly on $E$ iff the partial sums $S_N = \sum_{n\le N}f_n$ converge uniformly on $E$: $\sup_{x\in E}|S_N(x) - S(x)| \to 0$. To show it does not converge uniformly: exhibit $\eps > 0$ and points $x_N \in E$ with $|S_N(x_N) - S(x_N)| \ge \eps$ for infinitely many $N$ (or: the tail $\sup_{x\in E}|\sum_{n>N}f_n(x)|$ fails to tend to $0$).

:::

:::

::: pf-step

(c) If $\sum_n a_n$ converges, then $a_n \to 0$.

::: pf-proof

$a_n = s_n - s_{n-1} \to s - s = 0$.

:::

:::

::: pf-step

(d) Convergent series have small tails, and this condition is necessary and sufficient for convergence.

::: pf-proof

$\sum_{n\ge1}a_n$ converges iff the tails $T_N = \sum_{n>N}a_n$ satisfy $T_N \to 0$ as $N \to \infty$: if $s_N \to s$, then $T_N = s - s_N \to 0$; conversely, if every tail $T_N$ converges and $T_N \to 0$, then $s_N = T_0 - T_N$ converges.

:::

:::

::: pf-step

(e) Ratio test.

::: pf-proof

If $a_n \ne 0$ eventually and $\limsup |a_{n+1}/a_n| < 1$, then $\sum a_n$ converges absolutely; if $\liminf |a_{n+1}/a_n| > 1$, it diverges. Proof of the first: pick $r$ with $\limsup < r < 1$; then $|a_n| \le C r^n$ eventually, and the geometric series $\sum r^n$ converges.

:::

:::

::: pf-step

(e) Root test.

::: pf-proof

If $\limsup \sqrt[n]{|a_n|} < 1$, then $\sum a_n$ converges absolutely (choose $r$ with the limsup $< r < 1$; eventually $\sqrt[n]{|a_n|} \le r$, i.e. $|a_n| \le r^n$); if $\limsup\sqrt[n]{|a_n|} > 1$, the terms do not tend to $0$ and the series diverges.

:::

:::

::: pf-step

(e) Integral test.

::: pf-proof

If $f \ge 0$ is decreasing on $[1,\infty)$, then $\sum_{n=1}^N f(n)$ and $\int_1^N f$ converge or diverge together, since $\int_1^{N+1}f \le \sum_{n=1}^N f(n) \le f(1) + \int_1^N f$ (compare the sum to the integral over unit intervals).

:::

:::

::: {.pf-step #s8}

(e) Alternating series test.

::: pf-proof

If $a_n \ge 0$ decreases to $0$, then $\sum (-1)^{n+1}a_n$ converges: the even and odd partial sums are monotone and bounded (interleaved), so both converge to a common limit, and the error after $N$ terms is bounded by $a_{N+1}$.

:::

:::

::: {.pf-step #s9}

(f) The harmonic series diverges.

::: pf-proof

Group terms: $1 + \tfrac12 + (\tfrac13+\tfrac14) + (\tfrac15+\cdots+\tfrac18) + \cdots \ge 1 + \tfrac12 + \tfrac12 + \tfrac12 + \cdots = \infty$; or use the integral test with $f(x) = 1/x$ ($\int_1^\infty dx/x = \infty$).

:::

:::

::: pf-step

(g) Sum of a geometric series.

::: pf-proof

$s_N = \sum_{n=0}^{N-1} x^n$ satisfies $(1-x)s_N = 1 - x^N$, so $s_N = \frac{1-x^N}{1-x}$ for $x \ne 1$; if $|x| < 1$, $s_N \to \frac{1}{1-x}$. If $|x| \ge 1$ and $x \ne 1$, the terms do not tend to $0$, so it diverges; at $x = 1$, $s_N = N \to \infty$.

:::

:::

::: pf-step

(h) The $p$-test.

::: pf-proof

$\sum_{n\ge1} n^{-p}$ converges iff $p > 1$. For $p > 1$ use the integral test: $\int_1^\infty x^{-p}dx = \frac{1}{p-1} < \infty$; for $p \le 1$: $\sum n^{-p} \ge \sum n^{-1} = \infty$ (or integral test for $p < 1$).

:::

:::

::: pf-step

(i) Absolute and conditional convergence.

::: pf-proof

$\sum a_n$ converges absolutely iff $\sum |a_n| < \infty$, which implies convergence (by the Cauchy criterion: $|\sum_{M+1}^K a_n| \le \sum_{M+1}^K |a_n|$). Conditional convergence means $\sum a_n$ converges but $\sum|a_n| = \infty$. Example: $\sum (-1)^{n+1}/n$ converges (alternating series test, step [](#s8){.pf-ref}) but $\sum 1/n$ diverges (step [](#s9){.pf-ref}).

:::

:::

:::

:::
