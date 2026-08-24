---
schema: qual/card@1
id: P-RASP23G
kind: problem
title: "Riesz fractional integration formula via Fourier transform"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
solved: false
---

::: problem
Let $\Gamma(z)$ be the gamma function defined by $\Gamma(z) = \int_0^\infty e^{-t} t^{z-1}\,dt$ for $z$ with $\operatorname{Re}(z) > 0$.
For a compact support function $\phi$, prove that for any $0 < \alpha < n$,
$$
\frac{\Gamma((n-\alpha)/2)}{\pi^{(n-\alpha)/2}} \int_{\mathbb{R}^n} |x|^{\alpha-n} \hat{\phi}(x)\,dx = \frac{\Gamma(\alpha/2)}{\pi^{\alpha/2}} \int_{\mathbb{R}^n} |\xi|^{-\alpha} \phi(\xi)\,d\xi.
$$

Hint: Use the Fourier transform of the Gaussian, the identity $\int \hat{f} g = \int f \hat{g}$ for $L^1$ functions and the change of variables for the integral in the definition of $\Gamma$.
:::
