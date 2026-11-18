---
schema: qual/card@1
id: P-YVA5W
kind: problem
title: The winding number of a circle about the origin
classification:
  areas:
  - prelim
  topics:
  - Line Integrals
  - Green's Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The vanishing of the curl is now computed rather than asserted, the hypotheses of Green's theorem are checked in both cases (an open set containing the closed disk when the origin is outside, an open set containing the annulus when it is inside), the orientation of the annulus boundary is explained (C together with C_epsilon clockwise), and the parametrization computation keeps the factor eps^2 so that P dx + Q dy = dt is visible. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair; the two values 0 and 2 pi are correct.
---

::: {.problem}
Let $C$ be a circle in the $xy$-plane, oriented counterclockwise, and not passing through the origin.
Prove that $$\oint_C \frac{-y}{x^2+y^2}\,dx + \frac{x}{x^2+y^2}\,dy$$ equals $0$ if the origin is outside the circle, and $2\pi$ if the origin is inside the circle.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

Let $P=\dfrac{-y}{x^2+y^2}$ and $Q=\dfrac{x}{x^2+y^2}$ on $\RR^2\setminus\{0\}$.

::: pf

::: {.pf-step #curlfree}
$\dfrac{\partial Q}{\partial x}-\dfrac{\partial P}{\partial y}=0$ on $\RR^2\setminus\{0\}$.

::: pf-proof
Writing $r^2=x^2+y^2$, $\frac{\partial Q}{\partial x}=\frac{(x^2+y^2)-x(2x)}{(x^2+y^2)^2}=\frac{y^2-x^2}{r^4}$ and $\frac{\partial P}{\partial y}=\frac{-(x^2+y^2)+y(2y)}{(x^2+y^2)^2}=\frac{y^2-x^2}{r^4}$, so the difference vanishes wherever $r\ne0$.
:::

:::

::: {.pf-step #outside}
If the origin is outside $C$ then $\oint_CP\,dx+Q\,dy=0$.

::: pf-proof
Then $P$ and $Q$ are of class $C^1$ on an open set containing the closed disk $D$ bounded by $C$, so Green's theorem applies and the integral over $C$ (counterclockwise, the positive orientation of $\partial D$) equals $\iint_D\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dA=0$ by step [](#curlfree){.pf-ref}.
:::

:::

::: {.pf-step #annulus}
If the origin is inside $C$, then for $0<\varepsilon$ small the annulus $A_\varepsilon$ between $C$ and the circle $C_\varepsilon$ of radius $\varepsilon$ about the origin satisfies
$$
\oint_CP\,dx+Q\,dy=\oint_{C_\varepsilon}P\,dx+Q\,dy .
$$

::: pf-proof
For $\varepsilon$ small enough $C_\varepsilon$ lies inside $C$, and $P,Q$ are $C^1$ on an open set containing the closure of the annulus, on which the curl vanishes by step [](#curlfree){.pf-ref}. Green's theorem on the annulus gives $0=\oint_{\partial A_\varepsilon}P\,dx+Q\,dy$, and the positively oriented boundary of the annulus is $C$ together with $C_\varepsilon$ traversed clockwise, that is $C-C_\varepsilon$. Hence the two counterclockwise integrals are equal.
:::

:::

::: {.pf-step #small}
$\oint_{C_\varepsilon}P\,dx+Q\,dy=2\pi$.

::: pf-proof
Parametrize $C_\varepsilon$ by $x=\varepsilon\cos t$, $y=\varepsilon\sin t$, $0\le t\le2\pi$, so $dx=-\varepsilon\sin t\,dt$ and $dy=\varepsilon\cos t\,dt$. Then $x^2+y^2=\varepsilon^2$ and
$$
P\,dx+Q\,dy=\frac{-\varepsilon\sin t}{\varepsilon^2}(-\varepsilon\sin t)\,dt+\frac{\varepsilon\cos t}{\varepsilon^2}(\varepsilon\cos t)\,dt=(\sin^2t+\cos^2t)\,dt=dt,
$$
so the integral is $\int_0^{2\pi}dt=2\pi$.
:::

:::

::: {.pf-step}
The integral is $0$ when the origin is outside $C$ and $2\pi$ when it is inside.

::: pf-proof
Step [](#outside){.pf-ref} and steps [](#annulus){.pf-ref} with [](#small){.pf-ref} give the two cases.
:::

:::

:::
:::
