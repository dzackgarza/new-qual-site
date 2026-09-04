---
schema: qual/card@1
id: P-IIONX
kind: problem
title: A fractional linear transformation $\HH\to\DD$ and the image of the first quadrant
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Conformal Maps
relations: []
review: draft
audit:
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Replaced first-person uncertainty and orientation heuristics by direct modulus and imaginary-part calculations.
---

::: {.problem}
Find a fractional linear transformation $T$ which maps $\HH$ to $\DD$, and explicitly describe the image of the first quadrant under $T$.
:::

::: {.solution}
<1>1. The fractional linear map
\[
T(z)=\frac{z-i}{z+i}
\]
is a biholomorphism $\HH\to\DD$.
::: {.proof}
Let $z=x+iy$ with $y>0$.
Then
\[
|T(z)|^2
=\frac{x^2+(y-1)^2}{x^2+(y+1)^2}<1,
\]
so $T(\HH)\subseteq\DD$.

Solving $w=T(z)$ for $z$ gives
\[
z=i\frac{1+w}{1-w}.
\]
For $|w|<1$ this inverse has positive imaginary part, so it maps $\DD$ into $\HH$.
Thus $T$ is a biholomorphism.
:::

<1>2. For $z=x+iy\in\HH$,
\[
\Im T(z)=-\frac{2x}{|z+i|^2}.
\]
::: {.proof}
Multiply numerator and denominator by $\overline{z+i}=x-i(y+1)$:
\[
T(z)
=\frac{(x+i(y-1))(x-i(y+1))}{|z+i|^2}.
\]
The imaginary part of the numerator is
\[
x(y-1)-x(y+1)=-2x.
\]
:::

<1>3. The first quadrant
\[
Q_1=\{z:\Re z>0,\ \Im z>0\}
\]
is mapped into the lower half of the unit disk.
::: {.proof}
By <1>1, $T(Q_1)\subseteq\DD$.
By <1>2, $\Re z>0$ implies
\[
\Im T(z)<0.
\]
Hence
\[
T(Q_1)\subseteq\{w\in\DD:\Im w<0\}.
\]
:::

<1>4. In fact,
\[
\boxed{T(Q_1)=\{w\in\DD:\Im w<0\}}.
\]
::: {.proof}
Let $w\in\DD$ with $\Im w<0$, and let $z=T^{-1}(w)\in\HH$ by <1>1.
Applying <1>2 to this $z$ gives
\[
\Im w=-\frac{2\Re z}{|z+i|^2}<0,
\]
so $\Re z>0$.
Thus $z\in Q_1$ and $w=T(z)$.
:::

![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-12-31_03-15-00.png)
:::
