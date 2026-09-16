---
schema: qual/card@1
id: PR-FL6T7
kind: proposition
title: Half-plane to disc
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
F\colon \HH=\ts{z\st \Im(z) > 0 } &\to \DD=\ts{w\st \abs{w} < 1 }, \\
z &\mapsto {i-z \over i+z}
\end{aligned}
$$
is a [[D-TM4TE|biholomorphism]] with inverse $w\mapsto i \qty{1-w \over 1+w}$.
:::

::: {.proof}
For $z\in\HH$, the point $z$ is closer to $i$ than to $-i$, so $\abs{i-z}<\abs{i+z}$ and $F(z)\in\DD$.
Solving $w(i+z)=i-z$ for $z$ gives $z=i\frac{1-w}{1+w}$, and for $w\in\DD$,
$$
\Im\qty{i\frac{1-w}{1+w}}=\frac{1-\abs{w}^2}{\abs{1+w}^2}>0,
$$
so the inverse maps $\DD$ into $\HH$.
Both maps are holomorphic on these sets and mutually inverse.
:::

::: {.remark}
$F$ extends to a homeomorphism from $\RR\cup\theset{\infty}$ onto the unit circle, with $F(\infty) = -1$, $F(-1)=-i$, and $F(0)=1$.
As $x$ increases from $-\infty$ to $\infty$ along $\RR$, $F(x)$ travels counterclockwise around the circle, starting at $-1$ and passing through the lower half first.

![](../../assets/figures/2021-07-29_19-02-54.png)
:::
