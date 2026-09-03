---
schema: qual/card@1
id: E-SS8.PR-2
kind: problem
title: "The angle between two non-zero complex numbers z and  (taken in that order) is s"
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: exercise
2. The angle between two non-zero complex numbers z and $w$ (taken in that order) is simply the oriented angle, in $( - \pi , \pi ]$ , that is formed between the two vectors in $\mathbb { R } ^ { 2 }$ corresponding to the points z and w. This oriented angle, say $\alpha ,$ is uniquely determined by the two quantities

$$
\frac {(z , w)}{| z | | w |} \quad \mathrm{and} \quad \frac {(z , - i w)}{| z | | w |}
$$

which are simply the cosine and sine of $\alpha ,$ respectively.
Here, the notation $( \cdot , \cdot )$ corresponds to the usual Euclidian inner product in $\mathbb { R } ^ { 2 }$ , which in terms of complex numbers takes the form $( z , w ) = \operatorname { R e } ( z { \overline { { w } } } )$

In particular, we may now consider two smooth curves $\gamma : [ a , b ]  \mathbb { C }$ and $\eta :$ $[ a , b ] \to \mathbb { C }$ that intersect at $z _ { 0 }$ , say $\gamma ( t _ { 0 } ) = \eta ( t _ { 0 } ) = z _ { 0 }$ , for some $t _ { 0 } \in ( a , b )$ . If the quantities $\gamma ^ { \prime } ( t _ { 0 } )$ and $\eta ^ { \prime } ( t _ { 0 } )$ are non-zero, then they represent the tangents to the curves $\gamma$ and $\eta$ at the point $z _ { 0 }$ , and we say that the two curves intersect at $z _ { 0 }$ at the angle formed by the two vectors $\gamma ^ { \prime } ( t _ { 0 } )$ and $\eta ^ { \prime } ( t _ { 0 } )$

A holomorphic function $f$ defined near $z _ { 0 }$ is said to preserve angles at $z _ { 0 }$ if for any two smooth curves $\gamma$ and $\eta$ intersecting at $z _ { 0 }$ , the angle formed between the curves $\gamma$ and $\eta$ at $z _ { \mathrm { 0 } }$ equals the angle formed between the curves $f \circ \gamma$ and $f \circ \eta$ at $f ( z _ { 0 } )$ . (See Figure 12 for an illustration.)
In particular, we assume that the tangents to the curves $\gamma , \eta , f \circ \gamma$ , and $f \circ \eta$ at the point $z _ { 0 }$ and $f ( z _ { 0 } )$ are all non-zero.

Figure 12. Preservation of angles at $z _ { \mathrm { 0 } }$

(a) Prove that if $f : \Omega \to \mathbb { C }$ is holomorphic, and $f ^ { \prime } ( z _ { 0 } ) \neq 0$ , then $f$ preserves angles at $z _ { \mathrm { 0 } }$ . [Hint: Observe that

$$
(f ^ {\prime} (z _ {0}) \gamma^ {\prime} (t _ {0}), f ^ {\prime} (z _ {0}) \eta^ {\prime} (t _ {0})) = | f ^ {\prime} (z _ {0}) | ^ {2} (\gamma^ {\prime} (t _ {0}), \eta^ {\prime} (t _ {0})). ]
$$

(b) Conversely, prove the following: suppose $f : \Omega \to \mathbb { C }$ is a complex-valued function, that is real-diferentiable at $z _ { 0 } \in \Omega$ , and $J _ { f } ( z _ { 0 } ) \ne 0$ . If f preserves angles at $z _ { \mathrm { 0 } }$ , then $f$ is holomorphic at $z _ { \mathrm { 0 } }$ with $f ^ { \prime } ( z _ { 0 } ) \neq 0$

$\mathbf { 3 . ^ { * } }$ The Schwarz-Pick lemma (see Exercise 13) is the infinitesimal version of an important observation in complex analysis and geometry.

For complex numbers $w \in \mathbb { C }$ and $z \in \mathbb { D }$ we define the hyperbolic length of $w$ at $z$ by

$$
\| w \| _ {z} = \frac {| w |}{1 - | z | ^ {2}},
$$

where $| w |$ and $| z |$ denote the usual absolute values.
This length is sometimes referred to as the Poincar´e metric, and as a Riemann metric it is written as

$$
d s ^ {2} = \frac {| d z | ^ {2}}{(1 - | z | ^ {2}) ^ {2}}.
$$

The idea is to think of $w$ as a vector lying in the tangent space at $z .$ . Observe that for a fixed $w ,$ its hyperbolic length grows to infinity as z approaches the boundary of the disc.
We pass from the infinitesimal hyperbolic length of tangent vectors to the global hyperbolic distance between two points by integration.

(a) Given two complex numbers $z _ { 1 }$ and $z _ { 2 }$ in the disc, we define the hyperbolic distance between them by
:::

