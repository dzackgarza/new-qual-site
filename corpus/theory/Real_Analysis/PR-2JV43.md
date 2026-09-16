---
schema: qual/card@1
id: PR-2JV43
kind: proposition
title: Almost everywhere convergence does not imply $L^p$ convergence
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
**Escape to infinity.** Let $f_k\coloneqq\chi_{[k, k+1]}$.
For every $x\in\RR$, $f_k(x)=0$ once $k>x$, so $f_k\to0$ pointwise everywhere.
But $\norm{f_k}_p = 1$ for all $k$ and all $1\le p\le\infty$.
The convergence is not uniform, since $\sup_x\abs{f_k(x)}=1$.

**Concentration.** Let $f_k\coloneqq k \chi_{[0, 1/k]}$.
For $x\neq0$, $f_k(x)=0$ whenever $k>1/\abs{x}$, so $f_k\to0$ almost everywhere; at $x=0$, $f_k(0)=k\to\infty$.
Here $\norm{f_k}_p=k^{1-1/p}\geq1$ for $1\le p<\infty$ and $\norm{f_k}_\infty = k \to \infty$.
:::
