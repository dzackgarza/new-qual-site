---
schema: qual/card@1
id: P-JES3E
kind: problem
title: $\frac{e^{ny}-e^{-ny}}{2n^2}\sin nx$ solves the Laplace Cauchy problem on the
  disk with data $\sin(nx)/n$, and $\limsup_n\abs{u}=\infty$ at some points
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - PDEs
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-19
---

::: {.problem}
Show that the function $u=u(x,y)$ given by
$$
u(x,y)=\frac{e^{ny}-e^{-ny}}{2n^2}\sin nx\quad \text{for}\ n\in \NN
$$
is the solution on $D=\{(x,y)\ \st x^2+y^2<1\}$ of the Cauchy problem for the Laplace equation
$$
\frac{\partial ^2u}{\partial x^2}+\frac{\partial ^2u}{\partial y^2}=0,\quad
u(x,0)=0,\quad \frac{\partial u}{\partial y}(x,0)=\frac{\sin nx}{n}.
$$

Show that there exist points $(x,y)\in D$ such that $\limsup_{n\to\infty} \abs{u(x,y)}=\infty$.
:::

::: {.solution}
Write $u_n$ for the function $u$ with index $n$.

::: pf

::: pf-step
$u_n(x,0) = 0$ and $\dd{u_n}{y}(x,0) = \frac{\sin(nx)}{n}$.

::: pf-proof
$u_n(x,0) = \frac{e^0 - e^0}{2n^2}\sin(nx) = 0$, and
$$
\dd{u_n}{y} = \frac{e^{ny} + e^{-ny}}{2n}\sin(nx),
$$
which equals $\frac{\sin(nx)}{n}$ at $y = 0$.
:::

:::

::: pf-step
$\Delta u_n = 0$ on $D$.

::: pf-proof
$\frac{\partial^2 u_n}{\partial x^2} = -n^2 u_n$ and $\frac{\partial^2 u_n}{\partial y^2} = \frac{e^{ny} - e^{-ny}}{2}\sin(nx) = n^2 u_n$.
:::

:::

::: {.pf-step #sin-bound}
If $x/\pi$ is irrational, then $\abs{\sin(nx)} \ge 1/2$ for infinitely many $n$.

::: pf-proof
Since $x/(2\pi)$ is irrational, the sequence $nx \bmod 2\pi$ is dense in $[0, 2\pi]$, so it enters the arc $[\pi/6, 5\pi/6]$, where $\sin \geq 1/2$, infinitely often.
:::

:::

::: pf-step
At every $(x,y)\in D$ with $y \neq 0$ and $x/\pi$ irrational, for example $(1/\pi, 1/2)$, $\limsup_{n\to\infty}\abs{u_n(x,y)} = \infty$.

::: pf-proof
Along the $n$ of step [](#sin-bound){.pf-ref},
$$
\abs{u_n(x,y)} \ge \frac{e^{n\abs{y}} - e^{-n\abs{y}}}{4n^2},
$$
which tends to $\infty$ because $\abs{y} > 0$.
The point $(1/\pi, 1/2)$ lies in $D$ since $1/\pi^2 + 1/4 < 1$.
:::

:::

:::
:::
