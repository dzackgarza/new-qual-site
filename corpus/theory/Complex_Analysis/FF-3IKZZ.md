---
schema: qual/card@1
id: FF-3IKZZ
kind: fact
title: Maximum Length Lemma
prompts:
- State the maximum length (ML) estimate for a contour integral.
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Integrals
relations:
- kind: variant-of
  target: T-SFXI7
review: draft
---

::: {.fact}
$$
\abs{\int _\gamma f} \leq \sup_{z\in \gamma} \abs{f(z)} \cdot \ell(\gamma)
.$$
:::
