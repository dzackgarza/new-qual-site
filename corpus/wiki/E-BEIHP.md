---
schema: qual/card@1
id: E-BEIHP
kind: exercise
title: $1/1+\sin^2$
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
solved: true
---

:::{.exercise title="$1/1+\sin^2$"}
\[
\int_{[-\pi, \pi]} {1\over 1 + \sin^2(\theta)} \dtheta
.\]

:::

:::{.solution}
Set $z=e^{i\theta}$, so $\sin(\theta) = {z+z\inv\over 2i}$ and $\sin^2(\theta) = -{1\over 4}(z^{-2}-2+z^2)$.
Then
\[
I\da \int_{[-\pi, \pi]} {1\over 1 + \sin^2(\theta)} \dtheta
&= \int_{S^1} {1\over 1 - {1\over 4}(z^{-2} -2 + z^2) } {1\over iz}\dz \\
&= \int_{S^1} {-4i \over z(4-(z^{-2} -2 + z^2))}\dz \\
&= \int_{S^1} {-4iz \over z^2(6-z^{-2} - z^2)}\dz \\
&= \int_{S^1} {4iz \over z^4-6z^2+1}\dz \\
&= 2\pi i \sum_{z_k\in \DD} \Res_{z=z_k} {4iz\over z^4-6z^2+1}
.\]

Factoring the denominator:
\[
w^2 - 6w - 1 =0 
&\implies w^2 - 6w + \qty{-6\over 2}^2 - \qty{-6\over 2}^2 + 1 =0 \\
&\implies (w - 3)^2 = -1 + 9 = 8 \\
&\implies w-3 = \zeta_2^k \sqrt{8},\, k=0, 1 \\
&\implies w = 3 \pm \sqrt{8} \\
&\implies z= \pm\sqrt{3\pm \sqrt 8}
.\]
Write these roots as 

- $z_1 \da \sqrt{3-\sqrt 8}$
- $z_2 \da -\sqrt{3-\sqrt 8}$
- $z_3 \da \sqrt{3+\sqrt 8}$
- $z_4 \da -\sqrt{3 + \sqrt 8}$

Some numerology to figure out the modulus of these roots:

- $3 + \sqrt{8} = 3+2\sqrt{2} 3+2\cdot(1.4) \approx 5.8$, so $\abs{ \pm \sqrt{3+\sqrt 8}}>\sqrt{4}>2>1$.
- $3-\sqrt{8} \approx 3-2.8 \approx 0.2$ so $\abs{ \pm \sqrt{3-\sqrt 8} } < 1$.

So it suffices to compute the residues at $z_1, z_2 = \pm \sqrt{3-\sqrt 8}$:
At $z_1$:
\[
\Res_{z = z_1} 
&= \lim_{z\to z_1} {(z-z_1) 4i z \over z^4-6z^2+1 } \\
&\equalsbecause{\text{LH}} \lim_{z\to z_1} { 4iz + 4i(z-z_1) \over 4z^3 -12z} \\
&= {4iz_1 \over 4z_1^3 - 12z_1} \\
&= {i\over z_1^2 - 3} \\
&= {i\over (3-\sqrt 8) - 3} \\
&= -{i\over \sqrt 8}
.\]
At $z_2$:
\[
\Res_{z=z_2} 
&= \lim_{z\to z_2} {(z-z_2) 4i z \over z^4-6z^2+1 } \\
&= {4iz_2\over 4z_2^2 - 12z_2}\\
&= {i \over z_2^2 - 3} \\
&= -{i\over \sqrt 8}
.\]

Thus 
\[
I = 2\pi i \cdot -{2i\over \sqrt 8} = {4\pi \over \sqrt{8}}
.\]
:::

