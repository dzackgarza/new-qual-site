---
schema: qual/card@1
id: PR-YJJSY
kind: proposition
title: $L^1$-summable series converge almost everywhere and in $L^1$
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
  - L¹
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space, and let $f_n\in L^1(X,\mu)$ for $n\geq1$ satisfy
$$
\sum_{n=1}^\infty \norm{f_n}_1 < \infty.
$$
Then for almost every $x\in X$ the series $\sum_{n=1}^\infty f_n(x)$ converges absolutely, its sum $f$, defined almost everywhere, lies in $L^1(X,\mu)$, and
$$
\norm{f-\sum_{n=1}^N f_n}_1 \longrightarrow 0 \quad\text{as } N\to\infty.
$$
:::

::: {.proof}
Let $g\coloneqq\sum_{n=1}^\infty\abs{f_n}\in L^+$.
By the monotone convergence theorem [[T-5K3IO]] applied to the partial sums, $\int_X g\dmu=\sum_{n}\norm{f_n}_1<\infty$, so $g<\infty$ almost everywhere, and at each such point $\sum_n f_n(x)$ converges absolutely.
The partial sums $s_N\coloneqq\sum_{n\leq N}f_n$ satisfy $\abs{s_N}\leq g$ and $\abs{f-s_N}\leq g$ almost everywhere, and $\abs{f-s_N}\to0$ almost everywhere.
Hence $f\in L^1$, and the dominated convergence theorem [[T-IJQQG]] gives $\int_X\abs{f-s_N}\dmu\to0$.
:::
