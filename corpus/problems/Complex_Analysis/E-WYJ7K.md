---
schema: qual/card@1
id: E-WYJ7K
kind: problem
title: Lune, one intersection
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.problem}
Find a conformal map from the region bounded by $\abs{z - {i\over 2}} = {1\over 2}$ and $\abs{z-i} = 1$ to $\DD$.
:::

::: {.solution}
The two circles are internally tangent at $z=0$, not at $z=i$. The desired region is the part inside $|z-i|<1$ and outside $|z-i/2|<1/2$.

Since both boundary circles pass through $0$, inversion sends them to parallel lines. If
\[
w={1\over z},
\]
then the circle
\[
|z-ia|=a
\]
has equation $|z|^2=2a\Im z$, hence on its image
\[
\Im w=-{\Im z\over |z|^2}=-{1\over 2a}.
\]
Therefore
\[
|z-i|=1\longmapsto \Im w=-{1\over2},
\qquad
|z-i/2|={1\over2}\longmapsto \Im w=-1.
\]
The lune maps to the horizontal strip
\[
-1<\Im w<-{1\over2}.
\]

Now set
\[
\zeta=2\pi(w+i).
\]
Then $0<\Im\zeta<\pi$, so $u=e^\zeta$ maps the strip biholomorphically onto $\HH$. Finally the Cayley map
\[
C(u)={u-i\over u+i}
\]
sends $\HH$ to $\DD$.

Thus one conformal map is
\[
F(z)
=\frac{\exp\!\left(2\pi\left(z^{-1}+i\right)\right)-i}
{\exp\!\left(2\pi\left(z^{-1}+i\right)\right)+i}.
\]
:::
