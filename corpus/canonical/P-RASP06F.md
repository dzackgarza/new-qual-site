---
schema: qual/card@1
id: P-RASP06F
kind: problem
title: "Sobolev-type embedding via weighted L^p norms"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
---

::: problem
For each $N \in \mathbb{R}$ define in $\mathbb{R}^n$ the measures $d\mu_N := (1 + |x|)^N\,dx$ and, for each $1 \leq p < \infty$, the norms
$$
\|f\|_{p,N} := \|f\|_{L^p(\mathbb{R}^n, d\mu_N)} = \left(\int_{\mathbb{R}^n} |f(x)|^p (1 + |x|)^N\,dx\right)^{1/p}.
$$

(a) Show that for every $t > 0$ there is a constant $C_t$ such that for every $1 \leq r < p < \infty$ and every
$$
N_t := \frac{Np + n(p-r) + t(p-r)}{r}
$$
the estimate $\|f\|_{r,N} \leq C_t \|f\|_{p,N_t}$ holds.

(b) Show that the constants $C_t$ can be chosen such that $C_t \to 0$ as $t \to \infty$.

Hint: For part (a), observe that $1 = (1 + |x|)^M / (1 + |x|)^M$.
:::
