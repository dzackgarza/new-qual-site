---
schema: qual/card@1
id: P-FHW1-16
kind: problem
title: $\cos 20^\circ$ is not constructible
classification:
  areas: [algebra]
  topics: [Field Extensions, Geometry]
relations: []
review: draft
audit:
- event: source-checked
  by: Claude Opus 5.5
  date: 2026-10-30
  note: Transcribed from the MinerU Flash extraction of assets/attachments/fields-homework-1.pdf and checked against the page image.
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
A complex number $\alpha\in\CC$ is called constructible if $[\QQ(\alpha):\QQ]$ is a power of $2$. Assume without proof that $\alpha$ is constructible if and only if one can construct $\alpha$ (as a vector on the plane) using the ruler and the compass.

(a) Show that $\cos20^\circ$ is not constructible.

(b) Show that trisection of an angle is not always possible using the ruler and the compass.
:::

::: {.solution}
For a real angle $\theta$ put $\zeta=2\cos\theta$, so that $\zeta^3-3\zeta=2\cos3\theta$ by the triple-angle formula, and $\QQ(\zeta)=\QQ(\cos\theta)$.

::: pf

::: {.pf-step #part-a}
(a) $\cos20^\circ$ is not constructible.

::: pf-proof
Take $\theta=20^\circ$ and $\zeta=2\cos20^\circ$. Then $3\theta=60^\circ$ and $2\cos3\theta=1$, so $\zeta^3-3\zeta-1=0$.
The polynomial $x^3-3x-1$ has no rational root: its only possible rational roots are $\pm1$, and $1-3-1=-3\ne0$, $-1+3-1=1\ne0$; being a cubic it is therefore irreducible over $\QQ$.
Hence $[\QQ(\cos20^\circ):\QQ]=[\QQ(\zeta):\QQ]=3$.
A constructible complex number generates over $\QQ$ a field of degree a power of $2$, and $3$ is not a power of $2$; so $\cos20^\circ$ is not constructible.
:::

:::

::: {.pf-step #part-b}
(b) Some angle cannot be trisected with ruler and compass.

::: pf-proof
The angle $60^\circ$ is constructible, since $\cos60^\circ=\tfrac12$ is rational and every rational number is constructible.
Trisecting it means constructing a point whose cosine is $\cos20^\circ$, and step [](#part-a){.pf-ref} shows that no such construction exists.
Hence trisection of an arbitrary constructible angle is impossible with ruler and compass alone.
:::

:::

:::

:::
