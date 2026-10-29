---
schema: qual/card@1
id: P-CAF13E
kind: problem
title: "Conformal bijections involving half-planes, slits, and Möbius transformations"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
(a) Prove that the function $f(z) = \left(\frac{1 + \sqrt{z}}{1 - \sqrt{z}}\right)^2$ is a conformal bijection mapping $\CC_-$ onto $\mathbb{D} \setminus [0, 1)$.

(b) Let $f(z) = \frac{az + b}{cz + d}$ with $a, b, c, d \in \RR$ and $ad - bc < 0$.
Show that $f$ is a conformal bijection from $\CC_+$ onto $\CC_-$.
:::

::: {.remark}
The official Fall 2013 UCSD exam has $\CC_-$ in part (a). An earlier
transcription of this card incorrectly had $\CC_+$.
:::

::: {.solution}
For part (a), use on $\CC_-$ the square-root branch determined by
\[
\pi<\arg z<2\pi,
\qquad
\sqrt z=|z|^{1/2}e^{i\arg z/2}.
\]
This maps $\CC_-$ conformally onto the second quadrant
\[
Q=\{w:\operatorname{Re}w<0,\ \operatorname{Im}w>0\}.
\]
The Möbius map
\[
M(w)=\frac{1+w}{1-w}
\]
maps $Q$ conformally onto the upper half of the unit disk. Indeed, the negative
real boundary ray maps to $(-1,1)$, the positive imaginary boundary ray maps to
the upper unit semicircle, and for $\operatorname{Re}w<0$ one has
$|1+w|<|1-w|$. Finally, squaring maps the upper half-disk conformally onto
\[
\mathbb D\setminus[0,1),
\]
because it doubles arguments from $(0,\pi)$ to $(0,2\pi)$. The composition is
exactly
\[
z\longmapsto\left(\frac{1+\sqrt z}{1-\sqrt z}\right)^2,
\]
so this is the required conformal bijection.

For part (b), let
\[
T(z)=\frac{az+b}{cz+d},
\qquad a,b,c,d\in\RR,\quad ad-bc<0.
\]
Its derivative is
\[
T'(z)=\frac{ad-bc}{(cz+d)^2},
\]
so it is conformal away from its real pole. A direct computation gives
\[
\operatorname{Im}T(z)
=\frac{(ad-bc)\operatorname{Im}z}{|cz+d|^2}.
\]
Thus $\operatorname{Im}z>0$ implies $\operatorname{Im}T(z)<0$. Since a real
Möbius transformation is a bijection of the Riemann sphere preserving the real
circle, it maps one of the two complementary half-planes bijectively onto the
other; the sign calculation shows that $\CC_+$ maps onto $\CC_-$.
:::
