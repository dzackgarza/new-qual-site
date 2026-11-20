---
schema: qual/card@1
id: D-7DFVJ
kind: definition
title: Meromorphic function
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
  - Poles
relations: []
review: draft
---

::: {.definition}
Let $\Omega\subseteq\CC$ be open.
A function $f$ is \dfn{meromorphic} on $\Omega$ if there exists a set $P\subseteq\Omega$ with no [[D-TFSPT|limit point]] in $\Omega$ such that $f$ is [[D-E7A5W|holomorphic]] on $\Omega\setminus P$ and has a [[D-AUD6K|pole]] at each point of $P$.

This is [@Ahl73, ch. 4, §3.2, Zeros and Poles]: a function analytic in a region except for poles is said to be meromorphic there, and the section's precise restatement, that each point have a neighbourhood on which $f$ is either analytic throughout or analytic off the point with a pole at it, is the condition above together with the isolation of poles.
:::

::: {.remark}
A set $P\subseteq\Omega$ with no limit point in $\Omega$ meets each compact subset of $\Omega$ in finitely many points, so $P$ is finite or countable and can be listed as a finite or infinite sequence $(z_n)$.
:::
