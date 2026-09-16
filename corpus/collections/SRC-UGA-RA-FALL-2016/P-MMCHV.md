---
schema: qual/card@1
id: P-MMCHV
kind: problem
title: Termwise differentiation of $\sum n^{-x}$ on $(1,\infty)$
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
  - Differentiation
  - Uniform Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 1 of the official UGA August 2016 real-analysis qualifying exam; supplied the missing uniform-convergence argument needed for termwise differentiation.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Define
\[
f(x) = \sum_{n=1}^{\infty} \frac{1}{n^{x}}.
\] 
Show that $f$ converges to a differentiable function on $(1, \infty)$ and that
\[
f'(x)  =\sum_{n=1}^{\infty}\left(\frac{1}{n^{x}}\right)^{\prime}.
\]

> Hint:
\[
\left(\frac{1}{n^{x}}\right)' = -\frac{1}{n^{x}} \ln n
\]
:::

::: solution

Let
\[
f_N(x)=\sum_{n=1}^N n^{-x}.
\]
Fix a compact interval $[a,b]\subset(1,\infty)$. For $x\in[a,b]$,
\[
|n^{-x}|\le n^{-a},
\]
and $\sum n^{-a}$ converges. Hence $\sum n^{-x}$ converges uniformly on $[a,b]$ by the Weierstrass $M$-test.

Also
\[
\frac{d}{dx}n^{-x}=-(\log n)n^{-x}.
\]
Choose $\delta=(a-1)/2>0$. Since $\log n=o(n^\delta)$, there is $C>0$ such that
\[
\log n\le Cn^\delta
\]
for every $n\ge2$. Thus for $x\in[a,b]$,
\[
|(\log n)n^{-x}|
\le Cn^{-(a-\delta)}.
\]
Because
\[
a-\delta=\frac{a+1}{2}>1,
\]
the comparison series converges. Therefore
\[
\sum_{n=1}^\infty -(\log n)n^{-x}
\]
converges uniformly on $[a,b]$.

The standard theorem on termwise differentiation of a series of $C^1$ functions now applies: the original series converges at every point of $[a,b]$ (indeed uniformly there), and the derivative series converges uniformly. Hence its sum is differentiable on $[a,b]$ and
\[
f'(x)=-\sum_{n=1}^\infty\frac{\log n}{n^x}.
\]
Since every $x>1$ lies in such a compact interval,
\[
\boxed{f'(x)=\sum_{n=1}^\infty\left(n^{-x}\right)'\qquad(x>1).}
\]
:::
