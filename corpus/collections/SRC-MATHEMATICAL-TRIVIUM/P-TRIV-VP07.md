---
schema: qual/card@1
id: P-TRIV-VP07
kind: problem
title: Dirichlet energy and Laplace's equation
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Variational Principle, Problem 7, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the functional $J [ f ] = \iint d x d y \left[ \left( { \frac { \partial f } { \partial x } } \right) ^ { 2 } + \left( { \frac { \partial f } { \partial y } } \right) ^ { 2 } \right]$ , where D is a domain in (xy)-plane with the boundary $\partial D$.
Write the equation for f, whose solution in a class of functions $f \in C ^ { 2 } ( \bar { D } )$ , satisfying the boundary condition $f ( x , y ) \restrict _ { \partial D } = f _ { 0 } ( x , y )$ , is an extremum of $J [ f ]$
:::

::: {.solution}

::: pf

::: pf-step

Let
$$
f_\varepsilon=f+\varepsilon\eta,
$$
where
$$
\eta\restrict_{\partial D}=0.
$$


::: pf-proof

The boundary values of $f$ are fixed, so every admissible first-order
variation must vanish on $\partial D$.

:::

:::

::: {.pf-step #s1-2}

The first variation is
$$
\evaluated{
\frac d{d\varepsilon}
J[f_\varepsilon]
}_{\varepsilon=0}
=
2
\iint_D
\left(
f_x\eta_x
+
f_y\eta_y
\right)
\,dx\,dy.
$$


::: pf-proof

Expand
$$
(f_x+\varepsilon\eta_x)^2
+
(f_y+\varepsilon\eta_y)^2
$$
and differentiate at $\varepsilon=0$.

:::

:::

::: {.pf-step #s1-3}

Integration by parts gives
$$
\iint_D
\left(
f_x\eta_x
+
f_y\eta_y
\right)
\,dx\,dy
=
-
\iint_D
(f_{xx}+f_{yy})\eta
\,dx\,dy.
$$


::: pf-proof

Apply Green's identity:
$$
\iint_D
\nabla f\cdot\nabla\eta
\,dA
=
\int_{\partial D}
\eta\frac{\partial f}{\partial n}
\,ds
-
\iint_D
\eta\Delta f
\,dA.
$$
The boundary term vanishes because $\eta=0$ on $\partial D$.

:::

:::

::: {.pf-step #s1-4}

Hence every extremal satisfies
$$
\boxed{
f_{xx}+f_{yy}=0
}
$$
in $D$.


::: pf-proof

At an extremum, the first variation in step [](#s1-2){.pf-ref} must vanish for every smooth
variation $\eta$ with zero boundary values. By step [](#s1-3){.pf-ref},
$$
\iint_D
(f_{xx}+f_{yy})\eta
\,dx\,dy
=0
$$
for every such $\eta$. The fundamental lemma of the calculus of variations
therefore gives
$$
f_{xx}+f_{yy}=0.
$$

:::

:::

::: {.pf-step #s1-5}

Thus the extremal is a harmonic function satisfying
$$
\boxed{
\Delta f=0
\quad\text{in }D,
\qquad
f\restrict_{\partial D}=f_0.
}
$$


::: pf-proof

Step [](#s1-4){.pf-ref} gives the interior equation, and the boundary condition is the one
prescribed in the problem.

:::

:::

::: {.pf-step #s1-6}

Let $f_*$ be such a harmonic solution, and let
$$
f=f_*+\eta
$$
with $\eta\restrict_{\partial D}=0$. Then
$$
J[f]
=
J[f_*]
+
\iint_D
\norm{\nabla\eta}^2
\,dA.
$$


::: pf-proof

Expand
$$
\norm{\nabla(f_*+\eta)}^2
=
\norm{\nabla f_*}^2
+
2\nabla f_*\cdot\nabla\eta
+
\norm{\nabla\eta}^2.
$$
The cross term integrates to zero by step [](#s1-3){.pf-ref} because
$$
\Delta f_*=0
$$
and $\eta$ vanishes on the boundary.

:::

:::

::: {.pf-step #s1-7}

Therefore every harmonic solution of the Dirichlet problem is a
minimizer of $J$.


::: pf-proof

Step [](#s1-6){.pf-ref} gives
$$
J[f]-J[f_*]
=
\iint_D\norm{\nabla\eta}^2\,dA
\geq0.
$$
Thus no admissible perturbation decreases the energy.

:::

:::

::: {.pf-step #s1-8}

If $D$ is connected, the minimizer is unique.


::: pf-proof

Equality in step [](#s1-7){.pf-ref} forces
$$
\nabla\eta=0
$$
throughout $D$, so $\eta$ is constant on each connected component. Since
$\eta=0$ on the boundary and $D$ is connected, the constant is zero.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} give the required Euler--Lagrange equation, and steps
[](#s1-6){.pf-ref} through [](#s1-8){.pf-ref} identify its solution as the Dirichlet-energy minimizer.

:::

:::

:::
