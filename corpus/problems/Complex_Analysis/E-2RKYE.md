---
schema: qual/card@1
id: E-2RKYE
kind: problem
title: $\int_0^{2\pi}\frac{d\theta}{1+a^2-2a\cos\theta}$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Trigonometry
relations: []
review: draft
---

::: {.exercise}
\[
\int_{0}^{2 \pi} \frac{d \theta}{1+a^{2}-2 a \cos (\theta)}
= \begin{cases}\frac{2 \pi}{a^{2}-1} & \text { if }|a|>1 \\ \frac{2 \pi}{1-a^{2}} & \text { if }|a|<1\end{cases}
.\]
:::

::: {.solution}
Assume $\abs a\ne1$.
For $a=0$ both sides equal $2\pi$, so assume also $a\ne0$.

<1>1. $\displaystyle\int_{0}^{2 \pi} \frac{d \theta}{1+a^{2}-2 a \cos \theta}=\frac{i}{a}\int_{\abs z=1}\frac{dz}{(z-a)(z-1/a)}$.

::: {.proof}
Put $z=e^{i\theta}$, so $2\cos\theta=z+\inverseof{z}$ and $d\theta=dz/(iz)$.
Then
\[
\frac{d\theta}{1+a^2-2a\cos\theta}
=\frac{dz}{i\left(\left(1+a^{2}\right) z-a\left(z^{2}+1\right)\right)}
=\frac{dz}{-ia(z-a)(z-1/a)}
=\frac{i}{a}\,\frac{dz}{(z-a)(z-1/a)}.
\]
:::

<1>2. Q.E.D.

::: {.proof}
Exactly one of $a$, $1/a$ lies in the unit disk.
If $\abs a<1$, the residue theorem at $z=a$ gives $2\pi i\cdot\frac ia\cdot\frac{1}{a-1/a}=\frac{2\pi}{1-a^2}$.
If $\abs a>1$, the residue at $z=1/a$ gives $2\pi i\cdot\frac ia\cdot\frac{1}{1/a-a}=\frac{2\pi}{a^2-1}$.
Step <1>1 converts these into the two cases of the formula.
:::

:::