::: {.solution}
<1>1. Part (a): Holomorphic functions with non-zero derivative preserve angles:
<2>1. Let $\gamma, \eta$ be smooth curves intersecting at $z_0 = \gamma(t_0) = \eta(t_0)$ with non-zero tangent vectors $v = \gamma'(t_0)$ and $w = \eta'(t_0)$.
The tangent vectors to the image curves $\tilde{\gamma} = f \circ \gamma$ and $\tilde{\eta} = f \circ \eta$ at $f(z_0)$ are:
\[
\tilde{v} = f'(z_0) v \quad \text{and} \quad \tilde{w} = f'(z_0) w.
\]
::: {.proof}
chain rule for complex differentiation.
:::
<2>2. The Euclidean inner product on $\mathbb{R}^2 \cong \mathbb{C}$ is $(z_1, z_2) = \operatorname{Re}(z_1 \bar{z}_2)$.
Compute the inner product of $\tilde{v}$ and $\tilde{w}$:
\[
(\tilde{v}, \tilde{w}) = \operatorname{Re}\big((f'(z_0) v) \overline{(f'(z_0) w)}\big) = \operatorname{Re}\big(|f'(z_0)|^2 v \bar{w}\big) = |f'(z_0)|^2 \operatorname{Re}(v \bar{w}) = |f'(z_0)|^2 (v, w).
\]
::: {.proof}
algebraic properties of complex conjugation and modulus.
:::
<2>3. The norms are $|\tilde{v}| = |f'(z_0)| |v|$ and $|\tilde{w}| = |f'(z_0)| |w|$.
Thus the cosine of the angle $\tilde{\alpha}$ between $\tilde{v}$ and $\tilde{w}$ satisfies:
\[
\cos \tilde{\alpha} = \frac{(\tilde{v}, \tilde{w})}{|\tilde{v}| |\tilde{w}|} = \frac{|f'(z_0)|^2 (v, w)}{|f'(z_0)|^2 |v| |w|} = \frac{(v, w)}{|v| |w|} = \cos \alpha.
\]
::: {.proof}
<2>2 and norm scaling.
:::
<2>4. Similarly, compute the sine of the angle $\tilde{\alpha}$:
\[
(\tilde{v}, -i\tilde{w}) = \operatorname{Re}\big((f'(z_0) v) \overline{(-i f'(z_0) w)}\big) = |f'(z_0)|^2 \operatorname{Re}(v \cdot i \bar{w}) = |f'(z_0)|^2 (v, -iw).
\]
Dividing by $|\tilde{v}| |\tilde{w}|$ yields:
\[
\sin \tilde{\alpha} = \frac{(\tilde{v}, -i\tilde{w})}{|\tilde{v}| |\tilde{w}|} = \frac{(v, -iw)}{|v| |w|} = \sin \alpha.
\]
::: {.proof}
definition of oriented sine.
:::
<2>5. Since $\cos \tilde{\alpha} = \cos \alpha$ and $\sin \tilde{\alpha} = \sin \alpha$, the oriented angle is preserved: $\tilde{\alpha} = \alpha$.
::: {.proof}
angle is uniquely determined in $(-\pi, \pi]$ by its sine and cosine.
:::

<1>2. Part (b): Preservation of oriented angles implies holomorphicity:
<2>1. Let $T = Df(z_0): \mathbb{R}^2 \to \mathbb{R}^2$ be the real total derivative, represented by the Jacobian matrix:
\[
J = \begin{pmatrix} u_x & u_y \\ v_x & v_y \end{pmatrix}, \quad \text{with } \det(J) \neq 0.
\]
::: {.proof}
real differentiability of $f = u + iv$.
:::
<2>2. Since $f$ preserves oriented angles at $z_0$, the linear map $T$ preserves oriented angles between all pairs of non-zero vectors in $\mathbb{R}^2$.
::: {.proof}
tangent mapping of smooth curves.
:::
<2>3. Consider the standard basis $e_1 = (1, 0)^T$ and $e_2 = (0, 1)^T$.
$e_1$ and $e_2$ are orthogonal of equal length with $\det(e_1, e_2) = 1 > 0$.
Thus their images $T e_1 = (u_x, v_x)^T$ and $T e_2 = (u_y, v_y)^T$ must be orthogonal, have equal non-zero length $\lambda > 0$, and satisfy $\det(T e_1, T e_2) > 0$:
\[
u_x u_y + v_x v_y = 0, \qquad u_x^2 + v_x^2 = u_y^2 + v_y^2 = \lambda^2 > 0, \qquad u_x v_y - u_y v_x > 0.
\]
::: {.proof}
preservation of right angles and orientation.
:::
<2>4. Any $2 \times 2$ matrix satisfying these conditions has the form of a positive scalar times a rotation matrix:
\[
J = \begin{pmatrix} a & -b \\ b & a \end{pmatrix} \quad (a, b \in \mathbb{R}, \, a^2 + b^2 = \lambda^2 > 0).
\]
Therefore:
\[
u_x = v_y = a, \qquad u_y = -v_x = -b.
\]
::: {.proof}
classification of orientation-preserving conformal linear maps on $\mathbb{R}^2$.
:::
<2>5. The equations in <2>4 are the **Cauchy–Riemann equations** for $f$ at $z_0$.
Since $f$ is real-differentiable at $z_0$ and satisfies the Cauchy–Riemann equations, $f$ is complex-differentiable (holomorphic) at $z_0$ with:
\[
f'(z_0) = u_x(z_0) + i v_x(z_0) = a + ib \neq 0.
\]
::: {.proof}
complex differentiability characterization via Cauchy–Riemann equations and real differentiability.
:::

<1>3. Conclusion:
$f$ preserves angles if and only if $f$ is holomorphic with $f'(z_0) \neq 0$. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
