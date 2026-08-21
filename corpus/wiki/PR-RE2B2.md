---
schema: qual/card@1
id: PR-RE2B2
kind: proposition
title: Power Series are Smooth
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Holomorphic Functions
relations: []
review: draft
---

:::{.proposition title="Power Series are Smooth"}
Any power series is smooth (and thus holomorphic) on its disc of convergence, and its derivatives can be obtained using term-by-term differentiation:
\[
\dd{}{z} f(z) = \dd{}{z} \sum_{k\geq 0} c_k (z-z_0)^k = \sum_{k\geq 1} kc_k (z-z_0)^k
.\]
Moreover, the coefficients are given by
\[
c_k = {f^{(n)}(z_0) \over n! }
.\]
:::
