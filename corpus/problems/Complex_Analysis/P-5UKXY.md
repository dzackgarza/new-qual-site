---
schema: qual/card@1
id: P-5UKXY
kind: problem
title: A conformal map from $\{|z|<1,\ |z-1/2|>1/2\}$ onto $\DD$
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
Find a conformal map from $\theset{z\in \CC \suchthat \abs{z} < 1,\, \abs{z - {1\over 2}} > {1\over 2} }$ to $\DD$.
:::

::: {.solution}
Let
\[
\Omega=\left\{z:|z|<1,\ |z-1/2|>1/2\right\}.
\]
Both boundary circles pass through $1$. The Möbius map
\[
T(z)=\frac1{1-z}
\]
sends that common boundary point to infinity. If $w=T(z)$, then
\[
|z|=1
\iff
|w-1|=|w|
\iff
\operatorname{Re}w=\frac12,
\]
and
\[
|z-1/2|=1/2
\iff
|w-2|=|w|
\iff
\operatorname{Re}w=1.
\]
Testing, for example, $z=-1/2\in\Omega$ shows that
\[
T(\Omega)=\left\{\frac12<\operatorname{Re}w<1\right\}.
\]

Now
\[
E(w)=\exp\bigl(2\pi i(w-1/2)\bigr)
\]
maps this vertical strip biholomorphically onto the upper half-plane: its
argument ranges from $0$ to $\pi$, and its real period is $1$, larger than the
strip width $1/2$. Finally the Cayley map
\[
C(\zeta)=\frac{\zeta-i}{\zeta+i}
\]
maps the upper half-plane biholomorphically onto $\mathbb D$.

Therefore one required conformal map is
\[
\boxed{
z\longmapsto
\frac{
\exp\!\left(2\pi i\left(\frac1{1-z}-\frac12\right)\right)-i
}{
\exp\!\left(2\pi i\left(\frac1{1-z}-\frac12\right)\right)+i
}.}
\]
:::
