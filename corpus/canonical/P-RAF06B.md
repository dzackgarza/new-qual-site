---
schema: qual/card@1
id: P-RAF06B
kind: problem
title: "L^p convergence implies convergence in measure; converse with domination"
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Convergence in Measure
  - Dominated Convergence
relations: []
review: draft
solved: false
---

::: problem
Recall that $f_n \to f$ in measure if, for every $\varepsilon > 0$, $\mu(\{x : |f(x) - f_n(x)| \geq \varepsilon\}) \to 0$ as $n \to \infty$.
Let $1 \leq p < \infty$.

(a) Suppose $f_n \to f$ in $L^p(X, \mu)$.
Show that $f_n \to f$ in measure.

(b) Suppose $f_n \to f$ in measure and $|f_n| \leq g$ a.e. with $g \in L^p(X, \mu)$.
Show that $f \in L^p(X, \mu)$ and $f_n \to f$ in $L^p(X, \mu)$.
:::
