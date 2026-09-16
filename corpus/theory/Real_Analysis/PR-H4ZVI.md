---
schema: qual/card@1
id: PR-H4ZVI
kind: proposition
title: Convergence in $L^1$ implies convergence of norms
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Convergence of Integrals
  - Norms
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure space]] and let $f, f_n\in L^1(\mu)$ for $n\geq1$.

(a) If $\norm{f_n-f}_1\to0$, then $\norm{f_n}_1\to\norm{f}_1$.

(b) If $f_n\to f$ $\mu$-almost everywhere and $\norm{f_n}_1\to\norm{f}_1$, then $\norm{f_n-f}_1\to0$.
:::

::: {.proof}
(a) By the reverse triangle inequality, $\abs{\norm{f_n}_1-\norm{f}_1}\leq\norm{f_n-f}_1$.

(b) The functions $g_n\coloneqq\abs{f_n}+\abs{f}-\abs{f_n-f}$ are nonnegative by the triangle inequality and converge to $2\abs{f}$ almost everywhere.
By Fatou's lemma,
$$
2\norm{f}_1\leq\liminf_{n\to\infty}\int_X g_n\dmu=2\norm{f}_1-\limsup_{n\to\infty}\norm{f_n-f}_1,
$$
so $\limsup_n\norm{f_n-f}_1\leq0$.
:::

::: {.example}
Without almost everywhere convergence, convergence of norms does not imply convergence in $L^1$: for $f\in L^1(\mu)$ with $\norm{f}_1>0$ and $f_n\coloneqq-f$, $\norm{f_n}_1=\norm{f}_1$ for all $n$ but $\norm{f_n-f}_1=2\norm{f}_1$.
:::
