---
schema: qual/card@1
id: T-LDJNS
kind: theorem
title: Fatou's lemma and reverse Fatou's lemma
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
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space and let $f_n\colon X\to[0,\infty]$ be [[D-DHFN4|measurable]] for $n\geq1$.

1. (Fatou's lemma [@Fol13, §2.3])
$$
\liminf_{n\to\infty} \int_X f_n\dmu \geq \int_X \liminf_{n\to\infty} f_n\dmu .
$$

2. (Reverse Fatou's lemma) If moreover there is an [[D-R5DL3|integrable]] $g\colon X\to[0,\infty)$ with $f_n\leq g$ for all $n$, then
$$
\limsup_{n\to\infty} \int_X f_n\dmu \leq \int_X \limsup_{n\to\infty} f_n\dmu .
$$
:::

::: {.example}
The domination hypothesis in (2) cannot be dropped.
On $\RR$ with Lebesgue measure, $f_n\coloneqq\chi_{[n,n+1]}$ satisfies $\int f_n=1$ for all $n$, while $\limsup_n f_n=0$ pointwise, so $\limsup_n\int f_n=1>0=\int\limsup_n f_n$.
:::
