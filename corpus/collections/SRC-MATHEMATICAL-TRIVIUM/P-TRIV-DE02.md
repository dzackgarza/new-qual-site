---
schema: qual/card@1
id: P-TRIV-DE02
kind: problem
title: Linear system $x'=-x+6y$, $y'=2x+3y$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 2, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve $\left\{ { \begin{array} { l } { x ^ { \prime } ( t ) = - x ( t ) + 6 y ( t ) } \\ { y ^ { \prime } ( t ) = 2 x ( t ) + 3 y ( t ) } \end{array} } \right.$
:::

::: {.solution}

Write
$$
u(t)=
\begin{pmatrix}
x(t)\\
y(t)
\end{pmatrix},
\qquad
A=
\begin{pmatrix}
-1&6\\
2&3
\end{pmatrix}.
$$
Then the system is
$$
u'=Au.
$$

::: pf

::: pf-step

The characteristic polynomial is
$$
\det(A-\lambda I)
=
\lambda^2-2\lambda-15.
$$


::: pf-proof

Compute
$$
\begin{aligned}
\det
\begin{pmatrix}
-1-\lambda&6\\
2&3-\lambda
\end{pmatrix}
&=
(-1-\lambda)(3-\lambda)-12\\
&=
\lambda^2-2\lambda-15.
\end{aligned}
$$

:::

:::

::: pf-step

The eigenvalues are
$$
\boxed{\lambda_1=5,
\qquad
\lambda_2=-3}.
$$


::: pf-proof

Factor
$$
\lambda^2-2\lambda-15
=
(\lambda-5)(\lambda+3).
$$

:::

:::

::: {.pf-step #s1-3}

For $\lambda_1=5$, an eigenvector is
$$
v_1=
\begin{pmatrix}
1\\
1
\end{pmatrix}.
$$


::: pf-proof

The equation
$$
(A-5I)v=0
$$
is
$$
-6x+6y=0,
$$
so $y=x$.

:::

:::

::: {.pf-step #s1-4}

For $\lambda_2=-3$, an eigenvector is
$$
v_2=
\begin{pmatrix}
-3\\
1
\end{pmatrix}.
$$


::: pf-proof

The equation
$$
(A+3I)v=0
$$
is
$$
2x+6y=0,
$$
so $x=-3y$.

:::

:::

::: pf-step

Therefore two independent solutions are
$$
u_1(t)=e^{5t}v_1
$$
and
$$
u_2(t)=e^{-3t}v_2.
$$


::: pf-proof

If $Av=\lambda v$, then
$$
\frac d{dt}(e^{\lambda t}v)
=
\lambda e^{\lambda t}v
=
A(e^{\lambda t}v).
$$
The eigenvectors from steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} are linearly independent.

:::

:::

::: {.pf-step #s1-6}

Hence the general solution is
$$
\boxed{
\begin{aligned}
x(t)
&=
C_1e^{5t}
-
3C_2e^{-3t},\\
y(t)
&=
C_1e^{5t}
+
C_2e^{-3t},
\end{aligned}
}
$$
where $C_1,C_2\in\RR$.


::: pf-proof

Take the arbitrary linear combination
$$
u=C_1u_1+C_2u_2
$$
and read off the two coordinates.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the complete two-parameter solution family.

:::

:::

:::
