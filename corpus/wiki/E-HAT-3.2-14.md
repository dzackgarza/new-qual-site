---
schema: qual/card@1
id: E-HAT-3.2-14
kind: exercise
title: "Surjection from $\\mathbb{CP}^\\infty$ to $\\mathbb{RP}^\\infty$ on cohomology"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
solved: false
---

Let $q: \mathbb{RP}^\infty \to \mathbb{CP}^\infty$ be the natural quotient map obtained by regarding both spaces as quotients of $S^\infty$, modulo multiplication by real scalars in one case and complex scalars in the other.
Show that the induced map $q^*: H^*(\mathbb{CP}^\infty; \mathbb{Z}) \to H^*(\mathbb{RP}^\infty; \mathbb{Z})$ is surjective in even dimensions by showing first by a geometric argument that the restriction $q: \mathbb{RP}^2 \to \mathbb{CP}^1$ induces a surjection on $H^2$ and then appealing to cup product structures.

Next, form a quotient space $X$ of $\mathbb{RP}^\infty \amalg \mathbb{CP}^n$ by identifying each point $x \in \mathbb{RP}^{2n}$ with $q(x) \in \mathbb{CP}^n$.
Show there are ring isomorphisms $H^*(X; \mathbb{Z}) \approx \mathbb{Z}[\alpha]/(2\alpha^{n+1})$ and $H^*(X; \mathbb{Z}_2) \approx \mathbb{Z}_2[\alpha, \beta]/(\beta^2 - \alpha^{2n+1})$, where $|\alpha| = 2$ and $|\beta| = 2n+1$.
Make a similar construction and analysis for the quotient map $q: \mathbb{CP}^\infty \to \mathbb{HP}^\infty$.
