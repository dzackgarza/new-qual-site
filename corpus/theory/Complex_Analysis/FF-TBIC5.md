---
schema: qual/card@1
id: FF-TBIC5
kind: fact
title: $\sin\theta$ and $d\theta$ under the substitution $z=e^{i\theta}$
slogan: 'On the unit circle, replace trigonometry by rational functions: $\sin\theta=(z-z^{-1})/(2i)$ and $d\theta=dz/(iz)$.'
prompts:
- How is $\sin(\theta)$ written in $z$ for a contour integral on the unit circle, and what is $d\theta$?
classification:
  areas:
  - complex-analysis
  topics:
  - Trigonometry
  - Contour Integration
  - Residues
relations: []
review: draft
---

::: {.fact}
For $\theta\in\RR$ and $z=e^{i\theta}$ on the unit circle,
$$
\begin{aligned}
\sin(\theta) &= \frac{e^{i\theta} - e^{-i\theta}}{2i} = \frac{z - \inverseof{z}}{2i}, \\
d\theta &= \frac{dz}{iz}.
\end{aligned}
$$

This is the substitution of [@Ahl73, ch. 4, §5.3, Evaluation of Definite Integrals]: that section replaces an integral in $\theta$ over $[0,2\pi]$ by $-i$ times an integral over $\abs z=1$, displaying $\frac12(z+1/z)$ for $\cos\theta$, $\frac{1}{2i}(z-1/z)$ for $\sin\theta$ and $dz/z$ for $d\theta$, which is the display above with $z=e^{i\theta}$ and $dz=iz\,d\theta$.
:::
