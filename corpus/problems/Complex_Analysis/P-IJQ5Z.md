---
schema: qual/card@1
id: P-IJQ5Z
kind: problem
title: A conformal map from $\CC\setminus(-\infty,0]$ onto $\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Complex Logarithm
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Construct an explicit **conformal map** (biholomorphic equivalence) from the slit plane $\Omega = \mathbb{C} \setminus (-\infty, 0]$ onto the open unit disk $\mathbb{D} = \{w \in \mathbb{C} \mid |w| < 1\}$.
:::

::: solution
Use the principal square root on
\[
\Omega=\mathbb C\setminus(-\infty,0].
\]
If $z=re^{i\theta}$ with $-\pi<\theta<\pi$, define
\[
\sqrt z=\sqrt r\,e^{i\theta/2}.
\]
Then
\[
-\frac\pi2<\arg\sqrt z<\frac\pi2,
\]
so $\Re\sqrt z>0$. Thus
\[
z\longmapsto\sqrt z
\]
is a biholomorphism from $\Omega$ onto the right half-plane
\[
H=\{u:\Re u>0\}.
\]

<1>1. The Cayley transform
\[
C(u)=\frac{u-1}{u+1}
\]
maps $H$ biholomorphically onto $\mathbb D$. Indeed, if $u=x+iy$ with $x>0$, then
\[
|C(u)|^2
=\frac{(x-1)^2+y^2}{(x+1)^2+y^2}<1.
\]

<1>2. Therefore
\[
F(z)=\frac{\sqrt z-1}{\sqrt z+1}
\]
is a conformal bijection $\Omega\to\mathbb D$.

<1>3. Solving for $z$ gives
\[
F^{-1}(w)=\left(\frac{1+w}{1-w}\right)^2,
\qquad |w|<1.
\]
Since $(1+w)/(1-w)$ lies in the right half-plane, its square lies in $\Omega$, so this is indeed the inverse.
:::
