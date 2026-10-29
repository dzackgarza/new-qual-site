---
schema: qual/card@1
id: P-TRIV-DE49
kind: problem
title: Steady temperature in a semi-infinite cylinder
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 49, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash contains a leading nonprinting control byte at this source position; the byte was removed from the authored card as a nonsemantic extraction artifact.
---

::: {.problem}
Compute the stationary temperature distribution $u ( \rho , \theta , z )$ of a semi-infinite cylinder of radius 1 when the curved surface is kept at temperature 0 if

(a) the flat surface is kept at a temperature $u _ { 0 }$

(b) the flat surface is kept at a temperature $u _ { 0 } \rho$ sin θ
:::

::: {.solution}

The stationary temperature is harmonic in the semi-infinite cylinder
$$
0\leq\rho<1,
\qquad z>0,
$$
vanishes at $\rho=1$, and is required to remain bounded and decay as $z\to\infty$.

::: pf

::: {.pf-step #s1-1}

Separated harmonic modes with angular frequency $m$ have the form
$$
J_m(\alpha\rho)
\bigl(A\cos(m\theta)+B\sin(m\theta)\bigr)e^{-\alpha z},
$$
where the lateral boundary condition requires
$$
J_m(\alpha)=0.
$$


::: pf-proof

In cylindrical coordinates,
$$
\nabla^2u=u_{\rho\rho}+\frac1\rho u_\rho
+\frac1{\rho^2}u_{\theta\theta}+u_{zz}.
$$
Separating $u=R(\rho)\Theta(\theta)Z(z)$ gives periodic angular modes of integer order $m$, a Bessel equation for $R$, and $Z''=\alpha^2Z$. Regularity at $\rho=0$ selects $J_m$ over $Y_m$, decay in $z$ selects $e^{-\alpha z}$, and $u(1,\theta,z)=0$ gives $J_m(\alpha)=0$.

:::

:::

::: {.pf-step #s1-2}

Let $j_{m,n}$ be the $n$th positive zero of $J_m$. For part (a), the solution has the form
$$
u(\rho,z)=\sum_{n=1}^{\infty}A_n
J_0(j_{0,n}\rho)e^{-j_{0,n}z}.
$$


::: pf-proof

The boundary value $u_0$ at $z=0$ is independent of $\theta$, so only the $m=0$ angular mode occurs. Step [](#s1-1){.pf-ref} then gives precisely the displayed radial and axial factors.

:::

:::

::: {.pf-step #s1-3}

The coefficients in part (a) are
$$
A_n=\frac{2u_0}{j_{0,n}J_1(j_{0,n})}.
$$


::: pf-proof

The Fourier--Bessel coefficients for the expansion of the constant function $u_0$ on $0<\rho<1$ are
$$
A_n=\frac{2}{J_1(j_{0,n})^2}
\int_0^1\rho u_0J_0(j_{0,n}\rho)\,d\rho.
$$
Using
$$
\int_0^1\rho J_0(j\rho)\,d\rho=\frac{J_1(j)}j
$$
gives the formula.

:::

:::

::: {.pf-step #s1-4}

Hence part (a) is
$$
\boxed{
u(\rho,z)=2u_0\sum_{n=1}^{\infty}
\frac{J_0(j_{0,n}\rho)}{j_{0,n}J_1(j_{0,n})}
e^{-j_{0,n}z}.}
$$


::: pf-proof

Insert step [](#s1-3){.pf-ref} into step [](#s1-2){.pf-ref}. The Fourier--Bessel expansion recovers the constant flat-face temperature for $0\leq\rho<1$; the mismatch at the rim is the unavoidable corner incompatibility with the curved surface being held at zero.

:::

:::

::: {.pf-step #s1-5}

For part (b), only the $m=1$ sine mode occurs, so
$$
u(\rho,\theta,z)=\sin\theta
\sum_{n=1}^{\infty}B_nJ_1(j_{1,n}\rho)e^{-j_{1,n}z}.
$$


::: pf-proof

The flat-face datum $u_0\rho\sin\theta$ has angular dependence $\sin\theta$, corresponding to $m=1$. Step [](#s1-1){.pf-ref} gives the remaining factors.

:::

:::

::: {.pf-step #s1-6}

The coefficients in part (b) are
$$
B_n=\frac{2u_0}{j_{1,n}J_2(j_{1,n})}.
$$


::: pf-proof

Fourier--Bessel orthogonality gives
$$
B_n=\frac{2u_0}{J_2(j_{1,n})^2}
\int_0^1\rho^2J_1(j_{1,n}\rho)\,d\rho.
$$
The identity
$$
\frac d{d\rho}\left(\rho^2J_2(j\rho)\right)
=j\rho^2J_1(j\rho)
$$
gives
$$
\int_0^1\rho^2J_1(j\rho)\,d\rho=\frac{J_2(j)}j,
$$
and the result follows.

:::

:::

::: {.pf-step #s1-7}

Hence part (b) is
$$
\boxed{
u(\rho,\theta,z)=2u_0\sin\theta
\sum_{n=1}^{\infty}
\frac{J_1(j_{1,n}\rho)}{j_{1,n}J_2(j_{1,n})}
e^{-j_{1,n}z}.}
$$


::: pf-proof

Insert step [](#s1-6){.pf-ref} into step [](#s1-5){.pf-ref}. The resulting harmonic function vanishes at $\rho=1$, decays as $z\to\infty$, and its Fourier--Bessel expansion at $z=0$ equals $u_0\rho\sin\theta$.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} and [](#s1-7){.pf-ref} give the stationary temperature distributions for parts (a) and (b).

:::

:::

:::
