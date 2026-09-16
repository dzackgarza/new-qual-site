---
schema: qual/card@1
id: FT-P5UNP
kind: theorem
title: Fatou's lemma
prompts:
- State Fatou's lemma.
classification:
  areas:
  - real-analysis
  topics:
  - Fatou
  - Convergence of Integrals
relations: []
review: draft
---

::: {.theorem}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space and let $f_n$ for $n\geq1$ belong to [[D-BF5L2|$L^+$]].
Then
$$
\int_X \liminf_{n\to\infty} f_n \dmu \leq \liminf_{n\to\infty} \int_X f_n \dmu .
$$
:::

::: {.example}
The inequality can be strict.
On $\RR$ with Lebesgue measure, let $f_n\coloneqq\one_{[n,n+1]}$.
Then $\liminf_n f_n=0$ pointwise, so the left side is $0$, while $\int_\RR f_n=1$ for every $n$.
:::
