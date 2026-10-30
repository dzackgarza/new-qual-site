---
schema: qual/card@1
id: P-UCLARA13S-05
kind: problem
title: Norm of derivative evaluation on harmonic Bergman space
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Bounded Operators
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2013 section.
---

::: {.problem}
Let $D$ be the unit disk and define
$$
H=\left\{u:D\to\RR:\ u\text{ is harmonic and }\int_D \abs{u(x,y)}^2\,dx\,dy<\infty\right\},
$$
with inner product
$$
\langle f,g\rangle=\int_D fg\,dx\,dy.
$$

(a) Show that $u\mapsto u_x(0,0)$ is a bounded linear functional on $H$.

(b) Compute its norm.
:::

::: {.solution}

Let
$$
T:H\to\RR,
\qquad
T(u)=u_x(0,0).
$$

::: pf

::: pf-step

Every $u\in H$ is the real part of a holomorphic function
$$
F(z)=\sum_{n=0}^{\infty}a_nz^n
$$
on $D$.


::: pf-proof

The unit disk is simply connected, so every real-valued harmonic function on $D$ has a harmonic conjugate $v$. Thus
$$
F=u+iv
$$
is holomorphic on $D$. Every holomorphic function on the disk has a power-series expansion about $0$ with radius of convergence at least $1$.

:::

:::

::: {.pf-step #s1-2}

If
$$
a_n=\alpha_n+i\beta_n,
$$
then for $0\le r<1$,
$$
u(re^{i\theta})
=
\alpha_0
+
\sum_{n=1}^{\infty}
r^n
\bigl(
\alpha_n\cos(n\theta)
-
\beta_n\sin(n\theta)
\bigr),
$$
and
$$
u_x(0,0)=\alpha_1.
$$


::: pf-proof

Taking real parts of
$$
F(re^{i\theta})
=
\sum_{n=0}^{\infty}
(\alpha_n+i\beta_n)r^ne^{in\theta}
$$
gives the first identity. Also,
$$
F'(0)=a_1.
$$
The Cauchy--Riemann equations give
$$
F'(0)=u_x(0,0)-iu_y(0,0),
$$
so
$$
u_x(0,0)=\operatorname{Re}a_1=\alpha_1.
$$

:::

:::

::: {.pf-step #s1-3}

For every $0<R<1$,
$$
\int_{\abs{z}<R}u(z)^2\,dA(z)
=
\pi\alpha_0^2R^2
+
\pi
\sum_{n=1}^{\infty}
\frac{\alpha_n^2+\beta_n^2}{2n+2}
R^{2n+2}.
$$


::: pf-proof

For each fixed $R<1$, the power series from step [](#s1-2){.pf-ref} converges uniformly on $\abs{z}\le R$, so it may be integrated term-by-term. Orthogonality on $[0,2\pi]$ gives
$$
\int_0^{2\pi}\cos(n\theta)\cos(m\theta)\,d\theta
=
\int_0^{2\pi}\sin(n\theta)\sin(m\theta)\,d\theta
=
\begin{cases}
\pi,&n=m\ge1,\\
0,&n\ne m,
\end{cases}
$$
and all sine--cosine cross terms vanish. Hence
$$
\int_0^{2\pi}u(re^{i\theta})^2\,d\theta
=
2\pi\alpha_0^2
+
\pi
\sum_{n=1}^{\infty}
(\alpha_n^2+\beta_n^2)r^{2n}.
$$
Integrating this identity against $r\,dr$ from $0$ to $R$ gives the formula.

:::

:::

::: {.pf-step #s1-4}

For every $u\in H$,
$$
\norm{u}_H^2
\ge
\frac\pi4\,\abs{u_x(0,0)}^2.
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, every term in the expansion of the integral is nonnegative. In particular, for every $R<1$,
$$
\int_{\abs{z}<R}u(z)^2\,dA(z)
\ge
\pi
\frac{\alpha_1^2}{4}
R^4.
$$
Letting $R\uparrow1$ and using monotone convergence on the left yields
$$
\norm{u}_H^2
\ge
\frac\pi4\alpha_1^2.
$$
By step [](#s1-2){.pf-ref}, $\alpha_1=u_x(0,0)$.

:::

:::

::: {.pf-step #s1-5}

The functional $T$ is bounded and
$$
\norm{T}
\le
\frac2{\sqrt\pi}.
$$


::: pf-proof

Step [](#s1-4){.pf-ref} gives
$$
\abs{T(u)}
=
\abs{u_x(0,0)}
\le
\frac2{\sqrt\pi}\norm{u}_H
\qquad
(u\in H).
$$
Linearity follows from linearity of differentiation.

:::

:::

::: {.pf-step #s1-6}

For
$$
u_0(x,y)=x,
$$
one has
$$
T(u_0)=1
\qquad\text{and}\qquad
\norm{u_0}_H^2=\frac\pi4.
$$


::: pf-proof

The function $u_0$ is harmonic and
$$
(u_0)_x(0,0)=1.
$$
Using polar coordinates,
$$
\begin{aligned}
\norm{u_0}_H^2
&=
\int_0^1\int_0^{2\pi}
r^2\cos^2\theta\,r\,d\theta\,dr\\
&=
\left(\int_0^1r^3\,dr\right)
\left(\int_0^{2\pi}\cos^2\theta\,d\theta\right)\\
&=
\frac14\pi.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
\norm{T}
=
\frac2{\sqrt\pi}
}.
$$


::: pf-proof

Step [](#s1-5){.pf-ref} gives the upper bound. Step [](#s1-6){.pf-ref} gives
$$
\frac{\abs{T(u_0)}}{\norm{u_0}_H}
=
\frac1{\sqrt\pi/2}
=
\frac2{\sqrt\pi},
$$
so the upper bound is attained.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves boundedness in part (a), and step [](#s1-7){.pf-ref} gives the exact norm required in part (b).

:::

:::

:::
