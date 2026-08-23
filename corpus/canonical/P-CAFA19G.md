---
schema: qual/card@1
id: P-CAFA19G
kind: problem
title: "The Perron function on the punctured disk with trivial boundary data is zero"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
solved: false
---

::: problem
Let $G = \mathbb{D} \setminus \{0\}$ and let $f$ be the function on $\partial G$ such that $f(z) = 0$ for $|z| = 1$ and $f(0) = 1$.
Show that the Perron function $u(z)$ of $f$, $$u(z) = \sup\{\phi(z) : \phi \text{ is subharmonic and } \forall a \in \partial G,\; \limsup_{\zeta \to a} \phi(\zeta) \leq f(a)\}$$ is identically zero.

Hint: Consider the family of functions $u_\epsilon(z) = \frac{\log|z|}{\log\epsilon}$ in the annulus $\epsilon < |z| < 1$ for $\epsilon > 0$.
:::
