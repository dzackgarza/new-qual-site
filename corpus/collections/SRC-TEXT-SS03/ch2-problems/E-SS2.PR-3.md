---
schema: qual/card@1
id: E-SS2.PR-3
kind: exercise
title: "SS 2.PR-3: Morera's theorem for circles and toy contours"
classification:
  areas:
  - complex-analysis
  topics:
  - Morera
  - Contour Integration
relations: []
review: draft
---

::: exercise
3. Morera’s theorem states that if f is continuous in $\mathbb { C } .$ and $\textstyle \int _ { T } f ( z ) d z = 0$ for all triangles T , then f is holomorphic in C. Naturally, we may ask if the conclusion still holds if we replace triangles by other sets.

(a) Suppose that f is continuous on $\mathbb { C } .$ and

$$
\int_ {C} f (z) d z = 0\tag{16}
$$

for every circle C. Prove that f is holomorphic.

(b) More generally, let Γ be any toy contour, and $\mathcal { F }$ the collection of all trans lates and dilates of Γ. Show that if f is continuous on $\mathbb { C } .$ and

$$
\int_ {\gamma} f (z) d z = 0 \quad \text { for   all } \gamma \in \mathcal {F}
$$

then $f$ is holomorphic.
In particular, Morera’s theorem holds under the weaker assumption that $\begin{array} { r } { \int _ { T } f ( z ) d z = 0 } \end{array}$ for all equilateral triangles.

[Hint: As a first step, assume that f is twice real diferentiable, and write $f ( z ) =$ $f ( z _ { 0 } ) + a ( z - z _ { 0 } ) + b ( \overline { { z - z _ { 0 } } } ) + O ( | z - z _ { 0 } | ^ { 2 } )$ for z near $z _ { \mathrm { 0 } }$ . Integrating this expansion over small circles around z<sub>0</sub> yields $\partial f / \partial { \overline { { z } } } = b = 0$ at $z _ { 0 }$ . Alternatively, suppose only that $f$ is diferentiable and apply Green’s theorem to conclude that the real and imaginary parts of f satisfy the Cauchy-Riemann equations.

In general, let $\varphi ( w ) = \varphi ( x , y )$ (when $w = x + i y )$ denote a smooth function with $0 \leq \varphi ( w ) \leq 1$ , and $\begin{array} { r } { \int _ { \mathbb { R } ^ { 2 } } \varphi ( w ) d V ( w ) = 1 } \end{array}$ , where $d V ( w ) = d x d y .$ and $\scriptstyle \int$ denotes the usual integral of a function of two variables in $\mathbb { R } ^ { 2 }$ . For each $\epsilon > 0$ , let $\varphi _ { \epsilon } ( z ) =$ $\epsilon ^ { - 2 } \varphi ( \epsilon ^ { - 1 } z )$ , as well as

$$
f _ {\epsilon} (z) = \int_ {\mathbb {R} ^ {2}} f (z - w) \varphi_ {\epsilon} (w) d V (w),
$$

where the integral denotes the usual integral of functions of two variables, with $d V ( w )$ the area element of $\mathbb { R } ^ { 2 }$ . Then $f _ { \epsilon }$ is smooth, satisfies condition (16), and $f _ { \epsilon }  f$ uniformly on any compact subset of C.]
:::
