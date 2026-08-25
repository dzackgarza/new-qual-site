---
schema: qual/card@1
id: P-RASP15C
kind: problem
title: "Extension of a Radon measure from a closed subspace via Riesz-Markov"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
---

::: problem
Let $X$ be a locally compact Hausdorff space.
Let $Y$ be a closed subspace and $\mu$ be a Radon measure on $Y$.
Define a linear functional on $C_c(X)$ by $I(f) = \int_Y (f|_Y)\,d\mu$.

Prove that: (i) $I(f)$ is a positive linear functional; (ii) The functional $I(f) = \int_X f\,d\nu$ induces a Radon measure $\nu$ (via the Riesz-Markov theorem) which satisfies $\nu(E) = \mu(E \cap Y)$.

Precisely you need to show that (a) $\nu$ as defined above is a Radon measure; (b) the linear functional $I(f)$ can be represented by $\int_X f\,d\nu$.
:::
