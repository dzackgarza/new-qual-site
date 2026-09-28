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

<1>1. If $A\neq0$ and $\Delta_2\neq0$, then
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

::: {.proof}
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

<1>2. If
$$
A>0,
\qquad
\Delta_2>0,
\qquad
\Delta_3>0,
$$
then $q$ is positive definite.

::: {.proof}
Under these inequalities, all three coefficients
$$
A,
\qquad
\frac{\Delta_2}{A},
\qquad
\frac{\Delta_3}{\Delta_2}
$$
in step <1>1 are positive. The three linear forms occurring there arise
successively as
$$
x+\frac BAy+\frac DAz,
\qquad
y+\frac{AE-BD}{\Delta_2}z,
\qquad
z.
$$
If all three vanished, then $z=0$, then $y=0$, then $x=0$. Thus for every
nonzero $(x,y,z)$ at least one square in step <1>1 is positive, and
therefore $q(x,y,z)>0$.
:::

<1>3. If $q$ is positive definite, then $A>0$.

::: {.proof}
Evaluating at $(1,0,0)$ gives
$$
A=q(1,0,0)>0.
$$
:::

<1>4. If $q$ is positive definite, then $\Delta_2>0$.

::: {.proof}
By step <1>3, $A>0$. Evaluate $q$ at the nonzero vector
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

<1>5. If $q$ is positive definite, then $\Delta_3>0$.

::: {.proof}
By steps <1>3 and <1>4, the identity in step <1>1 applies. Set
$$
z=1,
\qquad
y=-\frac{AE-BD}{\Delta_2},
\qquad
x=-\frac BAy-\frac DA.
$$
This is a nonzero vector because $z=1$, and the first two squares in
step <1>1 vanish. Hence positive definiteness gives
$$
0<q(x,y,1)=\frac{\Delta_3}{\Delta_2}.
$$
Since $\Delta_2>0$, it follows that $\Delta_3>0$.
:::

<1>6. Therefore $q$ is positive definite if and only if
$$
\boxed{
A>0,
\qquad
\Delta_2>0,
\qquad
\Delta_3>0
}.
$$

::: {.proof}
Step <1>2 proves sufficiency. Steps <1>3--<1>5 prove necessity.
:::

<1>7. Q.E.D.

::: {.proof}
The definitions of $\Delta_2$ and $\Delta_3$ make step <1>6 exactly the
three determinant inequalities in the problem.
:::
:::
