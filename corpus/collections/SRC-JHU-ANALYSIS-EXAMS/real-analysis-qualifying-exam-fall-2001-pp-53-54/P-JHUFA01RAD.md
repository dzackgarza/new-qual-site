---
schema: qual/card@1
id: P-JHUFA01RAD
kind: problem
title: 'Step function approximation converges in $L^1$'
classification:
  areas:
  - real-analysis
  topics:
  - Lebesgue Integration
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 4 of the JHU Real Analysis Qualifying Exam, Fall 2001, in the preserved exam compilation.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f\in L^1([0,1])$. For $k\in\mathbb N$, define the step function $f_k$ by
\[
f_k(x)=k\int_{j/k}^{(j+1)/k}f(t)\,dt,
\qquad \frac jk\le x<\frac{j+1}{k}.
\]
Show that $f_k\to f$ in $L^1([0,1])$ as $k\to\infty$.
:::

::: {.solution}
Let $A_k:L^1([0,1])\to L^1([0,1])$ denote the averaging operator $A_k f=f_k$.

<1>1. $A_k$ is an $L^1$ contraction.
::: {.proof}
On each interval
\[
I_{j,k}=\left[\frac jk,\frac{j+1}{k}\right),
\]
one has
\[
A_k f=k\int_{I_{j,k}}f.
\]
Therefore
\[
\int_{I_{j,k}}|A_k f(x)|\,dx
=
\left|\int_{I_{j,k}}f(t)\,dt\right|
\le
\int_{I_{j,k}}|f(t)|\,dt.
\]
Summing over $j$ gives
\[
\|A_k f\|_1\le\|f\|_1.
\]
:::

<1>2. $A_k g\to g$ uniformly for every continuous $g$.
::: {.proof}
Let $g\in C([0,1])$. Since $g$ is uniformly continuous, its modulus of continuity
\[
\omega_g(\delta)=\sup_{|x-y|\le\delta}|g(x)-g(y)|
\]
satisfies $\omega_g(\delta)\to0$ as $\delta\downarrow0$. If $x\in I_{j,k}$, then
\[
\begin{aligned}
|A_k g(x)-g(x)|
&=\left|k\int_{I_{j,k}}(g(t)-g(x))\,dt\right|\\
&\le k\int_{I_{j,k}}|g(t)-g(x)|\,dt\\
&\le \omega_g(1/k).
\end{aligned}
\]
Hence
\[
\|A_k g-g\|_\infty\le\omega_g(1/k)\longrightarrow0,
\]
and therefore also $\|A_k g-g\|_1\to0$.
:::

<1>3. Approximate an arbitrary $L^1$ function by continuous functions.
::: {.proof}
Fix $\varepsilon>0$. Choose $g\in C([0,1])$ with
\[
\|f-g\|_1<\frac\varepsilon3,
\]
using density of $C([0,1])$ in $L^1([0,1])$. By <1>2, for all sufficiently large $k$,
\[
\|A_k g-g\|_1<\frac\varepsilon3.
\]
Then the contraction estimate from <1>1 gives
\[
\begin{aligned}
\|A_k f-f\|_1
&\le\|A_k(f-g)\|_1+\|A_k g-g\|_1+\|g-f\|_1\\
&\le2\|f-g\|_1+\|A_k g-g\|_1\\
&<\varepsilon.
\end{aligned}
\]
Thus $f_k=A_kf\to f$ in $L^1$.
:::
:::
