---
schema: qual/card@1
id: P-TRIV-DE16
kind: problem
title: Oscillator $y''+16y=\theta(\pi-t)$ with Heaviside forcing
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 16, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve $y ^ { \prime \prime } + 1 6 y = \theta ( \pi - t )$ with $y ( 0 ) = y ^ { \prime } ( 0 ) = 0$ and where θ is the Heaviside function, $\theta ( x ) = 0 { \mathrm { ~ i f ~ } } x < 0$ and $\theta ( x ) = 1 { \mathrm { ~ i f ~ } } x > 0$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $t<\pi$, the initial-value problem reduces to
$$
y''+16y=1,\qquad y(0)=y'(0)=0.
$$


::: pf-proof

If $t<\pi$, then $\pi-t>0$, so $\theta(\pi-t)=1$ by the definition of the Heaviside function.

:::

:::

::: {.pf-step #s1-2}

On $t<\pi$, the solution is
$$
y(t)=\frac{1-\cos(4t)}{16}.
$$


::: pf-proof

A particular solution of the equation in step [](#s1-1){.pf-ref} is $1/16$, while the complementary solution is $A\cos(4t)+B\sin(4t)$. Hence
$$
y(t)=A\cos(4t)+B\sin(4t)+\frac1{16}.
$$
The condition $y(0)=0$ gives $A=-1/16$. Differentiating gives
$$
y'(t)=-4A\sin(4t)+4B\cos(4t),
$$
so $y'(0)=0$ gives $B=0$.

:::

:::

::: {.pf-step #s1-3}

At the switching time,
$$
y(\pi)=0,\qquad y'(\pi)=0.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
\lim_{t\to\pi^-}y(t)=\frac{1-\cos(4\pi)}{16}=0
$$
and
$$
\lim_{t\to\pi^-}y'(t)=\frac{\sin(4\pi)}4=0.
$$
The forcing has only a jump discontinuity at $t=\pi$ and contains no impulse, so a classical piecewise-$C^2$ solution has continuous $y$ and $y'$ there. Thus these left limits supply the initial data for the equation after the switch.

:::

:::

::: {.pf-step #s1-4}

For $t>\pi$, one has $y(t)=0$.


::: pf-proof

If $t>\pi$, then $\theta(\pi-t)=0$, so the equation is $y''+16y=0$. By step [](#s1-3){.pf-ref} its data at $t=\pi$ are $y(\pi)=y'(\pi)=0$. The general solution is $A\cos(4(t-\pi))+B\sin(4(t-\pi))$, and these two conditions give $A=B=0$.

:::

:::

::: {.pf-step #s1-5}

Therefore the solution is
$$
\boxed{
y(t)=
\begin{cases}
\dfrac{1-\cos(4t)}{16},&t<\pi,\\[4pt]
0,&t\geq\pi.
\end{cases}}
$$


::: pf-proof

Steps [](#s1-2){.pf-ref} and [](#s1-4){.pf-ref} give the two branches. Step [](#s1-3){.pf-ref} shows that they join with matching value and first derivative at $t=\pi$, so the displayed function satisfies the differential equation on each side of the forcing discontinuity and the prescribed initial conditions.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the requested solution.

:::

:::

:::
