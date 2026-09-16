---
schema: qual/card@1
id: PR-BPP7D
kind: proposition
title: Sector to disc
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
---

::: {.proposition}
For $0<\alpha\le2\pi$, let $S_\alpha\coloneqq\ts{ z \st 0 < \arg(z) < \alpha }$, with $\arg z\in(0,\alpha)$ as in [[PR-AQFRA]].
Then
$$
\begin{aligned}
F\colon S_{\alpha} &\to \DD, \\
z &\mapsto {z^{\pi/\alpha} - i \over z^{\pi/\alpha} + i}
\end{aligned}
$$
is a [[D-TM4TE|biholomorphism]].

![](../../assets/figures/image_2020-07-22-13-22-46.png)
:::

::: {.proof}
$F$ is the composite
$$
S_{\alpha} \xrightarrow{\ z\mapsto z^{\pi/\alpha}\ } S_{\pi} = \HH \xrightarrow{\ u\mapsto \frac{u-i}{u+i}\ } \DD.
$$
The first map is a biholomorphism by [[PR-AQFRA]].
The second is a Möbius transformation; for $u\in\HH$ the point $u$ is closer to $i$ than to $-i$, so $\abs{u-i}<\abs{u+i}$ and the image lies in $\DD$, and its inverse $w\mapsto i\frac{1+w}{1-w}$ maps $\DD$ into $\HH$, since $\Im\qty{i\frac{1+w}{1-w}}=\frac{1-\abs{w}^2}{\abs{1-w}^2}>0$.
A composite of biholomorphisms is a biholomorphism.
:::
