---
schema: qual/card@1
id: P-73UFB
kind: problem
title: Unique fractional linear transformation sending a circle $C$ to $C'$ with $f(z_1)=z'_1$
  and $f(z_2)=z'_2$
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Conformal Maps
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $C$ and $C'$ be two circles and let $z_1 \in C$, $z_2 \notin C$, $z'_1 \in C'$, $z'_2 \notin C'$.
Show that there is a unique fractional linear transformation $f$ with $f(C) = C'$ and $f(z_1) = z'_1$, $f(z_2) = z'_2$.
:::

::: {.solution}
Work on the Riemann sphere $\hat\CC$.
For a circle $\Gamma$ and a point $w\notin\Gamma$, let $w^*_\Gamma$ be the reflection (inverse point) of $w$ in $\Gamma$; it is the point other than $w$ such that every circle through $w$ and $w^*_\Gamma$ meets $\Gamma$ orthogonally.
Write $z_2^* = (z_2)^*_C$ and $z_2'^* = (z'_2)^*_{C'}$.

::: pf

::: {.pf-step #three-points}
A fractional linear transformation is determined by its values at three distinct points, and any three distinct points can be sent to any three distinct points.

::: pf-proof
This is the standard property of the cross-ratio: $f$ is the unique map with $(f(z), w_1, w_2, w_3) = (z, u_1, u_2, u_3)$.
:::

:::

::: {.pf-step #symmetry}
If $f$ is a fractional linear transformation and $f(\Gamma)=\Gamma'$, then $f(w^*_\Gamma) = f(w)^*_{\Gamma'}$.

::: pf-proof
$f$ maps circles to circles and preserves angles, so it carries the circles through $w$ and $w^*_\Gamma$ orthogonal to $\Gamma$ onto circles through $f(w)$ and $f(w^*_\Gamma)$ orthogonal to $\Gamma'$.
This characterizes $f(w^*_\Gamma)$ as $f(w)^*_{\Gamma'}$.
:::

:::

::: {.pf-step #apollonius}
Given points $u\neq u^*$ and a point $p\notin\theset{u,u^*}$, exactly one circle $\Gamma$ passes through $p$ and has $u^*=u^*_\Gamma$.

::: pf-proof
Apply a fractional linear transformation $T$ with $T(u)=0$ and $T(u^*)=\infty$; by step [](#symmetry){.pf-ref} it suffices to treat $u=0$, $u^*=\infty$.
The circles for which $0$ and $\infty$ are inverse points are exactly the circles $\abs{w}=\rho$ with $\rho>0$, and exactly one of them passes through $p$.
:::

:::

::: {.pf-step #uniqueness}
There is at most one such $f$.

::: pf-proof
By step [](#symmetry){.pf-ref}, any such $f$ satisfies $f(z_2^*)=z_2'^*$.
The points $z_1$, $z_2$, $z_2^*$ are distinct because $z_2\notin C$, $z_2^*\notin C$ and $z_2^*\neq z_2$, so step [](#three-points){.pf-ref} gives uniqueness.
:::

:::

::: pf-step
There is such an $f$.

::: pf-proof
By step [](#three-points){.pf-ref}, let $f$ send $z_1, z_2, z_2^*$ to $z_1', z_2', z_2'^*$, which are distinct for the same reason.
By step [](#symmetry){.pf-ref}, $f(C)$ is a circle through $z_1'$ for which $z_2'$ and $z_2'^*$ are inverse points.
So is $C'$, and by step [](#apollonius){.pf-ref} $f(C)=C'$.
:::

:::

:::

:::
