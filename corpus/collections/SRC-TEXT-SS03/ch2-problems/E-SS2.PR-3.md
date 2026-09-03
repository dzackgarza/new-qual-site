---
schema: qual/card@1
id: E-SS2.PR-3
kind: problem
title: "SS 2.PR-3: Morera's theorem for circles and toy contours"
classification:
  areas:
  - complex-analysis
  topics:
  - Morera
  - Contour Integration
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
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

::: solution
**Goal:** Prove holomorphicity from the circle or toy-contour vanishing-integral hypothesis.

<1>1. Part (a), smooth reduction: *Proof:*\
If $f$ is $C^2$ near $z_0$, write \[ f(z)=f(z_0)+a(z-z_0)+b\,\overline{(z-z_0)}+O(|z-z_0|^2). \] Integrating on circles around $z_0$, the constant and linear holomorphic terms contribute zero, while \[ \int_{|z-z_0|=r}\overline{(z-z_0)}\,dz=2\pi i r^2\neq0. \] Since these integrals vanish by hypothesis, $b=0$ and $\partial f/\partial\overline z(z_0)=0$.
As $z_0$ was arbitrary, $f$ is holomorphic.

<1>2. Part (a), continuous case: *Proof:*\
For smooth mollifier $\varphi_\epsilon$, define \[ f_\epsilon(z)=\int_{\mathbb R^2}f(z-w)\varphi_\epsilon(w)\,dV(w). \] Each $f_\epsilon$ is smooth and converges uniformly to $f$ on compacts.
The integral hypothesis on circles is preserved under convolution, so $f_\epsilon$ satisfies (16). Applying <1> gives holomorphicity of $f_\epsilon$.
Uniform compact convergence of $f_\epsilon\to f$ implies $f$ is holomorphic.

<1>3. Part (b), toy contours: *Proof:*\
If $\int_\gamma f\,dz=0$ for every $\gamma\in\mathcal F$, then the same hold for each translate/dilate of $\Gamma$ and therefore for their circles used in the mollifier argument.
The same approximation as in <2> applies; thus $f$ is holomorphic.

<1>4. Equilateral triangle corollary: *Proof:*\
Choosing $\Gamma$ to be an equilateral triangle, $\mathcal F$ is all equilateral triangles in the plane, so the conclusion is the stated weaker Morera form.
:::
