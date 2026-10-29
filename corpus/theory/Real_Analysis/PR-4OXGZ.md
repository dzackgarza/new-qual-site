---
schema: qual/card@1
id: PR-4OXGZ
kind: proposition
title: Absolute continuity of the integral of an $L^1$ function
prompts:
- What does absolute continuity of the integral say about $f \in L^1$?
slogan: 'For $f\in L^1$ and $\varepsilon>0$, $\int_E\abs{f}<\varepsilon$ for every set $E$ of sufficiently small measure.'
classification:
  areas:
  - real-analysis
  topics:
  - Continuity of Measure
  - L¹
relations: []
review: draft
---

::: {.proposition}
Let $m$ be Lebesgue measure on $\RR^n$ and let $f\in L^1(\RR^n)$.
For every $\varepsilon>0$ there exists $\delta>0$ such that every [[D-MDJII|Lebesgue measurable]] set $E\subseteq\RR^n$ with $m(E)<\delta$ satisfies
$$
\abs{\int_E f}\le\int_E \abs{f} < \varepsilon .
$$
:::

::: {.proof}
Put $f_M\coloneqq\min(\abs{f}, M)$ for $M\in\NN$.
By monotone convergence $\int(\abs{f} - f_M)\to 0$, so there is $M$ with $\int(\abs{f} - f_M)<\varepsilon/2$.
With $\delta\coloneqq\varepsilon/(2M)$ and $m(E)<\delta$,
$$
\int_E\abs{f}\leq\int(\abs{f} - f_M) + \int_E f_M < \frac{\varepsilon}{2} + M\,m(E) < \varepsilon.
$$
:::
