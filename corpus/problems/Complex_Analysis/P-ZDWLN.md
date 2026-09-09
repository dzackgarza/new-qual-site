---
schema: qual/card@1
id: P-ZDWLN
kind: problem
title: Real differentiability of $f:\RR^2\to\RR$ via linear maps, the inverse function
  theorem, and the Cauchy–Riemann criterion for complex differentiability
classification:
  areas:
  - complex-analysis
  topics:
  - Calculus
  - Cauchy-Riemann
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Let $f:\mathbb{R}^2\to \mathbb{R}^2$ (or $\mathbb{R}^2 \to \mathbb{R}$).

a. Define in terms of linear transformations what it means for $f$ to be differentiable at a point $(a, b) \in \mathbb{R}^2$.

b. State a version of the inverse function theorem in this setting.

c. Identify $\mathbb{R}^2$ with $\mathbb{C}$ and give a necessary and sufficient condition for a real-differentiable function at $(a, b)$ to be complex differentiable at the point $a+ib$.
:::

::: solution
<1>1. Let $p=(a,b)$. A map $f:U\subset\mathbb R^2\to\mathbb R^m$ is differentiable at $p$ if there is a linear map
\[
L:\mathbb R^2\to\mathbb R^m
\]
such that
\[
\frac{\|f(p+h)-f(p)-Lh\|}{\|h\|}\longrightarrow0
\qquad(h\to0).
\]
The map $L$ is the Fréchet derivative $Df(p)$.

<1>2. If $f:U\to\mathbb R^2$ is $C^1$ near $p$ and $Df(p)$ is invertible, then there are neighborhoods $V$ of $p$ and $W$ of $f(p)$ such that
\[
f|_V:V\to W
\]
is a $C^1$ diffeomorphism. Moreover
\[
D(f|_V)^{-1}(f(p))=(Df(p))^{-1}.
\]

<1>3. Identify $\mathbb R^2$ with $\mathbb C$ and write
\[
f=u+iv.
\]
Assume $f$ is real-differentiable at $(a,b)$. Then $f$ is complex differentiable at $z_0=a+ib$ iff the real-linear map $Df(a,b)$ is actually complex-linear. A real-linear map is complex-linear iff its matrix has the form
\[
\begin{pmatrix}\alpha&-\beta\\ \beta&\alpha\end{pmatrix}.
\]
Since
\[
Df(a,b)=
\begin{pmatrix}u_x&u_y\\v_x&v_y\end{pmatrix},
\]
this is equivalent to the Cauchy--Riemann equations
\[
u_x=v_y,\qquad u_y=-v_x
\]
at $(a,b)$. In that case
\[
f'(z_0)=u_x(a,b)+i\,v_x(a,b).
\]
:::
