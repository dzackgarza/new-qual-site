---
schema: qual/card@1
id: P-C3MKZ
kind: problem
title: Determine the values of $x\in\mathbb{R}$ for which
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
  - Convergence of Functions
relations: []
review: draft
solved: true
---

::: problem
Determine the values of $x\in\mathbb{R}$ for which $\displaystyle\sum_{n=1}^\infty \frac{x^n}{1+n|x|^n}$ converges, justifying your answer carefully.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. For $|x| < 1$: the series converges absolutely.
Proof: $\left|\dfrac{x^n}{1 + n|x|^n}\right| \le |x|^n$ (denominator $\ge 1$), and $\sum |x|^n$ is a convergent geometric series.

<1>2. At $x = 1$: the series diverges to $+\infty$.
Proof: every term is positive and $\dfrac{1}{1+n} \ge \dfrac{1}{2n}$, so the series dominates a divergent harmonic tail.

<1>3. At $x = -1$: the series converges.
Proof: $\sum \dfrac{(-1)^n}{1+n}$ is an alternating series whose terms decrease to $0$; Leibniz's test applies.

<1>4. For $x > 1$: the series diverges to $+\infty$.
Proof: every term is positive and $\dfrac{x^n}{1 + nx^n} = \dfrac{1}{n + x^{-n}} \ge \dfrac{1}{n+1}$, so the series dominates $\sum \dfrac{1}{n+1} = \infty$.

<1>5. For $x < -1$: the series converges (conditionally).
<2>1. Write the terms as $(-1)^n a_n$ with $a_n = \dfrac{|x|^n}{1 + n|x|^n} = \dfrac{1}{n + |x|^{-n}}$.
Proof: $x^n = (-1)^n|x|^n$; divide numerator and denominator by $|x|^n$.
<2>2. $a_n \downarrow 0$.
Proof: $n + |x|^{-n} \uparrow \infty$; the increment $\big((n+1) + |x|^{-(n+1)}\big) - \big(n + |x|^{-n}\big) = 1 - |x|^{-n}(1 - 1/|x|) > 0$ since $|x|^{-n}(1 - 1/|x|) < 1$ for $|x| > 1$.
<2>3. $\sum (-1)^n a_n$ converges.
Proof: alternating series test with <2>2. <2>4. The convergence is not absolute.
Proof: $a_n \ge \dfrac{1}{n+1}$ (by <2>1), so $\sum a_n$ diverges.

<1>6. Q.E.D.: the series converges for $x \in (-\infty, 1)$ — absolutely for $|x| < 1$, conditionally for $x \le -1$ — and diverges for $x \ge 1$.
Proof: <1>1–<1>5 cover all real $x$.
:::
