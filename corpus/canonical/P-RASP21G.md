---
schema: qual/card@1
id: P-RASP21G
kind: problem
title: "Multiplying a sigma-finite Radon measure by a positive continuous function stays Radon"
classification:
  areas:
  - real-analysis
  topics:
  - Radon Measures
  - Riesz Representation
  - LCH Spaces
relations: []
review: draft
solved: false
---

::: problem
Let $\mu$ be a $\sigma$-finite Radon measure on an LCH space $X$, and $\varphi$ a positive continuous function on $X$. Show that $\nu(E) := \int_E \varphi \, d\mu$ defines a Radon measure $\nu$ on $X$.

Hint: First consider the positive linear functional $I(f) := \int f \varphi \, d\mu$ on $C_c(X)$ and show that $\nu$ coincides with the Radon measure associated with this functional on open sets.
:::