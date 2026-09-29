---
schema: qual/card@1
id: P-BKS09-7A
kind: problem
title: Evaluation of $\int_0^\pi d\theta/(a+\cos\theta)$ by residues
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: >-
    Compared the authored statement with the Spring 2009 solution-packet
    extraction; the retained source solution evaluates the full-circle
    integral and is too large by a factor of two for the stated interval.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the symmetry reduction and both pole locations and residues.
---

::: {.problem}
Compute

$$
\int _ { 0 } ^ { \pi } { \frac { d \theta } { a + \cos \theta } }
$$

for $a > 1$ using the method of residues.
:::

::: {.solution}
Set
$$
I\coloneqq\int_0^\pi\frac{d\theta}{a+\cos\theta}.
$$

::: pf

::: {.pf-step #symmetry-doubling}
One has
$$
2I
=
\int_0^{2\pi}\frac{d\theta}{a+\cos\theta}.
$$

::: pf-proof
With the substitution $u=2\pi-\theta$,
$$
\int_\pi^{2\pi}\frac{d\theta}{a+\cos\theta}
=
\int_0^\pi\frac{du}{a+\cos u}
=
I.
$$
Adding the integral over $[0,\pi]$ proves the claim.
:::

:::

::: {.pf-step #contour-form}
The full-period integral satisfies
$$
\int_0^{2\pi}\frac{d\theta}{a+\cos\theta}
=
-2i\int_{\abs z=1}\frac{dz}{z^2+2az+1}.
$$

::: pf-proof
Put $z=e^{i\theta}$. Then
$$
dz=iz\,d\theta,
\qquad
\cos\theta=\frac{z+z^{-1}}{2}.
$$
As $\theta$ runs from $0$ to $2\pi$, $z$ traverses the unit circle once
counterclockwise. Therefore
$$
\begin{aligned}
\int_0^{2\pi}\frac{d\theta}{a+\cos\theta}
&=
\int_{\abs z=1}
\frac{dz/(iz)}{a+(z+z^{-1})/2}\\
&=
\frac{2}{i}
\int_{\abs z=1}\frac{dz}{z^2+2az+1}\\
&=
-2i\int_{\abs z=1}\frac{dz}{z^2+2az+1}.
\end{aligned}
$$
:::

:::

::: {.pf-step #pole-inside}
Of the two poles
$$
\alpha=-a+\sqrt{a^2-1},
\qquad
\beta=-a-\sqrt{a^2-1},
$$
only $\alpha$ lies inside the unit circle.

::: pf-proof
The denominator factors as
$$
z^2+2az+1=(z-\alpha)(z-\beta).
$$
Since $a>1$,
$$
\abs\alpha
=
a-\sqrt{a^2-1}
=
\frac{1}{a+\sqrt{a^2-1}}
<1.
$$
Also
$$
\abs\beta
=
a+\sqrt{a^2-1}
>1.
$$
:::

:::

::: {.pf-step #full-period-value}
The full-period integral equals
$$
\frac{2\pi}{\sqrt{a^2-1}}.
$$

::: pf-proof
By step [](#pole-inside){.pf-ref}, the residue theorem uses only the pole $\alpha$. Its residue is
$$
\operatorname{Res}_{z=\alpha}
\frac{1}{z^2+2az+1}
=
\frac{1}{\alpha-\beta}
=
\frac{1}{2\sqrt{a^2-1}}.
$$
Thus step [](#contour-form){.pf-ref} gives
$$
\begin{aligned}
\int_0^{2\pi}\frac{d\theta}{a+\cos\theta}
&=
-2i\left(
2\pi i\frac{1}{2\sqrt{a^2-1}}
\right)\\
&=
\frac{2\pi}{\sqrt{a^2-1}}.
\end{aligned}
$$
:::

:::

::: {.pf-step #final-value}
The requested integral is
$$
\boxed{
I=\frac{\pi}{\sqrt{a^2-1}}
}.
$$

::: pf-proof
Combine step [](#symmetry-doubling){.pf-ref} with step [](#full-period-value){.pf-ref} and divide by $2$.
:::

:::

::: pf-qed
Step [](#final-value){.pf-ref} gives the requested value.
:::

:::

:::
