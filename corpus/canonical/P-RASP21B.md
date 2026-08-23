---
schema: qual/card@1
id: P-RASP21B
kind: problem
title: "Uniform integrability: L^p boundedness, failure at p=1, and convergence in measure"
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Integrability
  - Lp Spaces
  - Vitali Convergence Theorem
relations: []
review: draft
solved: false
---

::: problem
Let $(X, \mathcal{M}, \mu)$ be a finite measure space, and let $F \subseteq L^1(\mu)$.
We say that $F$ is uniformly integrable iff for every $\varepsilon > 0$ there is $\delta > 0$ such that $|\int_E f \, d\mu| < \varepsilon$ whenever $f \in F$ and $E \in \mathcal{M}$ satisfies $\mu(E) < \delta$.

(a) If $p \in (1, \infty]$ and $F \subseteq L^p(\mu)$ is bounded, prove that $F$ is uniformly integrable.

(b) Give an example where (a) fails for $p = 1$.

(c) Let $f_n, f \in L^1(\mu)$ and assume that $F := \{f_1, f_2, \ldots\}$ is uniformly integrable.
If $f_n \to f$ in measure, prove that $f_n \to f$ in $L^1(\mu)$.
:::
