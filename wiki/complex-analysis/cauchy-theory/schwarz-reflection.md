---
title: Schwarz reflection
order: 70
topics:
- Schwarz Reflection
- Reflection Principle
---

# Schwarz reflection

A holomorphic function on the upper half of a symmetric region that is real on the real axis extends to the whole region by reflection.
The proof glues two holomorphic functions along a segment and applies Morera's theorem.

::: {.remark}
Throughout, $\Omega$ is an open set symmetric about the real axis, so $z\in \Omega \iff \bar{z} \in \Omega$, and $\Omega^+ \coloneqq \Omega\cap\ts{\Im z>0}$, $I\coloneqq\Omega\cap\RR$, and $\Omega^- \coloneqq \Omega\cap\ts{\Im z<0}$.

:::

## The symmetry principle

[[T-5SKNT]]

::: {.proof title="Symmetry principle, by Morera"}
The glued function $f$ is holomorphic on $\Omega^\pm$ by hypothesis, so it remains to check holomorphy along $I$.
Let $T\subset\Omega$ be a closed triangle.
If $T$ misses $I$, then $T$ lies in $\Omega^+$ or in $\Omega^-$ and $\int_{\partial T} f=0$ by Goursat.

If $T$ meets $I$, let $T^+\coloneqq T\cap\ts{\Im z\geq 0}$ and $T^-\coloneqq T\cap\ts{\Im z\leq 0}$, convex polygons with positively oriented boundaries.
The boundaries share the segment $T\cap\RR$ with opposite orientations, so $\int_{\partial T} f = \int_{\partial T^+} f + \int_{\partial T^-} f$.
For small $\varepsilon>0$, the convex polygon $T^+_\varepsilon \coloneqq T^+\cap\ts{\Im z\geq\varepsilon}$ lies in $\Omega^+$, so $\int_{\partial T^+_\varepsilon} f = 0$ by Goursat's theorem applied to a triangulation of $T^+_\varepsilon$.
As $\varepsilon\to 0$ the boundaries $\partial T^+_\varepsilon$ converge to $\partial T^+$, and since $f$ is uniformly continuous on the compact set $T$, $\int_{\partial T^+} f = \lim_{\varepsilon\to 0}\int_{\partial T^+_\varepsilon} f = 0$; likewise $\int_{\partial T^-} f=0$.
Thus $\int_{\partial T} f=0$, and Morera's theorem gives holomorphy on $\Omega$.

:::

## The reflection

[[T-Q3GGF]]

::: {.proof title="Schwarz reflection"}
Define $F(z)\coloneqq f(z)$ for $z\in \Omega^+\cup I$, and $F(z)\coloneqq \overline{f(\bar z)}$ for $z\in \Omega^-$.
On $\Omega^-$ the difference quotient is
$$
\frac{F(z+h)-F(z)}{h}
= \overline{\frac{f(\bar z+\bar h)-f(\bar z)}{\bar h}}
,$$
using $\overline{A}/h = \overline{A/\bar h}$.
As $h\to 0$ we have $\bar h\to 0$, so $F'(z)=\overline{f'(\bar z)}$ and $F$ is holomorphic on $\Omega^-$.
On $I$ the function $f$ is real valued, so $\overline{f(\bar x)}=\overline{f(x)}=f(x)$ for $x\in I$, and $\overline{f(\bar z)}\to f(x)$ as $z\to x$ from $\Omega^-$.
Thus $F$ is continuous on $\Omega$, its restrictions to $\Omega^\pm$ are holomorphic, and the symmetry principle [[T-5SKNT]] gives holomorphy on $\Omega$.

:::

::: {.remark}
Composing with Möbius transformations in the domain and the target, the same argument extends a function holomorphic on one side of a line segment or circular arc and continuous up to it, with boundary values on a line or circle, by reflection in the arc and in the target line or circle.

:::

::: {.example title="The real-valued hypothesis is used"}
The constant function $f(z) = i$ on $\Omega^+$ is continuous up to $I$ but not real valued there.
Its reflection is $\overline{f(\bar z)} = -i$ on $\Omega^-$, and the glued function is discontinuous on $I$.

:::
