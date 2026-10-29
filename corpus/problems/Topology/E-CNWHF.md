---
schema: qual/card@1
id: E-CNWHF
kind: problem
title: Compact metric spaces are complete
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Completeness
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that every compact metric space $(X, d)$ is complete (every Cauchy sequence in $X$ converges to a point in $X$).
:::

::: {.solution}

Let $(x_n)$ be a Cauchy sequence in $X$.

::: pf

::: {.pf-step #subseq}

Some subsequence satisfies $x_{n_k}\to x$ for a point $x\in X$.

::: pf-proof

A compact metric space is sequentially compact.

:::

:::

::: pf-qed

Fix $\varepsilon>0$. Since $(x_n)$ is Cauchy, choose $N$ such that $m,n\ge N$ implies $d(x_m,x_n)<\varepsilon/2$. By step [](#subseq){.pf-ref}, choose $k$ with $n_k\ge N$ and $d(x_{n_k},x)<\varepsilon/2$. Then for every $n\ge N$,
$$
d(x_n,x)\le d(x_n,x_{n_k})+d(x_{n_k},x)<\varepsilon.
$$
Thus $x_n\to x$, and $X$ is complete.

:::

:::

:::
