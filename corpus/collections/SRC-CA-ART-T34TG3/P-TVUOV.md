---
schema: qual/card@1
id: P-TVUOV
kind: problem
title: $z^4+2z^3-2z+10$ has one root in each open quadrant
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Polynomials
  - Argument Principle
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Prove that $z^4 + 2 z^3 - 2z + 10 =0$ has exactly one root in each open quadrant.
:::

::: {.solution}
Let $P(z) = z^4 + 2z^3 - 2z + 10$. For $R>0$, let $Q_R=\{z:\abs{z}<R,\ 0<\arg z<\pi/2\}$, whose boundary consists of $\gamma_1=[0,R]$, the arc $\gamma_2$: $z=Re^{i\theta}$, $0\le\theta\le\pi/2$, and the segment $\gamma_3$ from $iR$ to $0$.

::: pf

::: {.pf-step #no-real-roots}
$P$ has no real root.

::: pf-proof
For real $x$, $P(x) = (x^2 + x - 1)^2 + x^2 + 9 \ge 9$.
:::

:::

::: {.pf-step #no-imaginary-roots}
$P$ has no root on the imaginary axis, and $\operatorname{Re}P(iy)>0$ for all real $y$.

::: pf-proof
$P(iy) = (y^4 + 10) - 2iy(y^2 + 1)$, whose real part is at least $10$.
:::

:::

::: {.pf-step #roots-bounded-by-three}
For $R\ge3$ and $\abs{z}=R$, $\abs{P(z)-z^4} < \abs{z^4}$. In particular every root of $P$ satisfies $\abs{z}<3$.

::: pf-proof
$\abs{P(z) - z^4} \le 2R^3 + 2R + 10$, and $R^4 - 2R^3 - 2R - 10$ is positive at $R=3$ (it equals $11$) and increasing for $R\ge3$, since its derivative $4R^3-6R^2-2$ is positive there.
:::

:::

::: {.pf-step #argument-increase-around-boundary}
For $R\ge3$, a continuous argument of $P$ increases by exactly $2\pi$ around $\partial Q_R$.

::: pf-proof

::: {.pf-step #arg-constant-on-real-axis}
Along $\gamma_1$ the argument does not change.

::: pf-proof
$P>0$ on $[0,R]$ by step [](#no-real-roots){.pf-ref} (and $P(0)=10$).
:::

:::

::: {.pf-step #arg-increase-on-arc}
Along $\gamma_2$ the argument increases by $2\pi+\delta$, where $\delta\in(-\pi/2,\pi/2)$ is the principal argument of $P(iR)$.

::: pf-proof
Write $P(z) = z^4\,w(z)$ with $w(z) = P(z)/z^4$. By step [](#roots-bounded-by-three){.pf-ref}, $\abs{w(z)-1}<1$ on $\gamma_2$, so $w$ stays in the right half-plane and its principal argument is a continuous argument there. It is $0$ at $z=R$ (where $w>0$) and $\delta$ at $z=iR$ (where $w=P(iR)/R^4$). The factor $z^4$ contributes $4\cdot\pi/2=2\pi$.
:::

:::

::: {.pf-step #arg-change-on-imaginary-segment}
Along $\gamma_3$ the argument changes by $-\delta$.

::: pf-proof
By step [](#no-imaginary-roots){.pf-ref}, $P(iy)$ lies in the right half-plane for every $y$, so the principal argument is continuous along $\gamma_3$. It equals $\delta$ at $iR$ and $0$ at $P(0)=10$.
:::

:::

::: pf-qed
Add steps [](#arg-constant-on-real-axis){.pf-ref}, [](#arg-increase-on-arc){.pf-ref} and [](#arg-change-on-imaginary-segment){.pf-ref}: $0 + (2\pi+\delta) - \delta = 2\pi$.
:::

:::

:::

::: {.pf-step #one-root-first-quadrant}
$P$ has exactly one root in the open first quadrant.

::: pf-proof
$P$ has no zeros on $\partial Q_R$ by steps [](#no-real-roots){.pf-ref}, [](#no-imaginary-roots){.pf-ref} and [](#roots-bounded-by-three){.pf-ref}. By the argument principle and step [](#argument-increase-around-boundary){.pf-ref}, $P$ has exactly one zero in $Q_R$ for every $R\ge3$, and by step [](#roots-bounded-by-three){.pf-ref} all zeros lie in $\abs{z}<3$.
:::

:::

::: {.pf-step #one-root-each-quadrant}
$P$ has exactly one root in each open quadrant.

::: pf-proof
$P$ has real coefficients, so $z\mapsto\bar z$ maps its roots in the first quadrant bijectively onto its roots in the fourth; by step [](#one-root-first-quadrant){.pf-ref} there is exactly one in each. $P$ has degree $4$ and no roots on the axes (steps [](#no-real-roots){.pf-ref} and [](#no-imaginary-roots){.pf-ref}), so the remaining two roots lie in the open second and third quadrants, and conjugation again matches them, giving one in each.
:::

:::

::: pf-qed
Step [](#one-root-each-quadrant){.pf-ref} is the required statement.
:::

:::
:::
