---
schema: qual/card@1
id: P-RAF09E
kind: problem
title: "Alternate proof of the Lebesgue-Radon-Nikodym theorem"
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
The following provides steps to give an alternate proof of the Lebesgue-Radon-Nikodym theorem. Suppose that $\mu$ and $\nu$ are positive finite measures on $(X, \mathcal{M})$ and let $\lambda = \mu + \nu$.

(a) The map $f \mapsto \int f\,d\nu$ is a bounded linear functional on $L^2(\lambda)$, so there exists $g \in L^2(\lambda)$ such that for any $f \in L^2(\lambda)$, $\int f(1-g)\,d\nu = \int fg\,d\mu$.

(b) $0 \leq g \leq 1$ $\lambda$-a.e., so we can assume that $0 \leq g \leq 1$ everywhere.

(c) Let $A = \{x : g(x) < 1\}$, $B = \{x : g(x) = 1\}$, and set $\nu_a(E) = \nu(A \cap E)$, $\nu_s(E) = \nu(B \cap E)$. Then $\nu_a \ll \mu$ and $\nu_s \perp \mu$.

(d) Moreover $d\nu_a = g(1-g)^{-1}\,d\mu$.
:::
