---
title: Schwarz reflection
order: 70
problems:
  topics:
  - Schwarz Reflection
  - Reflection Principle
---

# Schwarz reflection

Extending a holomorphic function across a segment of the real line by reflecting it.
The mechanism is Morera: the glued function has vanishing integrals over triangles that straddle the segment, because the two contributions along the segment cancel.

:::{.remark}
Throughout, $\Omega$ is a region symmetric about the real axis, so $z\in \Omega \iff \bar{z} \in \Omega$, partitioned as $\Omega^+ \subseteq \HH$, $I \subseteq \RR$, and $\Omega^- \subseteq \bar{\HH}$.

:::

## The symmetry principle

[[T-5SKNT]]

:::{.proof title="Symmetry principle, by Morera"}
The glued function $f$ is holomorphic on $\Omega^\pm$ by hypothesis, so it remains to check holomorphy along $I$.
Let $T\subset\Omega$ be a closed triangle.
If $T$ misses $I$, then $T$ lies in $\Omega^+$ or in $\Omega^-$ and $\int_{\partial T} f=0$ by Goursat.

If $T$ meets $I$, split it along $I$ into $T^+\da T\cap\overline{\Omega^+}$ and $T^-\da T\cap\overline{\Omega^-}$.
The two integrals along the segment $T\cap I$ cancel: $f^+$ and $f^-$ agree continuously on $I$ and the orientations are opposite.
Approximate $T^\pm$ from inside $\Omega^\pm$ by triangles missing $I$; those integrals vanish by Goursat, and uniform continuity of $f$ on $T$ passes to the limit.
Thus $\int_{\partial T} f=0$, and Morera gives holomorphy on $\Omega$.

:::

## The reflection

[[T-Q3GGF]]

:::{.proof title="Schwarz reflection"}
Write $F(z)\da f(z)$ for $z\in \Omega^+\cup I$, and $F(z)\da \overline{f(\bar z)}$ for $z\in \Omega^-$.
On $\Omega^-$ the difference quotient is
\[
\frac{F(z+h)-F(z)}{h}
= \overline{\frac{f(\bar z+\bar h)-f(\bar z)}{\bar h}}
,\]
using $\overline{A}/h = \overline{A/\bar h}$.
As $h\to 0$ we have $\bar h\to 0$, so $F'(z)=\overline{f'(\bar z)}$ and $F$ is holomorphic on $\Omega^-$.
On $I\subseteq\RR$ the function $f$ is real valued, so $\overline{f(\bar x)}=\overline{f(x)}=f(x)$.
Thus $F$ is continuous on $\Omega$ and its two holomorphic pieces agree on $I$, and the symmetry principle supplies holomorphy on all of $\Omega$.

:::

:::{.remark}
The real axis is not special: $\HH^\pm$ may be replaced by any region symmetric about a line segment, and by a Möbius transformation, about any arc of a circle.
After a Möbius change of coordinates, the same reflection argument therefore applies across circular boundary arcs.

:::

:::{.remark title="What the hypothesis buys"}
Reflection needs $f$ to be real valued on $I$, not merely continuous up to it.
Real values are what make $\overline{f(\bar x)}$ agree with $f(x)$ there, so the two definitions glue.
Replace real by "lands in a circle" and the same argument runs after composing with a Möbius map that carries the circle to $\RR$.

:::
