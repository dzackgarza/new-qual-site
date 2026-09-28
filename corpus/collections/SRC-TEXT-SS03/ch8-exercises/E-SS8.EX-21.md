---
schema: qual/card@1
id: E-SS8.EX-21
kind: problem
title: "We consider conformal mappings to triangles"
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
21. We consider conformal mappings to triangles.

(a) Show that

$$
\int_ {0} ^ {z} z ^ {- \beta_ {1}} (1 - z) ^ {- \beta_ {2}} d z,
$$

with $0 < \beta _ { 1 } < 1 , \ 0 < \beta _ { 2 } < 1$ , and $1 < \beta _ { 1 } + \beta _ { 2 } < 2$ , maps $\mathbb { H }$ to a triangle whose vertices are the images of 0, 1, and $\infty ;$ , and with angles $\alpha _ { 1 } \pi$ , α<sub>2</sub>π, and $\alpha _ { 3 } \pi _ { \ i }$ where $\alpha _ { j } + \beta _ { j } = 1$ and $\beta _ { 1 } + \beta _ { 2 } + \beta _ { 3 } = 2$

(b) What happens when $\beta _ { 1 } + \beta _ { 2 } = 1 ?$

(c) What happens when $0 < \beta _ { 1 } + \beta _ { 2 } < 1 ?$

(d) In (a), the length of the side of the triangle opposite angle $\alpha _ { j } \pi$ is $\begin{array} { r l } {  { \frac { \sin ( \alpha _ { j } \pi ) } { \pi } \Gamma ( \alpha _ { 1 } ) \Gamma ( \alpha _ { 2 } ) \Gamma ( \alpha _ { 3 } ) } } \end{array}$
:::

::: {.solution}
Let
\[
F(z)=\int_0^z \zeta^{-\beta_1}(1-\zeta)^{-\beta_2}\,d\zeta
\]
with branches chosen holomorphically on $\mathbb H$. At the finite prevertices $0$ and $1$, the Schwarz--Christoffel exponents are $-\beta_1$ and $-\beta_2$, hence the interior angles are
\[
\alpha_1\pi=(1-\beta_1)\pi,
\qquad
\alpha_2\pi=(1-\beta_2)\pi.
\]
Near infinity,
\[
F'(z)\sim C z^{-(\beta_1+\beta_2)}.
\]
Under $w=1/z$ this becomes
\[
\frac d{dw}F(1/w)\sim C' w^{\beta_1+\beta_2-2}=C'w^{-\beta_3},
\qquad
\beta_3=2-\beta_1-\beta_2.
\]
Thus the angle at the image of infinity is
\[
\alpha_3\pi=(1-\beta_3)\pi=(\beta_1+\beta_2-1)\pi.
\]
When $1<\beta_1+\beta_2<2$, all three $\alpha_j$ lie in $(0,1)$ and sum to $1$, so the image is a triangle with precisely these angles.

If $\beta_1+\beta_2=1$, then $\alpha_3=0$. The two sides issuing toward infinity become parallel and the image is an infinite strip-type degenerate triangle; analytically, $F(z)=C\log z+O(1)$ at infinity.

If $0<\beta_1+\beta_2<1$, then $F(z)\sim C z^{1-\beta_1-\beta_2}$ at infinity, so the two boundary rays separate by the angle $(1-\beta_1-\beta_2)\pi$. The image is an unbounded polygonal region with the finite angles $(1-\beta_1)\pi$ and $(1-\beta_2)\pi$ and an exterior vertex at infinity rather than a bounded triangle.

For part (d), the side opposite $\alpha_3\pi$ is the image of $[0,1]$, so its length is
\[
L_3=\int_0^1 x^{-\beta_1}(1-x)^{-\beta_2}\,dx
=B(\alpha_1,\alpha_2)
=\frac{\Gamma(\alpha_1)\Gamma(\alpha_2)}{\Gamma(\alpha_1+\alpha_2)}.
\]
Since $\alpha_1+\alpha_2=1-\alpha_3$, Euler reflection gives
\[
\frac1{\Gamma(1-\alpha_3)}
=\frac{\sin(\pi\alpha_3)}{\pi}\Gamma(\alpha_3),
\]
so
\[
L_3=\frac{\sin(\pi\alpha_3)}{\pi}
\Gamma(\alpha_1)\Gamma(\alpha_2)\Gamma(\alpha_3).
\]
The same argument after permuting the three prevertices gives, for each $j$,
\[
L_j=\frac{\sin(\pi\alpha_j)}{\pi}
\Gamma(\alpha_1)\Gamma(\alpha_2)\Gamma(\alpha_3).
\]
:::
