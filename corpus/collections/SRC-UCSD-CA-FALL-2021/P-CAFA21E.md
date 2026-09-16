---
schema: qual/card@1
id: P-CAFA21E
kind: problem
title: "Biholomorphism to a strip and unbounded harmonic function"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $G = \{ z = x+iy : x > 0,\, y > 0,\, xy < 1 \}$.

(i) Construct a biholomorphism between $G$ and the strip $S = \{ z = x+iy : 0 < y < 1 \}$.

(ii) Construct an unbounded continuous function $u : \overline{G} \to \mathbb{R}$, harmonic in $G$, and such that $u$ vanishes on $\partial G$.
:::

::: {.solution}
(i) The map
\[
\Phi(z)=\frac{z^2}{2}
\]
is biholomorphic from $G$ onto
\[
S=\{w:0<\operatorname{Im}w<1\}.
\]
Indeed, if $z=x+iy\in G$, then
\[
\operatorname{Im}\Phi(z)=xy\in(0,1).
\]
Conversely, every $w\in S$ lies in the upper half-plane, so its principal
square root has positive real and imaginary parts; for
$z=\sqrt{2w}$ we have $xy=\operatorname{Im}w<1$. This gives the inverse.

(ii) On the strip, the function
\[
U(w)=e^{\pi\operatorname{Re}w}\sin(\pi\operatorname{Im}w)
\]
is harmonic, continuous on the closed strip, vanishes on both boundary lines,
and is unbounded. Pulling back by $\Phi$ gives
\[
\boxed{\displaystyle
u(x+iy)=e^{\frac\pi2(x^2-y^2)}\sin(\pi xy).}
\]
It is continuous on $\overline G$, harmonic in $G$, and vanishes on the three
boundary pieces $x=0$, $y=0$, and $xy=1$. It is unbounded, for example along
$y=1/(2x)$ as $x\to\infty$.
:::
