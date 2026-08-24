---
schema: qual/card@1
id: P-AMD-JWY5GWNO
kind: problem
title: Conformal maps from circular lunes, slit discs, and half-discs
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Blaschke Factors
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.problem}
Find a conformal map

```
1.  from $\{ z: |z - 1/2| > 1/2, \text{Re}(z)>0 \}$ to $\mathbb H$

2.  from $\{ z: |z - 1/2| > 1/2, |z| <1  \}$ to $\mathbb D$

3.  from the intersection of the disk $|z + i| < \sqrt{2}$ with
    ${\mathbb H}$ to ${\mathbb D}$.

4.  from ${\mathbb D}  \backslash [a, 1)$ to
    ${\mathbb D} \backslash [0, 1)$ ($0<a<1)$. \[ Short solution
    possible using Blaschke factor\]

5.  from $\{ z: |z| < 1, \text{Re}(z) > 0 \} \backslash (0, 1/2]$ to
    $\mathbb H$.
```
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Construct explicit conformal mappings (biholomorphisms) for each of the five given domains.

* * *

### Part 1: Map from $\Omega_1 = \{ z \in \mathbb{C} : |z - 1/2| > 1/2, \text{Re}(z)>0 \}$ to $\mathbb{H} = \{w : \text{Im}(w) > 0\}$

<1>1. **The inversion $w_1 = \frac{1}{z}$ maps $\Omega_1$ conformally onto the vertical strip $S_1 = \{w_1 \in \mathbb{C} : 0 < \text{Re}(w_1) < 1\}$.** <2>1. For $z = x+iy \neq 0$, $\text{Re}(1/z) = \frac{x}{x^2+y^2}$.
*Proof:* $\frac{1}{x+iy} = \frac{x-iy}{x^2+y^2}$.
<2>2. $\text{Re}(z) > 0 \iff x > 0 \iff \text{Re}(1/z) > 0$.
*Proof:* $x^2+y^2 > 0$ for all $z \neq 0$, so $x > 0 \iff \frac{x}{x^2+y^2} > 0$.
<2>3. $|z - 1/2| > 1/2 \iff (x - 1/2)^2 + y^2 > 1/4 \iff x^2 - x + y^2 > 0 \iff x^2+y^2 > x \iff \frac{x}{x^2+y^2} < 1 \iff \text{Re}(1/z) < 1$.
*Proof:* Direct algebraic manipulation of the disc boundary equation.
<2>4. The Möbius transformation $z \mapsto 1/z$ is biholomorphic from $\Omega_1$ to $S_1$.
*Proof:* Möbius transformations are conformal automorphisms of the Riemann sphere, and this map is a bijection between the open sets $\Omega_1$ and $S_1$.
<2>5. Q.E.D.

<1>2. **The transformation $w_2 = i\pi w_1$ maps $S_1$ onto the horizontal strip $\{w_2 \in \mathbb{C} : 0 < \text{Im}(w_2) < \pi\}$.** <2>1. For $w_1 = u+iv$, $w_2 = i\pi(u+iv) = -\pi v + i\pi u$.
*Proof:* Multiplication by $i\pi$.
<2>2. $0 < u < 1 \iff 0 < \text{Im}(w_2) < \pi$, while $\text{Re}(w_2) = -\pi v \in \mathbb{R}$.
*Proof:* Follows from definition of $w_2$.
<2>3. Q.E.D.

<1>3. **The exponential map $w \mapsto e^{w_2} = \exp\left(\frac{i\pi}{z}\right)$ maps the horizontal strip conformally onto the upper half-plane $\mathbb{H}$.** <2>1. The exponential function maps the strip $\{ \xi + i\eta : \xi \in \mathbb{R}, 0 < \eta < \pi \}$ biholomorphically onto $\mathbb{H} = \{ r e^{i\theta} : r > 0, 0 < \theta < \pi \}$.
*Proof:* Standard property of the complex exponential function.
<2>2. Thus, the composite map $f_1(z) = \exp\left(\frac{i\pi}{z}\right)$ is a conformal map from $\Omega_1$ to $\mathbb{H}$.
*Proof:* Composition of biholomorphisms is a biholomorphism.
<2>3. Q.E.D.

* * *

### Part 2: Map from $\Omega_2 = \{ z : |z - 1/2| > 1/2, |z| < 1 \}$ to $\mathbb{D}$

