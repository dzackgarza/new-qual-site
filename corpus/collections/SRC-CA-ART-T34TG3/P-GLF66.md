---
schema: qual/card@1
id: P-GLF66
kind: problem
title: $\int_0^{2\pi}\frac{d\theta}{a+b\cos\theta}=\frac{2\pi}{\sqrt{a^2-b^2}}$ for
  $a>|b|$
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
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Show that if $a,b\in \RR$ with $a > \abs{b}$, then
\[
\int_{0}^{2 \pi} \frac{d \theta}{a+b \cos \theta}=\frac{2 \pi}{\sqrt{a^{2}-b^{2}}}
.\]
:::

::: {.solution}
<1>1. Special case $b = 0$:
<2>1. If $b = 0$, the integral simplifies directly to:
\[
\int_0^{2\pi} \frac{d\theta}{a} = \frac{2\pi}{a} = \frac{2\pi}{\sqrt{a^2 - b^2}}.
\]
::: {.proof}
elementary integration of a constant.
:::

<1>2. Transformation to a contour integral on $|z| = 1$ for $b \neq 0$:
<2>1. Let $z = e^{i\theta}$, so $d\theta = \frac{dz}{iz}$ and $\cos \theta = \frac{z + z^{-1}}{2}$.
The integrand becomes:
\[
a + b \cos \theta = a + \frac{b(z + z^{-1})}{2} = \frac{bz^2 + 2az + b}{2z}.
\]
::: {.proof}
Euler's formula for cosine.
:::
<2>2. Substituting into the integral:
\[
I = \oint_{|z| = 1} \frac{1}{\frac{bz^2 + 2az + b}{2z}} \frac{dz}{iz} = \frac{2}{i} \oint_{|z| = 1} \frac{dz}{bz^2 + 2az + b}.
\]
::: {.proof}
substitution along the unit circle oriented counterclockwise.
:::

<1>3. Poles and Residue Calculation:
<2>1. The denominator $bz^2 + 2az + b = 0$ has roots:
\[
z_1 = \frac{-a + \sqrt{a^2 - b^2}}{b}, \qquad z_2 = \frac{-a - \sqrt{a^2 - b^2}}{b}.
\]
Notice that $z_1 z_2 = \frac{a^2 - (a^2 - b^2)}{b^2} = 1$.
::: {.proof}
quadratic formula.
:::
<2>2. Since $a > |b| > 0$, $|z_2| = \frac{a + \sqrt{a^2 - b^2}}{|b|} > \frac{a}{|b|} > 1$.
Since $z_1 z_2 = 1$, we have $|z_1| = \frac{1}{|z_2|} < 1$.
Thus $z_1$ is the unique pole lying strictly inside the unit circle $|z| = 1$.
::: {.proof}
root product equals 1.
:::
<2>3. The integrand $g(z) = \frac{1}{b(z - z_1)(z - z_2)}$ has a simple pole at $z_1$, with residue:
\[
\operatorname{Res}(g, z_1) = \lim_{z \to z_1} (z - z_1) g(z) = \frac{1}{b(z_1 - z_2)} = \frac{1}{b \cdot \frac{2\sqrt{a^2 - b^2}}{b}} = \frac{1}{2\sqrt{a^2 - b^2}}.
\]
::: {.proof}
formula for simple pole residue.
:::

<1>4. Evaluation by the Residue Theorem:
<2>1. By the Cauchy Residue Theorem:
\[
I = \frac{2}{i} \cdot 2\pi i \operatorname{Res}(g, z_1) = 4\pi \left(\frac{1}{2\sqrt{a^2 - b^2}}\right) = \frac{2\pi}{\sqrt{a^2 - b^2}}.
\]
::: {.proof}
Residue Theorem.
:::

<1>5. Conclusion:
$\int_0^{2\pi} \frac{d\theta}{a + b\cos\theta} = \frac{2\pi}{\sqrt{a^2 - b^2}}$. Q.E.D.
::: {.proof}
<1>1 through <1>4.
:::
:::
