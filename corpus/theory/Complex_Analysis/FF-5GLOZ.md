---
schema: qual/card@1
id: FF-5GLOZ
kind: fact
title: Laurent expansion of $\csch z$ at $0$
slogan: '$\csch z$ has principal part $1/z$ at $0$, and $\csch z-1/z$ is odd and holomorphic on $\abs{z}<\pi$.'
prompts:
- What is the series expansion of $\csch(z)$?
classification:
  areas:
  - complex-analysis
  topics:
  - Hyperbolic Functions
  - Laurent Series
relations: []
review: draft
---

::: {.fact}
The function $\csch z\coloneqq\frac{1}{\sinh z}$ has a simple pole at $0$, and for $0<\abs{z}<\pi$
$$
\csch z=\frac1z-\frac{z}{6}+\frac{7z^{3}}{360}-\frac{31z^{5}}{15120}+\cdots.
$$

This is the Laurent development of [@Ahl73, ch. 5, §1.3, The Laurent Series] on the annulus $0<\abs z<\pi$, with the coefficients given there by (3) and by the integral for the negative powers. The odd series and the alternating signs are those of the expansion of $\csc$ at $i z$: $\sin(iz)=i\sinh z$, so $\csch z=i\csc(iz)$, and substituting $iz$ in [[FF-UQZNR]] multiplies the coefficient of $z^{2k+1}$ by $i\cdot i^{2k+1}=\pm1$.
:::
