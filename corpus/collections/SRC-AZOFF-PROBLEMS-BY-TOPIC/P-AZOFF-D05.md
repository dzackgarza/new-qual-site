---
schema: qual/card@1
id: P-AZOFF-D05
kind: problem
title: No polynomials converge uniformly to $1/z$ on the unit circle
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Integrals and Cauchy’s theorem, Problem 5, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used the positively oriented unit circle. Every polynomial has a global
    antiderivative, so its contour integral is zero. Uniform convergence on
    the circle would pass the integral to 1/z, whose contour integral is
    2*pi*i, a contradiction. The source compilation contains no worked
    solution.
---

::: {.problem}
Prove that there is no sequence of polynomials that converge uniformly to the function $\textstyle f ( z ) = { \frac { 1 } { z } }$ on the unit circle.
:::

::: {.solution}
Let
$$
\Gamma=\{z\in\CC:\abs z=1\}
$$
with counterclockwise orientation.

<1>1. For every polynomial $p$,
$$
\int_\Gamma p(z)\,dz=0.
$$

::: {.proof}
Every polynomial has a polynomial antiderivative on all of $\CC$. The
integral of a derivative over a closed curve is zero, so the displayed
integral vanishes.
:::

<1>2. If a sequence of polynomials $p_n$ converged uniformly to $1/z$ on
$\Gamma$, then
$$
\int_\Gamma p_n(z)\,dz
\longrightarrow
\int_\Gamma \frac{dz}{z}.
$$

::: {.proof}
Uniform convergence gives
$$
\sup_{z\in\Gamma}
\abs{p_n(z)-1/z}
\longrightarrow0.
$$
Therefore
$$
\begin{aligned}
\left|
\int_\Gamma
\left(p_n(z)-\frac1z\right)\,dz
\right|
&\leq
\operatorname{length}(\Gamma)
\sup_{z\in\Gamma}
\abs{p_n(z)-1/z}\\
&=
2\pi
\sup_{z\in\Gamma}
\abs{p_n(z)-1/z}
\longrightarrow0.
\end{aligned}
$$
This is exactly convergence of the contour integrals.
:::

<1>3. The contour integral of $1/z$ around $\Gamma$ is
$$
\int_\Gamma\frac{dz}{z}=2\pi i.
$$

::: {.proof}
Parametrize
$$
z=e^{it},
\qquad
0\leq t\leq2\pi.
$$
Then
$$
dz=ie^{it}\,dt,
$$
so
$$
\int_\Gamma\frac{dz}{z}
=
\int_0^{2\pi}i\,dt
=
2\pi i.
$$
:::

<1>4. No sequence of polynomials can converge uniformly to $1/z$ on the
unit circle.

::: {.proof}
If such a sequence existed, step <1>1 would give
$$
\int_\Gamma p_n(z)\,dz=0
$$
for every $n$. By step <1>2, these zero integrals would converge to
$$
\int_\Gamma\frac{dz}{z}.
$$
Step <1>3 says that limit is $2\pi i\neq0$, a contradiction.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required nonexistence statement.
:::
:::
