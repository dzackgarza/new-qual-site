---
schema: qual/card@1
id: PR-FL6T7
kind: proposition
title: Cayley transform $\frac{i-z}{i+z}$ from the upper half-plane to the disc
slogan: 'The Möbius map $(i-z)/(i+z)$ sends the upper half-plane biholomorphically onto the unit disc.'
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.proposition}
The [[D-FRVBV|Möbius transformation]]
$$
\begin{aligned}
F\colon \HH=\theset{z\st \Im(z) > 0 } &\to \DD=\theset{w\st \abs{w} < 1 }, \\
z &\mapsto {i-z \over i+z}
\end{aligned}
$$
is a [[D-TM4TE|biholomorphism]] with inverse $w\mapsto i \qty{1-w \over 1+w}$.
:::

::: {.remark}
$F$ extends to a homeomorphism from $\RR\cup\theset{\infty}$ onto the unit circle, with $F(\infty) = -1$, $F(-1)=-i$, and $F(0)=1$.
As $x$ increases from $-\infty$ to $\infty$ along $\RR$, $F(x)$ travels counterclockwise around the circle, starting at $-1$ and passing through the lower half first.
:::
