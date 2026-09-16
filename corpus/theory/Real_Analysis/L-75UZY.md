---
schema: qual/card@1
id: L-75UZY
kind: lemma
title: Function discontinuous on the rationals
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Counterexamples
relations: []
review: draft
---

::: {.lemma}
There is a function $f\colon\RR\to\RR$ whose set of points of discontinuity is exactly $\QQ$.
:::

::: {.proof}
Enumerate $\QQ=\theset{q_1,q_2,\ldots}$ and put $f(x)\coloneqq\sum_{n\,:\,q_n<x}2^{-n}$.
The function $f$ is nondecreasing and bounded by $1$.
Fix $x\in\RR$ and put $g(x)\coloneqq\sum_{n\,:\,q_n\le x}2^{-n}$.
For $\delta>0$,
$$
f(x)-f(x-\delta)=\sum_{n\,:\,x-\delta\le q_n<x}2^{-n}, \qquad f(x+\delta)-g(x)=\sum_{n\,:\,x<q_n<x+\delta}2^{-n}.
$$
Given $N$, for $\delta$ small enough neither index set contains any $n\le N$, so both sums are at most $\sum_{n>N}2^{-n}=2^{-N}$.
Hence $\lim_{t\to x^-}f(t)=f(x)$ and $\lim_{t\to x^+}f(t)=g(x)$.
If $x=q_n$, then $g(x)-f(x)=2^{-n}>0$; if $x\notin\QQ$, then $g(x)=f(x)$.
So $f$ is discontinuous at every rational and [[D-HHVPT|continuous]] at every irrational.
:::
