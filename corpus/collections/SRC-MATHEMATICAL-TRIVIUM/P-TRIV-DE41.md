---
schema: qual/card@1
id: P-TRIV-DE41
kind: problem
title: First-order PDE $(\partial_x+\partial_y+\partial_z)f=x-y$ by characteristics
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 41, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find the most general solution of $\left( { \frac { \partial } { \partial x } } + { \frac { \partial } { \partial y } } + { \frac { \partial } { \partial z } } \right) f ( x , y , z ) = x - y$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The characteristic curves satisfy
$$
\frac{dx}{ds}=\frac{dy}{ds}=\frac{dz}{ds}=1.
$$
Consequently
$$
\eta=y-x,
\qquad
\zeta=z-x
$$
are constant along each characteristic.


::: pf-proof

The transport vector field is $\partial_x+\partial_y+\partial_z$. Along its integral curves, $x'=y'=z'=1$, so $(y-x)'=(z-x)'=0$.

:::

:::

::: {.pf-step #s1-2}

Along a characteristic with fixed $(\eta,\zeta)$, one has
$$
x-y=-\eta,
$$
and therefore
$$
\frac{df}{dx}=-\eta.
$$


::: pf-proof

Using $x$ itself as the characteristic parameter,
$$
\frac{df}{dx}=f_x+f_y+f_z.
$$
The PDE identifies this with $x-y$, while $y=x+\eta$ by step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

Integration along the characteristic gives
$$
f=-\eta x+C(\eta,\zeta),
$$
where $C$ is an arbitrary function of two variables.


::: pf-proof

Step [](#s1-2){.pf-ref} has constant right side along a fixed characteristic, so integration in $x$ gives the displayed formula. The integration constant may depend arbitrarily on the two independent characteristic invariants.

:::

:::

::: {.pf-step #s1-4}

Hence the most general solution is
$$
\boxed{
f(x,y,z)=x(x-y)+\Phi(y-x,z-x)},
$$
where $\Phi$ is arbitrary.


::: pf-proof

Substitute $\eta=y-x$ and $\zeta=z-x$ into step [](#s1-3){.pf-ref}. Conversely,
$$
(\partial_x+\partial_y+\partial_z)\Phi(y-x,z-x)=0
$$
because both arguments are characteristic invariants, while
$$
(\partial_x+\partial_y+\partial_z)\bigl(x(x-y)\bigr)=x-y.
$$
Thus every displayed function solves the PDE.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives and verifies the general characteristic solution.

:::

:::

:::