<1>4. **Apply the inversion $w_1 = \frac{1}{z-1}$.** <2>1. The boundary circle $|z| = 1$ passes through $z=1$, so under $w_1 = \frac{1}{z-1}$, it maps to a straight line.
Since $\text{Re}\left(\frac{1}{e^{i\theta}-1}\right) = \text{Re}\left(\frac{e^{-i\theta}-1}{|e^{i\theta}-1|^2}\right) = \frac{\cos\theta - 1}{2-2\cos\theta} = -\frac{1}{2}$, the image of $|z| < 1$ is the half-plane $\text{Re}(w_1) < -\frac{1}{2}$.
*Proof:* Standard property of inversion mapping circles through the pole to straight lines.
<2>2. The inner circle $|z - 1/2| = 1/2$ also passes through $z=1$.
For points on this circle, $z = \frac{1}{2} + \frac{1}{2}e^{i\theta}$, so $z-1 = -\frac{1}{2}(1 - e^{i\theta})$.
Then $\text{Re}\left(\frac{1}{z-1}\right) = \text{Re}\left(\frac{-2}{1-e^{i\theta}}\right) = -2 \cdot \frac{1}{2} = -1$.
*Proof:* Calculation of real part of $\frac{-2}{1 - \cos\theta - i\sin\theta}$.
<2>3. Since $|z-1/2| > 1/2$, the region $\Omega_2$ maps conformally onto the vertical strip $S_2 = \{w_1 : -1 < \text{Re}(w_1) < -1/2\}$.
*Proof:* By continuity and connectedness, evaluating at the test point $z = -1/2 \in \Omega_2$ gives $w_1 = \frac{1}{-3/2} = -2/3 \in (-1, -1/2)$.
<2>4. Q.E.D.

<1>5. **Map the strip $S_2$ to $\mathbb{D}$.** <2>1. Shift and scale $w_1$ to the standard strip: $w_2 = 2\pi\left(w_1 + 1\right) = 2\pi\left(\frac{1}{z-1} + 1\right) = \frac{2\pi z}{z-1}$.
When $w_1 \in (-1, -1/2)$, $\text{Re}(w_2) \in (0, \pi)$.
*Proof:* Linear change of variable maps $(-1, -1/2)$ to $(0, \pi)$.
<2>2. Map to horizontal strip: $w_3 = i w_2 = \frac{2\pi i z}{z-1}$, which has $0 < \text{Im}(w_3) < \pi$.
*Proof:* $\text{Im}(i w_2) = \text{Re}(w_2) \in (0, \pi)$.
<2>3. Exponentiate: $w_4 = e^{w_3} = \exp\left(\frac{2\pi i z}{z-1}\right)$ maps onto the upper half-plane $\mathbb{H}$.
*Proof:* Standard exponential mapping of a horizontal strip of width $\pi$.
<2>4. Cayley transform to $\mathbb{D}$: $f_2(z) = \frac{w_4 - i}{w_4 + i} = \frac{\exp\left(\frac{2\pi i z}{z-1}\right) - i}{\exp\left(\frac{2\pi i z}{z-1}\right) + i}$ is a conformal map from $\Omega_2$ to $\mathbb{D}$.
*Proof:* The Cayley transform $w \mapsto \frac{w-i}{w+i}$ maps $\mathbb{H}$ biholomorphically onto $\mathbb{D}$.
<2>5. Q.E.D.

* * *

### Part 3: Map from $\Omega_3 = \{z \in \mathbb{H} : |z + i| < \sqrt{2}\}$ to $\mathbb{D}$

<1>6. **Identify the geometry of $\Omega_3$.** <2>1. The region is bounded by the real line $\text{Im}(z) = 0$ and the circular arc $|z+i| = \sqrt{2}$ in the upper half-plane.
*Proof:* By definition of $\Omega_3$.
<2>2. The circle $|z+i|^2 = x^2 + (y+1)^2 = 2$ intersects $y=0$ at $x^2 + 1 = 2 \implies x = \pm 1$.
The vertices of the circular lune are $z_1 = -1$ and $z_2 = 1$.
*Proof:* Solving $x^2+(0+1)^2=2$.
<2>3. The circle $|z+i|=\sqrt{2}$ meets the real axis at an angle: the normal to the circle at $z=1$ is $1 - (-i) = 1+i$ (angle $\pi/4$), while the real axis has normal $i$ (angle $\pi/2$). The internal angle of $\Omega_3$ at both vertices $\pm 1$ is $\pi/4$.
*Proof:* At $z=1$, the tangent vector to the circle is $e^{i 3\pi/4}$, which makes an angle of $\pi/4$ with the real segment $[-1, 1]$.
<2>4. Q.E.D.

