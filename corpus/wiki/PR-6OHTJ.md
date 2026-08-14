---
schema: qual/card@1
id: PR-6OHTJ
kind: proposition
title: "p-tests"
classification:
  areas:
  - real-analysis
  topics:
  - integrals
  - series-of-numbers
  - convergence-tests
relations: []
review: draft
---
:::{.proposition title="p-tests"}
Let $n$ be a fixed dimension and set $B = \theset{x\in \RR^n \suchthat \norm{x} \leq 1}$. 
\[
\sum \frac 1 {n^p} < \infty &\iff p>1 \\
\int_\varepsilon^\infty \frac 1 {x^p} < \infty 
&\iff p>1 \\
\int_0^1 \frac 1 {x^p} < \infty 
&\iff p<1 \\
\int_B \frac{1}{\abs{x}^p} < \infty &\iff p < n \\
\int_{B^c} \frac{1}{\abs{x}^p} < \infty &\iff p > n \\
.\]
:::
