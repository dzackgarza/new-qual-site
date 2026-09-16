---
schema: qual/card@1
id: PR-KNYSF
kind: proposition
title: Convergence in $L^1$ implies convergence of norms
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Convergence of Integrals
  - Norms
relations:
- kind: variant-of
  target: PR-H4ZVI
review: draft
---

::: {.proposition}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure space]] and let $f, f_n\in L^1(\mu)$ for $n\geq1$.

(a) If $\int_X\abs{f_n-f}\dmu\to0$, then $\int_X\abs{f_n}\dmu\to\int_X\abs{f}\dmu$.

(b) If $f_n\to f$ $\mu$-almost everywhere and $\int_X\abs{f_n}\dmu\to\int_X\abs{f}\dmu$, then $\int_X\abs{f_n-f}\dmu\to0$ [@Fol13].
:::

::: {.example}
Without almost everywhere convergence, (b) fails: for $f\in L^1(\mu)$ with $\int_X\abs f\dmu>0$ and $f_n\coloneqq-f$, $\int_X\abs{f_n}\dmu=\int_X\abs{f}\dmu$ for all $n$ but $\int_X\abs{f_n-f}\dmu=2\int_X\abs{f}\dmu$.
:::
