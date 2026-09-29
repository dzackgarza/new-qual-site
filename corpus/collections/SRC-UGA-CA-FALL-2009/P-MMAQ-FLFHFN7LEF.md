---
schema: qual/card@1
id: P-MMAQ-FLFHFN7LEF
kind: problem
title: '$\int_0^\infty \frac{\cos x}{(1+x^2)^2}\,dx$ by residues'
classification:
  areas:
  - complex-analysis
  topics:
  - Integrals
  - Residues
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Complex Analysis (1) of Arango-Piñeros, Some quals problems; merged the duplicate P-EMCA1, whose solution repeats this residue computation."
---

::: {.problem}
Use residues to compute the integral `\begin{align*} \int_{0}^{\infty} \dfrac{\cos x}{(x^2+1)^2} \mathrm{d}x \end{align*}`{=tex}
:::

::: {.solution}
**Goal:** Compute the definite integral $I = \int_{0}^{\infty} \frac{\cos x}{(x^2+1)^2} \, dx$ using the calculus of residues.

* * *

### Step 1: Parity and Complex Extension

::: pf

::: pf-step
**Symmetry of the integrand over the real line.**

::: pf-proof

::: pf-step
The integrand $g(x) = \frac{\cos x}{(x^2+1)^2}$ is an even function: $g(-x) = \frac{\cos(-x)}{((-x)^2+1)^2} = \frac{\cos x}{(x^2+1)^2} = g(x)$.

::: pf-proof
$\cos(-x) = \cos x$ and $(-x)^2 = x^2$.
:::

:::

