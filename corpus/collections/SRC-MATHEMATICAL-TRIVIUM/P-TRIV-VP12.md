---
schema: qual/card@1
id: P-TRIV-VP12
kind: problem
title: Action functionals for the time-dependent and stationary Schrödinger equations
classification:
  areas: [prelim]
  topics:
  - Calculus of Variations
  - Schrodinger Equation
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Variational Principle, Problem 12, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Construct the functional $S[\psi, \psi^\dagger]$ whose variation with respect to $\psi = \psi(\vec{r}, t)$ and $\psi^\dagger = \psi^\dagger(\vec{r}, t)$ gives

(a) the Schrodinger equation $i\hbar\frac{\partial\psi}{\partial t} = \hat{H}\psi$ and its conjugated,

(b) the stationary Schrodinger equation $\hat{H}\psi = E\psi$ and its conjugated.

Here $\hat{H}$ is some hermitian operator.
:::

::: {.solution}

Treat $\psi$ and $\psi^\dagger$ as independent variables in the variational
calculation. Assume variations vanish at the temporal endpoints and satisfy
spatial boundary conditions for which $\hat H$ is Hermitian.

::: pf

::: {.pf-step #s1-1}

Define the time-dependent action
$$
\boxed{
S[\psi,\psi^\dagger]
=
\int_{t_1}^{t_2}dt
\int d^3r
\left[
\frac{i\hbar}{2}
\left(
\psi^\dagger\dot\psi
-
\dot\psi^\dagger\psi
\right)
-
\psi^\dagger\hat H\psi
\right].
}
$$


::: pf-proof

The first term is the standard real first-order kinetic term for a complex
field, and the second is the expectation-density associated with the
Hamiltonian.

:::

:::

::: {.pf-step #s1-2}

Varying $S$ with respect to $\psi^\dagger$ gives
$$
\delta_{\psi^\dagger}S
=
\int dt,d^3r
\left[
\frac{i\hbar}{2}
\delta\psi^\dagger\dot\psi
-
\frac{i\hbar}{2}
\delta\dot\psi^\dagger\psi
-
\delta\psi^\dagger\hat H\psi
\right].
$$


::: pf-proof

Differentiate the integrand from step [](#s1-1){.pf-ref} with respect to
$\psi^\dagger$ and $\dot\psi^\dagger$, keeping $\psi$ fixed.

:::

:::

::: {.pf-step #s1-3}

Integrating the middle term in step [](#s1-2){.pf-ref} by parts in time gives
$$
\delta_{\psi^\dagger}S
=
\int dt,d^3r
\delta\psi^\dagger
\left(
i\hbar\dot\psi
-
\hat H\psi
\right).
$$


::: pf-proof

Since the variation vanishes at $t_1,t_2$,
$$
-
\frac{i\hbar}{2}
\int
\delta\dot\psi^\dagger\psi,dt
=
\frac{i\hbar}{2}
\int
\delta\psi^\dagger\dot\psi,dt.
$$
This combines with the first term in step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Therefore stationarity with respect to $\psi^\dagger$ gives
$$
\boxed{
i\hbar\frac{\partial\psi}{\partial t}
=
\hat H\psi.
}
$$


::: pf-proof

The variation $\delta\psi^\dagger$ is arbitrary, so the coefficient in
step [](#s1-3){.pf-ref} must vanish.

:::

:::

::: {.pf-step #s1-5}

Varying $S$ with respect to $\psi$ gives
$$
\delta_\psi S
=
\int dt,d^3r
\delta\psi
\left(
-i\hbar\dot\psi^\dagger
-
(\hat H\psi)^\dagger
\right).
$$


::: pf-proof

The time-derivative terms are treated exactly as in steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}, with
$\psi$ and $\psi^\dagger$ interchanged. For the Hamiltonian term, hermiticity
of $\hat H$ and the assumed spatial boundary conditions move all derivatives
off $\delta\psi$ and onto $\psi^\dagger$.

:::

:::

::: {.pf-step #s1-6}

Hence stationarity with respect to $\psi$ gives the conjugate
Schrödinger equation
$$
\boxed{
-i\hbar\frac{\partial\psi^\dagger}{\partial t}
=
(\hat H\psi)^\dagger.
}
$$


::: pf-proof

The variation $\delta\psi$ is arbitrary in step [](#s1-5){.pf-ref}, so its coefficient must
vanish.

:::

:::

::: {.pf-step #s1-7}

Part (a) follows.


::: pf-proof

Steps [](#s1-4){.pf-ref} and [](#s1-6){.pf-ref} give the Schrödinger equation and its Hermitian conjugate.

:::

:::

::: {.pf-step #s1-8}

For the stationary problem, define
$$
\boxed{
S_E[\psi,\psi^\dagger]
=
\int d^3r
\psi^\dagger
(\hat H-E)
\psi.
}
$$


::: pf-proof

This functional is quadratic and vanishes on an eigenstate of energy $E$.

:::

:::

::: {.pf-step #s1-9}

Variation with respect to $\psi^\dagger$ gives
$$
\delta_{\psi^\dagger}S_E
=
\int d^3r
\delta\psi^\dagger
(\hat H-E)
\psi.
$$


::: pf-proof

The functional in step [](#s1-8){.pf-ref} is linear in $\psi^\dagger$.

:::

:::

::: {.pf-step #s1-10}

Therefore stationarity with respect to $\psi^\dagger$ gives
$$
\boxed{
\hat H\psi=E\psi.
}
$$


::: pf-proof

The variation $\delta\psi^\dagger$ is arbitrary in step [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

Variation with respect to $\psi$ gives
$$
\boxed{
(\hat H\psi)^\dagger
=
E\psi^\dagger.
}
$$


::: pf-proof

Hermiticity of $\hat H$ allows the variation to be transferred from
$\hat H\delta\psi$ onto the conjugate field, exactly as in step [](#s1-5){.pf-ref}. Since
$E$ is real for a Hermitian Hamiltonian, the result is the Hermitian conjugate
of step [](#s1-10){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

Part (b) follows.


::: pf-proof

Steps [](#s1-10){.pf-ref} through [](#s1-11){.pf-ref} give the stationary Schrödinger equation and its conjugate.

:::

:::

::: pf-qed

Steps [](#s1-7){.pf-ref} and [](#s1-12){.pf-ref} establish parts (a) and (b), respectively.

:::

:::

:::
