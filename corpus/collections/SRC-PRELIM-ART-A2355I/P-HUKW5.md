---
schema: qual/card@1
id: P-HUKW5
kind: problem
title: The Jacobian matrix of a map $\RR^n\to\RR^m$, and the Jacobian
  of $(r\cos\theta,r\sin\theta)$ at the origin
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Define the Jacobian matrix of a mapping $f: \RR^n \to \RR^m$ at a point $a = (a_1, \dots, a_n)$ of $\RR^n$.
Compute the Jacobian matrix of $f(r,\theta) = (r\cos\theta, r\sin\theta)$ at $a = (0,0)$.
:::

::: {.solution}

::: pf

::: pf-step

Let $f=(f_1,\ldots,f_m):\RR^n\to\RR^m$ and suppose every partial derivative $\frac{\partial f_i}{\partial x_j}(a)$ exists. The \dfn{Jacobian matrix} of $f$ at $a$ is the $m\times n$ matrix
$$
J_f(a)=\left(\frac{\partial f_i}{\partial x_j}(a)\right)_{1\le i\le m,\ 1\le j\le n}
=\begin{pmatrix}
\frac{\partial f_1}{\partial x_1}(a) & \cdots & \frac{\partial f_1}{\partial x_n}(a) \\
\vdots & \ddots & \vdots \\
\frac{\partial f_m}{\partial x_1}(a) & \cdots & \frac{\partial f_m}{\partial x_n}(a)
\end{pmatrix}.
$$

::: pf-proof

When $f$ is differentiable at $a$, this is the matrix of the derivative $Df(a)$ with respect to the standard bases.

:::

:::

::: {.pf-step #general-jacobian}

For $f(r,\theta)=(r\cos\theta,r\sin\theta)$,
$$
J_f(r,\theta)=\begin{pmatrix}
\cos\theta & -r\sin\theta \\
\sin\theta & r\cos\theta
\end{pmatrix}.
$$

::: pf-proof

The components are $f_1=r\cos\theta$ and $f_2=r\sin\theta$, so $\partial_r f_1=\cos\theta$, $\partial_\theta f_1=-r\sin\theta$, $\partial_r f_2=\sin\theta$ and $\partial_\theta f_2=r\cos\theta$.

:::

:::

::: pf-step

$$
J_f(0,0)=\boxed{\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}}.
$$

::: pf-proof

Substitute $r=0$, $\theta=0$ into step [](#general-jacobian){.pf-ref}:
$$
J_f(0,0)=\begin{pmatrix}
\cos 0 & -0\cdot\sin 0 \\
\sin 0 & 0\cdot\cos 0
\end{pmatrix}
=\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}.
$$

:::

:::

:::

:::
