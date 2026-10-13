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

(a) Find an extremum of $S [ \psi , \psi ^ { \dagger } ]$ in a class of $C ^ { 1 } ( \mathbb { R } )$ functions of the form $\psi ( x ) = { \sqrt { \pi \sigma ^ { 2 } } } e ^ { - { \frac { x ^ { 2 } } { 2 \sigma ^ { 2 } } } }$

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

<1>1. The derivatives are
$$
\psi_\sigma'=-\frac{x}{\sigma^2}\psi_\sigma,
$$
and
$$
\psi_\sigma''=\left(\frac{x^2}{\sigma^4}-\frac1{\sigma^2}\right)\psi_\sigma.
$$

::: {.proof}
Differentiate the Gaussian once and then differentiate the result again.
:::

<1>2. Acting with the Hamiltonian gives
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

::: {.proof}
Substitute step <1>1 into the definition of $\hat H$ and collect the constant and $x^2$ coefficients.
:::

<1>3. The Gaussian is an exact eigenfunction precisely when
$$
\frac{m\omega^2}{2}-\frac{\hbar^2}{2m\sigma^4}=0.
$$

::: {.proof}
For $\hat H\psi_\sigma=E\psi_\sigma$ with constant $E$, the bracket in step <1>2 must be independent of $x$.
:::

<1>4. Therefore the distinguished width is
$$
\boxed{\sigma_*^2=\frac{\hbar}{m\omega}}.
$$

::: {.proof}
Step <1>3 gives $m^2\omega^2\sigma^4=\hbar^2$. Since $\sigma>0$, take the positive square root.
:::

<1>5. The same width is the unique minimum of the Gaussian Rayleigh quotient
$$
\mathcal E(\sigma)
=
\frac{\langle\psi_\sigma,\hat H\psi_\sigma\rangle}
{\langle\psi_\sigma,\psi_\sigma\rangle}.
$$

::: {.proof}
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
whose unique positive zero is step <1>4. Moreover
$$
\mathcal E''(\sigma)
=
\frac{3\hbar^2}{2m\sigma^4}
+
\frac{m\omega^2}{2}
>0.
$$
:::

<1>6. Hence the Gaussian extremum occurs at
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

::: {.proof}
Substitute the minimizing width from step <1>4 into the source ansatz.
:::

<1>7. Part (a) follows.

::: {.proof}
Steps <1>4--<1>6 identify the extremizing member of the Gaussian family.
:::

<1>8. At this width, step <1>2 reduces to
$$
\hat H\psi_*
=
\frac{\hbar^2}{2m\sigma_*^2}\psi_*.
$$

::: {.proof}
The $x^2$ coefficient vanishes by step <1>3.
:::

<1>9. Hence the corresponding eigenvalue is
$$
\boxed{E_0=\frac{\hbar\omega}{2}}.
$$

::: {.proof}
Use $\sigma_*^2=\hbar/(m\omega)$ in step <1>8.
:::

<1>10. At $E=E_0$, the functional is stationary at $\psi_*$ even under full independent variations of $\psi$ and $\psi^\dagger$.

::: {.proof}
At the pair from steps <1>6 and <1>9,
$$
(E_0-\hat H)\psi_*=0.
$$
Since $\hat H$ is Hermitian, the conjugate equation also holds. Therefore the first variation of $S$ vanishes for arbitrary independent variations, and hence in particular inside the Gaussian ansatz family.
:::

<1>11. Part (b) follows.

::: {.proof}
Step <1>9 gives the requested eigenvalue.
:::

<1>12. Q.E.D.

::: {.proof}
Steps <1>7 and <1>11 establish parts (a) and (b), respectively.
:::
:::
