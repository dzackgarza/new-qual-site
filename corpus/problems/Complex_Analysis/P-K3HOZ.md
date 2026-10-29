---
schema: qual/card@1
id: P-K3HOZ
kind: problem
title: Identity theorem and Schwarz reflection for harmonic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Identity Theorem
  - Schwarz Reflection
  - Mean Value Property
relations: []
review: draft
audit:
- event: solution-reviewed
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The earlier solution to (2) mixed the names f, g, h and did not treat a disconnected O; its reflection in (3) defined U in terms of itself and conjugated the circle average incorrectly. All three parts were rewritten. The source's reference and hint moved to a remark and a hint block.
---

::: {.problem}
(1) Assume $u$ is harmonic on open set $O$ and $z_n$ is a sequence in $O$ such that $u(z_n) = 0$ and $\lim z_n \in O$.
Prove or disprove that $u$ is identically zero.
What if $O$ is a region?

(2) Assume $u$ is harmonic on open set $O$ and $u(z) = 0$ on a disc in $O$.
Prove or disprove that $u$ is identically zero.
What if $O$ is a region?

(3) Formulate and prove a Schwarz reflection principle for harmonic functions
:::

::: {.hint}
(3) Verify the mean value property for the function obtained by reflection.
:::

::: {.solution}
(1)

::: pf

::: pf-step
The claim is false, even when $O$ is a region.

::: pf-proof
Take $O = \CC$, $u(z) = \Re z$ and $z_n = i/n$.
Then $u$ is harmonic, $u(z_n) = 0$ and $z_n \to 0 \in O$, but $u(1) = 1$.
:::

:::

:::

(2)

::: pf

::: pf-step
The claim is false for a general open set.

::: pf-proof
Let $O = D(0,1) \cup D(3,1)$ and let $u$ be $0$ on $D(0,1)$ and $1$ on $D(3,1)$.
:::

:::

::: pf-step
The claim is true when $O$ is a region.

::: pf-proof
The function $f = u_x - iu_y$ is holomorphic on $O$, since the Cauchy--Riemann equations for $f$ are $u_{xx} = -u_{yy}$ and $u_{xy} = u_{yx}$.
It vanishes on the given disc, so $f \equiv 0$ on the connected set $O$ by the identity theorem.
Hence $u_x = u_y = 0$ on $O$, so $u$ is constant on $O$, and the constant is $0$.
:::

:::

:::

(3)
Let $\Omega$ be an open set symmetric about $\RR$, and let $\Omega^{\pm} = \Omega \cap \{\pm\Im z > 0\}$ and $I = \Omega \cap \RR$.
We prove the following reflection principle: if $u$ is continuous on $\Omega^+ \cup I$, harmonic on $\Omega^+$, and $u = 0$ on $I$, then
$$
U(z) \coloneqq
\begin{cases}
u(z) & z\in \Omega^+ \cup I, \\
-u(\bar z) & z\in \Omega^-
\end{cases}
$$
is harmonic on $\Omega$.

::: pf

::: {.pf-step #continuous-odd}
$U$ is continuous on $\Omega$ and $U(\bar z) = -U(z)$ for every $z \in \Omega$.

::: pf-proof
The two formulas are continuous on their pieces and both tend to $0$ at points of $I$, where $U = 0$.
The symmetry holds by definition off $\RR$, and on $I$ both sides are $0$.
:::

:::

::: {.pf-step #off-axis}
$U$ is harmonic on $\Omega^+$ and on $\Omega^-$.

::: pf-proof
On $\Omega^+$, $U = u$.
On $\Omega^-$, $U(x,y) = -u(x,-y)$, and $\Delta[u(x,-y)] = (\Delta u)(x,-y) = 0$.
:::

:::

::: {.pf-step #axis-mean}
For $x_0 \in I$ and $\overline{D}(x_0,\rho) \subset \Omega$, $U(x_0) = \frac{1}{2\pi}\int_{-\pi}^{\pi} U(x_0 + \rho e^{it})\,dt$.

::: pf-proof
$U(x_0) = 0$.
By step [](#continuous-odd){.pf-ref}, $U(x_0 + \rho e^{-it}) = U(\overline{x_0 + \rho e^{it}}) = -U(x_0 + \rho e^{it})$, so the substitution $t \mapsto -t$ shows that the integral equals its own negative.
:::

:::

::: pf-step
$U$ is harmonic on $\Omega$.

::: pf-proof
By steps [](#continuous-odd){.pf-ref}, [](#off-axis){.pf-ref} and [](#axis-mean){.pf-ref}, $U$ is continuous and has the mean value property on all sufficiently small circles about every point of $\Omega$; harmonic functions have it off $\RR$.
A continuous function with this local mean value property is harmonic.
:::

:::

:::
:::

::: {.remark}
The source compares part (3) with Theorem 5.6 on p. 60 of Stein and Shakarchi, *Complex Analysis*.
:::
