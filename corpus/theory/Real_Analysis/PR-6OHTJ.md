---
schema: qual/card@1
id: PR-6OHTJ
kind: proposition
title: $p$-tests for series and integrals
slogan: '$\sum k^{-p}$ and $\int_\varepsilon^\infty x^{-p}\,dx$ converge exactly for $p>1$ and $\int_0^1 x^{-p}\,dx$ exactly for $p<1$; in $\RR^n$ the threshold for $\abs{x}^{-p}$ is $p=n$.'
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Series of Numbers
  - Convergence Tests
relations: []
review: draft
---

::: {.proposition}
Let $p\in\RR$, let $\varepsilon>0$, let $n\geq1$, and let $B \coloneqq \theset{x\in \RR^n \suchthat \abs{x} \leq 1}$ be the closed unit ball for the Euclidean norm.
Then
$$
\begin{aligned}
\sum_{k=1}^\infty \frac 1 {k^p} < \infty &\iff p>1, \\
\int_\varepsilon^\infty \frac {dx} {x^p} < \infty &\iff p>1, \\
\int_0^1 \frac {dx} {x^p} < \infty &\iff p<1, \\
\int_B \frac{dx}{\abs{x}^p} < \infty &\iff p < n, \\
\int_{\RR^n\setminus B} \frac{dx}{\abs{x}^p} < \infty &\iff p > n .
\end{aligned}
$$
:::
