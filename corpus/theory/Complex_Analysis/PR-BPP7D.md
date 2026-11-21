---
schema: qual/card@1
id: PR-BPP7D
kind: proposition
title: Sector to disc
slogan: 'Straighten a sector to the upper half-plane by a power map, then use a Cayley transform to reach the disc.'
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
---

::: {.proposition}
For $0<\alpha\le2\pi$, let $S_\alpha\coloneqq\theset{ z \st 0 < \arg(z) < \alpha }$, with $\arg z\in(0,\alpha)$ as in [[PR-AQFRA]].
Then
$$
\begin{aligned}
F\colon S_{\alpha} &\to \DD, \\
z &\mapsto {z^{\pi/\alpha} - i \over z^{\pi/\alpha} + i}
\end{aligned}
$$
is a [[D-TM4TE|biholomorphism]].

The map is the composite of the two steps of [@Ahl73, ch. 3, §4.2, A Survey of Elementary Mappings]: the power $z^{\pi/\alpha}$ carries the sector onto $\HH$, which is the sector rule of §4.1 of that chapter for $\alpha(\varphi_2-\varphi_1)\le2\pi$, and $(w-i)/(w+i)$ carries $\HH$ onto $\DD$, which is [@SS03, ch. 8, Theorem 1.2]. The section's own advice is that "the general problem of conformal mapping can be reduced" to these two steps, first onto a circular region and then onto the target.

![](../../assets/figures/image_2020-07-22-13-22-46.png)
:::
