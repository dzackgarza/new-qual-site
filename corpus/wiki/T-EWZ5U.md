---
schema: qual/card@1
id: T-EWZ5U
kind: theorem
title: "Lagrange and Cauchy Remainders"
classification:
  areas:
  - real-analysis
  topics:
  - differentiation
  - series-of-functions
relations: []
review: draft
---

::: {.theorem title="Lagrange and Cauchy Remainders"}
If $f$ is $n$ times differentiable on a neighborhood of a point $p$, say $N_\delta(p)$, then for all points $x$ in the deleted neighborhood $N_\delta(p) - \theset{p}$ , there exists a point $\xi$ strictly between $x$ and $p$ such that
\[
x \in N_\delta(p)-\theset{p} \implies f(x) 
&= \sum_{k=0}^{n-1} \frac{f^{(k)}(p)}{k!}(x-p)^k + \frac{f^{(n)}(\xi)}{n!}(x-p)^n \\ \\
&= \sum_{k=0}^{n-1} \frac{f^{(k)}(p)}{k!}(x-p)^k + \int_c^x \frac{1}{n!} \dd{^n f}{x^n}(t) (x-t)^n ~dt
\]
:::
