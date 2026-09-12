---
schema: qual/card@1
id: P-FS6W6
kind: problem
title: A conformal map from $\DD$ to $\HH$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: problem
Find a conformal map from $\DD$ to $\HH$.
:::

::: solution
The Cayley transform
\[
\boxed{F(z)=i\frac{1+z}{1-z}}
\]
is a Möbius transformation. For $|z|<1$,
\[
\Im F(z)
=\Re\frac{1+z}{1-z}
=\frac{1-|z|^2}{|1-z|^2}>0,
\]
so $F(\mathbb D)\subset\mathbb H$. Its inverse is
\[
F^{-1}(w)=\frac{w-i}{w+i},
\]
and for $\Im w>0$ one has
\[
\left|\frac{w-i}{w+i}\right|<1.
\]
Hence $F$ is a biholomorphism from $\mathbb D$ onto $\mathbb H$.
:::
