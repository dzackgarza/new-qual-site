---
schema: qual/card@1
id: P-PRACT20-W5-28
kind: problem
title: Contour integral of $\sin z-\frac{\cos z}{z-\pi/4}$ around $\abs{z}=\pi$
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
  - Contour Integration
  - Cauchy Integral Formula
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 28).
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against the Lamport standard and checked with a residue computation. sin z is entire so its
    integral over the closed curve vanishes; the only singularity of the integrand inside |z| = pi is
    the simple pole at pi/4, whose residue is -cos(pi/4) = -sqrt2/2, so the integral is
    2 pi i (-sqrt2/2) = -sqrt2 pi i, which is the card's box. Confirmed by a computer algebra system,
    which returns residue -sqrt(2)/2 and integral -sqrt(2) I pi. The pole lies inside the contour
    since pi/4 < pi, which the card records. Not claimed: any variant where the numerator is not
    analytic.
---

::: {.problem}
Let $C$ be the circle $\abs{z} = \pi$, oriented positively. Evaluate $\oint_C \left(\sin(z) - \frac{\cos(z)}{z - \pi/4}\right) dz$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The entire term contributes
$$
\oint_C \sin z\,dz=0.
$$


::: pf-proof

The sine function is entire, and $C$ is a closed contour. Cauchy's integral
theorem gives the stated value.

:::

:::

::: {.pf-step #s1-2}

The point
$$
a=\frac{\pi}{4}
$$
lies inside $C$, and
$$
\oint_C\frac{\cos z}{z-a}\,dz
=2\pi i\cos a.
$$


::: pf-proof

Since
$$
\abs{\frac{\pi}{4}}<\pi,
$$
the point $a$ is inside the positively oriented circle. Cauchy's integral
formula applied to the entire function $\cos z$ gives
$$
\oint_C\frac{\cos z}{z-a}\,dz
=2\pi i\cos a.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
\oint_C\left(\sin z-\frac{\cos z}{z-\pi/4}\right)\,dz
=-\sqrt2\,\pi i }.
$$


::: pf-proof

By steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref},
$$
\begin{aligned}
\oint_C\left(\sin z-\frac{\cos z}{z-\pi/4}\right)\,dz
&=
-2\pi i\cos\frac{\pi}{4}\\
&=
-2\pi i\frac{\sqrt2}{2}\\
&=
-\sqrt2\,\pi i.
\end{aligned}
$$
The minus sign comes from the minus sign in the original integrand.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value.

:::

:::

:::
