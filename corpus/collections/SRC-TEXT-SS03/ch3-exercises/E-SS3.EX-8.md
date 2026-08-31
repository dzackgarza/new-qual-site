---
schema: qual/card@1
id: E-SS3.EX-8
kind: exercise
title: "SS 3.8: The integral of dtheta over a+b cos theta"
classification:
  areas:
  - complex-analysis
  topics: ['Meromorphic Functions', 'Residue Theorem', 'Argument Principle']
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: exercise
8. Prove that

$$
\int_ {0} ^ {2 \pi} \frac {d \theta}{a + b \cos \theta} = \frac {2 \pi}{\sqrt {a ^ {2} - b ^ {2}}}
$$

if $a > | b |$ and $a , b \in \mathbb { R }$
:::

::: {.solution}
<1>1. Case $b = 0$: <2>1. If $b = 0$, the integral is:
\[
\int_0^{2\pi} \frac{d\theta}{a} = \frac{2\pi}{a} = \frac{2\pi}{\sqrt{a^2 - 0^2}}.
\]
::: {.proof}
direct integration.
:::

<1>2. Transformation to a contour integral on the unit circle for $b \neq 0$: <2>1. Let $z = e^{i\theta}$ on the positively oriented unit circle $\gamma: |z| = 1$.
Then $d\theta = \frac{dz}{iz}$ and $\cos \theta = \frac{z + z^{-1}}{2}$.
::: {.proof}
Euler’s formula.
:::
<2>2. Substituting into the integral:
\[
I = \int_0^{2\pi} \frac{d\theta}{a + b\cos\theta} = \oint_{|z|=1} \frac{1}{a + b\frac{z + z^{-1}}{2}} \frac{dz}{iz} = \frac{2}{i} \oint_{|z|=1} \frac{dz}{b z^2 + 2az + b}.
\]
::: {.proof}
algebraic simplification.
:::

<1>3. Location of poles and residue computation: <2>1. The quadratic denominator $b z^2 + 2az + b = b(z - z_1)(z - z_2)$ has roots:
\[
z_1 = \frac{-a + \sqrt{a^2 - b^2}}{b}, \qquad z_2 = \frac{-a - \sqrt{a^2 - b^2}}{b}.
\]
::: {.proof}
quadratic formula.
:::
<2>2. Notice that the product of the roots is $z_1 z_2 = \frac{b}{b} = 1$.
Since $a > |b| > 0$, we have $\sqrt{a^2 - b^2} > 0$, so $|z_2| = \frac{a + \sqrt{a^2 - b^2}}{|b|} > \frac{a}{|b|} > 1$.
Consequently, $|z_1| = \frac{1}{|z_2|} < 1$.
Thus $z_1$ lies inside the unit circle $|z| = 1$, and $z_2$ lies outside.
::: {.proof}
root product relation and $a > |b|$.
:::
<2>3. The integrand has a unique simple pole inside $|z| < 1$ at $z = z_1$.
The residue of $g(z) = \frac{1}{b(z - z_1)(z - z_2)}$ at $z = z_1$ is:
\[
\operatorname{Res}(g, z_1) = \frac{1}{b(z_1 - z_2)} = \frac{1}{b \left( \frac{2\sqrt{a^2 - b^2}}{b} \right)} = \frac{1}{2\sqrt{a^2 - b^2}}.
\]
::: {.proof}
residue formula for simple poles.
:::

<1>4. Evaluation via Residue Theorem: <2>1. By Cauchy’s Residue Theorem:
\[
I = \frac{2}{i} \left( 2\pi i \operatorname{Res}(g, z_1) \right) = 4\pi \cdot \frac{1}{2\sqrt{a^2 - b^2}} = \frac{2\pi}{\sqrt{a^2 - b^2}}.
\]
::: {.proof}
Cauchy Residue Theorem.
:::

<1>5. Conclusion: $\int_0^{2\pi} \frac{d\theta}{a + b\cos\theta} = \frac{2\pi}{\sqrt{a^2 - b^2}}$ for all $a > |b|$.
::: {.proof}
<1>1 through <1>4.
:::
Q.E.D.
:::
