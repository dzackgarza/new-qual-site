---
schema: qual/card@1
id: PR-GT5RS
kind: proposition
title: Uniform Cauchy criterion for sequences and series of functions
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Completeness
relations: []
review: draft
---

::: {.proposition}
Let $S$ be a set, let $f_n\colon S\to\CC$ for $n\geq1$, and for $h\colon S\to\CC$ put $\norm{h}_\infty\coloneqq\sup_{x\in S}\abs{h(x)}$.
The sequence $(f_n)$ [[D-YZC3C|converges uniformly]] on $S$ to some function $f\colon S\to\CC$ if and only if it is uniformly Cauchy:
$$
\forall\varepsilon>0\ \exists N\ \forall m,n\geq N:\quad \norm{f_n-f_m}_\infty<\varepsilon .
$$
In particular, a series $\sum_{n\geq1}f_n$ converges uniformly on $S$ if and only if
$$
\forall\varepsilon>0\ \exists N\ \forall n>m\geq N:\quad \sup_{x\in S}\abs{\sum_{k=m+1}^{n}f_k(x)}<\varepsilon .
$$
:::

::: {.proof}
If $\norm{f_n-f}_\infty<\varepsilon/2$ for $n\geq N$, then $\norm{f_n-f_m}_\infty<\varepsilon$ for $m,n\geq N$.
Conversely, if $(f_n)$ is uniformly Cauchy, then for each $x\in S$ the sequence $(f_n(x))$ is Cauchy in $\CC$ and converges to some $f(x)$.
Given $\varepsilon>0$, choose $N$ with $\abs{f_n(x)-f_m(x)}<\varepsilon$ for all $x\in S$ and $m,n\geq N$; letting $m\to\infty$ gives $\abs{f_n(x)-f(x)}\leq\varepsilon$ for all $x\in S$ and $n\geq N$.
The statement for series is the statement for the partial sums $s_n\coloneqq\sum_{k=1}^n f_k$, since $s_n-s_m=\sum_{k=m+1}^n f_k$.
:::
