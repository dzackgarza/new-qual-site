---
schema: qual/card@1
id: PR-6OHTJ
kind: proposition
title: $p$-tests for series and integrals
prompts:
- Where is ${1\over x^p}$ integrable in $\RR$? (Depending on $p$)
- For which $p$ do $\int_0^1 x^{-p}$ and $\int_1^\infty x^{-p}$ converge?
- For which $p$ is $x^p$ integrable on $(0,1)$, and for which on $(1,\infty)$?
slogan: '$\sum k^{-p}$ and $\int_\varepsilon^\infty x^{-p}\,dx$ converge exactly for $p>1$ and $\int_0^1 x^{-p}\,dx$ exactly for $p<1$; in $\RR^n$ the threshold for $\abs{x}^{-p}$ is $p=n$.'
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Series of Numbers
  - Convergence Tests
  - Lp Spaces
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

::: {.proof}
For $0<a<b$, $\int_a^b x^{-p}\dx$ equals $\frac{b^{1-p} - a^{1-p}}{1-p}$ if $p\neq 1$ and $\log b - \log a$ if $p = 1$.
By monotone convergence, $\int_0^1 x^{-p}\dx = \lim_{a\to 0^+}\int_a^1 x^{-p}\dx$, which is finite exactly when $1-p>0$, and $\int_\varepsilon^\infty x^{-p}\dx = \lim_{b\to\infty}\int_\varepsilon^b x^{-p}\dx$, which is finite exactly when $1-p<0$.
:::

::: {.remark title="Variations"}
With the exponent written as $x^{p}$, the same computation shows that $x^p\in L^1((0,1))$ if and only if $p>-1$, and $x^p\in L^1((1,\infty))$ if and only if $p<-1$.
:::
