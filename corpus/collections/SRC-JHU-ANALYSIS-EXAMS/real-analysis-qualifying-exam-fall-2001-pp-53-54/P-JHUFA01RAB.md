---
schema: qual/card@1
id: P-JHUFA01RAB
kind: problem
title: Convolution of functions vanishing at infinity
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the JHU Real Analysis Qualifying Exam, Fall 2001, in the preserved exam compilation.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f,g:\RR\to\RR$ be continuous, suppose
$$
\lim_{\abs{x}\to\infty}f(x)=0,
\qquad
\int_{-\infty}^\infty \abs{g(y)}\,dy<\infty,
$$
and define
$$
h(x)=\int_{-\infty}^\infty f(x-y)g(y)\,dy.
$$
Prove that
$$
\lim_{\abs{x}\to\infty}h(x)=0.
$$
:::

::: {.solution}
Because $f$ is continuous and tends to $0$ at both ends, it is bounded; write
$$
M=\norm{f}_\infty<\infty.
$$
Fix $\varepsilon>0$. Choose $R>0$ so large that
$$
\int_{\abs{y}>R}\abs{g(y)}\,dy<\frac{\varepsilon}{2M}
$$
when $M>0$; if $M=0$, then $f\equiv0$ and there is nothing to prove.

Since $f(x)\to0$ as $\abs{x}\to\infty$, there exists $A>0$ such that
$$
\abs{f(z)}<\frac{\varepsilon}{2\norm{g}_1}
\qquad(\abs{z}>A)
$$
when $\norm{g}_1>0$; if $g=0$ a.e., the conclusion is immediate.

Now take $\abs{x}>A+R$. For every $\abs{y}\le R$ one has
$$
\abs{x-y}\ge \abs{x}-\abs{y}>A,
$$
so
$$
\begin{aligned}
\abs{h(x)}
&\le \int_{\abs{y}\le R}\abs{f(x-y)}\,\abs{g(y)}\,dy
 +\int_{\abs{y}>R}\abs{f(x-y)}\,\abs{g(y)}\,dy\\
&\le \frac{\varepsilon}{2\norm{g}_1}\int_{\abs{y}\le R}\abs{g(y)}\,dy
 +M\int_{\abs{y}>R}\abs{g(y)}\,dy\\
&<\frac\varepsilon2+\frac\varepsilon2
=\varepsilon.
\end{aligned}
$$
Hence $h(x)\to0$ as $\abs{x}\to\infty$.
:::
