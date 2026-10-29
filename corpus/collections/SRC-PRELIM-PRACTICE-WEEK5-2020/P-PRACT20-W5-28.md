---
schema: qual/card@1
id: P-PRACT20-W5-28
kind: problem
title: Contour integral of $\sin z-\frac{\cos z}{z-\pi/4}$ around $|z|=\pi$
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 28).
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
\left|\frac{\pi}{4}\right|<\pi,
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