<1>7. **Map the lune $\Omega_3$ conformally to $\mathbb{D}$.** <2>1. The Möbius transformation $w_1 = \frac{z+1}{z-1}$ maps $z = -1 \mapsto 0$ and $z = 1 \mapsto \infty$.
*Proof:* Definition of Möbius transformation send vertices to $0$ and $\infty$.
<2>2. Under $w_1$, the segment $(-1, 1) \subset \mathbb{R}$ maps to the negative real axis $(-\infty, 0)$ because for $x \in (-1,1)$, $\frac{x+1}{x-1} < 0$.
The circular arc (passing through $z = (\sqrt{2}-1)i$) maps to the ray of argument $-3\pi/4 \equiv 5\pi/4$.
*Proof:* For $z = (\sqrt{2}-1)i$, $w_1 = \frac{1+(\sqrt{2}-1)i}{-1+(\sqrt{2}-1)i} = \frac{(1+(\sqrt{2}-1)i)^2}{1+(\sqrt{2}-1)^2} = \frac{2\sqrt{2}-2 + 2(\sqrt{2}-1)i}{4-2\sqrt{2}} = -1 + i$, which has $\arg(w_1) = 3\pi/4$.
The sector formed between the real segment (ray $\arg = \pi$) and the arc has opening angle $\pi/4$, which is the sector $\{w_1 : 3\pi/4 < \arg(w_1) < \pi\}$.
<2>3. Rotate by $e^{-3\pi i/4}$: $w_2 = e^{-3\pi i/4} w_1 = e^{-3\pi i/4} \left(\frac{z+1}{z-1}\right)$ maps $\Omega_3$ to the sector $S = \{w_2 : 0 < \arg(w_2) < \pi/4\}$.
*Proof:* Rotation by $-3\pi/4$.
<2>4. Power map $w_3 = w_2^4 = \left(e^{-3\pi i/4} \frac{z+1}{z-1}\right)^4 = - \left(\frac{z+1}{z-1}\right)^4$ maps the sector of angle $\pi/4$ onto $\mathbb{H}$.
*Proof:* $z \mapsto z^4$ multiplies arguments by 4, sending $(0, \pi/4)$ to $(0, \pi) = \mathbb{H}$, and $(e^{-3\pi i/4})^4 = e^{-3\pi i} = -1$.
<2>5. Cayley transform: $f_3(z) = \frac{w_3 - i}{w_3 + i} = \frac{- \left(\frac{z+1}{z-1}\right)^4 - i}{- \left(\frac{z+1}{z-1}\right)^4 + i} = \frac{\left(\frac{z+1}{z-1}\right)^4 + i}{\left(\frac{z+1}{z-1}\right)^4 - i}$ maps $\Omega_3$ conformally to $\mathbb{D}$.
*Proof:* Composition of biholomorphisms.
<2>6. Q.E.D.

* * *

### Part 4: Map from $\mathbb{D} \setminus [a, 1)$ to $\mathbb{D} \setminus [0, 1)$ ($0 < a < 1$)

<1>8. **Use an automorphism of the unit disc (Blaschke factor) mapping $a$ to $0$.** <2>1. Define $\phi_a(z) = \frac{z - a}{1 - az}$.
*Proof:* For $a \in (-1, 1)$, $\phi_a$ is an automorphism of $\mathbb{D}$ (i.e. $\phi_a \in \text{Aut}(\mathbb{D})$). <2>2. $\phi_a(a) = \frac{a-a}{1-a^2} = 0$, and $\phi_a(1) = \frac{1-a}{1-a} = 1$.
*Proof:* Direct evaluation.
<2>3. For $x \in [a, 1)$, $\phi_a(x) = \frac{x-a}{1-ax}$ is strictly increasing since $\phi_a'(x) = \frac{1-a^2}{(1-ax)^2} > 0$, so $\phi_a([a, 1)) = [0, 1)$.
*Proof:* $\phi_a$ is a strictly increasing diffeomorphism on $[a, 1)$ with $\phi_a(a)=0$ and $\lim_{x\to 1^-} \phi_a(x)=1$.
<2>4. Since $\phi_a$ is a bijection of $\mathbb{D}$ to $\mathbb{D}$ and maps the slit $[a,1)$ bijectively onto the slit $[0,1)$, it restricts to a conformal map from $\mathbb{D} \setminus [a,1)$ onto $\mathbb{D} \setminus [0,1)$.
*Proof:* Restriction of a biholomorphism to an open subset.
<2>5. Q.E.D.

