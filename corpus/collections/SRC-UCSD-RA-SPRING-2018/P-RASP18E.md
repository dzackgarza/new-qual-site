---
schema: qual/card@1
id: P-RASP18E
kind: problem
title: "Convolution with a finite measure and Fourier multiplier"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
---

::: problem
Let $\mu$ be a finite positive measure on $(\mathbb{R}, \mathcal{B})$, $f : \mathbb{R} \to \mathbb{C}$ be a Borel measurable function, and for $x \in \mathbb{R}$, let
$$
(\mu * f)(x) := \begin{cases} \int_{\mathbb{R}} f(x - y)\,d\mu(y) & \text{if } \int_{\mathbb{R}} |f(x - y)|\,d\mu(y) < \infty, \\ 0 & \text{otherwise.} \end{cases}
$$

1. For $1 \leq p < \infty$ and $f \in L^p(m)$, show $\|\mu * f\|_{L^p(m)} \leq \mu(\mathbb{R}) \cdot \|f\|_{L^p(m)}$.

2. If $f \in L^1(\mathbb{R}, m)$, show $\widehat{\mu * f}(k) = \sqrt{2\pi}\,\hat{\mu}(k)\hat{f}(k)$ for all $k \in \mathbb{R}$.

3. If $f$ and $\hat{f}$ are in $L^1(\mathbb{R}, m)$, then
$$
(\mu * f)(x) = \int_{\mathbb{R}} \hat{\mu}(k)\hat{f}(k) e^{ikx}\,dk \quad \text{for } m\text{-a.e. } x.
$$
:::
