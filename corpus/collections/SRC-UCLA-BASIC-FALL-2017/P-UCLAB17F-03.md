---
schema: qual/card@1
id: P-UCLAB17F-03
kind: problem
title: Solve a two-dimensional linear differential system
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Fall 2017, `assets/attachments/basic-17F.pdf`.
---

::: {.problem}
Solve
\[
\begin{cases}
x_1'=6x_1-x_2,\\
x_2'=2x_1+3x_2.
\end{cases}
\]
:::

::: {.solution}
Write
\[
x(t)=
\begin{pmatrix}
x_1(t)\\
x_2(t)
\end{pmatrix},
\qquad
M=
\begin{pmatrix}
6&-1\\
2&3
\end{pmatrix}.
\]
Then the system is
\[
x'(t)=Mx(t).
\]

<1>1. The characteristic polynomial of $M$ is
\[
\chi_M(\lambda)
=
(\lambda-4)(\lambda-5).
\]

::: {.proof}
\[
\begin{aligned}
\det(\lambda I-M)
&=
\det
\begin{pmatrix}
\lambda-6&1\\
-2&\lambda-3
\end{pmatrix}\\
&=
(\lambda-6)(\lambda-3)+2\\
&=
\lambda^2-9\lambda+20\\
&=
(\lambda-4)(\lambda-5).
\end{aligned}
\]
:::

<1>2. An eigenvector for eigenvalue $4$ is
\[
v_4=
\begin{pmatrix}
1\\
2
\end{pmatrix}.
\]

::: {.proof}
\[
(M-4I)
\begin{pmatrix}
1\\
2
\end{pmatrix}
=
\begin{pmatrix}
2&-1\\
2&-1
\end{pmatrix}
\begin{pmatrix}
1\\
2
\end{pmatrix}
=
\begin{pmatrix}
0\\
0
\end{pmatrix}.
\]
:::

<1>3. An eigenvector for eigenvalue $5$ is
\[
v_5=
\begin{pmatrix}
1\\
1
\end{pmatrix}.
\]

::: {.proof}
\[
(M-5I)
\begin{pmatrix}
1\\
1
\end{pmatrix}
=
\begin{pmatrix}
1&-1\\
2&-2
\end{pmatrix}
\begin{pmatrix}
1\\
1
\end{pmatrix}
=
\begin{pmatrix}
0\\
0
\end{pmatrix}.
\]
:::

<1>4. The vectors $v_4$ and $v_5$ form a basis of $\mathbb R^2$.

::: {.proof}
They correspond to distinct eigenvalues, so they are linearly independent.
Since $\mathbb R^2$ has dimension $2$, they form a basis.
:::

<1>5. For arbitrary constants
\[
c_4,c_5\in\mathbb R,
\]
the function
\[
x(t)
=
c_4e^{4t}v_4
+
c_5e^{5t}v_5
\]
solves the system.

::: {.proof}
Differentiate:
\[
x'(t)
=
4c_4e^{4t}v_4
+
5c_5e^{5t}v_5.
\]
Using
\[
Mv_4=4v_4,
\qquad
Mv_5=5v_5,
\]
one gets
\[
Mx(t)
=
4c_4e^{4t}v_4
+
5c_5e^{5t}v_5
=
x'(t).
\]
:::

<1>6. Every solution has the form in step <1>5.

::: {.proof}
For any initial value
\[
x(0)\in\mathbb R^2,
\]
step <1>4 gives unique constants $c_4,c_5$ such that
\[
x(0)
=
c_4v_4+c_5v_5.
\]
The function in step <1>5 has exactly this initial value.
Uniqueness for linear systems with constant coefficients implies that it is the unique solution with that initial value.
Thus every solution is obtained in this way.
:::

<1>7. Hence the general solution is
\[
\boxed{
\begin{aligned}
x_1(t)
&=
c_4e^{4t}
+
c_5e^{5t},\\
x_2(t)
&=
2c_4e^{4t}
+
c_5e^{5t},
\end{aligned}
\qquad
c_4,c_5\in\mathbb R.
}
\]

::: {.proof}
Expand the vector formula from step <1>5 coordinatewise.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 gives all solutions of the system.
:::
:::