* * *

### Part 5: Map from $\Omega_5 = \{ z : |z| < 1, \text{Re}(z) > 0 \} \setminus (0, 1/2]$ to $\mathbb{H}$

<1>9. **Square map $w_1 = z^2$.** <2>1. The right half-disc $\{|z|<1, \text{Re}(z)>0\} = \{r e^{i\theta} : 0 < r < 1, -\pi/2 < \theta < \pi/2\}$.
*Proof:* Polar coordinate description of the right half-disc.
<2>2. The map $w_1 = z^2$ sends $r e^{i\theta} \mapsto r^2 e^{2i\theta}$, which maps the right half-disc conformally to the slit unit disc $\mathbb{D} \setminus (-1, 0]$.
*Proof:* Angles $-\pi/2 < \theta < \pi/2$ map bijectively to $-\pi < 2\theta < \pi$, so the negative real axis is the boundary slit coming from the imaginary axis.
<2>3. The slit $(0, 1/2]$ on the positive real axis maps under $z \mapsto z^2$ to the slit $(0, 1/4]$ on the positive real axis.
*Proof:* For $x \in (0, 1/2]$, $x^2 \in (0, 1/4]$.
<2>4. Thus, $w_1 = z^2$ maps $\Omega_5$ conformally onto $\mathbb{D} \setminus ( (-1, 0] \cup (0, 1/4] ) = \mathbb{D} \setminus (-1, 1/4]$.
*Proof:* Union of the two slits.
<2>5. Q.E.D.

<1>10. **Use an automorphism of $\mathbb{D}$ to center/shift the slit.** <2>1. Consider the Möbius transformation $\psi(w_1) = \frac{w_1 - 1/4}{1 - w_1/4}$.
*Proof:* This is a Blaschke factor mapping $\mathbb{D} \to \mathbb{D}$.
<2>2. $\psi(1/4) = 0$, $\psi(-1) = \frac{-1 - 1/4}{1 + 1/4} = \frac{-5/4}{5/4} = -1$, and $\psi(1) = 1$.
*Proof:* Direct evaluation.
<2>3. Since $\psi$ is monotone increasing on $(-1, 1)$, it maps the slit $(-1, 1/4]$ onto the slit $(-1, 0]$.
*Proof:* $\psi((-1, 1/4]) = (\psi(-1), \psi(1/4)] = (-1, 0]$.
<2>4. Hence $w_2 = \psi(z^2) = \frac{z^2 - 1/4}{1 - z^2/4} = \frac{4z^2 - 1}{4 - z^2}$ maps $\Omega_5$ conformally onto the slit disc $\mathbb{D} \setminus (-1, 0]$.
*Proof:* Composition of $z \mapsto z^2$ and $\psi$.
<2>5. Q.E.D.

<1>11. **Map $\mathbb{D} \setminus (-1, 0]$ onto the upper half-plane $\mathbb{H}$.** <2>1. The principal square root $w_3 = \sqrt{w_2}$ maps $\mathbb{D} \setminus (-1, 0]$ conformally onto the right half-disc $\{w_3 \in \mathbb{D} : \text{Re}(w_3) > 0\}$.
*Proof:* The principal square root maps the slit plane $\mathbb{C} \setminus (-\infty, 0]$ to the right half-plane $\text{Re}(w_3) > 0$, and preserves the condition $|w_2| < 1 \iff |w_3| < 1$.
<2>2. Joukowsky-type transform: $w_4 = -i \frac{w_3 - 1}{w_3 + 1}$ maps the right half-disc to the first quadrant, or directly use the Joukowsky map $J(\zeta) = -\frac{1}{2}(\zeta + 1/\zeta)$ which maps the upper half-disc to $\mathbb{H}$.
Rotating the right half-disc to the upper half-disc via $w_3 \mapsto i w_3$ and applying $J$ gives: $f_5(z) = -\frac{1}{2}\left(i\sqrt{\frac{4z^2-1}{4-z^2}} + \frac{1}{i\sqrt{\frac{4z^2-1}{4-z^2}}}\right) = -\frac{i}{2}\left(\sqrt{\frac{4z^2-1}{4-z^2}} - \sqrt{\frac{4-z^2}{4z^2-1}}\right)$.
*Proof:* Composition of biholomorphisms ending in $\mathbb{H}$.
<2>3. Q.E.D.
:::
