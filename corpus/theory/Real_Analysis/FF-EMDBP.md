---
schema: qual/card@1
id: FF-EMDBP
kind: fact
title: The $p$-test for $\int_0^1 x^{-p}\,dx$ and $\int_1^\infty x^{-p}\,dx$
prompts:
- For which $p$ do $\int_0^1 x^{-p}$ and $\int_1^\infty x^{-p}$ converge?
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Lp Spaces
relations: []
review: draft
---

::: {.fact}
For $p\in\RR$,
$$
\begin{aligned}
\int_0^1 \frac{dx}{x^p} < \infty &\iff p < 1, \\
\int_1^\infty \frac{dx}{x^p} < \infty &\iff p > 1.
\end{aligned}
$$
:::

::: {.proof}
For $0<a<b$, $\int_a^b x^{-p}\dx$ equals $\frac{b^{1-p} - a^{1-p}}{1-p}$ if $p\neq 1$ and $\log b - \log a$ if $p = 1$.
Letting $a\to 0^+$ with $b = 1$ gives a finite limit exactly when $1-p>0$; letting $b\to\infty$ with $a = 1$ gives a finite limit exactly when $1-p<0$.
:::
