---
schema: qual/card@1
id: E-SS2.PR-3
kind: problem
title: Morera's theorem for circles and toy contours
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

::: {.exercise}
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

[Hint: As a first step, assume that f is twice real diferentiable, and write $f ( z ) =$ $f ( z _ { 0 } ) + a ( z - z _ { 0 } ) + b ( \overline { { z - z _ { 0 } } } ) + O ( | z - z _ { 0 } | ^ { 2 } )$ for z near $z _ { \mathrm { 0 } }$ . Integrating this expansion over small circles around $z_0$ yields $\partial f / \partial { \overline { { z } } } = b = 0$ at $z _ { 0 }$ . Alternatively, suppose only that $f$ is diferentiable and apply Green’s theorem to conclude that the real and imaginary parts of f satisfy the Cauchy-Riemann equations.

In general, let $\varphi ( w ) = \varphi ( x , y )$ (when $w = x + i y )$ denote a smooth function with $0 \leq \varphi ( w ) \leq 1$ , and $\begin{array} { r } { \int _ { \mathbb { R } ^ { 2 } } \varphi ( w ) d V ( w ) = 1 } \end{array}$ , where $d V ( w ) = d x d y .$ and $\scriptstyle \int$ denotes the usual integral of a function of two variables in $\mathbb { R } ^ { 2 }$ . For each $\epsilon > 0$ , let $\varphi _ { \epsilon } ( z ) =$ $\epsilon ^ { - 2 } \varphi ( \epsilon ^ { - 1 } z )$ , as well as

$$
f _ {\epsilon} (z) = \int_ {\mathbb {R} ^ {2}} f (z - w) \varphi_ {\epsilon} (w) d V (w),
$$

where the integral denotes the usual integral of functions of two variables, with $d V ( w )$ the area element of $\mathbb { R } ^ { 2 }$ . Then $f _ { \epsilon }$ is smooth, satisfies condition (16), and $f _ { \epsilon }  f$ uniformly on any compact subset of C.]
:::

::: {.solution}
<1>1. If $f$ is $C^2$ and $\int_C f\,dz=0$ for every circle $C$, then $f$ is holomorphic.

::: {.proof}
Near $z_0$ write $f(z)=f(z_0)+a(z-z_0)+b\,\overline{(z-z_0)}+O(|z-z_0|^2)$ with $b=\partial f/\partial\overline z(z_0)$. On $\abs{z-z_0}=r$ the constant and $a(z-z_0)$ integrate to $0$, the error term integrates to $O(r^3)$, and $\int_{|z-z_0|=r}\overline{(z-z_0)}\,dz=2\pi i r^2$. Hence $0=2\pi i b r^2+O(r^3)$, so $b=0$. As $z_0$ is arbitrary, $\partial f/\partial\overline z=0$ and $f$ is holomorphic.
:::

<1>2. (a) If $f$ is continuous and $\int_C f\,dz=0$ for every circle $C$, then $f$ is holomorphic.

::: {.proof}
With $\varphi_\epsilon$ as in the hint, $f_\epsilon(z)=\int_{\mathbb R^2}f(z-w)\varphi_\epsilon(w)\,dV(w)$ is smooth, and $f_\epsilon\to f$ uniformly on compact sets. For a circle $C$, Fubini's theorem gives $\int_C f_\epsilon\,dz=\int_{\mathbb R^2}\bigl(\int_{C-w}f\,dz\bigr)\varphi_\epsilon(w)\,dV(w)=0$, since $C-w$ is again a circle. By step <1>1 each $f_\epsilon$ is holomorphic, and a locally uniform limit of holomorphic functions is holomorphic.
:::

<1>3. (b) If $\int_\gamma f\,dz=0$ for all translates and dilates $\gamma$ of a toy contour $\Gamma$, then $f$ is holomorphic.

::: {.proof}
Since $\mathcal F$ is closed under translation, the Fubini argument of step <1>2 shows that each $f_\epsilon$ also satisfies $\int_\gamma f_\epsilon\,dz=0$ for all $\gamma\in\mathcal F$; so, as in step <1>2, it suffices to treat smooth $f$. For smooth $f$, Green's theorem on the interior $U$ of $\Gamma$, which has positive area $\abs U$, gives for $\gamma=z_0+\delta\Gamma$
$$0=\int_\gamma f\,dz=\pm2i\iint_{z_0+\delta U}\frac{\partial f}{\partial\overline z}\,dA=\pm2i\,\delta^2\iint_U\frac{\partial f}{\partial\overline z}(z_0+\delta w)\,dA(w),$$
the sign depending on the orientation of $\Gamma$. Dividing by $\delta^2$ and letting $\delta\to0$ gives $\abs U\,\frac{\partial f}{\partial\overline z}(z_0)=0$. Hence $\partial f/\partial\overline z=0$ everywhere and $f$ is holomorphic.
:::

<1>4. Morera's theorem holds when $\int_T f\,dz=0$ is assumed only for equilateral triangles $T$.

::: {.proof}
Take $\Gamma$ to be an equilateral triangle; then $\mathcal F$ consists of the equilateral triangles with the orientation of $\Gamma$, and step <1>3 applies.
:::
:::
