---
schema: qual/card@1
id: P-MMAQ-FLFHFN7LEF
kind: problem
title: Use residues to compute the integral
classification:
  areas:
  - complex-analysis
  topics:
  - integrals
  - residues
relations: []
review: draft
solved: true
---

::: problem
Use residues to compute the integral `\begin{align*} \int_{0}^{\infty} \dfrac{\cos x}{(x^2+1)^2} \mathrm{d}x \end{align*}`{=tex}
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Compute the definite integral $I = \int_{0}^{\infty} \frac{\cos x}{(x^2+1)^2} \, dx$ using the calculus of residues.

* * *

### Step 1: Parity and Complex Extension

<1>1. **Symmetry of the integrand over the real line.** <2>1. The integrand $g(x) = \frac{\cos x}{(x^2+1)^2}$ is an even function: $g(-x) = \frac{\cos(-x)}{((-x)^2+1)^2} = \frac{\cos x}{(x^2+1)^2} = g(x)$.
*Proof:* $\cos(-x) = \cos x$ and $(-x)^2 = x^2$.
<2>2. Therefore, $I = \frac{1}{2} \int_{-\infty}^{\infty} \frac{\cos x}{(x^2+1)^2} \, dx = \frac{1}{2} \text{Re}\left( \int_{-\infty}^{\infty} \frac{e^{ix}}{(x^2+1)^2} \, dx \right)$.
*Proof:* $e^{ix} = \cos x + i \sin x$, and $\frac{\sin x}{(x^2+1)^2}$ is an odd function whose integral over $(-\infty, \infty)$ vanishes.
<2>3. Define $f(z) = \frac{e^{iz}}{(z^2+1)^2} = \frac{e^{iz}}{(z-i)^2(z+i)^2}$.
*Proof:* Factoring $z^2+1 = (z-i)(z+i)$.
<2>4. Q.E.D.

* * *

### Step 2: Set up Contour Integration in the Upper Half-Plane

<1>2. **Let $\Gamma_R = [-R, R] \cup C_R$ where $C_R = \{R e^{i\theta} : \theta \in [0, \pi]\}$ with $R > 1$.** <2>1. $\Gamma_R$ is a simple closed positively oriented contour enclosing the upper half-plane disk region.
*Proof:* Standard semicircular contour.
<2>2. The only singularity of $f(z)$ in the upper half-plane $\mathbb{H}$ is at $z = i$, which is a pole of order 2. *Proof:* The zeros of $(z^2+1)^2$ are $z = \pm i$.
Only $z = i$ has $\text{Im}(z) > 0$.
<2>3. By the Cauchy Residue Theorem: $$\oint_{\Gamma_R} f(z) \, dz = \int_{-R}^R \frac{e^{ix}}{(x^2+1)^2} \, dx + \int_{C_R} f(z) \, dz = 2\pi i \, \text{Res}(f, i).$$ *Proof:* Application of the residue theorem to the single enclosed pole $z = i$.
<2>4. Q.E.D.

* * *

### Step 3: Compute the Residue at $z = i$

<1>3. **$\text{Res}(f, i) = \frac{1}{4ie}$.** <2>1. For a pole of order 2, the residue formula is: $$\text{Res}(f, i) = \lim_{z \to i} \frac{d}{dz} \left[ (z-i)^2 f(z) \right] = \lim_{z \to i} \frac{d}{dz} \left[ \frac{e^{iz}}{(z+i)^2} \right].$$ *Proof:* Standard residue formula for order 2 poles.
<2>2. Compute the derivative using the quotient rule: $$\frac{d}{dz}\left( \frac{e^{iz}}{(z+i)^2} \right) = \frac{i e^{iz}(z+i)^2 - e^{iz} \cdot 2(z+i)}{(z+i)^4} = \frac{e^{iz} \big( i(z+i) - 2 \big)}{(z+i)^3}.$$ *Proof:* Direct differentiation.
<2>3. Evaluate at $z = i$: $$\text{Res}(f, i) = \frac{e^{i(i)} \big( i(2i) - 2 \big)}{(2i)^3} = \frac{e^{-1} (-2 - 2)}{-8i} = \frac{-4 e^{-1}}{-8i} = \frac{1}{2i e} = -\frac{i}{2e}.$$ *Proof:* Arithmetic evaluation: $i^2 = -1$, $(2i)^3 = -8i$.
<2>4. Therefore, $2\pi i \, \text{Res}(f, i) = 2\pi i \left( -\frac{i}{2e} \right) = \frac{2\pi}{2e} = \frac{\pi}{e}$.
*Proof:* $i(-i) = 1$.
<2>5. Q.E.D.

* * *

### Step 4: Vanishing of the Arc Integral

<1>4. **$\lim_{R \to \infty} \int_{C_R} f(z) \, dz = 0$.** <2>1. On $C_R$, $z = R e^{i\theta}$ with $\theta \in [0, \pi]$, so $\text{Im}(z) = R \sin\theta \geq 0$.
*Proof:* $\sin\theta \geq 0$ for $\theta \in [0, \pi]$.
<2>2. Thus $|e^{iz}| = e^{-\text{Im}(z)} = e^{-R\sin\theta} \leq 1$.
*Proof:* Exponential of non-positive real number.
<2>3. By the reverse triangle inequality, $|z^2+1| \geq |z|^2 - 1 = R^2 - 1$, so $|(z^2+1)^2| \geq (R^2-1)^2$.
*Proof:* Reverse triangle inequality for $R > 1$.
<2>4. The integrand is bounded by $|f(z)| \leq \frac{1}{(R^2-1)^2}$ on $C_R$, and the length of $C_R$ is $\pi R$.
*Proof:* Definition of arc length and supremum bound.
<2>5. By the $ML$-inequality: $$\left| \int_{C_R} f(z) \, dz \right| \leq \frac{\pi R}{(R^2-1)^2} \to 0 \quad \text{as } R \to \infty.$$ *Proof:* The degree of the denominator ($R^4$) exceeds the numerator ($R$) by 3. <2>6. Q.E.D.

* * *

### Step 5: Final Evaluation

<1>5. **Compute the real integral $I$.** <2>1. Taking the limit as $R \to \infty$ in <1>2.<2>3: $$\int_{-\infty}^\infty \frac{e^{ix}}{(x^2+1)^2} \, dx = 2\pi i \, \text{Res}(f, i) - \lim_{R\to\infty} \int_{C_R} f(z)\,dz = \frac{\pi}{e} - 0 = \frac{\pi}{e}.$$ *Proof:* Follows from <1>3.<2>4 and <1>4.<2>5. <2>2. Therefore, from <1>1.<2>2: $$I = \int_0^\infty \frac{\cos x}{(x^2+1)^2} \, dx = \frac{1}{2} \text{Re}\left( \frac{\pi}{e} \right) = \frac{\pi}{2e}.$$ *Proof:* Halving the bilateral integral.
<2>3. Q.E.D.
:::
