---
schema: qual/card@1
id: P-CASP19F
kind: problem
title: "Analytic function on the punctured disk vanishing on a boundary arc is identically zero"
classification:
  areas:
  - complex-analysis
  topics:
  - Identity Theorem
  - Analytic Continuation
  - Boundary Values
relations: []
review: draft
---

::: problem
Let $f$ be a continuous function on $\{z \in \mathbb{C} : 0 < |z| \leq 1\}$ that is analytic on $\{z \in \mathbb{C} : 0 < |z| < 1\}$.
Assume $f(z) = 0$ for every $z = e^{i\theta}$ with $\frac{\pi}{4} < \theta < \frac{\pi}{3}$.
Prove $f \equiv 0$.
:::

::: solution
Choose a closed subarc
\[
S_0=\{e^{i\theta}:\alpha\le\theta\le\beta\}
\subset
\{e^{i\theta}:\pi/4<\theta<\pi/3\}.
\]
Because $f$ is continuous up to the unit circle and vanishes on this arc,
extend $f$ by $0$ across $S_0$ to a small annular neighborhood outside the
unit disk. More precisely, define the extension to equal $f$ on the inside and
$0$ on the outside.

The extension is continuous across $S_0$. Morera's theorem shows it is
holomorphic across the arc: for any sufficiently small triangle crossing the
arc, split the triangle along the arc. The integral on the outer portion is
zero, while the integral on the inner portion is zero by Cauchy's theorem; the
common boundary contribution along the arc vanishes because the boundary value
is $0$.

The extended holomorphic function vanishes on an open set outside the disk, so
the identity theorem makes it vanish in a neighborhood of $S_0$. Thus the
original $f$ vanishes on a nonempty open subset of the punctured disk. Since
$0<|z|<1$ is connected, the identity theorem gives
\[
\boxed{f\equiv0}.
\]
:::
