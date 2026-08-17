---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-08
kind: problem
title: 'Determine convergence of a parameter-dependent power series'
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
(May 2011 #4a) Determine the values of $x\in\mathbb R$ for which
$$
\sum_{n=1}^{\infty}\frac{x^n}{1+n|x|^n}
$$
converges, justifying your answer carefully.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. For $|x| < 1$ the series converges (absolutely).
Proof: for $|x| < 1$, the denominator satisfies $1 + n|x|^n \ge 1$, so $\left|\frac{x^n}{1+n|x|^n}\right| \le |x|^n$, and $\sum |x|^n$ is a geometric series converging for $|x| < 1$.
By comparison the given series converges absolutely.
<1>2. For $x \ge 1$ the series diverges.
Proof: for $x \ge 1$ (in particular $x > 0$), the terms are positive and \[\frac{x^n}{1 + nx^n} = \frac{1}{x^{-n} + n} \ge \frac{1}{1 + n}\quad\text{(as } x^{-n} \le 1\text{)},\] and $\sum \frac{1}{n+1}$ diverges (harmonic).
Hence the given series diverges by comparison.
<1>3. For $x \le -1$ the series converges conditionally.
Proof: write $x = -r$ with $r \ge 1$; the terms are $t_n = \frac{(-r)^n}{1 + nr^n} = (-1)^n\frac{r^n}{1+nr^n}$.
The magnitudes $\frac{r^n}{1+nr^n} = \frac{1}{r^{-n} + n}$ decrease to $0$ (as $n \to \infty$), so by the alternating series test the series converges.
It does not converge absolutely: as in <1>2, $\frac{r^n}{1+nr^n} \ge \frac{1}{n+1}$, whose sum diverges.
For $x = -1$ this is the alternating harmonic-type series $\sum \frac{(-1)^n}{1+n}$, which converges by Leibniz.
<1>4. Summary: converges (absolutely) for $|x| < 1$, conditionally for $x \le -1$, and diverges for $x \ge 1$.
<1>5. Q.E.D.
:::
