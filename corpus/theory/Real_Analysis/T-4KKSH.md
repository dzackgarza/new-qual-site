---
schema: qual/card@1
id: T-4KKSH
kind: theorem
title: $L^p$ norms approach $\norm{f}_\infty$ on finite measure spaces
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - L∞
  - Limits
relations: []
review: draft
---

::: {.theorem}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space with $\mu(X)<\infty$, and let $f\colon X\to\CC$ be [[D-DHFN4|measurable]].
Then, in $[0,\infty]$,
$$
\lim_{p\to\infty} \norm{f}_p = \norm{f}_\infty ,
$$
where $\norm{f}_\infty$ is the [[D-3PVRB|essential supremum]] of $\abs{f}$.
:::

::: {.proof}
If $\mu(X)=0$, every $\norm{f}_p$ and $\norm{f}_\infty$ equal $0$; assume $\mu(X)>0$.
Since $\abs{f}\leq\norm{f}_\infty$ almost everywhere, $\norm{f}_p\leq\norm{f}_\infty\,\mu(X)^{1/p}$, so $\limsup_{p\to\infty}\norm{f}_p\leq\norm{f}_\infty$.
For $0\leq M<\norm{f}_\infty$, the set $S\coloneqq\theset{\abs{f}>M}$ has $\mu(S)>0$, and $\norm{f}_p\geq M\mu(S)^{1/p}\to M$.
Hence $\liminf_{p\to\infty}\norm{f}_p\geq M$ for every such $M$, which gives the claim, including the case $\norm{f}_\infty=\infty$.
:::
