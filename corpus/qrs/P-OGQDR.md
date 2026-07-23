---
schema: qual/card@1
id: P-OGQDR
kind: problem
title: "Suppose $f: \\DD \\to \\CC$ is holomorphic and let $d \\definedas \\sup_{z,\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
Suppose $f: \DD \to \CC$ is holomorphic and let $d \definedas \sup_{z, w\in \DD}\abs{f(z) - f(w)}$ be the diameter of the image of $f$.
Show that $2 \abs{f'(0)} \leq d$, and that equality holds iff $f$ is linear, so $f(z) = a_1 z + a_2$.

> Hint: 
\[
2f'(0) = \frac{1}{2\pi i} \int_{\abs \xi = r} \frac{ f(\xi) - f(-\xi)  }{\xi^2} ~d\xi
\]
whenever $0<r<1$.

