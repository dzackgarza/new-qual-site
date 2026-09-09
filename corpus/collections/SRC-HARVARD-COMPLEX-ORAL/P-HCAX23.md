---
schema: qual/card@1
id: P-HCAX23
kind: problem
title: Conformal automorphisms of the upper half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Mobius Transformations
relations: []
review: draft
---

::: problem
Determine all conformal automorphisms of the upper half-plane.
:::

::: solution
Let
\[
\mathbb H=\{z\in\mathbb C:\operatorname{Im}z>0\}.
\]
The conformal automorphisms of $\mathbb H$ are exactly the real Möbius transformations
\[
\boxed{
z\longmapsto \frac{az+b}{cz+d},
\qquad a,b,c,d\in\mathbb R,
\quad ad-bc>0,}
\]
where multiplying $a,b,c,d$ by a common nonzero real scalar does not change the map. Thus
\[
\operatorname{Aut}(\mathbb H)\cong PSL_2(\mathbb R).
\]

First, every such transformation preserves $\mathbb H$, because for $z\in\mathbb H$,
\[
\operatorname{Im}\frac{az+b}{cz+d}
=\frac{(ad-bc)\operatorname{Im}z}{|cz+d|^2}>0.
\]
Its inverse is again a real Möbius transformation with positive determinant, so it is an automorphism of $\mathbb H$.

Conversely, let $F\in\operatorname{Aut}(\mathbb H)$. The Cayley transform
\[
C(z)=\frac{z-i}{z+i}
\]
is a conformal isomorphism from $\mathbb H$ to $\mathbb D$. Hence
\[
C\circ F\circ C^{-1}\in\operatorname{Aut}(\mathbb D).
\]
By the classification of disk automorphisms, this conjugate is Möbius, so $F$ is Möbius as well. Since $F$ maps the boundary circle $\mathbb R\cup\{\infty\}$ to itself, its coefficients may be scaled to be real. The condition that $F$ sends the upper, rather than lower, half-plane to itself is exactly $ad-bc>0$ by the displayed imaginary-part formula. This gives the stated classification.
:::
