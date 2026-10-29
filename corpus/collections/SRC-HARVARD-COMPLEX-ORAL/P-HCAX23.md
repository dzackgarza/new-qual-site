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

::: {.problem}
Determine all conformal automorphisms of the upper half-plane.
:::

::: {.solution}
Let
$$
\halfplane=\{z\in\CC:\operatorname{Im}z>0\}.
$$
The conformal automorphisms of $\halfplane$ are exactly the real Möbius transformations
$$
\boxed{
z\longmapsto \frac{az+b}{cz+d},
\qquad a,b,c,d\in\RR,
\quad ad-bc>0,}
$$
where multiplying $a,b,c,d$ by a common nonzero real scalar does not change the map. Thus
$$
\operatorname{Aut}(\halfplane)\cong PSL_2(\RR).
$$

First, every such transformation preserves $\halfplane$, because for $z\in\halfplane$,
$$
\operatorname{Im}\frac{az+b}{cz+d}
=\frac{(ad-bc)\operatorname{Im}z}{|cz+d|^2}>0.
$$
Its inverse is again a real Möbius transformation with positive determinant, so it is an automorphism of $\halfplane$.

Conversely, let $F\in\operatorname{Aut}(\halfplane)$. The Cayley transform
$$
C(z)=\frac{z-i}{z+i}
$$
is a conformal isomorphism from $\halfplane$ to $\DD$. Hence
$$
C\circ F\circ C^{-1}\in\operatorname{Aut}(\DD).
$$
By the classification of disk automorphisms, this conjugate is Möbius, so $F$ is Möbius as well. Since $F$ maps the boundary circle $\RR\cup\{\infty\}$ to itself, its coefficients may be scaled to be real. The condition that $F$ sends the upper, rather than lower, half-plane to itself is exactly $ad-bc>0$ by the displayed imaginary-part formula. This gives the stated classification.
:::
