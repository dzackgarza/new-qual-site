---
schema: qual/card@1
id: E-PQ7NC
kind: exercise
title: "Complement of the disc to $\\mathbb{H}$"
classification:
  areas:
  - complex-analysis
  topics:
  - conformal-maps
  - geometry
relations: []
review: draft
---
:::{.exercise title="Complement of the disc to $\mathbb{H}$"}
Find a conformal map $\DD^c \intersect \HH \to \HH$.
:::

:::{.solution}
Claim: the map $f(z) \da z+z\inv$ works.
Consider the images of circles $\gamma_r(t) \da rei^{t}$ where $t\in [-\pi, \pi]$.
For $r=1$, 
\[
f(\gamma_1(t)) = e^{it} + e^{-it} = 2\cos(t)
,\]
which sweeps out $[-2, 2]$ twice.
For arbitrary $r$,
\[
f(\gamma_r(t)) = re^{it} + r\inv e^{-it} = (r+r\inv)\cos(t) +i(r-r\inv)\sin(t)
,\]
which sweeps out an ellipse with horizontal radius $r+r\inv$ and vertical radius $r-r\inv$.
For $1<r<\infty$, these sweep out all of $\CC\sm \DD$.
Restricting $t\in [0, \pi]$, the $\gamma_r(t)$ are top halves of circles which cover all of $\HH\sm\DD$, and the images $f(\gamma_r(t))$ are top halves of ellipses which sweep out all of $\HH$.
This includes points inside of $\DD \intersect \HH$ -- this is because for any $t\in (0, \infty)$, there is always a solution $r$ to $t=r-r\inv$:
\[
t = r-r\inv \implies r^2-tr-1 \implies r = {t \pm \sqrt{t^2+4}\over 2}
.\]
So there is an image ellipse at that vertical height.
Since every point $z_0\in \HH$ is on an ellipse of *some* vertical height $t$, $\HH$ is in the image.

That this map is conformal: a computation shows $f'(z) = 1 + {1\over r^2}$, which vanishes only at $z=\pm 1$.
Since these are not in the domain, the derivative is nonvanishing, making $f$ conformal.
:::

