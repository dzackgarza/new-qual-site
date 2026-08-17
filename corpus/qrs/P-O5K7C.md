---
schema: qual/card@1
id: P-O5K7C
kind: problem
title: Fresnel integrals $\int_0^\infty\sin(x^2)\,dx=\int_0^\infty\cos(x^2)\,dx=\frac{\sqrt{2\pi}}{4}$
classification:
  areas:
  - complex-analysis
  topics:
  - residues
  - contour-integration
  - integrals
relations: []
review: draft
solved: true
---

::: problem
Show that
\[
\int_{0}^{\infty} \sin \left(x^{2}\right) d x=\int_{0}^{\infty} \cos \left(x^{2}\right) d x=\frac{\sqrt{2 \pi}}{4}
.\]

> Hint: integrate $e^{-x^2}$ over the following contour, using the fact that $\int_{-\infty}^{\infty} e^{-x^{2}} d x=\sqrt{\pi}$:


![Image](../../assets/figures/2020-02-03-13%3A51.png)\
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Show $\int_0^\infty \sin(x^2)\, dx = \int_0^\infty \cos(x^2)\, dx = \frac{\sqrt{2\pi}}{4}$ by integrating $e^{-z^2}$ over a sector of angle $\pi/4$.

<1>1. Set up the contour: the sector $\Gamma_R$ with vertices $0$, $R$, and $Re^{i\pi/4}$, traversed as $0 \to R$ along the real axis, then along the arc $\abs{z} = R$ to $Re^{i\pi/4}$, then back along the ray $\arg z = \pi/4$ to $0$.
    Proof: $e^{-z^2}$ is entire, so by the Cauchy integral theorem $\int_{\Gamma_R} e^{-z^2}\, dz = 0$ for every $R$.

<1>2. $\int_0^R e^{-x^2}\, dx \to \frac{\sqrt{\pi}}{2}$ as $R \to \infty$.
    Proof: This is the given fact $\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt\pi$ together with evenness: $\int_0^\infty e^{-x^2} dx = \frac{1}{2}\int_{-\infty}^\infty e^{-x^2} dx = \frac{\sqrt\pi}{2}$.

<1>3. The arc contribution $\int_{\text{arc}} e^{-z^2}\, dz \to 0$ as $R \to \infty$.
    Proof: On the arc $z = Re^{i\theta}$, $0 \leq \theta \leq \pi/4$, $\abs{e^{-z^2}} = e^{-R^2 \cos 2\theta}$; and $\cos 2\theta \geq \cos(2\theta) \geq 0$ with $\cos 2\theta \geq 1/\sqrt2$ for $0 \leq \theta \leq \pi/8$ and the standard estimate gives $\abs{\int_{\text{arc}}} \leq R\int_0^{\pi/4} e^{-R^2\cos 2\theta}\, d\theta \to 0$ as $R\to\infty$ (split the integral at $\pi/8$; on $[\pi/8, \pi/4]$ bound $e^{-R^2\cos2\theta}$ by the endpoint value, or note the integrand is exponentially small on both pieces).

<1>4. $\int_{\text{ray}} e^{-z^2}\, dz = -e^{i\pi/4}\int_0^R e^{-ir^2}\, dr$.
    Proof: On the ray $z = re^{i\pi/4}$, $z^2 = r^2 e^{i\pi/2} = ir^2$ and $dz = e^{i\pi/4} dr$; traversed back toward $0$, the integral is $\int_R^0 e^{-ir^2} e^{i\pi/4}\, dr = -e^{i\pi/4}\int_0^R e^{-ir^2}\, dr$.

<1>5. Take $R \to \infty$ in <1>1 and solve: $\int_0^\infty e^{-ir^2}\, dr = e^{-i\pi/4}\frac{\sqrt\pi}{2}$.
    Proof: By <1>1, $\int_0^R e^{-x^2} dx + \text{(arc)} + \int_{\text{ray}} = 0$; passing to the limit with <1>2, <1>3 and <1>4 gives $\frac{\sqrt\pi}{2} - e^{i\pi/4}\int_0^\infty e^{-ir^2} dr = 0$, i.e. $\int_0^\infty e^{-ir^2} dr = e^{-i\pi/4}\frac{\sqrt\pi}{2}$.

<1>6. Extract real and imaginary parts.
    Proof: $e^{-i\pi/4} = \frac{\sqrt2}{2}(1 - i)$, so from <1>5, $\int_0^\infty \cos(r^2)\, dr = \Re\int_0^\infty e^{-ir^2} dr = \frac{\sqrt2}{2}\cdot\frac{\sqrt\pi}{2} = \frac{\sqrt{2\pi}}{4}$ and $\int_0^\infty \sin(r^2)\, dr = -\Im\int_0^\infty e^{-ir^2} dr = \frac{\sqrt2}{2}\cdot\frac{\sqrt\pi}{2} = \frac{\sqrt{2\pi}}{4}$.

<1>7. Q.E.D.
    Proof: <1>6 proves both identities.

:::
