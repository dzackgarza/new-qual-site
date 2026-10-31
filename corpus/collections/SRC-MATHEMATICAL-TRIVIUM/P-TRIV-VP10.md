---
schema: qual/card@1
id: P-TRIV-VP10
kind: problem
title: Natural boundary conditions from a boundary term in the functional
classification:
  areas: [prelim]
  topics:
  - Calculus of Variations
  - Natural Boundary Conditions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Variational Principle, Problem 10, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Cleaned Variational Principle Problem 10 against page 20 of the source PDF and added a remark on the stray plus sign printed in its boundary condition.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source prints the boundary condition in (16) as F_{f_x} n_x + F_{f_y} n_y + = g(s) with a dangling plus sign; the statement now reads F_{f_x} n_x + F_{f_y} n_y = g(s).
---

::: {.problem}
Consider the following problem
$$
\begin{cases}
F_f - \dfrac{\partial}{\partial x} F_{f_x} - \dfrac{\partial}{\partial y} F_{f_y} = 0, & (x, y) \in D \\
F_{f_x} n_x + F_{f_y} n_y = g(s), & x \in \partial D,
\end{cases}
\tag{16}
$$
where $f = f(x, y) \in C^2(\bar{D})$, $F = F[f, f_x, f_y](x, y) \in C^2(\RR^3 \times \bar{D})$, $g \in C^1(\partial D)$, $\partial/\partial n$ denotes a normal derivative on $\partial D$, $f_x \equiv \frac{\partial f}{\partial x}$ and $F_f \equiv \frac{\partial F}{\partial f}$.

(a) Show that the solutions to this equation are given by extrema of the functional
$$
J[f] = \iint_D dx\,dy\,F - \int_{\partial D} ds\,f g.
\tag{17}
$$

(b) How must the functional above be modified to give the mixed boundary conditions on the function $f$:
$$
F_{f_x} n_x + F_{f_y} n_y + h(s) f = g(s), \quad h \in C^1(\partial D)
\tag{18}
$$
:::

::: {.solution}

::: pf

::: pf-step

Let
$$
f_\varepsilon=f+\varepsilon\eta,
$$
where $\eta$ is an arbitrary $C^1$ variation on $\bar D$.


::: pf-proof

No boundary value of $f$ is prescribed in this problem, so the variation need
not vanish on $\partial D$.

:::

:::

::: {.pf-step #s1-2}

The first variation of
$$
J[f]
=
\iint_D F(f,f_x,f_y;x,y)
\,dx\,dy
-
\int_{\partial D}fg
\,ds
$$
is
$$
\delta J
=
\iint_D
\left(
F_f\eta
+
F_{f_x}\eta_x
+
F_{f_y}\eta_y
\right)dA
-
\int_{\partial D}g\eta\,ds.
$$


::: pf-proof

Differentiate $J[f_\varepsilon]$ with respect to $\varepsilon$ at
$\varepsilon=0$ and apply the chain rule to the interior integrand.

:::

:::

::: {.pf-step #s1-3}

Green's formula gives
$$
\iint_D
\left(
F_{f_x}\eta_x
+
F_{f_y}\eta_y
\right)dA
=
-
\iint_D
\left(
\partial_xF_{f_x}
+
\partial_yF_{f_y}
\right)
\eta\,dA
+
\int_{\partial D}
\left(
F_{f_x}n_x
+
F_{f_y}n_y
\right)
\eta\,ds.
$$


::: pf-proof

Apply the divergence theorem to the vector field
$$
\eta(F_{f_x},F_{f_y}).
$$
Its divergence is
$$
F_{f_x}\eta_x
+
F_{f_y}\eta_y
+
\eta
\left(
\partial_xF_{f_x}
+
\partial_yF_{f_y}
\right).
$$
Rearrange.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\begin{aligned}
\delta J
&=
\iint_D
\left[
F_f
-
\partial_xF_{f_x}
-
\partial_yF_{f_y}
\right]
\eta\,dA\\
&\quad
+
\int_{\partial D}
\left[
F_{f_x}n_x
+
F_{f_y}n_y
-
g
\right]
\eta\,ds.
\end{aligned}
$$


::: pf-proof

Substitute step [](#s1-3){.pf-ref} into step [](#s1-2){.pf-ref} and collect the interior and boundary
terms.

:::

:::

::: {.pf-step #s1-5}

At an extremum, the interior Euler--Lagrange equation is
$$
\boxed{
F_f
-
\partial_xF_{f_x}
-
\partial_yF_{f_y}
=0
}
$$
in $D$.


::: pf-proof

Choose variations supported compactly inside $D$. Then the boundary term in
step [](#s1-4){.pf-ref} vanishes, and the fundamental lemma of the calculus of variations
forces the interior coefficient of $\eta$ to vanish.

:::

:::

::: {.pf-step #s1-6}

Once step [](#s1-5){.pf-ref} holds, stationarity for arbitrary boundary values of
$\eta$ gives the natural boundary condition
$$
\boxed{
F_{f_x}n_x
+
F_{f_y}n_y
=
g(s)
}
$$
on $\partial D$.


::: pf-proof

With the interior term zero, step [](#s1-4){.pf-ref} reduces to the boundary integral. Since
$\eta\restrict_{\partial D}$ is arbitrary, the boundary coefficient must vanish.

:::

:::

::: {.pf-step #s1-7}

Thus the extrema of $J$ satisfy precisely the system in
part (a).


::: pf-proof

Combine steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

For part (b), define
$$
\boxed{
J_h[f]
=
\iint_D F\,dA
+
\int_{\partial D}
\left(
\frac12h(s)f^2
-
f g(s)
\right)ds.
}
$$


::: pf-proof

The added boundary term $\frac12hf^2$ is chosen because its first variation
is $hf\eta$.

:::

:::

::: {.pf-step #s1-9}

The first variation of the new boundary contribution is
$$
\int_{\partial D}
\left(
h f-g
\right)
\eta\,ds.
$$


::: pf-proof

Differentiate
$$
\frac12h(f+\varepsilon\eta)^2
-
(f+\varepsilon\eta)g
$$
with respect to $\varepsilon$ at $0$.

:::

:::

::: {.pf-step #s1-10}

Therefore $J_h$ has the same interior Euler--Lagrange equation as in
step [](#s1-5){.pf-ref} and the boundary condition
$$
\boxed{
F_{f_x}n_x
+
F_{f_y}n_y
+
h(s)f
=
g(s).
}
$$


::: pf-proof

The integration-by-parts boundary contribution from the interior functional
is still
$$
(F_{f_x}n_x+F_{f_y}n_y)\eta.
$$
Adding step [](#s1-9){.pf-ref} gives the total boundary coefficient
$$
F_{f_x}n_x
+
F_{f_y}n_y
+
hf
-
g.
$$
Stationarity for arbitrary boundary variations forces it to vanish.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} proves part (a), and steps [](#s1-8){.pf-ref} through [](#s1-10){.pf-ref} give the required modified
functional for part (b).

:::

:::

:::
