---
schema: qual/card@1
id: P-TRIV-VP10
kind: problem
title: Natural boundary conditions from a boundary term in the functional
classification:
  areas: [prelim]
  topics: []
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
---

::: {.problem}
Consider the following problem
$$
\begin{cases}
F_f - \dfrac{\partial}{\partial x} F_{f_x} - \dfrac{\partial}{\partial y} F_{f_y} = 0, & (x, y) \in D \\
F_{f_x} n_x + F_{f_y} n_y + = g(s), & x \in \partial D,
\end{cases}
\tag{16}
$$
where $f = f(x, y) \in C^2(\bar{D})$, $F = F[f, f_x, f_y](x, y) \in C^2(\mathbb{R}^3 \times \bar{D})$, $g \in C^1(\partial D)$, $\partial/\partial n$ denotes a normal derivative on $\partial D$, $f_x \equiv \frac{\partial f}{\partial x}$ and $F_f \equiv \frac{\partial F}{\partial f}$.

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

::: {.remark}
Erratum: the boundary condition in (16) is printed in the source as "$F_{f_x} n_x + F_{f_y} n_y + = g(s)$, $x \in \partial D$", with a dangling plus sign.
The condition that makes part (a) true, and that (18) reduces to for $h = 0$, is $F_{f_x} n_x + F_{f_y} n_y = g(s)$ on $\partial D$, where $(n_x, n_y)$ is the outward unit normal and $s$ is arc length along $\partial D$.
:::

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

::: pf-step

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

::: pf-step

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

::: pf-step

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

Substitute step <1>3 into step <1>2 and collect the interior and boundary
terms.

:::

:::

::: pf-step

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
step <1>4 vanishes, and the fundamental lemma of the calculus of variations
forces the interior coefficient of $\eta$ to vanish.

:::

:::

::: pf-step

Once step <1>5 holds, stationarity for arbitrary boundary values of
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

With the interior term zero, step <1>4 reduces to the boundary integral. Since
$\eta|_{\partial D}$ is arbitrary, the boundary coefficient must vanish.

:::

:::

::: pf-step

Thus the extrema of $J$ satisfy precisely the corrected system in
part (a).


::: pf-proof

Combine steps <1>5--<1>6.

:::

:::

::: pf-step

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

::: pf-step

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

::: pf-step

Therefore $J_h$ has the same interior Euler--Lagrange equation as in
step <1>5 and the boundary condition
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
Adding step <1>9 gives the total boundary coefficient
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

Step <1>7 proves part (a), and steps <1>8--<1>10 give the required modified
functional for part (b).

:::

:::
