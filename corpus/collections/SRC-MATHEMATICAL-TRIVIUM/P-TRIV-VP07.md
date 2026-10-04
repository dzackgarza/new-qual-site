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
Write the equation for f, whose solution in a class of functions $f \in C ^ { 2 } ( \bar { D } )$ , satisfying the boundary condition $f ( x , y ) | _ { \partial D } = f _ { 0 } ( x , y )$ , is an extremum of $J [ f ]$
:::

::: {.solution}
<1>1. Let
$$
f_\varepsilon=f+\varepsilon\eta,
$$
where
$$
\eta|_{\partial D}=0.
$$

::: {.proof}
The boundary values of $f$ are fixed, so every admissible first-order
variation must vanish on $\partial D$.
:::

<1>2. The first variation is
$$
\left.
\frac d{d\varepsilon}
J[f_\varepsilon]
\right|_{\varepsilon=0}
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

::: {.proof}
Expand
$$
(f_x+\varepsilon\eta_x)^2
+
(f_y+\varepsilon\eta_y)^2
$$
and differentiate at $\varepsilon=0$.
:::

<1>3. Integration by parts gives
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

::: {.proof}
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

<1>4. Hence every extremal satisfies
$$
\boxed{
f_{xx}+f_{yy}=0
}
$$
in $D$.

::: {.proof}
At an extremum, the first variation in step <1>2 must vanish for every smooth
variation $\eta$ with zero boundary values. By step <1>3,
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

<1>5. Thus the extremal is a harmonic function satisfying
$$
\boxed{
\Delta f=0
\quad\text{in }D,
\qquad
f|_{\partial D}=f_0.
}
$$

::: {.proof}
Step <1>4 gives the interior equation, and the boundary condition is the one
prescribed in the problem.
:::

<1>6. Let $f_*$ be such a harmonic solution, and let
$$
f=f_*+\eta
$$
with $\eta|_{\partial D}=0$. Then
$$
J[f]
=
J[f_*]
+
\iint_D
|\nabla\eta|^2
\,dA.
$$

::: {.proof}
Expand
$$
|\nabla(f_*+\eta)|^2
=
|\nabla f_*|^2
+
2\nabla f_*\cdot\nabla\eta
+
|\nabla\eta|^2.
$$
The cross term integrates to zero by step <1>3 because
$$
\Delta f_*=0
$$
and $\eta$ vanishes on the boundary.
:::

<1>7. Therefore every harmonic solution of the Dirichlet problem is a
minimizer of $J$.

::: {.proof}
Step <1>6 gives
$$
J[f]-J[f_*]
=
\iint_D|\nabla\eta|^2\,dA
\geq0.
$$
Thus no admissible perturbation decreases the energy.
:::

<1>8. If $D$ is connected, the minimizer is unique.

::: {.proof}
Equality in step <1>7 forces
$$
\nabla\eta=0
$$
throughout $D$, so $\eta$ is constant on each connected component. Since
$\eta=0$ on the boundary and $D$ is connected, the constant is zero.
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>4--<1>5 give the required Euler--Lagrange equation, and steps
<1>6--<1>8 identify its solution as the Dirichlet-energy minimizer.
:::
:::
