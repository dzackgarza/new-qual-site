---
schema: qual/card@1
id: FF-FSDJP
kind: fact
title: Small tails and absolute continuity for $L^1$ functions
prompts:
- What does small tails mean? Absolute continuity?
classification:
  areas:
  - real-analysis
  topics:
  - Small Tails
  - Continuity of Measure
  - L¹
relations: []
review: draft
---

::: {.fact}
Let $f\in L^1(\RR^n)$ and $\varepsilon> 0$, and let $B_N\coloneqq\theset{x\in\RR^n\suchthat\abs{x}<N}$.

- **Small tails.** There exists $N\in\NN$ such that $\int_{\RR^n\setminus B_N} \abs{f} < \varepsilon$.

- **Absolute continuity.** There exists $\delta>0$ such that $\int_E \abs{f} < \varepsilon$ for every Lebesgue measurable $E\subseteq\RR^n$ with $m(E) < \delta$.
:::

::: {.proof}
For small tails, $\abs{f}\chi_{\RR^n\setminus B_N}\to 0$ pointwise as $N\to\infty$ and is dominated by $\abs{f}\in L^1$, so $\int_{\RR^n\setminus B_N}\abs{f}\to 0$ by dominated convergence.

For absolute continuity, put $f_M\coloneqq\min(\abs{f}, M)$ for $M\in\NN$.
By monotone convergence $\int(\abs{f} - f_M)\to 0$, so there is $M$ with $\int(\abs{f} - f_M)<\varepsilon/2$.
With $\delta\coloneqq\varepsilon/(2M)$ and $m(E)<\delta$,
$$
\int_E\abs{f}\leq\int(\abs{f} - f_M) + \int_E f_M < \frac{\varepsilon}{2} + M\,m(E) < \varepsilon.
$$
:::
