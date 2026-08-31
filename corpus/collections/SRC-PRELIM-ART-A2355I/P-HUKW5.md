---
schema: qual/card@1
id: P-HUKW5
kind: problem
title: The Jacobian matrix of a map $\mathbb{R}^n\to\mathbb{R}^m$, and the Jacobian
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
Define the Jacobian matrix of a mapping $f: \mathbb{R}^n \to \mathbb{R}^m$ at a point $a = (a_1, \dots, a_n)$ of $\mathbb{R}^n$.
Compute the Jacobian matrix of $f(r,\theta) = (r\cos\theta, r\sin\theta)$ at $a = (0,0)$.
:::

::: {.solution}
<1>1. Definition of the Jacobian matrix:
<2>1. Let $f: \mathbb{R}^n \to \mathbb{R}^m$ be given by coordinate functions $f(x) = (f_1(x), f_2(x), \dots, f_m(x))^T$ for $x = (x_1, \dots, x_n) \in \mathbb{R}^n$.
::: {.proof}
vector-valued function definition.
:::
<2>2. If the partial derivatives $\frac{\partial f_i}{\partial x_j}(a)$ exist at $a \in \mathbb{R}^n$ for all $1 \le i \le m$ and $1 \le j \le n$, the **Jacobian matrix** $J_f(a) \in M_{m \times n}(\mathbb{R})$ is defined as:
\[
J_f(a) = \begin{pmatrix}
\frac{\partial f_1}{\partial x_1}(a) & \frac{\partial f_1}{\partial x_2}(a) & \cdots & \frac{\partial f_1}{\partial x_n}(a) \\
\frac{\partial f_2}{\partial x_1}(a) & \frac{\partial f_2}{\partial x_2}(a) & \cdots & \frac{\partial f_2}{\partial x_n}(a) \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial f_m}{\partial x_1}(a) & \frac{\partial f_m}{\partial x_2}(a) & \cdots & \frac{\partial f_m}{\partial x_n}(a)
\end{pmatrix}.
\]
::: {.proof}
definition of total derivative matrix representation with respect to standard bases.
:::

<1>2. Compute the Jacobian matrix for $f(r, \theta) = (r\cos\theta, r\sin\theta)$:
<2>1. The component functions are $f_1(r, \theta) = r\cos\theta$ and $f_2(r, \theta) = r\sin\theta$.
::: {.proof}
given mapping.
:::
<2>2. Compute the partial derivatives with respect to $r$ and $\theta$:
\[
\frac{\partial f_1}{\partial r} = \cos\theta, \qquad \frac{\partial f_1}{\partial \theta} = -r\sin\theta,
\]
\[
\frac{\partial f_2}{\partial r} = \sin\theta, \qquad \frac{\partial f_2}{\partial \theta} = r\cos\theta.
\]
::: {.proof}
product and trigonometric differentiation rules.
:::
<2>3. The general Jacobian matrix at $(r, \theta)$ is:
\[
J_f(r, \theta) = \begin{pmatrix}
\cos\theta & -r\sin\theta \\
\sin\theta & r\cos\theta
\end{pmatrix}.
\]
::: {.proof}
assembling partial derivatives into $2 \times 2$ matrix.
:::

<1>3. Evaluation at $a = (0, 0)$:
<2>1. Setting $(r, \theta) = (0, 0)$:
- $\cos(0) = 1$,
- $-0 \cdot \sin(0) = 0$,
- $\sin(0) = 0$,
- $0 \cdot \cos(0) = 0$.
::: {.proof}
trigonometric values $\cos(0) = 1, \sin(0) = 0$.
:::
<2>2. Thus:
\[
J_f(0, 0) = \begin{pmatrix}
1 & 0 \\
0 & 0
\end{pmatrix}.
\]
::: {.proof}
substituting values from <2>1 into <2>3.
:::

<1>4. Conclusion:
The Jacobian matrix of $f(r, \theta) = (r\cos\theta, r\sin\theta)$ at $(0, 0)$ is $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$. Q.E.D.
::: {.proof}
<1>1 through <1>3.
:::
:::
