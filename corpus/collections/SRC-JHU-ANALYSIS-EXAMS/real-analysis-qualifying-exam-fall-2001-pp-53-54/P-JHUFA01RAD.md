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
Let $f\in L^1([0,1])$. For $k\in\NN$, define the step function $f_k$ by
$$
f_k(x)=k\int_{j/k}^{(j+1)/k}f(t)\,dt,
\qquad \frac jk\le x<\frac{j+1}{k}.
$$
Show that $f_k\to f$ in $L^1([0,1])$ as $k\to\infty$.
:::

::: {.solution}
Let $A_k:L^1([0,1])\to L^1([0,1])$ denote the averaging operator $A_k f=f_k$.

::: pf

::: {.pf-step #s1}
$A_k$ is an $L^1$ contraction.

::: pf-proof
On each interval
$$
I_{j,k}=\left[\frac jk,\frac{j+1}{k}\right),
$$
one has
$$
A_k f=k\int_{I_{j,k}}f.
$$
Therefore
$$
\int_{I_{j,k}}\abs{A_k f(x)}\,dx
=
\abs{\int_{I_{j,k}}f(t)\,dt}
\le
\int_{I_{j,k}}\abs{f(t)}\,dt.
$$
Summing over $j$ gives
$$
\norm{A_k f}_1\le\norm{f}_1.
$$
:::

:::

::: {.pf-step #s2}
$A_k g\to g$ uniformly for every continuous $g$.

::: pf-proof
Let $g\in C([0,1])$. Since $g$ is uniformly continuous, its modulus of continuity
$$
\omega_g(\delta)=\sup_{\abs{x-y}\le\delta}\abs{g(x)-g(y)}
$$
satisfies $\omega_g(\delta)\to0$ as $\delta\downarrow0$. If $x\in I_{j,k}$, then
$$
\begin{aligned}
\abs{A_k g(x)-g(x)}
&=\abs{k\int_{I_{j,k}}(g(t)-g(x))\,dt}\\
&\le k\int_{I_{j,k}}\abs{g(t)-g(x)}\,dt\\
&\le \omega_g(1/k).
\end{aligned}
$$
Hence
$$
\norm{A_k g-g}_\infty\le\omega_g(1/k)\longrightarrow0,
$$
and therefore also $\norm{A_k g-g}_1\to0$.
:::

:::

::: pf-step
Approximate an arbitrary $L^1$ function by continuous functions.

::: pf-proof
Fix $\varepsilon>0$. Choose $g\in C([0,1])$ with
$$
\norm{f-g}_1<\frac\varepsilon3,
$$
using density of $C([0,1])$ in $L^1([0,1])$. By step [](#s2){.pf-ref}, for all sufficiently large $k$,
$$
\norm{A_k g-g}_1<\frac\varepsilon3.
$$
Then the contraction estimate from step [](#s1){.pf-ref} gives
$$
\begin{aligned}
\norm{A_k f-f}_1
&\le\norm{A_k(f-g)}_1+\norm{A_k g-g}_1+\norm{g-f}_1\\
&\le2\norm{f-g}_1+\norm{A_k g-g}_1\\
&<\varepsilon.
\end{aligned}
$$
Thus $f_k=A_kf\to f$ in $L^1$.
:::

:::

:::
:::
