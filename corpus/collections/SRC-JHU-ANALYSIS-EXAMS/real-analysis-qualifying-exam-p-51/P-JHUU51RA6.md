---
schema: qual/card@1
id: P-JHUU51RA6
kind: problem
title: "The principal value distribution is the derivative of log |x|"
classification:
  areas:
  - real-analysis
  topics:
  - Distributions
relations: []
review: draft
---

::: problem
Let $u \in \mathcal{D}'(\mathbb{R})$be given by

\[
(u, \varphi) = \lim_{\varepsilon \to 0^{+}} \left[ \int_{-\infty}^{-\varepsilon} \frac{\varphi(x)}{x}\, dx + \int_{\varepsilon}^{+\infty} \frac{\varphi(x)}{x}\, dx \right], \qquad \forall\ \varphi \in \mathcal{D}(\mathbb{R}) = \mathcal{C}_c^{\infty}(\mathbb{R}).
\]


Show that the above limit exists and that $u$ is the distribution derivative of the function $f \in L^1_{\mathrm{loc}}(\mathbb{R})$ given by $f(x) = \log|x|$.
:::
