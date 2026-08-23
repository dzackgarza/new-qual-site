---
schema: qual/card@1
id: P-RAF21G
kind: problem
title: "Heisenberg-type uncertainty inequality via Fourier analysis"
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
  - Inequalities
  - L2 Spaces
relations: []
review: draft
solved: false
---

::: problem
For any $f \in L^2(\mathbb{R}) \cap C^1(\mathbb{R})$ show that
$$
\left(\int_\mathbb{R} x^2 |f(x)|^2 \, dx\right) \left(\int_\mathbb{R} \xi^2 |\hat{f}(\xi)|^2 \, d\xi\right) \geq \frac{1}{16\pi^2} \left(\int_\mathbb{R} |f(x)|^2 \, dx\right)^2.
$$

Here $\hat{f}$ is the Fourier transform of $f$ and $dx, d\xi$ represent the Lebesgue measure on $\mathbb{R}$.
:::
