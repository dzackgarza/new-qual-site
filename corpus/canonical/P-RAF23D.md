---
schema: qual/card@1
id: P-RAF23D
kind: problem
title: "Sinc function, Shannon sampling, and bandlimited functions"
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
Let $\operatorname{sinc} x = \frac{\sin \pi x}{\pi x}$ (with $\operatorname{sinc} 0 = 1$). Prove:

(i) If $a > 0$, $\hat{\chi}_{[-a,a]} = \check{\chi}_{[-a,a]} = 2a\operatorname{sinc}(2ax)$.

(ii) Let $\mathcal{H}_a = \{f \in L^2 : \hat{f}(\xi) = 0 \text{ if } |\xi| > a\}$. Then $\mathcal{H}_a$ is a Hilbert space and $\{\sqrt{2a}\operatorname{sinc}(2ax - k) : k \in \mathbb{Z}\}$ is an orthonormal basis.

(iii) If $f \in \mathcal{H}_a$, then $f \in C_0$ (continuous vanishing at infinity) and $f = \sum_{-\infty}^{\infty} f\!\left(\frac{k}{2a}\right)\operatorname{sinc}(2ax - k)$ in $L^2$.
:::
