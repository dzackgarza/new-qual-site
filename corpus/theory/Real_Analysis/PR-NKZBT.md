---
schema: qual/card@1
id: PR-NKZBT
kind: proposition
title: Term-by-term integration of series of functions
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Series of Functions
  - L¹
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure space]].

(a) If $f_n\in$ [[D-BF5L2|$L^+$]] for $n\geq1$, then $\int_X\sum_n f_n\dmu=\sum_n\int_X f_n\dmu$ in $[0,\infty]$ [@Fol13].

(b) If $f_n\in L^1(\mu)$ for $n\geq1$ and $\sum_n\int_X\abs{f_n}\dmu<\infty$, then $\sum_n f_n$ converges almost everywhere to a function in $L^1(\mu)$ and $\int_X\sum_n f_n\dmu=\sum_n\int_X f_n\dmu$ [@Fol13].
:::

::: {.remark}
By (a) applied to $\abs{f_n}$, the hypothesis $\sum_n\int_X\abs{f_n}\dmu<\infty$ in (b) is the same as $\int_X\sum_n\abs{f_n}\dmu<\infty$.
:::
