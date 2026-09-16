---
schema: qual/card@1
id: FF-HO7RN
kind: fact
title: Cauchy estimates
prompts:
- State the Cauchy estimate for $\abs{f^{(n)}(0)}$.
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Estimates
  - Cauchy Integral Formula
relations: []
review: draft
---

::: {.fact}
Let $r>0$ and let $f$ be [[D-E7A5W|holomorphic]] on an open set containing the closed disc $\abs{z}\le r$.
Then for every integer $n\ge0$,
$$
\abs{f^{(n)}(0)} \leq \frac{n!}{r^{n}} \sup_{\abs{z}=r}\abs{f(z)}.
$$
:::
