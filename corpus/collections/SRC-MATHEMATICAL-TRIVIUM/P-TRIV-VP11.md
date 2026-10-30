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
Let $f \in C ^ { 2 } ( \bar { D } )$ be an extremum of the functional $S [ f ] = \int _ { { \cal D } } d x { \cal L } ( f , f ^ { \prime } )$ in a class of functions satisfying the boundary condition $f \restrict _ { \partial D } = f _ { 0 } \mathrm { ~ , ~ }$ What additional condition must be imposed on $f$ to make it an extremum of $S [ f ]$ in a class of $C ^ { 2 } ( \bar { D } )$ functions with all possible boundary conditions?
:::

::: {.solution}

Assume
$$
D=[a,b].
$$

::: pf

::: pf-step

For a variation
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


::: pf-proof

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

:::

::: {.pf-step #s1-2}

Integrating the second term by parts gives
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


::: pf-proof

Apply integration by parts to
$$
\int_a^b\mathcal L_{f'}\eta'\,dx.
$$

:::

:::

::: {.pf-step #s1-3}

Since $f$ is already an extremum for fixed boundary values, it satisfies
the Euler--Lagrange equation
$$
\mathcal L_f
-
\frac d{dx}\mathcal L_{f'}
=0
$$
in $(a,b)$.


::: pf-proof

For fixed endpoint values, admissible variations satisfy
$$
\eta(a)=\eta(b)=0,
$$
so the boundary term in step [](#s1-2){.pf-ref} vanishes. Stationarity for arbitrary
interior variations then gives the Euler--Lagrange equation.

:::

:::

::: {.pf-step #s1-4}

If the endpoint values are allowed to vary freely, then
$$
\eta(a)
$$
and
$$
\eta(b)
$$
are independent arbitrary numbers.


::: pf-proof

Without prescribed boundary values, the variation may be chosen with arbitrary
values at each endpoint independently.

:::

:::

::: {.pf-step #s1-5}

Under the Euler--Lagrange equation, the first variation reduces to
$$
\delta S
=
\mathcal L_{f'}(b)\eta(b)
-
\mathcal L_{f'}(a)\eta(a).
$$


::: pf-proof

Substitute step [](#s1-3){.pf-ref} into step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Therefore stationarity for all free-boundary variations requires
$$
\boxed{
\mathcal L_{f'}(a)=0,
\qquad
\mathcal L_{f'}(b)=0.
}
$$


::: pf-proof

By step [](#s1-4){.pf-ref}, the two endpoint values of $\eta$ are arbitrary and independent.
The linear expression in step [](#s1-5){.pf-ref} can vanish for all choices only if both
coefficients vanish.

:::

:::

::: {.pf-step #s1-7}

Equivalently, the additional natural boundary condition is
$$
\boxed{
\mathcal L_{f'}=0
\quad\text{on }\partial D.
}
$$


::: pf-proof

For the interval $D=[a,b]$, the boundary consists exactly of the two endpoints.
Step [](#s1-6){.pf-ref} gives the condition at both.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required additional condition.

:::

:::

:::
