---
schema: qual/card@1
id: E-IAQ6D
kind: problem
title: Continuous functions on $[0,1]$ with vanishing moments are identically zero
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Convergence of Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: exercise
Suppose $f\colon[0,1]\to\mathbb{R}$ is continuous and $\int_0^1 f(t)t^n\,dt=0$ for all $n=0,1,2,\ldots$.
Show that $f(t)=0$ for all $t\in[0,1]$.

![](../../assets/Real_Analysis/020_Integration/figures/2021-11-27_20-59-05.png)
:::


::: solution
<1>1. Extend the moment condition from monomials to all polynomials.
::: proof
If
\[
p(t)=\sum_{k=0}^N a_k t^k,
\]
then linearity of the integral and the hypotheses give
\[
\int_0^1 f(t)p(t)\,dt
=
\sum_{k=0}^N a_k\int_0^1 f(t)t^k\,dt
=0.
\]
Thus $f$ is orthogonal, in the integral pairing, to every polynomial.
:::

<1>2. Approximate $f$ uniformly by polynomials.
::: proof
By the Weierstrass approximation theorem, there are polynomials $p_n$ such that
\[
\|p_n-f\|_\infty\longrightarrow0.
\]
Since $f$ is continuous on $[0,1]$, it is integrable, and therefore
\[
\begin{aligned}
\left|\int_0^1 f(t)^2\,dt-\int_0^1 f(t)p_n(t)\,dt\right|
&=
\left|\int_0^1 f(t)(f(t)-p_n(t))\,dt\right|\\
&\le
\|f-p_n\|_\infty\int_0^1|f(t)|\,dt
\longrightarrow0.
\end{aligned}
\]
But Step 1 gives
\[
\int_0^1 f(t)p_n(t)\,dt=0
\]
for every $n$. Hence
\[
\int_0^1 f(t)^2\,dt=0.
\]
Since $f^2$ is continuous and nonnegative, this implies $f(t)^2=0$ for every $t\in[0,1]$. Therefore
\[
\boxed{f\equiv0.}
\]
:::
:::
