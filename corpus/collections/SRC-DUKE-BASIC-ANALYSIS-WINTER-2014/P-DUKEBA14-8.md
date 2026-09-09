---
schema: qual/card@1
id: P-DUKEBA14-8
kind: problem
title: Termwise differentiation of a trigonometric series
classification:
  areas: [real-analysis]
  topics: [Uniform Convergence, Differentiation of Series]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Part II, Problem 2 of the preserved Duke Winter 2014 Basic Analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Define
\[
f(x)=\sum_{k=0}^\infty\frac{\cos(kx)}{k^3+k^2+1}.
\]
Prove that $f$ is differentiable and
\[
f'(x)=\sum_{k=0}^\infty
\frac{-k\sin(kx)}{k^3+k^2+1}.
\]
:::

::: solution
<1>1. Prove uniform convergence of the derivative series.
::: proof
For $k\ge1$,
\[
\left|
\frac{k\sin(kx)}{k^3+k^2+1}
\right|
\le
\frac{k}{k^3}
=\frac1{k^2}.
\]
Since $\sum_{k=1}^\infty k^{-2}$ converges, the Weierstrass $M$-test shows that
\[
\sum_{k=0}^\infty
\frac{-k\sin(kx)}{k^3+k^2+1}
\]
converges uniformly on $\mathbb R$.
:::

<1>2. Verify convergence of the original series at one point.
::: proof
At $x=0$,
\[
\sum_{k=0}^\infty\frac1{k^3+k^2+1}
\]
converges by comparison with $\sum_{k\ge1}k^{-3}$.
:::

<1>3. Apply the termwise differentiation theorem.
::: proof
Each summand
\[
f_k(x)=\frac{\cos(kx)}{k^3+k^2+1}
\]
is continuously differentiable. Step 1 gives uniform convergence of $\sum f_k'$, and Step 2 gives convergence of $\sum f_k$ at one point. Therefore the standard theorem on differentiating a series of $C^1$ functions implies that $\sum f_k$ converges to a differentiable function and
\[
f'(x)=\sum_{k=0}^\infty f_k'(x)
=\sum_{k=0}^\infty
\frac{-k\sin(kx)}{k^3+k^2+1}.
\]
:::
:::
