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
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source states the formula with no hypothesis on a; the statement takes a real with |a| not equal to 1, where the integrand has no zero denominator and the formula holds.
---

::: {.exercise}
For real $a$ with $\abs a\ne1$,
$$
\int_{0}^{2 \pi} \frac{d \theta}{1+a^{2}-2 a \cos (\theta)}
= \begin{cases}\frac{2 \pi}{a^{2}-1} & \text { if }\abs a>1, \\ \frac{2 \pi}{1-a^{2}} & \text { if }\abs a<1.\end{cases}
$$
:::

::: {.solution}
For $a=0$ both sides equal $2\pi$, so assume $a\ne0$.

::: pf

::: {.pf-step #s1}
$\displaystyle\int_{0}^{2 \pi} \frac{d \theta}{1+a^{2}-2 a \cos \theta}=\frac{i}{a}\int_{\abs z=1}\frac{dz}{(z-a)(z-1/a)}$.

::: pf-proof
Put $z=e^{i\theta}$, so $2\cos\theta=z+z^{-1}$ and $d\theta=dz/(iz)$.
Then
$$
\frac{d\theta}{1+a^2-2a\cos\theta}
=\frac{dz}{i\left(\left(1+a^{2}\right) z-a\left(z^{2}+1\right)\right)}
=\frac{dz}{-ia(z-a)(z-1/a)}
=\frac{i}{a}\,\frac{dz}{(z-a)(z-1/a)}.
$$
:::

:::

::: pf-qed
Since $a$ is real with $\abs a\ne1$, exactly one of $a$, $1/a$ lies in the open unit disk, and neither lies on the unit circle.
If $\abs a<1$, the residue theorem at $z=a$ and step [](#s1){.pf-ref} give $2\pi i\cdot\frac ia\cdot\frac{1}{a-1/a}=\frac{2\pi}{1-a^2}$.
If $\abs a>1$, the residue at $z=1/a$ gives $2\pi i\cdot\frac ia\cdot\frac{1}{1/a-a}=\frac{2\pi}{a^2-1}$.
:::

:::

:::
