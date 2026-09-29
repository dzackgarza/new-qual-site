---
schema: qual/card@1
id: P-BERK85SU-18
kind: problem
title: General solution of $y_1'=-3y_1+10y_2$, $y_2'=-3y_1+8y_2$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    The coefficient matrix has characteristic polynomial
    (lambda-2)(lambda-3), with eigenvectors (2,1)^T and (5,3)^T.
    These form a basis, reducing the system to c_1'=2c_1 and
    c_2'=3c_2. Hence all solutions are
    C_1 e^{2x}(2,1)^T+C_2 e^{3x}(5,3)^T.
---

::: {.problem}
Solve the system
\[
\frac{dy_1}{dx}=-3y_1+10y_2,
\qquad
\frac{dy_2}{dx}=-3y_1+8y_2.
\]
:::

::: {.solution}
Write
$$
Y=
\begin{pmatrix}
y_1\\
y_2
\end{pmatrix},
\qquad
M=
\begin{pmatrix}
-3&10\\
-3&8
\end{pmatrix}.
$$
Then the system is $Y'=MY$.

::: pf

::: pf-step

The eigenvalues of $M$ are $2$ and $3$.

::: pf-proof

The characteristic polynomial is
$$
\begin{aligned}
\det(\lambda I-M)
&=
\det
\begin{pmatrix}
\lambda+3&-10\\
3&\lambda-8
\end{pmatrix}\\
&=
(\lambda+3)(\lambda-8)+30\\
&=
\lambda^2-5\lambda+6\\
&=
(\lambda-2)(\lambda-3).
\end{aligned}
$$

:::

:::

::: {.pf-step #s2}

Eigenvectors for the eigenvalues $2$ and $3$ are respectively
$$
v_2=
\begin{pmatrix}
2\\
1
\end{pmatrix},
\qquad
v_3=
\begin{pmatrix}
5\\
3
\end{pmatrix}.
$$

::: pf-proof

Direct multiplication gives
$$
Mv_2
=
\begin{pmatrix}
4\\
2
\end{pmatrix}
=
2v_2
$$
and
$$
Mv_3
=
\begin{pmatrix}
15\\
9
\end{pmatrix}
=
3v_3.
$$

:::

:::

::: {.pf-step #s3}

The vectors $v_2,v_3$ form a basis of $\RR^2$.

::: pf-proof

Their determinant is
$$
\det
\begin{pmatrix}
2&5\\
1&3
\end{pmatrix}
=
1\neq0.
$$
Hence they are linearly independent and therefore form a basis.

:::

:::

::: {.pf-step #s4}

If
$$
Y(x)=c_1(x)v_2+c_2(x)v_3,
$$
then the system $Y'=MY$ is equivalent to
$$
c_1'=2c_1,
\qquad
c_2'=3c_2.
$$

::: pf-proof

Differentiating the basis expansion gives
$$
Y'
=
c_1'v_2+c_2'v_3.
$$
By step [](#s2){.pf-ref},
$$
MY
=
c_1Mv_2+c_2Mv_3
=
2c_1v_2+3c_2v_3.
$$
Since $v_2,v_3$ are a basis by step [](#s3){.pf-ref}, equality $Y'=MY$ holds
exactly when the corresponding coefficients agree.

:::

:::

::: {.pf-step #s5}

The general solution is
$$
\boxed{
Y(x)
=
C_1e^{2x}
\begin{pmatrix}
2\\
1
\end{pmatrix}
+
C_2e^{3x}
\begin{pmatrix}
5\\
3
\end{pmatrix}
},
\qquad
C_1,C_2\in\RR.
$$

::: pf-proof

The scalar equations in step [](#s4){.pf-ref} have the general solutions
$$
c_1(x)=C_1e^{2x},
\qquad
c_2(x)=C_2e^{3x}.
$$
Substituting these into the basis expansion gives the displayed
formula. Conversely, every displayed function satisfies the two
scalar equations and hence, by step [](#s4){.pf-ref}, the original system.

:::

:::

::: {.pf-step #s6}

Equivalently,
$$
\boxed{
\begin{aligned}
y_1(x)&=2C_1e^{2x}+5C_2e^{3x},\\
y_2(x)&=C_1e^{2x}+3C_2e^{3x}.
\end{aligned}
}
$$

::: pf-proof

This is the coordinate form of the vector solution in step [](#s5){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s5){.pf-ref} and [](#s6){.pf-ref} give all solutions of the system.

:::

:::

:::
