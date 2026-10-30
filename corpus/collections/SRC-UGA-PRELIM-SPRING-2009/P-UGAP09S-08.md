---
schema: qual/card@1
id: P-UGAP09S-08
kind: problem
title: A non-diagonalizable real $2\times2$ matrix, $\int_C xy^2\,dy$ around a triangle, and $f^{(10)}(0)$ for $\cos(x^2)$
classification:
  areas: [prelim]
  topics:
  - Diagonalization
  - Line Integrals
  - Taylor Series
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained extraction garbles the final coordinate of the triangle as a barred 1; the surrounding statement identifies the intended right triangle with vertices $(0,0),(1,0),(0,1)$.
---

::: {.problem}
No proofs are required.

(a) Give an example of a matrix $A\in M_2(\RR)$ that is not diagonalizable.

(b) Calculate
$$
\int_C xy^2\,dy,
$$
where $C$ is the right triangle with vertices $(0,0)$, $(1,0)$, and $(0,1)$, oriented counterclockwise.

(c) Compute $f^{(10)}(0)$ for
$$
f(x)=\cos(x^2).
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

One example of a non-diagonalizable matrix is
$$
\boxed{
A=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}}.
$$


::: pf-proof

The characteristic polynomial is
$$
(\lambda-1)^2,
$$
while
$$
\ker(A-I)
=\operatorname{span}\!\left\{\binom10\right\}
$$
is one-dimensional. Hence there is no eigenbasis.

:::

:::

::: pf-step

The line integral is
$$
\boxed{\int_C xy^2\,dy=\frac1{12}}.
$$


::: pf-proof

Use the counterclockwise parametrization of the three edges
$$
(0,0)\to(1,0)\to(0,1)\to(0,0).
$$
On the first edge $dy=0$, so the contribution is $0$. On the diagonal edge,
write
$$
x=1-t,\qquad y=t,\qquad 0\le t\le1.
$$
Then $dy=dt$, so its contribution is
$$
\int_0^1(1-t)t^2\,dt
=\left[\frac{t^3}{3}-\frac{t^4}{4}\right]_0^1
=\frac1{12}.
$$
On the final vertical edge, $x=0$, so the contribution is again $0$.

:::

:::

::: {.pf-step #s1-3}

For $f(x)=\cos(x^2)$,
$$
\boxed{f^{(10)}(0)=0}.
$$


::: pf-proof

The power series is
$$
\cos(x^2)
=\sum_{k=0}^\infty
\frac{(-1)^k x^{4k}}{(2k)!}.
$$
There is no $x^{10}$ term, so the coefficient of $x^{10}$ is $0$. Therefore
$$
f^{(10)}(0)=10!\,[x^{10}]f(x)=0.
$$

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} give the three requested computations.

:::

:::

:::
