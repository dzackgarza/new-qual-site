---
schema: qual/card@1
id: P-TRIV-DE17
kind: problem
title: Green function of the damped harmonic oscillator
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 17, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider a forced damped harmonic oscillator:
$$
\ddot{y}(t) + 2k\dot{y}(t) + \Omega^2 y(t) = f(t) \tag{25}
$$
the Green function $G(t)$ is defined such that
$$
y(t) = \int dt'\, G(t - t') f(t'). \tag{26}
$$
Find $G(t)$ when

(a) $\Omega > k > 0$ (oscillating system)

(b) $\Omega = k$ (critical damping)

(c) $k > \Omega > 0$ (overdamped system)
:::

::: {.solution}

Take $G$ to be the retarded Green function, so $G(t)=0$ for $t<0$. Write
$$
L=\frac{d^2}{dt^2}+2k\frac d{dt}+\Omega^2.
$$

::: pf

::: {.pf-step #s1-1}

The retarded Green function is characterized by
$$
LG=\delta_0,\qquad G(0^+)=0,\qquad G'(0^+)=1.
$$


::: pf-proof

Applying $L$ to the convolution in the problem gives $Ly=(LG)*f$, so $LG=\delta_0$ is sufficient to obtain $Ly=f$. Away from $t=0$ this requires $LG=0$. Integrating $LG=\delta_0$ across $0$ gives
$$
G'(0^+)-G'(0^-)+2k\bigl(G(0^+)-G(0^-)\bigr)=1.
$$
The absence of a $\delta_0'$ term forces $G$ to be continuous at $0$. Retardedness gives $G(0^-)=G'(0^-)=0$, hence $G(0^+)=0$ and $G'(0^+)=1$.

:::

:::

::: {.pf-step #s1-2}

If $\Omega>k>0$ and $\omega=\sqrt{\Omega^2-k^2}$, then
$$
\boxed{G(t)=\theta(t)e^{-kt}\frac{\sin(\omega t)}{\omega}}.
$$


::: pf-proof

For $t>0$, the characteristic roots of $LG=0$ are $-k\pm i\omega$. Thus
$$
G(t)=e^{-kt}\bigl(A\cos(\omega t)+B\sin(\omega t)\bigr).
$$
The conditions in step [](#s1-1){.pf-ref} give $A=0$ and $B\omega=1$, so $B=1/\omega$. Multiplication by $\theta(t)$ imposes retardedness.

:::

:::

::: {.pf-step #s1-3}

If $\Omega=k$, then
$$
\boxed{G(t)=\theta(t)\,t e^{-kt}}.
$$


::: pf-proof

The characteristic polynomial has the repeated root $-k$, so for $t>0$,
$$
G(t)=(A+Bt)e^{-kt}.
$$
Step [](#s1-1){.pf-ref} gives $A=0$ and $B=1$.

:::

:::

::: {.pf-step #s1-4}

If $k>\Omega>0$ and $\lambda=\sqrt{k^2-\Omega^2}$, then
$$
\boxed{G(t)=\theta(t)e^{-kt}\frac{\sinh(\lambda t)}{\lambda}}.
$$


::: pf-proof

The characteristic roots are $-k\pm\lambda$. Hence for $t>0$ one may write
$$
G(t)=e^{-kt}\bigl(A\cosh(\lambda t)+B\sinh(\lambda t)\bigr).
$$
Step [](#s1-1){.pf-ref} gives $A=0$ and $B\lambda=1$, so $B=1/\lambda$.

:::

:::

::: {.pf-step #s1-5}

These formulas give the Green function in all three damping regimes, subject to the retarded condition.


::: pf-proof

Steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref} solve $LG=0$ for $t\ne0$ and satisfy the jump conditions in step [](#s1-1){.pf-ref}, hence each satisfies $LG=\delta_0$. Without a boundary condition such as retardedness, the differential equation alone does not select a unique Green function, since a homogeneous solution may be added to any particular Green function.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} establishes the three requested formulas and states the boundary condition under which they are uniquely determined.

:::

:::

:::
