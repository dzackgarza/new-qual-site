---
schema: qual/card@1
id: P-RAF20D
kind: problem
title: "Limits of L^p norms: power means approaching the measure of support and the essential supremum"
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Monotone Convergence
  - Essential Supremum
relations: []
review: draft
solved: false
---

::: problem
Let $(X, \mathcal{M}, \mu)$ be a finite measure space.
Prove the following:

(1) If $f \in L^1(\mu)$ and $f \geq 0$ on $X$, then $f^\alpha \in L^1(\mu)$ for any $\alpha \in (0, 1)$ and
$$
\lim_{\alpha \to 0^+} \int_X f^\alpha \, d\mu = \mu(\{x \in X : f(x) > 0\}).
$$

(2) If $g \in L^\infty(\mu)$ with $\|g\|_\infty > 0$, then $g \in L^p(\mu)$ for any $p \in [1, \infty)$ and
$$
\lim_{p \to +\infty} \int_X \frac{|g|^{p+1} \, d\mu}{\int_X |g|^p \, d\mu} = \|g\|_\infty.
$$
:::
