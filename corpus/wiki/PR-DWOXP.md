---
schema: qual/card@1
id: PR-DWOXP
kind: proposition
title: "Limits of differentiable functions need not be differentiable"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
:::{.proposition title="Limits of differentiable functions need not be differentiable"}
\[
\lim_{n\to \infty} \dd{}{x} f_n \neq \dd{}{n} \qty{\lim_{n\to \infty} f_n}
.\]
Note that uniform convergence of $f_n$ and $f_n'$ is sufficient to guarantee that $f$ is differentiable.
Even worse: every continuous function is a uniform limit of polynomials by the Weierstrass approximation theorem.
:::
