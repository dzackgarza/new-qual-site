---
schema: qual/card@1
id: E-SS8.PR-1
kind: problem
title: "Isogonality and isotropy at a point"
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
1. Let $f$ be a complex-valued $C ^ { 1 }$ function defined in the neighborhood of a point $z _ { \mathrm { 0 } }$ . There are several notions closely related to conformality at $z _ { 0 }$ . We say that $f$ is isogonal at $z _ { 0 }$ if whenever $\gamma ( t )$ and $\eta ( t )$ are two smooth curves with $\gamma ( 0 ) =$ $\eta ( 0 ) = z _ { 0 }$ , that make an angle θ there $( | \theta | < \pi )$ , then $f ( \gamma ( t ) )$ and $f ( \eta ( t ) )$ make an angle of $\theta ^ { \prime }$ at $t = 0$ with $| \theta ^ { \prime } | = | \theta |$ for all θ. Also, $f$ is said to be isotropic if it magnifies lengths by some factor for all directions emanating from $z _ { 0 }$ , that is, if the limit

$$
\lim _ {r \to 0} \frac {| f (z _ {0} + r e ^ {i \theta}) - f (z _ {0}) |}{r}
$$

exists, is non-zero, and independent of $\theta .$

Then $f$ is isogonal at $z _ { 0 }$ if and only if it is isotropic at $z _ { \mathrm { 0 } } ;$ moreover, $f$ is isogonal at $z _ { 0 }$ if and only if either $f ^ { \prime } ( z _ { 0 } )$ exists and is non-zero, or the same holds for $f$ replaced by ${ \overline { { f } } } .$
:::

::: {.solution}
Let $A=Df(z_0):\mathbb R^2\to\mathbb R^2$ be the real differential. For a unit vector $v=e^{i\theta}$,
\[
f(z_0+rv)-f(z_0)=rAv+o(r),
\]
so
\[
\lim_{r\to0}\frac{|f(z_0+rv)-f(z_0)|}{r}=|Av|.
\]
Thus $f$ is isotropic at $z_0$ exactly when there is a number $\lambda>0$ such that
\[
|Av|=\lambda|v|\qquad(v\in\mathbb R^2).
\tag{1}
\]
By polarization, (1) is equivalent to
\[
\langle Av,Aw\rangle=\lambda^2\langle v,w\rangle
\]
for all $v,w$, or equivalently
\[
A^TA=\lambda^2I.
\tag{2}
\]
Hence $A=\lambda Q$ with $Q\in O(2)$. Such a map preserves the absolute value of every angle, so isotropy implies isogonality.

Conversely, suppose $f$ is isogonal. Then $A$ cannot kill a nonzero direction, since otherwise the image tangent direction of a curve with that tangent would be undefined. Choose orthonormal vectors $e_1,e_2$. Isogonality gives $Ae_1\perp Ae_2$. Applying it also to the pair $e_1+e_2,e_1-e_2$, which are perpendicular, yields
\[
0=\langle A(e_1+e_2),A(e_1-e_2)\rangle
=|Ae_1|^2-|Ae_2|^2.
\]
Thus $|Ae_1|=|Ae_2|=\lambda>0$, and since their images are orthogonal, (2) follows. Therefore $f$ is isotropic.

It remains to identify the two possibilities for $A$. Every $Q\in O(2)$ has determinant $1$ or $-1$. If $\det Q=1$, then $Q$ is rotation by some angle and, after identifying $\mathbb R^2$ with $\mathbb C$,
\[
Av=cv
\]
for some $c\in\mathbb C\setminus\{0\}$. Hence the complex derivative $f'(z_0)$ exists and equals $c$.

If $\det Q=-1$, then $Q$ is a rotation followed by reflection, so
\[
Av=c\overline v
\]
for some $c\ne0$. Equivalently,
\[
D\overline f(z_0)(v)=\overline c\,v,
\]
so $\overline f$ has a nonzero complex derivative at $z_0$.

Conversely, either of these two differential forms is a nonzero similarity and therefore preserves absolute angles and magnifies every direction by the same factor. Thus the three stated conditions are equivalent.
:::
