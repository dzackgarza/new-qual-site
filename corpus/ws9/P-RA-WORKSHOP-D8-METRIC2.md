---
schema: qual/card@1
id: P-RA-WORKSHOP-D8-METRIC2
kind: problem
title: 'Characterize lower and upper semicontinuity by open inverse images and limits'
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

:::{.problem title="?"}
(May 2017, 6) Let $(X,d)$ be a metric space. A function $f:X\to\mathbb R$ is said to be lower semi-continuous
(l.s.c.) if
$f^{-1}(a,\infty)=\{x\in X:f(x)>a\}$ is open in $X$ for every $a\in\mathbb R$. Analogously, $f$ is upper
semi-continuous (u.s.c.) if
$f^{-1}(-\infty,b)=\{x\in X:f(x)<b\}$ is open in $X$ for every $b\in\mathbb R$.

(a) Prove that a function $f:X\to\mathbb R$ is continuous if and only if $f$ is both l.s.c. and u.s.c.

(b) Prove that $f$ is lower semi-continuous if and only if
$$
\liminf_{n\to\infty}f(x_n)\ge f(x)
$$
whenever $\{x_n\}_{n=1}^{\infty}\subseteq X$ is such that $x_n\to x$ in $X$.
:::
