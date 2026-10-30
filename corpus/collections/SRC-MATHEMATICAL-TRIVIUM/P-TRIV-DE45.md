---
schema: qual/card@1
id: P-TRIV-DE45
kind: problem
title: Steady temperature in a sphere with hemispheres at different temperatures
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 45, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
The surface of a sphere of radius $R$ is kept at a constant temperature $T_U$ for the upper hemisphere ($0 \leq \theta < \pi/2$) and $T_L$ for the lower hemisphere ($\pi/2 \leq \theta \leq \pi$). Find the stationary temperature distribution inside the sphere, at a distance $r$ from the center, in an expansion in terms of $\frac{r}{R}$. Compute terms up to third order.
:::

::: {.solution}

Put
$$
\mu=\cos\theta,
\qquad
T_0=\frac{T_U+T_L}{2},
\qquad
\Delta T=T_U-T_L.
$$
The boundary temperature is
$$
T(R,\mu)=T_0+\frac{\Delta T}{2}\operatorname{sgn}(\mu).
$$

::: pf

::: {.pf-step #s1-1}

Every axisymmetric harmonic function regular at the center has an expansion
$$
T(r,\theta)=\sum_{\ell=0}^{\infty}A_\ell
\left(\frac rR\right)^\ell P_\ell(\cos\theta).
$$


::: pf-proof

Separation of Laplace's equation in spherical coordinates gives radial factors $r^\ell$ and $r^{-\ell-1}$ multiplying Legendre polynomials $P_\ell(\cos\theta)$. Regularity at $r=0$ excludes the negative powers. Scaling by $R$ gives the displayed form.

:::

:::

::: {.pf-step #s1-2}

The coefficients are
$$
A_0=T_0,
\qquad
A_\ell=\frac{2\ell+1}{2}
\int_{-1}^{1}T(R,\mu)P_\ell(\mu)\,d\mu.
$$


::: pf-proof

At $r=R$, step [](#s1-1){.pf-ref} is the Legendre expansion of the boundary function. Orthogonality,
$$
\int_{-1}^{1}P_\ell(\mu)P_j(\mu)\,d\mu
=\frac{2}{2\ell+1}\delta_{\ell j},
$$
gives the coefficient formula. The average of the two hemisphere temperatures is $A_0=T_0$.

:::

:::

::: {.pf-step #s1-3}

Apart from $A_0$, only odd degrees occur, and
$$
A_1=\frac{3}{4}\Delta T.
$$


::: pf-proof

The function $\operatorname{sgn}(\mu)$ is odd, so its Legendre expansion contains only odd $P_\ell$. For $\ell=1$, $P_1(\mu)=\mu$, hence
$$
A_1=\frac32\frac{\Delta T}{2}
\int_{-1}^{1}\operatorname{sgn}(\mu)\mu\,d\mu
=\frac{3\Delta T}{4},
$$
because the integral is $1$.

:::

:::

::: {.pf-step #s1-4}

The cubic coefficient is
$$
A_3=-\frac{7}{16}\Delta T.
$$


::: pf-proof

Since $P_3(\mu)=(5\mu^3-3\mu)/2$,
$$
\int_{-1}^{1}\operatorname{sgn}(\mu)P_3(\mu)\,d\mu
=2\int_0^1P_3(\mu)\,d\mu
=-\frac14.
$$
Thus
$$
A_3=\frac72\frac{\Delta T}{2}\left(-\frac14\right)
=-\frac{7\Delta T}{16}.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore, through third order in $r/R$,
$$
\boxed{
T(r,\theta)=
\frac{T_U+T_L}{2}
+\frac{3(T_U-T_L)}{4}\frac rR\cos\theta
-\frac{7(T_U-T_L)}{32}
\left(\frac rR\right)^3
\bigl(5\cos^3\theta-3\cos\theta\bigr)
+O\!\left((r/R)^5\right).}
$$


::: pf-proof

Insert $A_0,A_1,A_3$ from steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref} into step [](#s1-1){.pf-ref} and use $P_1(\mu)=\mu$ and $P_3(\mu)=(5\mu^3-3\mu)/2$. The next nonconstant term has odd degree $5$, giving the stated remainder order.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the stationary interior temperature expansion through cubic order.

:::

:::

:::
