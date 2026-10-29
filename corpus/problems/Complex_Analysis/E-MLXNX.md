---
schema: qual/card@1
id: E-MLXNX
kind: problem
title: Hadamard's ill-posed Cauchy problem for Laplace's equation
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - PDEs
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
(a) Show that the function $u=u(x,y)$ given by
$$u(x,y)=\frac{e^{ny}-e^{-ny}}{2n^2}\sin nx\quad \text{for}\ n\in \NN$$
is the solution on $D=\{(x,y)\ | x^2+y^2<1\}$ of the Cauchy problem for the Laplace equation
$$\frac{\partial ^2u}{\partial x^2}+\frac{\partial ^2u}{\partial y^2}=0,\quad
u(x,0)=0,\quad \frac{\partial u}{\partial y}(x,0)=\frac{\sin nx}{n}.$$

(b) Show that there exist points $(x,y)\in D$ such that
$\displaystyle{\limsup_{n\to\infty} \abs{u(x,y)}=\infty}$.

:::

::: {.solution}
Write $u_n(x,y)\coloneqq\frac{\sinh(ny)}{n^2}\sin(nx)$ for the function of part (a) with index $n$.

::: pf

::: pf-step
(a) $u_n$ solves the Cauchy problem on $D$.

::: pf-proof
$(u_n)_{xx}=-\sinh(ny)\sin(nx)$ and $(u_n)_{yy}=\sinh(ny)\sin(nx)$, so $\Delta u_n=0$. Also $u_n(x,0)=0$ and $(u_n)_y(x,0)=\frac{n\cosh 0}{n^2}\sin(nx)=\frac{\sin(nx)}n$.
:::

:::

::: pf-step
(b) At $(x,y)=\qty(\frac\pi6,\frac12)\in D$, $\limsup_{n\to\infty}\abs{u_n(x,y)}=\infty$.

::: pf-proof
The point lies in $D$ because $\frac{\pi^2}{36}+\frac14<1$. For $n=6k+3$, $\frac{n\pi}6=k\pi+\frac\pi2$, so $\abs{\sin\frac{n\pi}6}=1$ and $\abs{u_n(\frac\pi6,\frac12)}=\frac{\sinh(n/2)}{n^2}\to\infty$.
:::

:::

:::

:::

::: {.remark}
The Cauchy data $\frac{\sin nx}n$ tend to $0$ uniformly while the solutions are unbounded at a fixed interior point: the Cauchy problem for the Laplace equation does not depend continuously on its data.
:::
