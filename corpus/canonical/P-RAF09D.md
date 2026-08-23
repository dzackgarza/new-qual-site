---
schema: qual/card@1
id: P-RAF09D
kind: problem
title: "Principal value integral and distributional derivatives of log|x|"
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
If $f \in L^1((-\infty, -\delta) \cup (\delta, \infty))$ for every $\delta > 0$, define its principal value integral to be
$$
\mathrm{PV} \int_{-\infty}^{\infty} f(x)\,dx = \lim_{\delta \to 0} \left(\int_{-\infty}^{-\delta} + \int_{\delta}^{\infty}\right) f(x)\,dx,
$$
if the limit exists. For $\phi \in \mathcal{D}(\mathbb{R})$, put $\Lambda(\phi) = \int_{-\infty}^{\infty} \dot{\phi}(x) \log|x|\,dx$. Show that

(a) $\Lambda'(\phi) = \mathrm{PV} \int_{-\infty}^{\infty} \frac{\phi(x)}{x}\,dx$,

(b) $\Lambda''(\phi) = -\mathrm{PV} \int_{-\infty}^{\infty} \frac{\phi(x) - \phi(0)}{x^2}\,dx$.
:::
