---
schema: qual/card@1
id: P-CWXEW
kind: problem
title: "Conformal map from a slit lens to the upper half plane"
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
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
Find a bijective conformal map from $G$ to $\mathbb{H} = \{w \in \mathbb{C} \mid \operatorname{Im}(w) > 0\}$, where
$$G \coloneqq \{z \in \mathbb{C} \mid |z-1| < \sqrt{2}, \, |z+1| < \sqrt{2}\} \setminus [0, i).$$
:::

::: solution
The two circles $|z-1|=\sqrt2$ and $|z+1|=\sqrt2$ meet orthogonally at $\pm i$. Set
$$
T(z)=\frac{z-i}{z+i}.
$$
Then $T(i)=0$, $T(-i)=\infty$, so the two circular boundary arcs become rays. Since $T(0)=-1$, the unslit lens maps to the sector
$$
\frac{3\pi}{4}<\arg w<\frac{5\pi}{4}.
$$
Moreover, for $0\le t<1$,
$$
T(it)=\frac{t-1}{t+1}\in[-1,0),
$$
so the slit maps to that radial segment.

<1>1. Rotate by $-1$:
$$
\zeta=-T(z).
$$
Then
$$
-\frac\pi4<\arg\zeta<\frac\pi4,
\qquad \zeta\notin(0,1].
$$
Squaring maps this slit sector biholomorphically onto
$$
\{u:\Re u>0\}\setminus(0,1].
$$

<1>2. The Cayley transform
$$
v=\frac{u-1}{u+1}
$$
maps the right half-plane to $\mathbb D$ and $(0,1]$ to $(-1,0]$. Thus
$$
v\in\mathbb D\setminus(-1,0].
$$
The principal square root maps this slit disk biholomorphically onto the right half-disk
$$
H_+=\{s:|s|<1,\ \Re s>0\}.
$$

<1>3. Finally,
$$
q=\frac{s-i}{s+i}
$$
maps the imaginary diameter of $H_+$ to the negative real axis and the semicircular boundary to the negative imaginary axis; hence it maps $H_+$ biholomorphically onto the third quadrant. Squaring then maps that quadrant biholomorphically onto the upper half-plane.

Therefore the composition
$$
z\mapsto T(z)\mapsto -T(z)\mapsto(-T(z))^2
\mapsto \frac{(-T(z))^2-1}{(-T(z))^2+1}
\mapsto \sqrt{\frac{(-T(z))^2-1}{(-T(z))^2+1}}
\mapsto q\mapsto q^2
$$
with the principal square root is a bijective conformal map $G\to\mathbb H$.
:::
