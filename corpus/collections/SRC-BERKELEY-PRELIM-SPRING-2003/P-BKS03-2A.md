---
schema: qual/card@1
id: P-BKS03-2A
kind: problem
title: Directional derivatives without differentiability at the origin
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the bound giving continuity, the directional derivatives
    computed in the two kinds of direction, the consequence that a derivative would have to vanish, and the
    curve along which differentiability fails. No retained solution set covers this exercise, so the
    argument is the card's own; every limit was recomputed for this pass, including the two-sided behaviour
    of $|t|/t$ in part (b).
---

::: {.problem}
Define $f:\RR^2\to\RR$ by $f(x,0)=0$ and, for $y\ne0$,
$$
f(x,y)=\left(1-\cos\frac{x^2}{y}\right)\sqrt{x^2+y^2}.
$$

(a) Show that $f$ is continuous at $(0,0)$.

(b) Calculate all directional derivatives at $(0,0)$.

(c) Show that $f$ is not differentiable at $(0,0)$.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own, and each limit was recomputed for this pass. The function is $f(x,0)=0$ and $f(x,y)=\left(1-\cos\frac{x^{2}}{y}\right)\sqrt{x^{2}+y^{2}}$ for $y\ne0$, so that $f(0,0)=0$.

::: pf

::: {.pf-step #continuous}
(a) $f$ is continuous at $(0,0)$.

::: pf-proof
Since $\abs{1-\cos\theta}\le2$ for every real $\theta$,
$$
\abs{f(x,y)}=\Bigl(1-\cos\frac{x^{2}}{y}\Bigr)\sqrt{x^{2}+y^{2}}\le 2\sqrt{x^{2}+y^{2}}
$$
for $y\ne0$, while $f(x,0)=0$; in both cases $\abs{f(x,y)}\le2\sqrt{x^{2}+y^{2}}$. The right side tends to $0$ as $(x,y)\to(0,0)$, and $f(0,0)=0$, so $\abs{f(x,y)-f(0,0)}\to0$ and $f$ is continuous there.
:::

:::

::: {.pf-step #directional}
(b) Every directional derivative of $f$ at $(0,0)$ exists and equals $0$.

::: pf-proof
Fix $(x,y)\ne(0,0)$. The directional derivative is $\lim_{t\to0}\bigl(f(tx,ty)-f(0,0)\bigr)/t$. If $y=0$ then $f(tx,0)=0$ for every $t$, so the quotient is $0$ identically. If $y\ne0$, then for $t\ne0$
$$
\frac{f(tx,ty)}{t}=\Bigl(1-\cos\frac{t^{2}x^{2}}{ty}\Bigr)\frac{\abs{t}\sqrt{x^{2}+y^{2}}}{t}=\Bigl(1-\cos\bigl(t\,\tfrac{x^{2}}{y}\bigr)\Bigr)\frac{\abs{t}}{t}\sqrt{x^{2}+y^{2}},
$$
and $\abs{1-\cos\theta}\le\theta^{2}/2$ gives $\abs{1-\cos(t x^{2}/y)}\le t^{2}x^{4}/(2y^{2})$, so the modulus of the whole quotient is at most $\abs{t}\,x^{4}\sqrt{x^{2}+y^{2}}/(2y^{2})$, which tends to $0$ with $t$ from either side. So the directional derivative is $0$ in every direction.
:::

:::

::: {.pf-step #derivative-zero}
If $f$ were differentiable at $(0,0)$, its derivative there would be the zero linear map.

::: pf-proof
The derivative at a point is a linear map whose value on a direction is that directional derivative; by step [](#directional){.pf-ref} all directional derivatives vanish, so a linear map with all values zero, that is the zero map.
:::

:::

::: {.pf-step}
(c) $f$ is not differentiable at $(0,0)$.

::: pf-proof
Were $f$ differentiable at the origin, step [](#derivative-zero){.pf-ref} would give
$$
\frac{f(x,y)-f(0,0)-0}{\sqrt{x^{2}+y^{2}}}\longrightarrow0\qquad\bigl((x,y)\to(0,0)\bigr).
$$
But approach the origin along the curve $x^{2}/y=\pi$ (that is $y=x^{2}/\pi$, with $y\ne0$ for $x\ne0$): there $\cos(x^{2}/y)=\cos\pi=-1$, so $f(x,y)=2\sqrt{x^{2}+y^{2}}$ and the quotient equals $2$ at every point of the curve. A quantity tending to $0$ cannot equal $2$ along a curve approaching the origin, so $f$ is not differentiable there.
:::

:::

:::
:::
