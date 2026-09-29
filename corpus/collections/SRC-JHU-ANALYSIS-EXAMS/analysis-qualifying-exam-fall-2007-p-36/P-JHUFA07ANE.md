---
schema: qual/card@1
id: P-JHUFA07ANE
kind: problem
title: 'Membership examples separating $L^1$ and $L^2$'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
5) Give examples of functions f and g on R so that $f \in L ^ { 1 } \setminus L ^ { 2 }$ and $g \in L ^ { 2 } \setminus L ^ { 1 }$
:::

::: {.solution}
Let $f(x)=x^{-1/2}\mathbf 1_{(0,1]}(x)$ and $g(x)=x^{-1}\mathbf 1_{[1,\infty)}(x)$.

::: pf

::: {.pf-step #f-in-l1-not-l2}
$\boxed{f=x^{-1/2}\mathbf 1_{(0,1]}}\in L^1(\RR)\setminus L^2(\RR)$.

::: pf-proof
$\int_\RR\abs f=\int_0^1x^{-1/2}\,dx=2$, while $\int_\RR\abs f^2=\int_0^1x^{-1}\,dx=\lim_{\eps\to0^+}(-\log\eps)=\infty$.
:::

:::

::: {.pf-step #g-in-l2-not-l1}
$\boxed{g=x^{-1}\mathbf 1_{[1,\infty)}}\in L^2(\RR)\setminus L^1(\RR)$.

::: pf-proof
$\int_\RR\abs g^2=\int_1^\infty x^{-2}\,dx=1$, while $\int_\RR\abs g=\int_1^\infty x^{-1}\,dx=\lim_{R\to\infty}\log R=\infty$.
:::

:::

::: pf-qed
Steps [](#f-in-l1-not-l2){.pf-ref} and [](#g-in-l2-not-l1){.pf-ref} give the two examples.
:::

:::
:::
