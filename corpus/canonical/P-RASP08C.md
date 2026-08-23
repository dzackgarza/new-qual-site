---
schema: qual/card@1
id: P-RASP08C
kind: problem
title: "Schur test inequality for integral operator"
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
Show that, for measurable functions $f, g : [1, \infty) \to [0, \infty)$, the following inequality holds:
$$
\left|\int_{[1,\infty)^2} e^{-xy} f(x) g(y)\,dx\,dy\right| \leq \frac{1}{2\epsilon} \left(\int_1^\infty |f(x)|^2\,dx\right)^{1/2} \left(\int_1^\infty |g(x)|^2\,dx\right)^{1/2},
$$
where $dx$ denotes the Lebesgue measure on $[1, \infty)$ and $dx\,dy$ denotes the Lebesgue measure on $[1, \infty)^2 = [1, \infty) \times [1, \infty)$.
:::
