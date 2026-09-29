---
schema: qual/card@1
id: P-BERK98S-11
kind: problem
title: Sylvester's criterion for a real quadratic form in three variables
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $A,B,C,D,E,F\in\mathbb R$. Show that
\[
Ax^2+2Bxy+Cy^2+2Dxz+2Eyz+Fz^2
\]
is positive definite if and only if
\[
A>0,
\qquad
\det\begin{pmatrix}A&B\\B&C\end{pmatrix}>0,
\qquad
\det\begin{pmatrix}A&B&D\\B&C&E\\D&E&F\end{pmatrix}>0.
\]
:::

::: {.solution}
Put
$$
\Delta_2\coloneqq AC-B^2,
\qquad
\Delta_3\coloneqq
\det
\begin{pmatrix}
A&B&D\\
B&C&E\\
D&E&F
\end{pmatrix},
$$
and write the quadratic form as $q(x,y,z)$.

::: pf

::: {.pf-step #s1}

If $A\neq0$ and $\Delta_2\neq0$, then
$$
\begin{aligned}
q(x,y,z)
={}&
A\left(
x+\frac BAy+\frac DAz
\right)^2\\
&+
\frac{\Delta_2}{A}
\left(
y+\frac{AE-BD}{\Delta_2}z
\right)^2
+
\frac{\Delta_3}{\Delta_2}z^2.
\end{aligned}
$$

::: pf-proof

Completing the square in $x$ gives
$$
\begin{aligned}
q(x,y,z)
={}&
A\left(
x+\frac BAy+\frac DAz
\right)^2\\
&+
\left(C-\frac{B^2}{A}\right)y^2
+
2\left(E-\frac{BD}{A}\right)yz
+
\left(F-\frac{D^2}{A}\right)z^2.
\end{aligned}
$$
Now
$$
C-\frac{B^2}{A}=\frac{\Delta_2}{A},
\qquad
E-\frac{BD}{A}=\frac{AE-BD}{A}.
$$
Completing the square in $y$ therefore gives the first two terms in the
displayed formula of this step. The remaining coefficient of $z^2$ is
$$
F-\frac{D^2}{A}
-
\frac{(AE-BD)^2}{A\Delta_2}.
$$
Multiplying this expression by $\Delta_2$ and expanding gives
$$
ACF-AE^2-B^2F+2BDE-CD^2
=\Delta_3.
$$
Hence the remaining coefficient is $\Delta_3/\Delta_2$.

:::

:::

::: {.pf-step #s2}

If
$$
A>0,
\qquad
\Delta_2>0,
\qquad
\Delta_3>0,
$$
then $q$ is positive definite.

::: pf-proof

Under these inequalities, all three coefficients
$$
A,
\qquad
\frac{\Delta_2}{A},
\qquad
\frac{\Delta_3}{\Delta_2}
$$
in step [](#s1){.pf-ref} are positive. The three linear forms occurring there arise
successively as
$$
x+\frac BAy+\frac DAz,
\qquad
y+\frac{AE-BD}{\Delta_2}z,
\qquad
z.
$$
If all three vanished, then $z=0$, then $y=0$, then $x=0$. Thus for every
nonzero $(x,y,z)$ at least one square in step [](#s1){.pf-ref} is positive, and
therefore $q(x,y,z)>0$.

:::

:::

::: {.pf-step #s3}

If $q$ is positive definite, then $A>0$.

::: pf-proof

Evaluating at $(1,0,0)$ gives
$$
A=q(1,0,0)>0.
$$

:::

:::

::: {.pf-step #s4}

If $q$ is positive definite, then $\Delta_2>0$.

::: pf-proof

By step [](#s3){.pf-ref}, $A>0$. Evaluate $q$ at the nonzero vector
$$
\left(-\frac BA,1,0\right).
$$
Then
$$
0
<
q\left(-\frac BA,1,0\right)
=
C-\frac{B^2}{A}
=
\frac{\Delta_2}{A}.
$$
Since $A>0$, this implies $\Delta_2>0$.

:::

:::

::: {.pf-step #s5}

If $q$ is positive definite, then $\Delta_3>0$.

::: pf-proof

By steps [](#s3){.pf-ref} and [](#s4){.pf-ref}, the identity in step [](#s1){.pf-ref} applies. Set
$$
z=1,
\qquad
y=-\frac{AE-BD}{\Delta_2},
\qquad
x=-\frac BAy-\frac DA.
$$
This is a nonzero vector because $z=1$, and the first two squares in
step [](#s1){.pf-ref} vanish. Hence positive definiteness gives
$$
0<q(x,y,1)=\frac{\Delta_3}{\Delta_2}.
$$
Since $\Delta_2>0$, it follows that $\Delta_3>0$.

:::

:::

::: {.pf-step #s6}

Therefore $q$ is positive definite if and only if
$$
\boxed{
A>0,
\qquad
\Delta_2>0,
\qquad
\Delta_3>0
}.
$$

::: pf-proof

Step [](#s2){.pf-ref} proves sufficiency. Steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} prove necessity.

:::

:::

::: pf-qed

The definitions of $\Delta_2$ and $\Delta_3$ make step [](#s6){.pf-ref} exactly the
three determinant inequalities in the problem.

:::

:::

:::
