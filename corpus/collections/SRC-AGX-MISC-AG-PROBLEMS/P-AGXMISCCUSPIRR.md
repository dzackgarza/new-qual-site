---
schema: qual/card@1
id: P-AGXMISCCUSPIRR
kind: problem
title: The cuspidal cubic is irreducible
classification:
  areas:
  - algebraic-geometry
  topics:
  - Irreducibility
  - Plane Curves
relations: []
review: draft
audit:
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked that the parametrization t -> (t^2,t^3) is polynomial and
    surjective onto the cusp, including the inverse formula t=y/x away from
    the origin, and applied preservation of irreducibility under continuous
    images.
---

::: {.problem}
Prove that the cuspidal cubic $Y \subseteq \AA^2_\CC$ with equation $x^3 - y^2 = 0$ is irreducible.
:::

::: {.hint}
Express $Y$ as the image of $\AA^1$ under a continuous map.
:::

::: {.solution}

::: pf

::: {.pf-step #image-contained-in-y}
The polynomial map
$$
\phi:\AA^1_\CC\longrightarrow\AA^2_\CC,
\qquad
t\longmapsto(t^2,t^3)
$$
has image contained in $Y$.

::: pf-proof
For every $t\in\CC$,
$$
(t^2)^3-(t^3)^2=t^6-t^6=0.
$$
Hence $\phi(t)\in Y$.
:::

:::

::: {.pf-step #phi-surjective}
The map $\phi:\AA^1_\CC\to Y$ is surjective.

::: pf-proof
Let
$$
(x,y)\in Y,
\qquad
x^3=y^2.
$$
If $x=0$, then $y=0$, and
$$
(x,y)=\phi(0).
$$

If $x\ne0$, put
$$
t=\frac yx.
$$
Then
$$
t^2
=
\frac{y^2}{x^2}
=
\frac{x^3}{x^2}
=x
$$
and
$$
t^3
=
t\,t^2
=
\frac yx\,x
=y.
$$
Thus $(x,y)=\phi(t)$.
:::

:::

::: {.pf-step #y-irreducible}
The variety $Y$ is irreducible.

::: pf-proof
The affine line $\AA^1_\CC$ is irreducible because its coordinate ring
$\CC[t]$ is an integral domain. The polynomial map $\phi$ is a morphism,
hence continuous in the Zariski topology. A continuous image of an
irreducible topological space is irreducible, and step [](#phi-surjective){.pf-ref} gives
$$
\phi(\AA^1_\CC)=Y.
$$
Therefore
$$
\boxed{Y\text{ is irreducible}.}
$$
:::

:::

::: pf-qed
Steps [](#image-contained-in-y){.pf-ref} and [](#phi-surjective){.pf-ref} identify $Y$ as the image of the irreducible affine line,
and step [](#y-irreducible){.pf-ref} applies the irreducible-image criterion.
:::

:::

:::
