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
---

::: {.problem}
Let $C$ be a circle in the $xy$-plane, oriented counterclockwise, and not passing through the origin.
Prove that $$\oint_C \frac{-y}{x^2+y^2}\,dx + \frac{x}{x^2+y^2}\,dy$$ equals $0$ if the origin is outside the circle, and $2\pi$ if the origin is inside the circle.
:::

::: {.solution}
Let
\[
P(x,y)=\frac{-y}{x^2+y^2},
\qquad
Q(x,y)=\frac{x}{x^2+y^2}.
\]
Away from the origin,
\[
\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}=0.
\]

If the origin lies outside $C$, then $P,Q$ are continuously differentiable on the disk bounded by $C$. Green's theorem therefore gives
\[
\oint_C P\,dx+Q\,dy=0.
\]

If the origin lies inside $C$, choose a small positively oriented circle $C_\varepsilon$ centered at the origin and contained inside $C$. Apply Green's theorem to the annular region between $C$ and $C_\varepsilon$. Its positively oriented boundary is $C-C_\varepsilon$, so
\[
\oint_C P\,dx+Q\,dy-\oint_{C_\varepsilon}P\,dx+Q\,dy=0.
\]
Parametrize $C_\varepsilon$ by
\[
x=\varepsilon\cos t,\qquad y=\varepsilon\sin t,\qquad 0\le t\le2\pi.
\]
Then
\[
P\,dx+Q\,dy
=\sin^2t\,dt+\cos^2t\,dt=dt.
\]
Hence
\[
\oint_C P\,dx+Q\,dy
=\int_0^{2\pi}dt
=2\pi.
\]
:::