::: {.pf-step #s1-2}
Therefore, $I = \frac{1}{2} \int_{-\infty}^{\infty} \frac{\cos x}{(x^2+1)^2} \, dx = \frac{1}{2} \text{Re}\left( \int_{-\infty}^{\infty} \frac{e^{ix}}{(x^2+1)^2} \, dx \right)$.

::: pf-proof
$e^{ix} = \cos x + i \sin x$, and $\frac{\sin x}{(x^2+1)^2}$ is an odd function whose integral over $(-\infty, \infty)$ vanishes.
:::

:::

::: pf-step
Define $f(z) = \frac{e^{iz}}{(z^2+1)^2} = \frac{e^{iz}}{(z-i)^2(z+i)^2}$.

::: pf-proof
Factoring $z^2+1 = (z-i)(z+i)$.
:::

:::

:::

:::

:::

* * *

### Step 2: Set up Contour Integration in the Upper Half-Plane

::: pf

::: pf-step
**Let $\Gamma_R = [-R, R] \cup C_R$ where $C_R = \{R e^{i\theta} : \theta \in [0, \pi]\}$ with $R > 1$.**

::: pf-proof

::: pf-step
$\Gamma_R$ is a simple closed positively oriented contour enclosing the upper half-plane disk region.

::: pf-proof
Standard semicircular contour.
:::

:::

::: pf-step
The only singularity of $f(z)$ in the upper half-plane $\mathbb{H}$ is at $z = i$, which is a pole of order 2.

::: pf-proof
The zeros of $(z^2+1)^2$ are $z = \pm i$.
Only $z = i$ has $\text{Im}(z) > 0$.
:::

:::

::: {.pf-step #s2-3}
By the Cauchy Residue Theorem: $$\oint_{\Gamma_R} f(z) \, dz = \int_{-R}^R \frac{e^{ix}}{(x^2+1)^2} \, dx + \int_{C_R} f(z) \, dz = 2\pi i \, \text{Res}(f, i).$$

::: pf-proof
Application of the residue theorem to the single enclosed pole $z = i$.
:::

:::

:::

:::

:::

* * *

### Step 3: Compute the Residue at $z = i$

::: pf

::: pf-step
**$\text{Res}(f, i) = \frac{1}{4ie}$.**

::: pf-proof

::: pf-step
For a pole of order 2, the residue formula is: $$\text{Res}(f, i) = \lim_{z \to i} \frac{d}{dz} \left[ (z-i)^2 f(z) \right] = \lim_{z \to i} \frac{d}{dz} \left[ \frac{e^{iz}}{(z+i)^2} \right].$$

::: pf-proof
Standard residue formula for order 2 poles.
:::

:::

::: pf-step
Compute the derivative using the quotient rule: $$\frac{d}{dz}\left( \frac{e^{iz}}{(z+i)^2} \right) = \frac{i e^{iz}(z+i)^2 - e^{iz} \cdot 2(z+i)}{(z+i)^4} = \frac{e^{iz} \big( i(z+i) - 2 \big)}{(z+i)^3}.$$

::: pf-proof
Direct differentiation.
:::

:::

::: pf-step
Evaluate at $z = i$: $$\text{Res}(f, i) = \frac{e^{i(i)} \big( i(2i) - 2 \big)}{(2i)^3} = \frac{e^{-1} (-2 - 2)}{-8i} = \frac{-4 e^{-1}}{-8i} = \frac{1}{2i e} = -\frac{i}{2e}.$$

::: pf-proof
Arithmetic evaluation: $i^2 = -1$, $(2i)^3 = -8i$.
:::

:::

::: {.pf-step #s3-4}
Therefore, $2\pi i \, \text{Res}(f, i) = 2\pi i \left( -\frac{i}{2e} \right) = \frac{2\pi}{2e} = \frac{\pi}{e}$.

::: pf-proof
$i(-i) = 1$.
:::

:::

:::

:::

:::

* * *

### Step 4: Vanishing of the Arc Integral

::: pf

::: pf-step
**$\lim_{R \to \infty} \int_{C_R} f(z) \, dz = 0$.**

::: pf-proof

::: pf-step
On $C_R$, $z = R e^{i\theta}$ with $\theta \in [0, \pi]$, so $\text{Im}(z) = R \sin\theta \geq 0$.

::: pf-proof
$\sin\theta \geq 0$ for $\theta \in [0, \pi]$.
:::

:::

::: pf-step
Thus $|e^{iz}| = e^{-\text{Im}(z)} = e^{-R\sin\theta} \leq 1$.

::: pf-proof
Exponential of non-positive real number.
:::

:::

::: pf-step
By the reverse triangle inequality, $|z^2+1| \geq |z|^2 - 1 = R^2 - 1$, so $|(z^2+1)^2| \geq (R^2-1)^2$.

::: pf-proof
Reverse triangle inequality for $R > 1$.
:::

:::

::: pf-step
The integrand is bounded by $|f(z)| \leq \frac{1}{(R^2-1)^2}$ on $C_R$, and the length of $C_R$ is $\pi R$.

::: pf-proof
Definition of arc length and supremum bound.
:::

:::

::: {.pf-step #s4-5}
By the $ML$-inequality: $$\left| \int_{C_R} f(z) \, dz \right| \leq \frac{\pi R}{(R^2-1)^2} \to 0 \quad \text{as } R \to \infty.$$

::: pf-proof
The degree of the denominator ($R^4$) exceeds the numerator ($R$) by 3.
:::

:::

:::

:::

:::

* * *

### Step 5: Final Evaluation

::: pf

::: pf-step
**Compute the real integral $I$.**

::: pf-proof

::: pf-step
Taking the limit as $R \to \infty$ in step [](#s2-3){.pf-ref}: $$\int_{-\infty}^\infty \frac{e^{ix}}{(x^2+1)^2} \, dx = 2\pi i \, \text{Res}(f, i) - \lim_{R\to\infty} \int_{C_R} f(z)\,dz = \frac{\pi}{e} - 0 = \frac{\pi}{e}.$$

::: pf-proof
Follows from steps [](#s3-4){.pf-ref} and [](#s4-5){.pf-ref}.
:::

:::

::: pf-step
Therefore, from step [](#s1-2){.pf-ref}: $$I = \int_0^\infty \frac{\cos x}{(x^2+1)^2} \, dx = \frac{1}{2} \text{Re}\left( \frac{\pi}{e} \right) = \frac{\pi}{2e}.$$

::: pf-proof
Halving the bilateral integral.
:::

:::

:::

:::

:::
:::
