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

:::{.problem}
 \envlist

- Show that the function $u=u(x,y)$ given by
$$u(x,y)=\frac{e^{ny}-e^{-ny}}{2n^2}\sin nx\quad \text{for}\ n\in {\mathbf N}$$
is the solution on $D=\{(x,y)\ | x^2+y^2<1\}$ of the Cauchy problem for the Laplace equation
$$\frac{\partial ^2u}{\partial x^2}+\frac{\partial ^2u}{\partial y^2}=0,\quad
u(x,0)=0,\quad \frac{\partial u}{\partial y}(x,0)=\frac{\sin nx}{n}.$$

- Show that there exist points $(x,y)\in D$ such that
$\displaystyle{\limsup_{n\to\infty} |u(x,y)|=\infty}$.


:::

::: solution
Write
\[
u_n(x,y)=\frac{\sinh(ny)}{n^2}\sin(nx).
\]
Then
\[
(u_n)_{xx}=-\sinh(ny)\sin(nx),
\qquad
(u_n)_{yy}=\sinh(ny)\sin(nx),
\]
so $\Delta u_n=0$. Also
\[
u_n(x,0)=0,
\qquad
(u_n)_y(x,0)=\frac{\cosh(0)}n\sin(nx)=\frac{\sin(nx)}n.
\]
Thus $u_n$ solves the stated Cauchy problem.

Take the fixed point
\[
(x,y)=\left(\frac\pi6,\frac12\right).
\]
It lies in $D$, because
\[
\frac{\pi^2}{36}+\frac14<1.
\]
For $n=6k+3$ we have $|\sin(n\pi/6)|=1$, and hence
\[
\left|u_n\left(\frac\pi6,\frac12\right)\right|
=\frac{\sinh(n/2)}{n^2}.
\]
Since $\sinh(n/2)/n^2\to\infty$, it follows that
\[
\limsup_{n\to\infty}
\left|u_n\left(\frac\pi6,\frac12\right)\right|=\infty.
\]
This is Hadamard's instability phenomenon: the Cauchy data
$\sin(nx)/n$ tend uniformly to $0$, while the corresponding harmonic
solutions are unbounded at a fixed interior point along a subsequence.
:::
