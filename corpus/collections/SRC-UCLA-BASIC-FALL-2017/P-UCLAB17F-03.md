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
$$
\begin{cases}
x_1'=6x_1-x_2,\\
x_2'=2x_1+3x_2.
\end{cases}
$$
:::

::: {.solution}

Write
$$
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
$$
Then the system is
$$
x'(t)=Mx(t).
$$

::: pf

::: pf-step

The characteristic polynomial of $M$ is
$$
\chi_M(\lambda)
=
(\lambda-4)(\lambda-5).
$$


::: pf-proof

$$
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
$$

:::

:::

::: pf-step

An eigenvector for eigenvalue $4$ is
$$
v_4=
\begin{pmatrix}
1\\
2
\end{pmatrix}.
$$


::: pf-proof

$$
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
$$

:::

:::

::: pf-step

An eigenvector for eigenvalue $5$ is
$$
v_5=
\begin{pmatrix}
1\\
1
\end{pmatrix}.
$$


::: pf-proof

$$
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
$$

:::

:::

::: {.pf-step #s1-4}

The vectors $v_4$ and $v_5$ form a basis of $\RR^2$.


::: pf-proof

They correspond to distinct eigenvalues, so they are linearly independent.
Since $\RR^2$ has dimension $2$, they form a basis.

:::

:::

::: {.pf-step #s1-5}

For arbitrary constants
$$
c_4,c_5\in\RR,
$$
the function
$$
x(t)
=
c_4e^{4t}v_4
+
c_5e^{5t}v_5
$$
solves the system.


::: pf-proof

Differentiate:
$$
x'(t)
=
4c_4e^{4t}v_4
+
5c_5e^{5t}v_5.
$$
Using
$$
Mv_4=4v_4,
\qquad
Mv_5=5v_5,
$$
one gets
$$
Mx(t)
=
4c_4e^{4t}v_4
+
5c_5e^{5t}v_5
=
x'(t).
$$

:::

:::

::: pf-step

Every solution has the form in step [](#s1-5){.pf-ref}.


::: pf-proof

For any initial value
$$
x(0)\in\RR^2,
$$
step [](#s1-4){.pf-ref} gives unique constants $c_4,c_5$ such that
$$
x(0)
=
c_4v_4+c_5v_5.
$$
The function in step [](#s1-5){.pf-ref} has exactly this initial value.
Uniqueness for linear systems with constant coefficients implies that it is the unique solution with that initial value.
Thus every solution is obtained in this way.

:::

:::

::: {.pf-step #s1-7}

Hence the general solution is
$$
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
c_4,c_5\in\RR.
}
$$


::: pf-proof

Expand the vector formula from step [](#s1-5){.pf-ref} coordinatewise.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} gives all solutions of the system.

:::

:::

:::
