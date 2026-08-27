---
schema: qual/card@1
id: PR-WS6NT
kind: proposition
title: Duals of $L^p$ spaces
classification:
  areas:
  - real-analysis
  topics:
  - Dual Spaces
  - Lp Spaces
  - Radon-Nikodym
relations: []
review: draft
---

:::{.proposition}
For $p\inv + q\inv = 1$, with $1<p<\infty$, there is an isomorphism of Banach spaces
\[
\kappa: L^p(\mu) &\to L^q(\mu) \\
f &\mapsto (g \mapsto \int_X f g d\mu )
.\]

This is surjective by Radon-Nikodym, and an isometry by Holder's inequality, which is enough to be an isometric isomorphism.

:::
