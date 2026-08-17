---
schema: qual/card@1
id: P-X1WOB
kind: exercise
title: -- What does it mean for a series to converge? How can you check this?
classification:
  areas:
  - real-analysis
  topics:
  - series-of-numbers
  - convergence-tests
  - small-tails
relations: []
review: draft
---

::: exercise
-- What does it mean for a series to converge? How can you check this?
		- What does it mean for a series to converge *uniformly*? What do you have to show to prove it does *not* converge uniformly?
- Show that if $\sum_{n\in \NN} a_n < \infty$ converges, then $$a_n \ctz{n}$$.
- Show that convergent sequences *have small tails* in the following sense: $$\sum_{n > N} a_n \ctz{N}$$.
	- Is this a necessary and sufficient condition for convergence?
- State the ratio, root, integral, and alternating series tests.
- Prove that the harmonic series diverges
- Derive a formula for the sum of a geometric series.
- State and prove the $p\dash$test.
- What does it mean for a series to converge absolutely?
	- Find a sequence that converges but not absolutely.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. What convergence of a series means, and how to check it.
    Proof: $\sum_{n\ge 1}a_n$ converges iff the sequence of partial sums $s_N = \sum_{n\le N}a_n$ converges (to a finite limit). Practical checks: (i) necessary: $a_n \to 0$; (ii) Cauchy criterion: for every $\eps > 0$ there is $N$ with $|\sum_{n=M+1}^{K}a_n| < \eps$ for all $K > M \ge N$; (iii) tests: comparison, ratio, root, integral, alternating series, and absolute convergence.
<1>2. Uniform convergence of a series, and how to disprove it.
    Proof: $\sum f_n$ converges uniformly on $E$ iff the partial sums $S_N = \sum_{n\le N}f_n$ converge uniformly on $E$: $\sup_{x\in E}|S_N(x) - S(x)| \to 0$. To show it does NOT converge uniformly: exhibit $\eps > 0$ and points $x_N \in E$ with $|S_N(x_N) - S(x_N)| \ge \eps$ for infinitely many $N$ (or: the tail $\sup_{x\in E}|\sum_{n>N}f_n(x)|$ fails to tend to $0$).
<1>3. If $\sum_n a_n$ converges, then $a_n \to 0$.
    Proof: $a_n = s_n - s_{n-1} \to s - s = 0$.
<1>4. Convergent sequences have small tails; this is necessary and sufficient.
    Proof: $\sum_{n\ge1}a_n$ converges iff the tails $T_N = \sum_{n>N}a_n$ satisfy $T_N \to 0$ as $N \to \infty$ (this is just $s_N \to s$, with $T_N = s - s_N$). So yes, it is a necessary and sufficient condition for convergence (of the partial sums themselves); note this concerns series, and it is equivalent to the Cauchy criterion.
<1>5. Ratio test.
    Proof: if $a_n \ne 0$ eventually and $\limsup |a_{n+1}/a_n| < 1$, then $\sum a_n$ converges absolutely; if $\liminf |a_{n+1}/a_n| > 1$, it diverges. Proof of the first: pick $r$ with $\limsup < r < 1$; then $|a_n| \le C r^n$ eventually, and the geometric series $\sum r^n$ converges.
<1>6. Root test.
    Proof: if $\limsup \sqrt[n]{|a_n|} < 1$, then $\sum a_n$ converges absolutely (choose $r$ with the limsup $< r < 1$; eventually $\sqrt[n]{|a_n|} \le r$, i.e. $|a_n| \le r^n$); if $\limsup\sqrt[n]{|a_n|} > 1$, the terms do not tend to $0$ and the series diverges.
<1>7. Integral test.
    Proof: if $f \ge 0$ is decreasing on $[1,\infty)$, then $\sum_{n=1}^N f(n)$ and $\int_1^N f$ converge or diverge together, since $\int_1^{N+1}f \le \sum_{n=1}^N f(n) \le f(1) + \int_1^N f$ (compare the sum to the integral over unit intervals).
<1>8. Alternating series test.
    Proof: if $a_n \ge 0$ decreases to $0$, then $\sum (-1)^{n+1}a_n$ converges: the even and odd partial sums are monotone and bounded (interleaved), so both converge to a common limit, and the error after $N$ terms is bounded by $a_{N+1}$.
<1>9. The harmonic series diverges.
    Proof: group terms: $1 + \tfrac12 + (\tfrac13+\tfrac14) + (\tfrac15+\cdots+\tfrac18) + \cdots \ge 1 + \tfrac12 + \tfrac12 + \tfrac12 + \cdots = \infty$; or use the integral test with $f(x) = 1/x$ ($\int_1^\infty dx/x = \infty$).
<1>10. Sum of a geometric series.
    Proof: $s_N = \sum_{n=0}^{N-1} x^n$ satisfies $(1-x)s_N = 1 - x^N$, so $s_N = \frac{1-x^N}{1-x}$ for $x \ne 1$; if $|x| < 1$, $s_N \to \frac{1}{1-x}$. If $|x| \ge 1$ and $x \ne 1$, the terms do not tend to $0$, so it diverges; at $x = 1$, $s_N = N \to \infty$.
<1>11. The $p$-test.
    Proof: $\sum_{n\ge1} n^{-p}$ converges iff $p > 1$. For $p > 1$ use the integral test: $\int_1^\infty x^{-p}dx = \frac{1}{p-1} < \infty$; for $p \le 1$: $\sum n^{-p} \ge \sum n^{-1} = \infty$ (or integral test for $p < 1$).
<1>12. Absolute vs. conditional convergence.
    Proof: $\sum a_n$ converges absolutely iff $\sum |a_n| < \infty$, which implies convergence (by the Cauchy criterion: $|\sum_{M+1}^K a_n| \le \sum_{M+1}^K |a_n|$). Conditional convergence means $\sum a_n$ converges but $\sum|a_n| = \infty$. Example: $\sum (-1)^{n+1}/n$ converges (alternating series test, <1>8) but $\sum 1/n$ diverges (<1>9).
<1>13. Q.E.D.
:::
