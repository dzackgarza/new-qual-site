---
schema: qual/card@1
id: E-CFTRQ
kind: problem
title: Automorphisms of $\CP^1$
classification:
  areas:
  - complex-analysis
  topics:
  - Biholomorphisms
  - Fractional Linear Transformations
  - Riemann Surfaces
relations: []
review: draft
---

::: {.exercise}
Show that
\[
\Aut(\CP^1)
=\left\{z\longmapsto {az+b\over cz+d}:a,b,c,d\in\CC,\ ad-bc\neq0\right\}.
\]
:::

::: {.solution}
Let
\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\GL_2(\CC).
\]
The linear automorphism $A:\CC^2\to\CC^2$ descends to a holomorphic automorphism of projective space
\[
[z_0:z_1]\longmapsto[az_0+bz_1:cz_0+dz_1].
\]
On the affine chart $z=[z:1]$, this is
\[
z\longmapsto\frac{az+b}{cz+d}.
\]
Its inverse is induced by $A^{-1}$, so every fractional linear transformation with $ad-bc\neq0$ lies in $\Aut(\CP^1)$.

Conversely, let $f\in\Aut(\CP^1)$.
By the classification of meromorphic functions on $\CP^1$, write
\[
f(z)=\frac{p(z)}{q(z)}
\]
with coprime polynomials $p,q$, and put
\[
d=\max\{\deg p,\deg q\}.
\]
For every finite value $w$ except possibly the ratio of the leading coefficients when $\deg p=\deg q=d$, the equation
\[
f(z)=w
\]
is equivalent to
\[
p(z)-wq(z)=0,
\]
a polynomial equation of degree $d$.
Hence it has $d$ solutions counted with multiplicity.

Because $f$ is an automorphism, its inverse is holomorphic.
Therefore $f$ has no critical points: in local coordinates,
\[
(f^{-1})'(f(z))f'(z)=1.
\]
Thus every point in every fiber has multiplicity one.
Since $f$ is also injective, a generic fiber contains exactly one point.
Consequently $d=1$.

Therefore $p(z)=az+b$ and $q(z)=cz+d$ for some $a,b,c,d\in\CC$.
The determinant $ad-bc$ is nonzero, since otherwise the two linear polynomials are proportional and $f$ is constant.
Hence $f$ is fractional linear.
:::
