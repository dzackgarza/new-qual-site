---
schema: qual/card@1
id: P-BLAR-07
kind: problem
title: Decide linearity and find transformation matrices
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Review Problem 7 in the deterministic MinerU Flash extraction assets/attachments/Basic_Linear_Algebra_Review_extracted.md. In part (d), the deterministic source declares a map from R^3 to R^2 but writes the input as T(x,y); the card preserves this mismatch explicitly rather than silently inventing a third argument.
---

::: {.problem}
Decide which of the following transformations are linear. For those that are, find the matrix of the transformation (using the standard bases):

(a) $T\colon \RR^2 \to \RR^2$ is defined by $T(x,y) = (2x, y)$

(b) $T\colon \RR^2 \to \RR^2$ is defined by $T(x,y) = (x+1, y+2)$

(c) $T\colon \RR^2 \to \RR^2$ rotates an object by an angle of $\pi/3$

(d) $T\colon \RR^3 \to \RR^2$ is defined by $T(x,y) = (x+2y, x+3y)$
:::

::: {.remark}
In part (d) the declared domain is $\RR^3$, but the formula has two input variables. As a map $\RR^2\to\RR^2$, $T(x,y)=(x+2y,x+3y)$ is linear with matrix $\begin{pmatrix}1&2\\1&3\end{pmatrix}$.
:::

::: {.solution}
Use the standard ordered bases in every matrix representation below, and use the standard convention that a positive planar rotation is counterclockwise.

::: pf

::: pf-step
In part (1), $T$ is linear, with matrix
$$
\boxed{\begin{bmatrix}2&0\\0&1\end{bmatrix}}.
$$

::: pf-proof
For $(x,y)\in\RR^2$,
$$
T(x,y)=x(2,0)+y(0,1).
$$
Thus $T$ is given by multiplication by the displayed matrix, hence is linear.
:::

:::

::: pf-step
In part (2), $T$ is $\boxed{\text{not linear}}$.

::: pf-proof
A linear map must send the zero vector to the zero vector, but here
$$
T(0,0)=(1,2)\neq(0,0).
$$
:::

:::

::: pf-step
In part (3), the rotation is linear, with matrix
$$
\boxed{
\begin{bmatrix}
\tfrac12&-\tfrac{\sqrt3}{2}\\
\tfrac{\sqrt3}{2}&\tfrac12
\end{bmatrix}}.
$$

::: pf-proof
Rotation through angle $\theta$ sends the standard basis vectors to
$$
e_1\longmapsto(\cos\theta,\sin\theta),
\qquad
e_2\longmapsto(-\sin\theta,\cos\theta).
$$
These images determine a linear transformation whose standard matrix is
$$
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}.
$$
Substituting $\theta=\pi/3$ gives the displayed matrix.
:::

:::

::: pf-step
In part (4), the source as written does $\boxed{\text{not define a map }\RR^3\to\RR^2}$, so its linearity and a $2\times3$ transformation matrix are not determined.

::: pf-proof
An element of $\RR^3$ has three coordinates, whereas the displayed rule accepts only two inputs, $T(x,y)$. No dependence on a third coordinate is specified, so the rule does not assign an output to a general element $(x,y,z)\in\RR^3$.

If the displayed formula is instead read literally as a map $\RR^2\to\RR^2$, it is linear and has matrix
$$
\begin{bmatrix}1&2\\1&3\end{bmatrix},
$$
because $(x+2y,x+3y)^T=\begin{bmatrix}1&2\\1&3\end{bmatrix}(x,y)^T$. This observation does not determine which $\RR^3\to\RR^2$ map the source intended.
:::

:::

:::

:::
