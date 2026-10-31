---
schema: qual/card@1
id: P-TRIV-DE46
kind: problem
title: Heat equation on a half-line with delta initial data
classification:
  areas: [prelim]
  topics:
  - Heat Equation
  - Method of Images
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 46, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider an semi-infinite ($x \geq 0$) metal rod with conductivity $\kappa$. Find the heat distribution $u(x, t)$ if $u(x, 0) = u_0\delta(x)$.
:::

::: {.solution}

Take the heat equation to be
$$
u_t=\kappa u_{xx},\qquad x>0, t>0.
$$
The source does not state a boundary condition at $x=0$, so the half-line problem is not uniquely determined. For an insulated endpoint, $u_x(0,t)=0$, the solution is as follows.

::: pf

::: pf-step

The whole-line heat kernel is
$$
K(x,t)=\frac1{\sqrt{4\pi\kappa t}}
\exp\left(-\frac{x^2}{4\kappa t}\right).
$$


::: pf-proof

Direct differentiation verifies $K_t=\kappa K_{xx}$. Also $\int_{\RR}K(x,t)\,dx=1$, and $K(\cdot,t)$ converges to $\delta_0$ distributionally as $t\to0^+$.

:::

:::

::: {.pf-step #s1-2}

The Neumann heat kernel on the half-line for a source at $\xi\geq0$ is
$$
K_N(x,\xi,t)=K(x-\xi,t)+K(x+\xi,t).
$$


::: pf-proof

This is the even-image construction. Each summand solves the heat equation for $x>0$, and differentiating in $x$ gives cancellation at $x=0$, so $\partial_xK_N(0,\xi,t)=0$.

:::

:::

::: {.pf-step #s1-3}

For a source at the endpoint $\xi=0$,
$$
K_N(x,0,t)=2K(x,t).
$$


::: pf-proof

Set $\xi=0$ in step [](#s1-2){.pf-ref}. The factor $2$ is also required by mass normalization on the half-line, since $\int_0^\infty K(x,t)\,dx=1/2$.

:::

:::

::: {.pf-step #s1-4}

Thus for the insulated half-line,
$$
\boxed{
u(x,t)=\frac{u_0}{\sqrt{\pi\kappa t}}
\exp\left(-\frac{x^2}{4\kappa t}\right),
\qquad x\geq0, t>0.}
$$


::: pf-proof

Multiply step [](#s1-3){.pf-ref} by the source strength $u_0$. The resulting function satisfies $u_t=\kappa u_{xx}$, has $u_x(0,t)=0$, and has total heat
$$
\int_0^\infty u(x,t)\,dx=u_0.
$$
For every smooth compactly supported test function on $[0,\infty)$, the same change of variables as for the heat-kernel approximate identity gives convergence to $u_0\phi(0)$ as $t\to0^+$, i.e. to $u_0\delta_0$.

:::

:::

::: {.pf-step #s1-5}

Without a boundary condition at $x=0$, the source statement does not specify a unique heat distribution.


::: pf-proof

For example, the Neumann image kernel in step [](#s1-2){.pf-ref} and the Dirichlet image kernel $K(x-\xi,t)-K(x+\xi,t)$ impose different endpoint conditions and hence define different half-line evolutions for general initial data. A boundary condition is therefore part of the well-posed half-line heat problem.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the standard insulated-end solution, while step [](#s1-5){.pf-ref} records the missing boundary datum in the source.

:::

:::

:::
