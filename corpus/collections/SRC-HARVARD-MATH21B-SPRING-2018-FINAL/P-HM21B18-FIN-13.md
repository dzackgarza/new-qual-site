---
schema: qual/card@1
id: P-HM21B18-FIN-13
kind: problem
title: Heat and modified wave equations by Fourier modes
classification: {areas: [applied-algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Assume $2\pi$-periodic spatial boundary conditions, and use the course
Fourier norm
$$
\norm{g}^2=\frac1\pi\int_{-\pi}^{\pi}\abs{g(x)}^2\,dx.
$$
In part (c), the initial velocity $x$ is understood as the corresponding
$2\pi$-periodic $L^2$ function on $(-\pi,\pi)$.

(a) Solve
$$
u_t=9u_{xx}
$$
with initial condition
$$
u(x,0)=4\sin x+5\sin(2x).
$$

(b) Use Parseval's equality to compute $\norm{u(x,1)}^2$.

(c) Solve
$$
u_{tt}=9u_{xx}-2u+1
$$
with
$$
u(x,0)=7\sin(5x),
\qquad
u_t(x,0)=x.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For the heat equation, each sine mode evolves by
$$
\sin(nx)\longmapsto e^{-9n^2t}\sin(nx).
$$


::: pf-proof

If $u(x,t)=a(t)\sin(nx)$, then
$$
u_t=a'(t)\sin(nx),
\qquad
9u_{xx}=-9n^2a(t)\sin(nx).
$$
Thus $a'=-9n^2a$, so $a(t)=a(0)e^{-9n^2t}$.

:::

:::

::: {.pf-step #s1-2}

The solution of part (a) is
$$
u(x,t)=4e^{-9t}\sin x+5e^{-36t}\sin(2x).
$$


::: pf-proof

Apply step [](#s1-1){.pf-ref} to the $n=1$ and $n=2$ terms in the initial condition.
At $t=0$ the resulting expression is
$4\sin x+5\sin(2x)$, as required.

:::

:::

::: {.pf-step #s1-3}

The answer to part (b) is
$$
\norm{u(x,1)}^2=16e^{-18}+25e^{-72}.
$$


::: pf-proof

With the stated norm, the functions $\sin(nx)$ are orthonormal. By
step [](#s1-2){.pf-ref},
$$
u(x,1)=4e^{-9}\sin x+5e^{-36}\sin(2x).
$$
Parseval's identity therefore gives
$$
\norm{u(x,1)}^2
=(4e^{-9})^2+(5e^{-36})^2
=16e^{-18}+25e^{-72}.
$$

:::

:::

::: {.pf-step #s1-4}

On $(-\pi,\pi)$,
$$
x=2\sum_{n=1}^\infty\frac{(-1)^{n+1}}n\sin(nx)
$$
in the Fourier sense.


::: pf-proof

The function $x$ is odd, so only sine coefficients occur. For $n\geq1$,
$$
\begin{aligned}
b_n
&=\frac1\pi\int_{-\pi}^{\pi}x\sin(nx)\,dx\\
&=\frac2\pi\int_0^\pi x\sin(nx)\,dx\\
&=\frac2\pi\left[
-\frac{x\cos(nx)}n+\frac{\sin(nx)}{n^2}
\right]_{0}^{\pi}\\
&=\frac{2(-1)^{n+1}}n.
\end{aligned}
$$
This gives the displayed sine series. It represents $x$ for
$-\pi<x<\pi$ and its periodic $L^2$ class globally.

:::

:::

::: {.pf-step #s1-5}

For part (c), let
$$
\omega_n=\sqrt{9n^2+2}.
$$
The nonconstant sine-mode amplitudes satisfy
$$
q_n''+\omega_n^2q_n=0.
$$


::: pf-proof

For $q_n(t)\sin(nx)$,
$$
9u_{xx}-2u
=-(9n^2+2)q_n(t)\sin(nx).
$$
The constant forcing $1$ has no sine component, so comparison of the
$n$th sine coefficients in
$u_{tt}=9u_{xx}-2u+1$ yields
$$
q_n''+(9n^2+2)q_n=0.
$$

:::

:::

::: {.pf-step #s1-6}

The component determined by the initial position
$7\sin(5x)$ is
$$
u_{\mathrm{pos}}(x,t)
=7\cos(\sqrt{227}\,t)\sin(5x).
$$


::: pf-proof

For $n=5$, step [](#s1-5){.pf-ref} gives
$$
\omega_5=\sqrt{9\cdot25+2}=\sqrt{227}.
$$
The amplitude with initial data $q_5(0)=7$ and $q_5'(0)=0$ is
$q_5(t)=7\cos(\sqrt{227}\,t)$.

:::

:::

::: {.pf-step #s1-7}

The component determined by the initial velocity $x$ is
$$
u_{\mathrm{vel}}(x,t)
=
\sum_{n=1}^\infty
\frac{2(-1)^{n+1}}{n\sqrt{9n^2+2}}
\sin\!\bigl(\sqrt{9n^2+2}\,t\bigr)\sin(nx).
$$


::: pf-proof

By step [](#s1-4){.pf-ref}, the initial velocity coefficient of $\sin(nx)$ is
$$
v_n=\frac{2(-1)^{n+1}}n.
$$
For the oscillator in step [](#s1-5){.pf-ref} with zero initial position and initial
velocity $v_n$, the amplitude is
$$
q_n(t)=\frac{v_n}{\omega_n}\sin(\omega_nt).
$$
Substituting $v_n$ and $\omega_n$ gives the displayed series.

:::

:::

::: {.pf-step #s1-8}

The spatially constant component forced by $1$ is
$$
u_{\mathrm{const}}(t)
=\frac{1-\cos(\sqrt2\,t)}2.
$$


::: pf-proof

For a spatially constant function $c(t)$, the PDE becomes
$$
c''=-2c+1,
\qquad\text{equivalently}\qquad
c''+2c=1.
$$
To preserve the given initial position and velocity, this component must
satisfy $c(0)=c'(0)=0$. The function
$$
c(t)=\frac{1-\cos(\sqrt2\,t)}2
$$
satisfies both initial conditions and
$c''+2c=1$.

:::

:::

::: {.pf-step #s1-9}

The solution of part (c) is
$$
\begin{aligned}
u(x,t)
={}&7\cos(\sqrt{227}\,t)\sin(5x)\\
&+\sum_{n=1}^\infty
\frac{2(-1)^{n+1}}{n\sqrt{9n^2+2}}
\sin\!\bigl(\sqrt{9n^2+2}\,t\bigr)\sin(nx)\\
&+\frac{1-\cos(\sqrt2\,t)}2.
\end{aligned}
$$


::: pf-proof

The operator
$$
L[u]=u_{tt}-9u_{xx}+2u
$$
is linear. Steps [](#s1-6){.pf-ref} and [](#s1-7){.pf-ref} give solutions of $L[u]=0$, while
step [](#s1-8){.pf-ref} gives a solution of $L[u]=1$. Their sum therefore solves the
inhomogeneous PDE. At $t=0$, the second and third components vanish and
the first is $7\sin(5x)$. Differentiating at $t=0$, the first and third
components have zero derivative, while step [](#s1-7){.pf-ref} yields the sine series
in step [](#s1-4){.pf-ref}, namely the prescribed initial velocity $x$ in the periodic
$L^2$ sense.

:::

:::

::: {.pf-step #s1-10}

Collecting the requested outputs,
$$
\boxed{
\begin{aligned}
\text{(a)}\quad&
u(x,t)=4e^{-9t}\sin x+5e^{-36t}\sin(2x),\\
\text{(b)}\quad&
\norm{u(x,1)}^2=16e^{-18}+25e^{-72},\\
\text{(c)}\quad&
u(x,t)=7\cos(\sqrt{227}\,t)\sin(5x)\\
&\quad+
\sum_{n=1}^\infty
\frac{2(-1)^{n+1}\sin(\sqrt{9n^2+2}\,t)}
{n\sqrt{9n^2+2}}\sin(nx)
+\frac{1-\cos(\sqrt2\,t)}2.
\end{aligned}}
$$


::: pf-proof

Parts (a), (b), and (c) are established by steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}, and
[](#s1-9){.pf-ref}, respectively.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} records all three requested answers.

:::

:::

:::
