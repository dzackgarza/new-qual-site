---
schema: qual/card@1
id: E-I6CYR
kind: exercise
title: $B(z,w)=\frac{\Gamma(z)\Gamma(w)}{\Gamma(z+w)}$
classification:
  areas:
  - complex-analysis
  topics:
  - Gamma Function
  - Integrals
  - Convolution
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

:::{.exercise}
Show that
\[
B(z, w) = {\Gamma(z) \Gamma(w) \over \Gamma(z+w)}
.\]

> Hint: find $\mcl(t^{z-1})$ and $\mcl(t^{z-1}\convolve t^{w-1})$.
:::

::: solution
**Goal:** Prove the identity $B(z, w) = \frac{\Gamma(z)\Gamma(w)}{\Gamma(z+w)}$ for $\operatorname{Re}(z) > 0$ and $\operatorname{Re}(w) > 0$ using Laplace transforms and convolution.

<1>1. Laplace transforms of power functions on $[0, \infty)$:
    *Proof:*
    <2>1. For $\operatorname{Re}(z) > 0$ and $s > 0$, define $f(t) = t^{z-1}$ for $t > 0$.
    <2>2. The Laplace transform of $f$ is
    $$\mathcal{L}\{f\}(s) = \int_0^\infty t^{z-1} e^{-st}\,dt.$$
    <2>3. Substituting $u = st$ (so $t = u/s$ and $dt = du/s$):
    $$\mathcal{L}\{f\}(s) = \int_0^\infty \left(\frac{u}{s}\right)^{z-1} e^{-u} \frac{du}{s} = \frac{1}{s^z} \int_0^\infty u^{z-1} e^{-u}\,du = \frac{\Gamma(z)}{s^z}.$$
    <2>4. Similarly, for $g(t) = t^{w-1}$ with $\operatorname{Re}(w) > 0$:
    $$\mathcal{L}\{g\}(s) = \frac{\Gamma(w)}{s^w}.$$

<1>2. Convolution of $f$ and $g$:
    *Proof:*
    <2>1. The convolution $(f * g)(x)$ for $x > 0$ is defined by
    $$(f * g)(x) = \int_0^x f(t) g(x - t)\,dt = \int_0^x t^{z-1} (x - t)^{w-1}\,dt.$$
    <2>2. Make the substitution $t = xu$, so $dt = x\,du$, where $u$ ranges from $0$ to $1$:
    $$(f * g)(x) = \int_0^1 (xu)^{z-1} (x - xu)^{w-1} x\,du = x^{z-1+w-1+1} \int_0^1 u^{z-1} (1 - u)^{w-1}\,du.$$
    <2>3. By definition of the Beta integral $B(z, w) = \int_0^1 u^{z-1} (1 - u)^{w-1}\,du$:
    $$(f * g)(x) = x^{z+w-1} B(z, w).$$

<1>3. Laplace transform of the convolution:
    *Proof:*
    <2>1. Taking the Laplace transform of $(f * g)(x) = B(z, w) x^{z+w-1}$:
    $$\mathcal{L}\{f * g\}(s) = B(z, w) \int_0^\infty x^{z+w-1} e^{-sx}\,dx = B(z, w) \frac{\Gamma(z+w)}{s^{z+w}}.$$
    <2>2. By the Convolution Theorem for Laplace transforms:
    $$\mathcal{L}\{f * g\}(s) = \mathcal{L}\{f\}(s) \cdot \mathcal{L}\{g\}(s) = \frac{\Gamma(z)}{s^z} \cdot \frac{\Gamma(w)}{s^w} = \frac{\Gamma(z)\Gamma(w)}{s^{z+w}}.$$

<1>4. Conclusion:
    *Proof:*
    Equating the two expressions from <1>3 gives
    $$B(z, w) \frac{\Gamma(z+w)}{s^{z+w}} = \frac{\Gamma(z)\Gamma(w)}{s^{z+w}} \implies B(z, w) = \frac{\Gamma(z)\Gamma(w)}{\Gamma(z+w)}.$$
:::
