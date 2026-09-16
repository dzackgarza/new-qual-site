---
schema: qual/card@1
id: PR-YFVA2
kind: proposition
title: $L^1$ is a Banach space and $L^2$ is a Hilbert space
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Hilbert Spaces
  - Completeness
relations: []
review: draft
---

::: {.proposition}
Let $(X, \mcm, \mu)$ be a [[D-QYLPH|measure]] space.

- $L^1(X,\mu)$, with the norm $\norm{f}_1 \coloneqq \int_X \abs{f}\dmu$, is a [[D-BG455|Banach space]].

- $L^2(X,\mu)$, with the inner product $\inner{f}{g} \coloneqq \int_X f\,\overline{g}\dmu$, is a [[D-7QQUO|Hilbert space]].
:::

::: {.example}
$L^2(X,\mu)$ need not be separable.
Let $X$ be an uncountable set, $\mcm$ its power set, and $\mu$ counting measure.
The indicator functions $\chi_{\theset{x}}$ for $x\in X$ lie in $L^2(X,\mu)$ and satisfy $\norm{\chi_{\theset{x}}-\chi_{\theset{y}}}_2=\sqrt2$ for $x\neq y$, so the open balls of radius $\sqrt2/2$ about them are pairwise disjoint and uncountably many; a countable dense subset would meet each of them.
:::
