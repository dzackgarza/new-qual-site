---
schema: qual/card@1
id: P-RASP13A
kind: problem
title: "True/false on absolutely continuous functions, Radon measures, weak convergence, and convergence in measure"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the official UCSD Spring 2013 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Determine if the statements below are True or False.

(a) (5 points) If the derivative of a real-valued, absolutely continuous function $f$ on $\mathbb{R}$ vanishes almost everywhere, then $f$ must be a constant on $\mathbb{R}$.

(b) (5 points) If $X$ is a locally compact Hausdorff topological space and $x \in X$, then the Dirac delta measure $\delta_x$ is a Radon measure on Borel sets of $X$.

(c) (5 points) Let $H$ be a real Hilbert space.
Assume a sequence $\{x_n\}$ converges to $x$ weakly in $H$.
Then $\lim_{n \to \infty} \|x_n\| = \|x\|$ implies that $\{x_n\}$ converges to $x$ in $H$.

(d) (5 points) Let $f, g$, and $f_n$ and $g_n$ ($n = 1, 2, \ldots$) be all real-valued, Lebesgue measurable functions on $\mathbb{R}$.
If $f_n \to f$ and $g_n \to g$ in measure, then $f_n g_n \to fg$ in measure.
:::

::: solution
<1>1. Part (a) is true.
::: proof
Fix $a<b$. Since $f$ is absolutely continuous, the fundamental theorem of calculus gives
\[
f(b)-f(a)=\int_a^b f'(x)\,dx.
\]
Because $f'=0$ almost everywhere,
\[
f(b)-f(a)=0.
\]
Thus $f(a)=f(b)$ for all $a,b\in\mathbb R$, so $f$ is constant.
:::

<1>2. Part (b) is true.
::: proof
For a Borel set $E\subseteq X$,
\[
\delta_x(E)=
\begin{cases}
1,&x\in E,\\
0,&x\notin E.
\end{cases}
\]
The measure is finite, hence finite on every compact set. It is inner regular: if $x\in E$, then the compact set $\{x\}\subseteq E$ has measure $1=\delta_x(E)$; if $x\notin E$, then both $E$ and every compact subset of it have measure $0$. Thus $\delta_x$ is a Radon measure.
:::

<1>3. Part (c) is true.
::: proof
Weak convergence gives
\[
\langle x_n,x\rangle\longrightarrow\langle x,x\rangle=\|x\|^2.
\]
Therefore
\[
\begin{aligned}
\|x_n-x\|^2
&=\|x_n\|^2+\|x\|^2-2\langle x_n,x\rangle\\
&\longrightarrow \|x\|^2+\|x\|^2-2\|x\|^2=0,
\end{aligned}
\]
using the assumed convergence $\|x_n\|\to\|x\|$. Hence $x_n\to x$ strongly in $H$.
:::

<1>4. Part (d) is false on the infinite-measure space $\mathbb R$.
::: proof
Let
\[
f_n(x)=f(x)=x,
\qquad
g_n(x)=\frac1n,
\qquad
g(x)=0.
\]
Then $f_n\to f$ in measure trivially. Also $g_n\to0$ uniformly, hence in measure.

But
\[
f_ng_n(x)=\frac xn.
\]
For every $n$,
\[
m\left(\left\{x:\left|\frac xn\right|>1\right\}\right)
=m(\{|x|>n\})
=\infty.
\]
Thus $f_ng_n$ does not converge to $0=fg$ in measure. Hence the statement is false.
:::
:::
