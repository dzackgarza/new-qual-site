---
schema: qual/card@1
id: FD-3BK6U
kind: definition
title: Chebyshev's inequality
prompts:
- State Chebyshev's inequality.
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Lp Spaces
  - Integrals
relations: []
review: draft
---

::: {.definition}
Let $m$ be Lebesgue measure on $\RR^n$, let $f\colon\RR^n\to\CC$ be [[D-DHFN4|measurable]], and let $0<p<\infty$.
For every $\alpha>0$,
$$
m\qty{\theset{x \in\RR^n \suchthat \abs{f(x)} \geq \alpha}} \leq \qty{\frac{\norm{f}_p}{\alpha}}^p, \qquad \norm{f}_p\coloneqq\qty{\int_{\RR^n}\abs{f(x)}^p\,dx}^{1/p}.
$$
Taking $p=1$ gives
$$
m\qty{\theset{x \in \RR^n\suchthat \abs{f(x)} \geq \alpha}} \leq \frac{1}{\alpha} \int_{\RR^n} \abs{f(x)} \, dx.
$$
:::

::: {.proof}
Let $E_\alpha\coloneqq\theset{x \suchthat \abs{f(x)}\geq\alpha}$.
Then $\alpha^p\chi_{E_\alpha}\leq\abs{f}^p$ pointwise, and integrating gives $\alpha^p\, m(E_\alpha)\leq\norm{f}_p^p$.
:::
