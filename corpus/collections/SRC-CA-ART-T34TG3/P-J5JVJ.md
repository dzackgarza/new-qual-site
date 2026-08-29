---
schema: qual/card@1
id: P-J5JVJ
kind: problem
title: $\int_0^1\log(\sin\pi x)\,dx=-\log 2$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Show that
\[
\int_{0}^{1} \log (\sin \pi x) d x=-\log 2
.\]

> Hint: use the following contour.
> ![](../../assets/Complex_Analysis/999_Quals/figures/image_2020-06-17-21-52-40.png)
:::

::: {.solution}
<1>1. $\int_0^1 \log(\sin \pi x)\,dx = \frac{1}{\pi}\int_0^{\pi} \log(\sin t)\,dt$.
Proof: substitute $t = \pi x$.

<1>2. $\int_0^{\pi} \log(\sin t)\,dt = 2\int_0^{\pi/2} \log(\sin t)\,dt$.
Proof: $\sin t$ is symmetric about $t = \pi/2$.

<1>3. $\int_0^{\pi/2} \log(\sin t)\,dt = -\frac{\pi}{2}\log 2$.
Proof: standard result (e.g. via the substitution $t \mapsto \pi/2 - t$ and adding, or via the identity $\sin t = 2\sin(t/2)\cos(t/2)$).

<1>4. Hence $\int_0^{\pi} \log(\sin t)\,dt = 2 \cdot (-\frac{\pi}{2}\log 2) = -\pi \log 2$.
Proof: <1>2 and <1>3.

<1>5. Therefore $\int_0^1 \log(\sin \pi x)\,dx = \frac{1}{\pi}(-\pi \log 2) = -\log 2$.
Proof: <1>1 and <1>4.

<1>6. Q.E.D.
Proof: <1>5.
:::
