---
schema: qual/card@1
id: P-TRIV-VP13
kind: problem
title: Gaussian variational ansatz for the harmonic oscillator ground state
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Variational Principle, Problem 13, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the functional $S [ \psi , \psi ^ { \dagger } ] = \int _ { - \infty } ^ { \infty } d x \psi ^ { \dagger } ( E - \hat { H } ) \psi$ , where

$$
{ \hat { H } } = - { \frac { \hbar ^ { 2 } } { 2 m } } { \frac { \partial ^ { 2 } } { \partial x ^ { 2 } } } + { \frac { m \omega ^ { 2 } x ^ { 2 } } { 2 } } .\tag{19}
$$

(a) Find an extremum of $S [ \psi , \psi ^ { \dagger } ]$ in a class of $C ^ { 1 } ( \RR )$ functions of the form $\psi ( x ) = { \sqrt { \pi \sigma ^ { 2 } } } e ^ { - { \frac { x ^ { 2 } } { 2 \sigma ^ { 2 } } } }$

(b) Find an eigenvalue of $\hat { H }$ corresponding to this extremum.
:::

::: {.remark}
The source Gaussian $\psi_\sigma(x)=\sqrt{\pi\sigma^2}\,e^{-x^2/(2\sigma^2)}$ is not normalized. This does not affect the optimal width or eigenvalue, because an overall nonzero scalar cancels from the Rayleigh quotient and does not change an eigenvalue equation.
:::

::: {.solution}

Write
$$
\psi_\sigma(x)=A(\sigma)e^{-x^2/(2\sigma^2)},
\qquad
A(\sigma)=\sqrt{\pi\sigma^2}.
$$

::: pf

::: {.pf-step #s1-1}

The derivatives are
$$
\psi_\sigma'=-\frac{x}{\sigma^2}\psi_\sigma,
$$
and
$$
\psi_\sigma''=\left(\frac{x^2}{\sigma^4}-\frac1{\sigma^2}\right)\psi_\sigma.
$$


::: pf-proof

Differentiate the Gaussian once and then differentiate the result again.

:::

:::

::: {.pf-step #s1-2}

Acting with the Hamiltonian gives
$$
\hat H\psi_\sigma
=
\left[
\frac{\hbar^2}{2m\sigma^2}
+
\left(
\frac{m\omega^2}{2}
-
\frac{\hbar^2}{2m\sigma^4}
\right)x^2
\right]
\psi_\sigma.
$$


::: pf-proof

Substitute step [](#s1-1){.pf-ref} into the definition of $\hat H$ and collect the constant and $x^2$ coefficients.

:::

:::

::: {.pf-step #s1-3}

The Gaussian is an exact eigenfunction precisely when
$$
\frac{m\omega^2}{2}-\frac{\hbar^2}{2m\sigma^4}=0.
$$


::: pf-proof

For $\hat H\psi_\sigma=E\psi_\sigma$ with constant $E$, the bracket in step [](#s1-2){.pf-ref} must be independent of $x$.

:::

:::

::: {.pf-step #s1-4}

Therefore the distinguished width is
$$
\boxed{\sigma_*^2=\frac{\hbar}{m\omega}}.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} gives $m^2\omega^2\sigma^4=\hbar^2$. Since $\sigma>0$, take the positive square root.

:::

:::

::: {.pf-step #s1-5}

The same width is the unique minimum of the Gaussian Rayleigh quotient
$$
\mathcal E(\sigma)
=
\frac{\langle\psi_\sigma,\hat H\psi_\sigma\rangle}
{\langle\psi_\sigma,\psi_\sigma\rangle}.
$$


::: pf-proof

The overall factor $A(\sigma)$ cancels. For this Gaussian,
$$
\frac{\int x^2|\psi_\sigma|^2dx}{\int|\psi_\sigma|^2dx}
=
\frac{\sigma^2}{2}
$$
and
$$
\frac{\int|\psi_\sigma'|^2dx}{\int|\psi_\sigma|^2dx}
=
\frac1{2\sigma^2}.
$$
Thus
$$
\mathcal E(\sigma)
=
\frac{\hbar^2}{4m\sigma^2}
+
\frac{m\omega^2\sigma^2}{4}.
$$
Differentiating gives
$$
\mathcal E'(\sigma)
=
-\frac{\hbar^2}{2m\sigma^3}
+
\frac{m\omega^2\sigma}{2},
$$
whose unique positive zero is step [](#s1-4){.pf-ref}. Moreover
$$
\mathcal E''(\sigma)
=
\frac{3\hbar^2}{2m\sigma^4}
+
\frac{m\omega^2}{2}
>0.
$$

:::

:::

::: {.pf-step #s1-6}

Hence the Gaussian extremum occurs at
$$
\boxed{
\psi_*(x)
=
\sqrt{\pi\sigma_*^2}
\exp\left(-\frac{x^2}{2\sigma_*^2}\right),
\qquad
\sigma_*^2=\frac{\hbar}{m\omega}.
}
$$


::: pf-proof

Substitute the minimizing width from step [](#s1-4){.pf-ref} into the source ansatz.

:::

:::

::: {.pf-step #s1-7}

Part (a) follows.


::: pf-proof

Steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref} identify the extremizing member of the Gaussian family.

:::

:::

::: {.pf-step #s1-8}

At this width, step [](#s1-2){.pf-ref} reduces to
$$
\hat H\psi_*
=
\frac{\hbar^2}{2m\sigma_*^2}\psi_*.
$$


::: pf-proof

The $x^2$ coefficient vanishes by step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Hence the corresponding eigenvalue is
$$
\boxed{E_0=\frac{\hbar\omega}{2}}.
$$


::: pf-proof

Use $\sigma_*^2=\hbar/(m\omega)$ in step [](#s1-8){.pf-ref}.

:::

:::

::: pf-step

At $E=E_0$, the functional is stationary at $\psi_*$ even under full independent variations of $\psi$ and $\psi^\dagger$.


::: pf-proof

At the pair from steps [](#s1-6){.pf-ref} and [](#s1-9){.pf-ref},
$$
(E_0-\hat H)\psi_*=0.
$$
Since $\hat H$ is Hermitian, the conjugate equation also holds. Therefore the first variation of $S$ vanishes for arbitrary independent variations, and hence in particular inside the Gaussian ansatz family.

:::

:::

::: {.pf-step #s1-11}

Part (b) follows.


::: pf-proof

Step [](#s1-9){.pf-ref} gives the requested eigenvalue.

:::

:::

::: pf-qed

Steps [](#s1-7){.pf-ref} and [](#s1-11){.pf-ref} establish parts (a) and (b), respectively.

:::

:::

:::
