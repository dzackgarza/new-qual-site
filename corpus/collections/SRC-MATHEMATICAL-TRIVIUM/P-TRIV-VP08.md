---
schema: qual/card@1
id: P-TRIV-VP08
kind: problem
title: Variational principle for Poisson's equation
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Variational Principle, Problem 8, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the functional $J [ f ] = \iint d x d y \left[ \left( { \frac { \partial f } { \partial x } } \right) ^ { 2 } + \left( { \frac { \partial f } { \partial y } } \right) ^ { 2 } + 2 f g \right]$ , where D is a domain in (xy)-plane with the boundary $\partial D$, and $g = g ( x , y )$ is a continuous function in $\bar { D }$ Write the equation on $f ,$ whose solution In a class of functions $f \in$ $C ^ { 2 } ( \bar { D } )$ , satisfying the boundary condition $f ( x , y ) | _ { \partial D } = f _ { 0 } ( x , y )$ , is an extremum of $J [ f ]$
:::

::: pf

::: pf-step

Let
$$
f_\varepsilon=f+\varepsilon\eta,
$$
where
$$
\eta|_{\partial D}=0.
$$


::: pf-proof

The boundary values of $f$ are fixed, so every admissible first-order
variation must vanish on $\partial D$.

:::

:::

::: pf-step

The first variation is
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
+
g\eta
\right)
\,dx\,dy.
$$


::: pf-proof

Differentiate
$$
(f_x+\varepsilon\eta_x)^2
+
(f_y+\varepsilon\eta_y)^2
+
2(f+\varepsilon\eta)g
$$
with respect to $\varepsilon$ at $0$.

:::

:::

::: pf-step

Green's identity gives
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

Use
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

::: pf-step

Hence the first variation becomes
$$
2
\iint_D
\left(
-\Delta f
+
g
\right)
\eta
\,dA.
$$


::: pf-proof

Substitute step <1>3 into step <1>2.

:::

:::

::: pf-step

Therefore every extremal satisfies
$$
\boxed{
\Delta f=g
}
$$
in $D$.


::: pf-proof

At an extremum, the expression in step <1>4 vanishes for every smooth
variation $\eta$ with zero boundary values. The fundamental lemma of the
calculus of variations gives
$$
-\Delta f+g=0.
$$

:::

:::

::: pf-step

Thus the boundary-value problem is
$$
\boxed{
\Delta f=g
\quad\text{in }D,
\qquad
f|_{\partial D}=f_0.
}
$$


::: pf-proof

Combine the interior Euler--Lagrange equation from step <1>5 with the fixed
boundary data from the problem.

:::

:::

::: pf-step

Let $f_*$ solve step <1>6, and let
$$
f=f_*+\eta,
$$
with
$$
\eta|_{\partial D}=0.
$$
Then
$$
J[f]-J[f_*]
=
\iint_D
|\nabla\eta|^2
\,dA.
$$


::: pf-proof

Expand
$$
|\nabla(f_*+\eta)|^2
+
2(f_*+\eta)g.
$$
The linear cross term is
$$
2
\iint_D
\left(
\nabla f_*\cdot\nabla\eta
+
g\eta
\right)dA.
$$
By step <1>3, this equals
$$
2
\iint_D
(-\Delta f_*+g)\eta
\,dA
=0
$$
because $\Delta f_*=g$. The remaining quadratic term is
$\iint_D|\nabla\eta|^2dA$.

:::

:::

::: pf-step

Therefore every solution of step <1>6 is a minimizer of $J$.


::: pf-proof

Step <1>7 gives
$$
J[f]-J[f_*]
=
\iint_D|\nabla\eta|^2,dA
\geq0.
$$

:::

:::

::: pf-step

If $D$ is connected, the minimizer is unique.


::: pf-proof

Equality in step <1>8 implies $\nabla\eta=0$, so $\eta$ is constant on $D$.
The boundary condition $\eta=0$ forces that constant to be zero.

:::

:::

::: pf-qed

Steps <1>5--<1>6 give the required equation, and steps <1>7--<1>9 identify
the extremum as the Dirichlet minimizer.

:::

:::
