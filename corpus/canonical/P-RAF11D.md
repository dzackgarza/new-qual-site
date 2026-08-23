---
schema: qual/card@1
id: P-RAF11D
kind: problem
title: "Convolution with L^1 kernel preserves weak L^2 convergence"
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
Let $K \in L^1(\mathbb{R}^d)$ with Lebesgue measure. Suppose that $\psi_n \in L^2(\mathbb{R}^d)$ is a sequence of functions such that $\psi_n \to \psi$ (weak $L^2$ convergence), and also with the property that $\psi_n \equiv 0$ for $|x| > 1$. Show that
$$
f_n(x) = \int_{\mathbb{R}^d} K(x-y)\,\psi_n(y)\,dy
$$
converges to
$$
f(x) = \int_{\mathbb{R}^d} K(x-y)\,\psi(y)\,dy
$$
strongly in $L^2(\mathbb{R}^d)$.
:::
