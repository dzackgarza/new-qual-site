---
schema: qual/card@1
id: P-V2OBF
kind: problem
title: The sets $\abs{z-\alpha}+\abs{z+\alpha}=k$ and $\abs{z-\alpha}+\abs{z+\alpha}\leq k$ for $2\abs{\alpha}<k$
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
relations: []
review: draft
---

::: {.problem}
Describe each set in the $z$-plane in (a) and (b) below, where $\alpha$ is a complex number and $k$ is a positive number such that $2\abs{\alpha}<k$.

(a) $\abs{z-\alpha}+\abs{z+\alpha}=k$;

(b) $\abs{z-\alpha}+\abs{z+\alpha} \leq k$.
:::

::: {.solution}
Rotate coordinates so that $\alpha = \abs{\alpha} \geq 0$; a rotation about $0$ preserves distances. Write $z = x + iy$ and $c = \abs{\alpha}$.

::: pf

::: {.pf-step #ellipse}

(a) The set is the ellipse with foci $\pm\alpha$, center $0$, major axis along the line through $\pm\alpha$, semi-major axis $\frac{k}{2}$ and semi-minor axis $\frac12\sqrt{k^2-4\abs{\alpha}^2}$; in the rotated coordinates,
$$
\boxed{
\frac{x^2}{(k/2)^2}
+\frac{y^2}{k^2/4-\abs{\alpha}^2}=1.}
$$
When $\alpha = 0$ it is the circle of radius $k/2$ about $0$.

::: pf-proof

The set is the locus of points whose distances to the foci $\pm c$ have the constant sum $k > 2c$, which is the ellipse with semi-major axis $a = k/2$, focal distance $c$, and semi-minor axis $\sqrt{a^2 - c^2} = \frac12\sqrt{k^2 - 4c^2}$.

:::

:::

::: pf-step

(b) The set is the closed region bounded by the ellipse of step [](#ellipse){.pf-ref}.

::: pf-proof

The function $s(z) = \abs{z-\alpha}+\abs{z+\alpha}$ is convex, continuous, and tends to infinity, and $s = k$ exactly on the ellipse. Its sublevel set $\{s \leq k\}$ is therefore a compact convex set with boundary $\{s = k\}$, which is the closed region the ellipse bounds.

:::

:::

:::

:::
