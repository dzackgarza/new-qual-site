---
schema: qual/card@1
id: P-CAF13G
kind: problem
title: "A holomorphic function on the upper half-plane vanishing on a boundary interval is zero"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Suppose $f \in \operatorname{Hol}(\mathbb{C}_+)$ has the property that, for any sequence $z_n$ in $\mathbb{C}_+$ that converges to a point in $(0, 1)$, $f(z_n) \to 0$.
Prove that $f \equiv 0$ on $\mathbb{C}_+$.
:::

::: solution
The sequential hypothesis says precisely that $f$ extends continuously to the
interval $(0,1)$ by setting
\[
f(x)=0\qquad(0<x<1).
\]
These boundary values are real. By the Schwarz reflection principle, for each
$x_0\in(0,1)$ the function extends holomorphically across a small interval
about $x_0$, with reflected values
\[
F(z)=\overline{f(\overline z)}
\]
in the lower half-plane.

The resulting holomorphic extension vanishes at every point of a real interval.
By the identity theorem it is identically zero in a neighborhood of that
interval. Hence $f$ vanishes on a nonempty open subset of $\mathbb C_+$, and a
second application of the identity theorem on the connected upper half-plane
gives
\[
f\equiv0.
\]
:::
