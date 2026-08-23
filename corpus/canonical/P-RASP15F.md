---
schema: qual/card@1
id: P-RASP15F
kind: problem
title: "Fourier transform from L^1 to C_0 is not onto"
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
Let $g_k = \chi_{[-1,1]} * \chi_{[-k,k]}$.
Here $f * g$ is the convolution of $f$ and $g$.

(i) Compute $\|g_k\|_{L^\infty}$.

(ii) Compute the inverse Fourier transform of $g_k$, namely $\mathcal{F}^{-1}(g_k)$.

(iii) Using the above computation show that the Fourier transform $\mathcal{F} : L^1(\mathbb{R}) \to C_0(\mathbb{R})$ is not onto.
Here $C_0(\mathbb{R})$ is the space of continuous functions which vanish at infinity.

Hint: Use the open mapping theorem.
:::
