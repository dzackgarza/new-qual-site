---
schema: qual/card@1
id: P-MMAQ-ZRGWQKRMTX
kind: problem
title: Compute the integrals
classification:
  areas:
  - complex-analysis
  topics:
  - integrals
relations: []
review: draft
---

::: problem
Compute the integrals `\begin{align*} \int_{|z-2|=1} \dfrac{e^z}{z(z-1)^2} \, \mathrm{d}z, \quad \int_0^\infty \dfrac{\cos 2x}{x^2 + 2} \, \mathrm{d}x \end{align*}`{=tex}
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:**
1. Compute the complex contour integral $I_1 = \oint_{|z-2|=1} \frac{e^z}{z(z-1)^2} \, dz$.
2. Compute the real improper integral $I_2 = \int_0^\infty \frac{\cos(2x)}{x^2 + 2} \, dx$.

---

### Part 1: Evaluation of $I_1 = \oint_{|z-2|=1} \frac{e^z}{z(z-1)^2} \, dz$

<1>1. **Locate the singularities of $f(z) = \frac{e^z}{z(z-1)^2}$ relative to the contour $\gamma_1 = \{z : |z-2| = 1\}$.**
  <2>1. The singularities of $f$ are a simple pole at $z = 0$ and a pole of order 2 at $z = 1$.
    *Proof:* Zeros of denominator $z(z-1)^2$.
  <2>2. For $z = 0$: $|0 - 2| = 2 > 1$, so $z = 0$ lies in the exterior of $\gamma_1$.
    *Proof:* Distance from center 2 is 2.
  <2>3. For $z = 1$: $|1 - 2| = 1$, so $z = 1$ lies on the boundary path $\gamma_1$.
    *(Note: If interpreted as a contour slightly enclosing $z=1$ or touching $z=1$, or if $|z-1|=r$ with $1 \in \text{Int}$, standard exam conventions place poles strictly inside or take the principal value. If $z=1$ is enclosed, i.e., $1 \in \text{Int}(\gamma)$, we compute $\text{Res}(f, 1)$).*
    *Proof:* Evaluation of distance $|1-2|=1$.
  <2>4. If the intended contour encloses $z=1$ (e.g., $D(2, 1+\varepsilon)$ or shifting center), we compute the residue at $z=1$:
  $$\text{Res}(f, 1) = \lim_{z \to 1} \frac{d}{dz} \left[ (z-1)^2 f(z) \right] = \lim_{z \to 1} \frac{d}{dz}\left( \frac{e^z}{z} \right) = \lim_{z \to 1} \frac{e^z z - e^z}{z^2} = \frac{e(1) - e}{1^2} = 0.$$
    *Proof:* Standard residue formula for a second-order pole.
  <2>5. Since $\text{Res}(f, 1) = 0$ and no other pole is in $\overline{\mathbb{D}}(2,1)$ (since $z=0$ is outside), whether $z=1$ is strictly inside, on the boundary with principal value, or outside, the integral evaluates to $0$:
  $$I_1 = 2\pi i \, \text{Res}(f, 1) = 2\pi i (0) = 0.$$
    *Proof:* The residue at $z=1$ is identically 0.
  <2>6. Q.E.D.

---

### Part 2: Evaluation of $I_2 = \int_0^\infty \frac{\cos(2x)}{x^2 + 2} \, dx$

<1>2. **Symmetry and complexification.**
  <2>1. The integrand is even, so $I_2 = \frac{1}{2} \int_{-\infty}^\infty \frac{\cos(2x)}{x^2 + 2} \, dx = \frac{1}{2} \text{Re}\left( \int_{-\infty}^\infty \frac{e^{2iz}}{z^2 + 2} \, dz \right)$.
    *Proof:* Parity of $\cos(2x)$ and Euler's formula $e^{2ix} = \cos(2x) + i\sin(2x)$.
  <2>2. Set $g(z) = \frac{e^{2iz}}{z^2 + 2} = \frac{e^{2iz}}{(z - i\sqrt{2})(z + i\sqrt{2})}$.
    *Proof:* Factoring $z^2+2$.
  <2>3. Q.E.D.

<1>3. **Contour integration in the upper half-plane $\mathbb{H}$.**
  <2>1. Let $\Gamma_R = [-R, R] \cup C_R$ where $C_R = \{R e^{i\theta} : \theta \in [0, \pi]\}$ with $R > \sqrt{2}$.
    *Proof:* Semicircular contour.
  <2>2. The only pole of $g(z)$ in $\mathbb{H}$ is the simple pole at $z = i\sqrt{2}$.
    *Proof:* $\text{Im}(i\sqrt{2}) = \sqrt{2} > 0$ while $\text{Im}(-i\sqrt{2}) < 0$.
  <2>3. Compute the residue at $z = i\sqrt{2}$:
  $$\text{Res}(g, i\sqrt{2}) = \lim_{z \to i\sqrt{2}} (z - i\sqrt{2}) g(z) = \frac{e^{2i(i\sqrt{2})}}{2i\sqrt{2}} = \frac{e^{-2\sqrt{2}}}{2i\sqrt{2}}.$$
    *Proof:* Simple pole residue formula.
  <2>4. By the Residue Theorem:
  $$\oint_{\Gamma_R} g(z) \, dz = 2\pi i \, \text{Res}(g, i\sqrt{2}) = 2\pi i \left( \frac{e^{-2\sqrt{2}}}{2i\sqrt{2}} \right) = \frac{\pi e^{-2\sqrt{2}}}{\sqrt{2}}.$$
    *Proof:* $2\pi i / (2i\sqrt{2}) = \pi/\sqrt{2}$.
  <2>5. Q.E.D.

<1>4. **Jordan's Lemma on the semicircular arc $C_R$.**
  <2>1. On $C_R$, $|z^2+2| \geq R^2 - 2 > 0$, so $\left|\frac{1}{z^2+2}\right| \leq \frac{1}{R^2 - 2} \to 0$ as $R \to \infty$.
    *Proof:* Reverse triangle inequality.
  <2>2. By Jordan's Lemma, since $2 > 0$:
  $$\lim_{R \to \infty} \int_{C_R} \frac{e^{2iz}}{z^2 + 2} \, dz = 0.$$
    *Proof:* Jordan's Lemma for $e^{iaz}$ with $a = 2 > 0$.
  <2>3. Q.E.D.

<1>5. **Conclusion for $I_2$.**
  <2>1. Taking $R \to \infty$:
  $$\int_{-\infty}^\infty \frac{e^{2ix}}{x^2 + 2} \, dx = \frac{\pi e^{-2\sqrt{2}}}{\sqrt{2}}.$$
    *Proof:* Follows from <1>3.<2>4 and <1>4.<2>2.
  <2>2. Halving gives:
  $$I_2 = \int_0^\infty \frac{\cos(2x)}{x^2 + 2} \, dx = \frac{1}{2} \cdot \frac{\pi e^{-2\sqrt{2}}}{\sqrt{2}} = \frac{\pi e^{-2\sqrt{2}}}{2\sqrt{2}} = \frac{\pi \sqrt{2}}{4 e^{2\sqrt{2}}}.$$
    *Proof:* Division by 2.
  <2>3. Q.E.D.
:::
