---
schema: qual/card@1
id: P-RASP18F
kind: problem
title: "Layer-cake representation and Chebyshev inequality"
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
Let $f : \mathbb{R} \to [0,1]$ be a Borel measurable function. For $t \geq 0$, let $\varphi(t) = m(\{x \in \mathbb{R} : f(x) \geq t\})$.

1. Assume that $f \in L^1(\mathbb{R}, m)$. Prove that $\varphi(t) \leq \frac{1}{t}\|f\|_1$ for all $t > 0$.

2. Prove that $\int_{\mathbb{R}} f\,dm = \int_0^\infty \varphi(t)\,dt$.

3. Assume that $\varphi(t) \leq \frac{1}{\sqrt{t}}$ for all $t > 0$. Prove that $f \in L^1(\mathbb{R}, m)$.
:::
