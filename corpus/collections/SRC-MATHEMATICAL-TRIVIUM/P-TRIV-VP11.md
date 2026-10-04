---
schema: qual/card@1
id: P-TRIV-VP11
kind: problem
title: Natural boundary conditions for free-boundary extremals
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Variational Principle, Problem 11, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Let $f \in C ^ { 2 } ( \bar { D } )$ be an extremum of the functional $S [ f ] = \int _ { { \cal D } } d x { \cal L } ( f , f ^ { \prime } )$ in a class of functions satisfying the boundary condition $f | _ { \partial D } = f _ { 0 } \mathrm { ~ , ~ }$ What additional condition must be imposed on $f$ to make it an extremum of $S [ f ]$ in a class of $C ^ { 2 } ( \bar { D } )$ functions with all possible boundary conditions?
:::

::: {.solution}
Assume
$$
D=[a,b].
$$

<1>1. For a variation
$$
f_\varepsilon=f+\varepsilon\eta,
$$
the first variation is
$$
\delta S
=
\int_a^b
\left(
\mathcal L_f\eta
+
\mathcal L_{f'}\eta'
\right)dx.
$$

::: {.proof}
Differentiate
$$
S[f_\varepsilon]
=
\int_a^b
\mathcal L(f+\varepsilon\eta,f'+\varepsilon\eta')
\,dx
$$
with respect to $\varepsilon$ at $0$.
:::

<1>2. Integrating the second term by parts gives
$$
\delta S
=
\int_a^b
\left(
\mathcal L_f
-
\frac d{dx}\mathcal L_{f'}
\right)
\eta\,dx
+
\left[
\mathcal L_{f'}\eta
\right]_a^b.
$$

::: {.proof}
Apply integration by parts to
$$
\int_a^b\mathcal L_{f'}\eta'\,dx.
$$
:::

<1>3. Since $f$ is already an extremum for fixed boundary values, it satisfies
the Euler--Lagrange equation
$$
\mathcal L_f
-
\frac d{dx}\mathcal L_{f'}
=0
$$
in $(a,b)$.

::: {.proof}
For fixed endpoint values, admissible variations satisfy
$$
\eta(a)=\eta(b)=0,
$$
so the boundary term in step <1>2 vanishes. Stationarity for arbitrary
interior variations then gives the Euler--Lagrange equation.
:::

<1>4. If the endpoint values are allowed to vary freely, then
$$
\eta(a)
$$
and
$$
\eta(b)
$$
are independent arbitrary numbers.

::: {.proof}
Without prescribed boundary values, the variation may be chosen with arbitrary
values at each endpoint independently.
:::

<1>5. Under the Euler--Lagrange equation, the first variation reduces to
$$
\delta S
=
\mathcal L_{f'}(b)\eta(b)
-
\mathcal L_{f'}(a)\eta(a).
$$

::: {.proof}
Substitute step <1>3 into step <1>2.
:::

<1>6. Therefore stationarity for all free-boundary variations requires
$$
\boxed{
\mathcal L_{f'}(a)=0,
\qquad
\mathcal L_{f'}(b)=0.
}
$$

::: {.proof}
By step <1>4, the two endpoint values of $\eta$ are arbitrary and independent.
The linear expression in step <1>5 can vanish for all choices only if both
coefficients vanish.
:::

<1>7. Equivalently, the additional natural boundary condition is
$$
\boxed{
\mathcal L_{f'}=0
\quad\text{on }\partial D.
}
$$

::: {.proof}
For the interval $D=[a,b]$, the boundary consists exactly of the two endpoints.
Step <1>6 gives the condition at both.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required additional condition.
:::
:::
