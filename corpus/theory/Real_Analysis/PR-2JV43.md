---
schema: qual/card@1
id: PR-2JV43
kind: proposition
title: Almost everywhere convergence does not imply $L^p$ convergence
slogan: 'Almost everywhere convergence can lose mass by escape or concentration, so $L^p$ convergence need not follow.'
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - Lp Spaces
  - Counterexamples
relations: []
review: draft
---

::: {.proposition}
For every $1\le p\le\infty$ there is a sequence $(f_k)_{k\geq1}$ in $L^p(\RR)$ with $f_k\to0$ almost everywhere but $\norm{f_k}_p\not\to0$.
:::

::: {.proof}
The sequence $f_k\coloneqq\chi_{(k, k+1)}$ of [[FE-BFDRF]] tends to $0$ everywhere and has $\norm{f_k}_p = 1$ for all $k$ and all $1\le p\le\infty$.
The spikes $k\chi_{[0,1/k]}$ of [[FE-VT5N3]] are a second such sequence, with $\norm{k\chi_{[0,1/k]}}_p=k^{1-1/p}\geq1$ for $1\le p<\infty$ and $\norm{k\chi_{[0,1/k]}}_\infty = k$.
:::
