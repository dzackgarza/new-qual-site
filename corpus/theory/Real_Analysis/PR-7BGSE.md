---
schema: qual/card@1
id: PR-7BGSE
kind: proposition
title: Hölder's inequality
classification:
  areas:
  - real-analysis
  topics:
  - Norms
  - Lp Spaces
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space, let $1\le p,q\le\infty$ satisfy $\frac 1 p + \frac 1 q = 1$, and let $f,g\colon X\to\CC$ be [[D-DHFN4|measurable]].
Then
$$
\norm{f g}_{1} \leq \norm{f}_{p} \norm{g}_{q} .
$$
For $1<p,q<\infty$, this reads
$$
\int_X \abs{fg}\dmu \leq \qty{\int_X \abs{f}^p\dmu}^{1/p} \qty{\int_X \abs{g}^q\dmu}^{1/q} .
$$
:::
