---
order: 30
---

# Schwarz reflection principle

::: {.remark}
In this section, take $\Omega$ to be a region symmetric about the real axis, so $z\in \Omega \iff \bar{z} \in \Omega$.
Partition this set as $\Omega^+ \subseteq \HH, I \subseteq \RR, \Omega^- \subseteq \bar{\HH}$.
:::

[[T-5SKNT]]

::: {.proof title="Symmetry principle, by Morera"}
The glued function $f$ is holomorphic on $\Omega^\pm$ by hypothesis, so it remains to check holomorphy along $I$.
Let $T\subset\Omega$ be a closed triangle.
If $T$ misses $I$, then $T$ lies in $\Omega^+$ or in $\Omega^-$ and $\int_{\partial T} f=0$ by Goursat.

If $T$ meets $I$, split $T$ along $I$ into $T^+\da T\cap\overline{\Omega^+}$ and $T^-\da T\cap\overline{\Omega^-}$.
The two integrals along the segment $T\cap I$ cancel: $f^+$ and $f^-$ agree continuously on $I$, and the orientations are opposite.
Approximate $T^\pm$ from inside $\Omega^\pm$ by triangles (or rectangles) missing $I$; the integrals of $f^\pm$ over those boundaries vanish by Goursat, and uniform continuity of $f$ on $T$ passes to the limit.
Thus $\int_{\partial T} f=0$.
Morera's theorem yields that $f$ is holomorphic on $\Omega$.

:::

[[T-Q3GGF]]

::: {.proof title="Schwarz reflection"}
Write $F(z)\da f(z)$ for $z\in \Omega^+\cup I$, and $F(z)\da \overline{f(\bar z)}$ for $z\in \Omega^-$.
On $\Omega^-$, the difference quotient is
\[
\frac{F(z+h)-F(z)}{h}
= \overline{\frac{f(\bar z+\bar h)-f(\bar z)}{\bar h}}
,\]
because $\overline{A}/h = \overline{A/\bar h}$.
As $h\to 0$ one has $\bar h\to 0$, so $F'(z)=\overline{f'(\bar z)}$ and $F$ is holomorphic on $\Omega^-$.
On $I\subseteq\RR$, $f$ is real-valued, so $\overline{f(\bar x)}=\overline{f(x)}=f(x)$.
Thus $F$ is continuous on $\Omega$ and the two holomorphic pieces agree on $I$.
The symmetry principle supplies holomorphy of $F$ on $\Omega$.

:::

The same argument works with $\HH^\pm$ replaced by any region symmetric about a line segment $L\subseteq\RR$.
