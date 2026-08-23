---
schema: qual/card@1
id: P-RASP08A
kind: problem
title: "True/false on FTC, Urysohn, Baire category, and absolute continuity"
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
Determine if the statements below are True or False.

(a) Suppose $f : [0,1] \to \mathbb{C}$ is a continuous function that is differentiable a.e. with respect to Lebesgue measure. If $f' \in L^1([0,1])$, then
$$
f(1) - f(0) = \int_0^1 f'(x)\,dx.
$$

(b) Given any two points $a \neq b$ in a locally compact Hausdorff space, there is a real-valued continuous function $f$ such that $f(a) \neq f(b)$.

(c) Let $X$ be a Banach space and $\{f_n\}_{n=1}^{\infty}$ a sequence in the dual $X^*$ such that $f_n \neq 0$ for all $n$. Then the set $\{x \in X : f_n(x) \neq 0, \forall n = 1, 2, \ldots\}$ is dense in $X$.

(d) Let $X$ be a measurable space. Let $\nu$ be a complex measure on $X$ and $\mu$ a $\sigma$-finite positive measure on $X$. Suppose that there is a constant $C$ such that for every $f \in L^1(X, d\mu)$,
$$
\left|\int_X f\,d\nu\right| \leq C \left|\int_X f\,d\mu\right|.
$$
Then $d\nu = h\,d\mu$ for some $h \in L^1(X, d\mu)$.
:::
