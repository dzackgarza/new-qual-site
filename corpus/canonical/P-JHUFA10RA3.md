---
schema: qual/card@1
id: P-JHUFA10RA3
kind: problem
title: Schur's test for integral operators
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

Let $Tf(x) = \int_{\mathbb{R}^n} K(x,y) f(y) \, dy$, where $K(x,y)$ is a nonnegative measurable function on $\mathbb{R}^n \times \mathbb{R}^n$.
Suppose that there are measurable functions $p(x) > 0$ and $q(x) > 0$ on $\mathbb{R}^n$ and real numbers $\alpha, \beta > 0$ for which

$$\int K(x,y) q(y) \, dy \leq \alpha p(x),$$

for almost all $x$ and

$$\int p(x) K(x,y) \, dx \leq \beta q(y)$$

for almost all $y$.
Show that for $f \in L^2(\mathbb{R}^n)$ we have

$$\|Tf\|_{L^2} \leq \sqrt{\alpha \beta} \|f\|_{L^2}.$$

(This is called Schur's test.)
