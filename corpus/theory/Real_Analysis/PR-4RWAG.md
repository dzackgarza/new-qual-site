---
schema: qual/card@1
id: PR-4RWAG
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
Then
$$
\norm{f_n - f_m}_\infty \to 0 \text{ as } m, n\to \infty \iff \text{there exists } f\colon S\to\CC \text{ with } \norm{f_n - f}_\infty \to 0 \text{ as } n\to\infty,
$$
that is, $(f_n)$ is uniformly Cauchy if and only if it [[D-YZC3C|converges uniformly]] to some function on $S$.

Applied to the partial sums $s_N\coloneqq\sum_{n=1}^N f_n$: the series $\sum_{n\geq1}f_n$ converges uniformly on $S$ if and only if $\sup_{x\in S}\abs{\sum_{n=M+1}^N f_n(x)}\to0$ as $N>M\to\infty$.
:::
