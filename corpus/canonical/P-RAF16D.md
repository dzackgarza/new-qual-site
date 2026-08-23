---
schema: qual/card@1
id: P-RAF16D
kind: problem
title: "Conditional expectation via Radon-Nikodym"
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
Let $(X, \mathcal{M}, \mu)$ be a measure space with $\mu(X) = 1$, $\mathcal{M}_0$ a sub-$\sigma$-algebra of $\mathcal{M}$, and $\nu = \mu|_{\mathcal{M}_0}$ (the restriction of $\mu$ onto $\mathcal{M}_0$). Let $f \in L^1(\mathcal{M}, \mu)$ be real-valued.
Use the Radon-Nikodym Theorem to prove that there exists a unique $g \in L^1(\mathcal{M}_0, \nu)$ such that
$$
\int_E f\,d\mu = \int_E g\,d\nu \qquad \forall E \in \mathcal{M}_0.
$$
(Note that $g$ is, but $f$ may not be, measurable with respect to $\mathcal{M}_0$.)
:::
