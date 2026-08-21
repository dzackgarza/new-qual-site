---
schema: qual/card@1
id: P-AZFIB
kind: problem
title: $2|f'(0)|\le\operatorname{diam} f(\DD)$, with equality iff $f$ is linear
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Estimates
  - Schwarz Lemma
  - Cauchy Integral Formula
relations: []
review: draft
solved: false
---

::: problem
Suppose $f: \DD \to \CC$ is holomorphic and let $d \definedas \sup_{z, w\in \DD}\abs{f(z) - f(w)}$ be the diameter of the image of $f$.
Show that $2 \abs{f'(0)} \leq d$, and that equality holds iff $f$ is linear, so $f(z) = a_1 z + a_2$.

> Hint:
\[
2f'(0) = \frac{1}{2\pi i} \int_{\abs \xi = r} \frac{ f(\xi) - f(-\xi)  }{\xi^2} ~d\xi
\]
whenever $0<r<1$.
:::
