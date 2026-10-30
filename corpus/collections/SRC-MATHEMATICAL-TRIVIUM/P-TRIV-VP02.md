---
schema: qual/card@1
id: P-TRIV-VP02
kind: problem
title: Extremal of $\int_0^{\pi/2}(f'^2-f^2)\,dx$ with fixed endpoints
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Variational Principle, Problem 2, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find an extremum of the functional $J[f] = \int_0^{\pi/2} dx\, (f'^2 - f^2)$ in a class of functions $f \in C^2[0, \pi/2]$ satisfying the boundary conditions $f(0) = 0$, $f(\pi/2) = 1$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The Euler--Lagrange equation is
$$
\boxed{f''+f=0}.
$$


::: pf-proof

The Lagrangian is
$$
L(f,f')=(f')^2-f^2.
$$
Thus
$$
\frac{\partial L}{\partial f}=-2f,
\qquad
\frac{\partial L}{\partial f'}=2f'.
$$
The Euler--Lagrange equation
$$
\frac{\partial L}{\partial f}
-
\frac d{dx}
\frac{\partial L}{\partial f'}
=0
$$
therefore becomes
$$
-2f-2f''=0.
$$

:::

:::

::: {.pf-step #s1-2}

The general solution is
$$
f(x)=A\sin x+B\cos x.
$$


::: pf-proof

This is the general solution of the linear ODE from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

The boundary condition
$$
f(0)=0
$$
forces
$$
B=0.
$$


::: pf-proof

Substitute $x=0$ into step [](#s1-2){.pf-ref}:
$$
f(0)=B.
$$

:::

:::

::: {.pf-step #s1-4}

The boundary condition
$$
f(\pi/2)=1
$$
then forces
$$
A=1.
$$


::: pf-proof

With $B=0$,
$$
f(\pi/2)=A\sin(\pi/2)=A.
$$

:::

:::

::: {.pf-step #s1-5}

Hence the unique stationary function is
$$
\boxed{f_*(x)=\sin x}.
$$


::: pf-proof

Combine steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref}.

:::

:::

::: pf-step

Its functional value is
$$
J[f_*]=0.
$$


::: pf-proof

Since
$$
f_*'=\cos x,
$$
one has
$$
\begin{aligned}
J[f_*]
&=
\int_0^{\pi/2}
(\cos^2x-\sin^2x)
\,dx\\
&=
\int_0^{\pi/2}\cos2x\,dx\\
&=0.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-7}

Let
$$
f=f_*+\eta,
$$
where
$$
\eta(0)=\eta(\pi/2)=0.
$$
Then
$$
J[f]-J[f_*]
=
\int_0^{\pi/2}
\bigl((\eta')^2-\eta^2\bigr)
\,dx.
$$


::: pf-proof

Expand
$$
(f_*'+\eta')^2-(f_*+\eta)^2.
$$
The linear cross term is
$$
2
\int_0^{\pi/2}
(f_*'\eta'-f_*\eta)
\,dx.
$$
Integrating the first term by parts gives
$$
2[f_*'\eta]_0^{\pi/2}
-
2\int_0^{\pi/2}(f_*''+f_*)\eta\,dx.
$$
The boundary term vanishes because $\eta$ vanishes at both endpoints, and the
integral vanishes by step [](#s1-1){.pf-ref}. The remaining quadratic term is the displayed
expression.

:::

:::

::: {.pf-step #s1-8}

Every nonzero admissible variation satisfies
$$
\int_0^{\pi/2}(\eta')^2\,dx
\geq
4
\int_0^{\pi/2}\eta^2\,dx.
$$


::: pf-proof

This is the Dirichlet Poincaré inequality on an interval of length
$$
L=\frac\pi2.
$$
Its first Dirichlet eigenvalue is
$$
\left(\frac\pi L\right)^2
=
4.
$$

:::

:::

::: {.pf-step #s1-9}

Therefore, for every nonzero admissible variation,
$$
J[f]-J[f_*]
\geq
3
\int_0^{\pi/2}\eta^2\,dx
>0.
$$


::: pf-proof

Apply step [](#s1-8){.pf-ref} to the expression in step [](#s1-7){.pf-ref}:
$$
\int
\bigl((\eta')^2-\eta^2\bigr)
\geq
3\int\eta^2.
$$
The last integral is positive for nonzero $\eta$.

:::

:::

::: {.pf-step #s1-10}

Hence
$$
\boxed{f_*(x)=\sin x}
$$
is the unique strict minimizer, with
$$
\boxed{J[f_*]=0}.
$$


::: pf-proof

Step [](#s1-5){.pf-ref} gives the only stationary function, and step [](#s1-9){.pf-ref} shows every other
admissible function has strictly larger functional value.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} gives the required extremum and its value.

:::

:::

:::
