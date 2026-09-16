---
schema: qual/card@1
id: PR-7TLAS
kind: proposition
title: Vertical half-strip to right half-disc
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
relations: []
review: draft
---

::: {.proposition}
Let $S\coloneqq\theset{z\in\CC : -\pi/2<\Re z<\pi/2,\ \Im z>0}$ and $H\coloneqq\DD \intersect \ts{\Re(w) > 0}$.
Then
$$
\begin{aligned}
F\colon S &\to H, \\
z &\mapsto e^{iz}
\end{aligned}
$$
is a [[D-TM4TE|biholomorphism]] with inverse $w\mapsto -i\Log(w)$, where $\Log$ is the [[D-4CSPM|principal branch]] of the logarithm.

![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-11-28_18-22-45.png)
:::

::: {.proof}
For $z=x+iy\in S$, $e^{iz}=e^{-y}e^{ix}$ has modulus $e^{-y}\in(0,1)$ and argument $x\in(-\pi/2,\pi/2)$, so $e^{iz}\in H$, and $-i\Log(e^{iz})=-i(-y+ix)=x+iy=z$.
Conversely, every $w\in H$ is $w=re^{i\theta}$ with $r\in(0,1)$ and $\theta\in(-\pi/2,\pi/2)$, and $-i\Log(w)=\theta-i\log r$ has real part $\theta\in(-\pi/2,\pi/2)$ and imaginary part $-\log r>0$, so it lies in $S$, and $e^{i(-i\Log w)}=e^{\Log w}=w$.
Both maps are holomorphic and mutually inverse.
:::
