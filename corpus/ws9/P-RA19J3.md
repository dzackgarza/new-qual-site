---
schema: qual/card@1
id: P-RA19J3
kind: problem
title: 'UGA analysis qualifying exam, January 2019, problem 3'
classification:
  areas:
  - real-analysis
  topics:
  - series-of-functions
  - convergence-of-functions
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Determine the values of $x\in\mathbb R$ for which $$\sum_{n=1}^{\infty}\frac{x^n}{1+n|x|^n}$$ converges.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Determine the $x \in \mathbb R$ for which $\sum_{n=1}^\infty \frac{x^n}{1 + n|x|^n}$ converges.

<1>1. For $|x| < 1$: absolute convergence.
Proof: $\left|\frac{x^n}{1+n|x|^n}\right| \le |x|^n$ and $\sum|x|^n$ converges (geometric, ratio $|x| < 1$).

<1>2. At $x = 1$: divergence.
Proof: the series is $\sum \frac{1}{1+n}$, and $\frac{1}{1+n} \ge \frac{1}{2n}$; comparison with the divergent harmonic series.

<1>3. At $x = -1$: conditional convergence.
Proof: the series is $\sum \frac{(-1)^n}{1+n}$, alternating with magnitudes $\frac{1}{1+n} \downarrow 0$; Leibniz test.

<1>4. For $x > 1$: divergence.
Proof: all terms are positive ($x^n/(1+nx^n) > 0$), and $\frac{x^n}{1+nx^n} = \frac{1}{n + x^{-n}} \ge \frac{1}{n+1}$ (since $x^{-n} \le 1$), so the series dominates $\sum \frac{1}{n+1} = \infty$ term-by-term.

<1>5. For $x < -1$: conditional convergence.
<2>1. The terms are $\frac{x^n}{1+n|x|^n} = \frac{(-1)^n|x|^n}{1+n|x|^n} = (-1)^n b_n$ with $b_n := \frac{|x|^n}{1 + n|x|^n} = \frac{1}{n + |x|^{-n}} > 0$.
Proof: write $x^n = (-1)^n|x|^n$ and divide by $|x|^n$.
<2>2. $b_n \downarrow 0$: decreasing and tending to $0$.
Proof: $b_n = 1/(n + |x|^{-n})$; the denominator increases in $n$ (both $n$ and $|x|^{-n}$ do), so $b_n$ decreases; and $b_n \to 0$ since $n + |x|^{-n} \to \infty$.
<2>3. The alternating series $\sum (-1)^n b_n$ converges.
Proof: Leibniz test applied to <2>1–<2>2. It is not absolutely convergent: $b_n \ge \frac{1}{2n}$ for large $n$ (as $|x|^{-n} \le n$ eventually), and $\sum 1/n$ diverges.
<2>4. Q.E.D. Proof: <2>3 establishes conditional convergence for every $x < -1$.

<1>6. Q.E.D. Proof: <1>1–<1>5: the series converges absolutely for $|x| < 1$, conditionally for $x \le -1$, and diverges for $x \ge 1$ (at $x = 1$ and for $x > 1$). Domain: $(-\infty, 1)$.
:::
