---
schema: qual/card@1
id: PR-3LBLV
kind: proposition
title: Upper half-plane to centered vertical half-strip
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Trigonometry
relations: []
review: draft
---

:::{.proposition}
\[
F: \HH &\to \qty{-{\pi \over 2}, {\pi \over 2}} \cross i\RR \\
z &\mapsto \sin(z)
.\]

The mapping $z\mapsto \sin(z)$:
![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-12-31_23-01-11.png)


- As $z$ travels from $i\infty \to i0$, $\sin(iz) = i\sinh(z)$ also traverses $i\infty\to i0$ 
- For $z\in[-\pi/2, \pi/2]$, $\sin(z)$ is real and in $[-1, 1]$.
- As $z$ travels along $\pi/2 + it$ for $t\in [0, \infty)$, $\sin(\pi/2 + it) = \cosh(t)$ traverses $1\to \infty$ along $\RR$

To express this through the exponential map, set $w \da e^{iz}$, then
\[
\sin(z) = -{1\over 2}\qty{iw + {1\over iw}}
,\]
which is the composition
\[
\qty{w\mapsto {w-w\inv\over 2i}} \circ \qty{z \mapsto e^{z}} \circ \qty{z\mapsto iz}
.\]



:::
