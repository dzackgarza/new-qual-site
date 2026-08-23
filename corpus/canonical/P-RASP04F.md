---
schema: qual/card@1
id: P-RASP04F
kind: problem
title: "Multiplication operators on L^2 and bounded convergence"
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
Suppose $f : X \to [-1,1]$ is a measurable function and $\varphi : [-1,1] \to \mathbb{R}$ is a bounded Borel measurable function. Show:

(a) $\|M_{\varphi \circ f}\|_{B(L^2(\mu))} \leq \|\varphi\|_u := \sup_{|x| \leq 1} |\varphi(x)|$.

(b) Suppose $\varphi_n : [-1,1] \to \mathbb{R}$ are bounded Borel measurable functions converging boundedly to $\varphi$. Then for all $h \in L^2(\mu)$,
$$
L^2(\mu)\text{-}\lim_{n \to \infty} M_{\varphi_n \circ f}\,h = M_{\varphi \circ f}\,h.
$$

(c) Show by example that it is possible that $\lim_{n \to \infty} \|M_{\varphi_n \circ f}\|_{B(L^2(\mu))} \neq 0$ even though $\varphi_n \to 0$ boundedly.
:::
