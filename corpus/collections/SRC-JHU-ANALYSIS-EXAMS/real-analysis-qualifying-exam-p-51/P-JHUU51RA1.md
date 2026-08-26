---
schema: qual/card@1
id: P-JHUU51RA1
kind: problem
title: "Quantitative Riemann-Lebesgue decay under vanishing endpoint conditions"
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
relations: []
review: draft
---

::: problem
Let $f : [0,2] \to \mathbb{R}$ be a $\mathcal{C}^{1}$ function such that $f(x)$ and $f'(x)$ vanish at $x = 0$ and at $x = 2$.
Prove that for all $\varepsilon > 0$ there exists $t_{\varepsilon} \in \mathbb{R}^{+}$such that

\[
\left| \int_0^2 f(x) e^{itx}\, dx \right| \leq \frac{\varepsilon}{t} \qquad \text{for } t \geq t_{\varepsilon}.
\]
:::
