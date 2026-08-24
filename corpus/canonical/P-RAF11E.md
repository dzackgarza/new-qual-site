---
schema: qual/card@1
id: P-RAF11E
kind: problem
title: "Uniform convergence of Fourier series for Hölder continuous functions"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
---

::: problem
Let $f : \mathbb{R} \to \mathbb{R}$ be a $2\pi$-periodic function, i.e. $f(x) = f(x + 2\pi)$, such that there exists $C > 0$ (possibly large) and $\epsilon > 0$ (possibly small) with
$$
|f(x) - f(y)| \leq C|x - y|^{1/2 + \epsilon}.
$$
Show that the Fourier series of $f$ converges uniformly.

Hint: Half credit will be given for the special case $\epsilon = 1/2$, which can be treated more directly.
For the general case try computing $\int_0^{2\pi} |f(x+h) - f(x)|^2\,dx$ two different ways.
:::
