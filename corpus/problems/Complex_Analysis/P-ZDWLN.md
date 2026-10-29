---
schema: qual/card@1
id: P-ZDWLN
kind: problem
title: Real differentiability of $f:\RR^2\to\RR^2$ via linear maps, the inverse function
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

::: {.problem}
Let $f:\RR^2\to \RR^2$ (or $\RR^2 \to \RR$).

(a) Define in terms of linear transformations what it means for $f$ to be differentiable at a point $(a, b) \in \RR^2$.

(b) State a version of the inverse function theorem in this setting.

(c) Identify $\RR^2$ with $\CC$ and give a necessary and sufficient condition for a real-differentiable function at $(a, b)$ to be complex differentiable at the point $a+ib$.
:::

::: {.solution}
Let $p=(a,b)$ and let $f$ be defined on an open set $U\ni p$.

::: pf

::: pf-step
(a) $f:U\to\RR^m$ is differentiable at $p$ if there is a linear map $L:\RR^2\to\RR^m$ with
$$
\frac{\norm{f(p+h)-f(p)-Lh}}{\norm{h}}\longrightarrow0
\qquad(h\to0).
$$

::: pf-proof
This is the definition; $L$ is unique and is the derivative $Df(p)$.
:::

:::

::: pf-step
(b) If $f:U\to\RR^2$ is $C^1$ near $p$ and $Df(p)$ is invertible, then there are open neighborhoods $V$ of $p$ and $W$ of $f(p)$ such that $f|_V:V\to W$ is a $C^1$ diffeomorphism, and $D(f|_V)^{-1}(f(p))=(Df(p))^{-1}$.

::: pf-proof
This is the inverse function theorem.
:::

:::

::: {.pf-step #complex-linear}
A real-linear map $\RR^2\to\RR^2$ is complex-linear if and only if its matrix has the form $\begin{pmatrix}\alpha&-\beta\\ \beta&\alpha\end{pmatrix}$.

::: pf-proof
A real-linear map $T$ is complex-linear if and only if $T(iz)=iT(z)$, that is, $T$ commutes with multiplication by $i$, whose matrix is $J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$. Writing $T=\begin{pmatrix}p&q\\r&s\end{pmatrix}$, the equation $TJ=JT$ reads $\begin{pmatrix}q&-p\\s&-r\end{pmatrix}=\begin{pmatrix}-r&-s\\p&q\end{pmatrix}$, that is, $s=p$ and $r=-q$.
:::

:::

::: pf-step
(c) Write $f=u+iv$ and suppose $f$ is real-differentiable at $p$. Then $f$ is complex differentiable at $z_0=a+ib$ if and only if the Cauchy--Riemann equations $u_x=v_y$, $u_y=-v_x$ hold at $p$; in that case $f'(z_0)=u_x(p)+iv_x(p)$.

::: pf-proof
$f$ is complex differentiable at $z_0$ if and only if $Df(p)$ is multiplication by a complex number $c$, that is, complex-linear, and then $f'(z_0)=c$. Since $Df(p)=\begin{pmatrix}u_x&u_y\\v_x&v_y\end{pmatrix}$, step [](#complex-linear){.pf-ref} turns this into the Cauchy--Riemann equations, and $c=Df(p)(1)=u_x+iv_x$.
:::

:::

:::

:::
