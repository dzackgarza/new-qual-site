---
schema: qual/card@1
id: P-NRCTX
kind: problem
title: Uniformly continuous increasing convex function is differentiable a.e.
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 3 of the Spring 2015 JHU analysis qualifying exam in the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Assume $f : [0,1] \to \mathbb{R}$ is uniformly continuous, increasing and convex.
Prove $f$ is differentiable almost everywhere and

$$f(1) - f(0) = \int_0^1 f'(x) \, dx.$$

::: solution
<1>1. Prove differentiability almost everywhere.
::: proof
Since $f$ is increasing on $[0,1]$, Lebesgue's theorem on monotone functions implies that $f$ is differentiable almost everywhere on $(0,1)$. Moreover,
\[
f'(x)\ge0
\]
at every point where the derivative exists.
:::

<1>2. Use convexity to obtain absolute continuity on interior compact intervals.
::: proof
Fix
\[
0<a<b<1.
\]
Choose $a_0,b_0$ with
\[
0<a_0<a<b<b_0<1.
\]
For any $a\le x<y\le b$, convexity implies monotonicity of secant slopes, so
\[
\frac{f(a)-f(a_0)}{a-a_0}
\le
\frac{f(y)-f(x)}{y-x}
\le
\frac{f(b_0)-f(b)}{b_0-b}.
\]
Hence the secant slopes on $[a,b]$ are uniformly bounded. Therefore $f$ is Lipschitz on $[a,b]$, and hence absolutely continuous there.

The Fundamental Theorem of Calculus for absolutely continuous functions gives
\[
f(b)-f(a)=\int_a^b f'(x)\,dx.
\]
:::

<1>3. Let the interior interval expand to $[0,1]$.
::: proof
Take
\[
a_n=1/n,
\qquad
b_n=1-1/n
\]
for $n$ large. Since $f$ is uniformly continuous on $[0,1]$,
\[
f(a_n)\to f(0),
\qquad
f(b_n)\to f(1).
\]
By Step 2,
\[
f(b_n)-f(a_n)=\int_{a_n}^{b_n}f'(x)\,dx.
\]
Because $f'\ge0$ almost everywhere and the intervals $[a_n,b_n]$ increase to $(0,1)$, the Monotone Convergence Theorem yields
\[
\int_0^1 f'(x)\,dx
=\lim_{n\to\infty}\int_{a_n}^{b_n}f'(x)\,dx.
\]
Therefore
\[
\boxed{
f(1)-f(0)=\int_0^1 f'(x)\,dx.}
\]
:::
:::
