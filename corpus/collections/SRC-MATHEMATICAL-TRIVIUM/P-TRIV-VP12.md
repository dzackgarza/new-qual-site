---
schema: qual/card@1
id: P-TRIV-VP12
kind: problem
title: Action functionals for the time-dependent and stationary Schrödinger equations
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Variational Principle, Problem 12, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Construct the functional $S [ \psi , \psi ^ { \dagger } ]$ whose variation with respect to $\psi = \psi ( \vec { r } , t )$ and $\psi ^ { \dagger } = \psi ^ { \dagger } ( \vec { r } , t )$ gives

(a) the Schrodinger equation $i \hbar \frac { \partial \psi } { \partial t } = \hat { H } \psi$ and its conjugated,

(b) the stationary Schrodinger equation ${ \hat { H } } \psi = E \psi$ and its conjugated.

Here $\hat { H }$ is some hermitian operator.
:::

::: {.solution}
Treat $\psi$ and $\psi^\dagger$ as independent variables in the variational
calculation. Assume variations vanish at the temporal endpoints and satisfy
spatial boundary conditions for which $\hat H$ is Hermitian.

<1>1. Define the time-dependent action
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

::: {.proof}
The first term is the standard real first-order kinetic term for a complex
field, and the second is the expectation-density associated with the
Hamiltonian.
:::

<1>2. Varying $S$ with respect to $\psi^\dagger$ gives
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

::: {.proof}
Differentiate the integrand from step <1>1 with respect to
$\psi^\dagger$ and $\dot\psi^\dagger$, keeping $\psi$ fixed.
:::

<1>3. Integrating the middle term in step <1>2 by parts in time gives
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

::: {.proof}
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
This combines with the first term in step <1>2.
:::

<1>4. Therefore stationarity with respect to $\psi^\dagger$ gives
$$
\boxed{
i\hbar\frac{\partial\psi}{\partial t}
=
\hat H\psi.
}
$$

::: {.proof}
The variation $\delta\psi^\dagger$ is arbitrary, so the coefficient in
step <1>3 must vanish.
:::

<1>5. Varying $S$ with respect to $\psi$ gives
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

::: {.proof}
The time-derivative terms are treated exactly as in steps <1>2--<1>3, with
$\psi$ and $\psi^\dagger$ interchanged. For the Hamiltonian term, hermiticity
of $\hat H$ and the assumed spatial boundary conditions move all derivatives
off $\delta\psi$ and onto $\psi^\dagger$.
:::

<1>6. Hence stationarity with respect to $\psi$ gives the conjugate
Schrödinger equation
$$
\boxed{
-i\hbar\frac{\partial\psi^\dagger}{\partial t}
=
(\hat H\psi)^\dagger.
}
$$

::: {.proof}
The variation $\delta\psi$ is arbitrary in step <1>5, so its coefficient must
vanish.
:::

<1>7. Part (a) follows.

::: {.proof}
Steps <1>4 and <1>6 give the Schrödinger equation and its Hermitian conjugate.
:::

<1>8. For the stationary problem, define
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

::: {.proof}
This functional is quadratic and vanishes on an eigenstate of energy $E$.
:::

<1>9. Variation with respect to $\psi^\dagger$ gives
$$
\delta_{\psi^\dagger}S_E
=
\int d^3r
\delta\psi^\dagger
(\hat H-E)
\psi.
$$

::: {.proof}
The functional in step <1>8 is linear in $\psi^\dagger$.
:::

<1>10. Therefore stationarity with respect to $\psi^\dagger$ gives
$$
\boxed{
\hat H\psi=E\psi.
}
$$

::: {.proof}
The variation $\delta\psi^\dagger$ is arbitrary in step <1>9.
:::

<1>11. Variation with respect to $\psi$ gives
$$
\boxed{
(\hat H\psi)^\dagger
=
E\psi^\dagger.
}
$$

::: {.proof}
Hermiticity of $\hat H$ allows the variation to be transferred from
$\hat H\delta\psi$ onto the conjugate field, exactly as in step <1>5. Since
$E$ is real for a Hermitian Hamiltonian, the result is the Hermitian conjugate
of step <1>10.
:::

<1>12. Part (b) follows.

::: {.proof}
Steps <1>10--<1>11 give the stationary Schrödinger equation and its conjugate.
:::

<1>13. Q.E.D.

::: {.proof}
Steps <1>7 and <1>12 establish parts (a) and (b), respectively.
:::
:::
