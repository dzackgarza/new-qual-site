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

(a) $\sum_{n\ge 1}a_n$ converges if and only if its partial sums $s_N = \sum_{n\le N}a_n$ converge to a finite limit.
It converges if and only if it satisfies the Cauchy criterion: for every $\varepsilon > 0$ there is $N$ with $\abs{\sum_{n=M+1}^{K}a_n} < \varepsilon$ for all $K > M \ge N$.

::: pf-proof

The first sentence is the definition.
The second is the Cauchy criterion for the sequence $(s_N)$ in the complete space $\RR$, since $s_K - s_M = \sum_{n=M+1}^K a_n$.
In practice the criterion is checked through the comparison, ratio, root, integral and alternating series tests of part (e), or through absolute convergence (part (i)); $a_n \to 0$ is necessary (part (c)) but not sufficient (part (f)).

:::

:::

::: pf-step

(b) $\sum f_n$ converges uniformly on $E$ if and only if its partial sums $S_N = \sum_{n\le N}f_n$ converge uniformly on $E$ to some $S$, that is, $\sup_{x\in E}\abs{S_N(x) - S(x)} \to 0$.
It fails to converge uniformly to its pointwise sum $S$ if and only if there are $\varepsilon > 0$, infinitely many $N$ and points $x_N \in E$ with $\abs{S_N(x_N) - S(x_N)} \ge \varepsilon$.

::: pf-proof

The first sentence is the definition.
The second is its negation: the supremum does not tend to $0$ exactly when it is at least some $\varepsilon > 0$ for infinitely many $N$, and a supremum at least $\varepsilon$ is witnessed by a point at which the difference is at least $\varepsilon/2$; replace $\varepsilon$ by $\varepsilon/2$.

:::

:::

::: pf-step

(c) If $\sum_n a_n$ converges, then $a_n \to 0$.

::: pf-proof

If $s_N \to s$, then $a_n = s_n - s_{n-1} \to s - s = 0$.

:::

:::

::: pf-step

(d) If $\sum_{n\ge1}a_n$ converges, then each tail $T_N = \sum_{n>N}a_n$ converges and $T_N \to 0$.
The tail condition is not a criterion for convergence, since $T_N$ is defined only when the series converges; the necessary and sufficient condition in this spirit is the Cauchy criterion $\sup_{K>N}\abs{\sum_{N<n\le K} a_n} \to 0$.

::: pf-proof

If $s_N \to s$, then $\sum_{N<n\le K} a_n = s_K - s_N \to s - s_N$ as $K\to\infty$, so $T_N = s - s_N$, and $T_N \to 0$.
A series whose partial sums converge has every tail convergent, and conversely the convergence of a single tail $T_N$ already gives $s_K = s_N + \sum_{N<n\le K}a_n \to s_N + T_N$; so the tail condition presupposes convergence.
The finite blocks $\sum_{N<n\le K}a_n = s_K - s_N$ are always defined, and $\sup_{K>N}\abs{s_K - s_N} \to 0$ is equivalent to $(s_N)$ being Cauchy, which is equivalent to convergence by part (a).

:::

:::

::: pf-step

(e) The four tests hold as stated in the substeps.

::: pf-proof

::: pf-step

Ratio test: if $a_n \ne 0$ eventually and $\limsup \abs{a_{n+1}/a_n} < 1$, then $\sum a_n$ converges absolutely; if $\liminf \abs{a_{n+1}/a_n} > 1$, it diverges.

::: pf-proof

Pick $r$ with $\limsup\abs{a_{n+1}/a_n} < r < 1$; then $\abs{a_n} \le C r^n$ eventually, and the geometric series $\sum r^n$ converges.
If $\liminf \abs{a_{n+1}/a_n} > 1$, then $\abs{a_n}$ is eventually increasing, so $a_n \not\to 0$ and the series diverges by part (c).

:::

:::

::: pf-step

Root test: if $\limsup \sqrt[n]{\abs{a_n}} < 1$, then $\sum a_n$ converges absolutely; if $\limsup\sqrt[n]{\abs{a_n}} > 1$, it diverges.

::: pf-proof

Choose $r$ with the limsup $< r < 1$; eventually $\abs{a_n} \le r^n$, and the geometric series converges.
If the limsup exceeds $1$, then $\abs{a_n} > 1$ for infinitely many $n$, so $a_n \not\to 0$.

:::

:::

::: pf-step

Integral test: if $f \ge 0$ is decreasing on $[1,\infty)$, then $\sum_{n\ge1} f(n)$ and $\int_1^\infty f$ converge or diverge together.

::: pf-proof

Comparing the sum with the integral over unit intervals gives $\int_1^{N+1}f \le \sum_{n=1}^N f(n) \le f(1) + \int_1^N f$, and both sides are monotone in $N$.

:::

:::

::: {.pf-step #alternating}

Alternating series test: if $a_n \ge 0$ decreases to $0$, then $\sum (-1)^{n+1}a_n$ converges, and the error after $N$ terms is at most $a_{N+1}$.

::: pf-proof

The even partial sums increase, the odd partial sums decrease, and each odd partial sum exceeds each even one, so both converge; their difference is $\pm a_n \to 0$, so the limits agree.

:::

:::

:::

:::

::: {.pf-step #harmonic}

(f) $\sum_{n\ge1} 1/n = \infty$.

::: pf-proof

Group the terms: $1 + \tfrac12 + (\tfrac13+\tfrac14) + (\tfrac15+\cdots+\tfrac18) + \cdots \ge 1 + \tfrac12 + \tfrac12 + \tfrac12 + \cdots = \infty$.

:::

:::

::: pf-step

(g) For $\abs{x} < 1$, $\sum_{n\ge0} x^n = \boxed{\frac{1}{1-x}}$, and for $\abs{x} \ge 1$ the geometric series diverges.

::: pf-proof

$s_N = \sum_{n=0}^{N-1} x^n$ satisfies $(1-x)s_N = 1 - x^N$, so $s_N = \frac{1-x^N}{1-x}$ for $x \ne 1$, and $s_N \to \frac{1}{1-x}$ when $\abs{x} < 1$.
If $\abs{x} \ge 1$, the terms $x^n$ do not tend to $0$, so the series diverges by part (c).

:::

:::

::: pf-step

(h) $\sum_{n\ge1} n^{-p}$ converges if and only if $p > 1$.

::: pf-proof

For $p > 1$, $\int_1^\infty x^{-p}\,dx = \frac{1}{p-1} < \infty$, so the integral test of part (e) gives convergence.
For $p \le 1$, $n^{-p} \ge n^{-1}$, so the series diverges by comparison with step [](#harmonic){.pf-ref}.

:::

:::

::: pf-step

(i) $\sum a_n$ converges absolutely if $\sum \abs{a_n} < \infty$, and absolute convergence implies convergence.
The series $\sum (-1)^{n+1}/n$ converges but not absolutely.

::: pf-proof

By the Cauchy criterion of part (a), since $\abs{\sum_{M+1}^K a_n} \le \sum_{M+1}^K \abs{a_n}$, absolute convergence implies convergence.
The series $\sum (-1)^{n+1}/n$ converges by step [](#alternating){.pf-ref}, and $\sum 1/n$ diverges by step [](#harmonic){.pf-ref}.

:::

:::

:::

:::
