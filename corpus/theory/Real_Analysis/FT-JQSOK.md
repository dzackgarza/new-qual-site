---
schema: qual/card@1
id: FT-JQSOK
kind: theorem
title: Arzelà--Ascoli theorem
prompts:
- State the Arzela-Ascoli theorem.
classification:
  areas:
  - real-analysis
  topics:
  - Arzelà-Ascoli
  - Equicontinuity
  - Uniform Convergence
relations:
- kind: variant-of
  target: FF-XZGIY
review: draft
---

::: {.theorem}
Let $(K,d)$ be a compact metric space, and let $\mathcal F$ be a family of continuous functions $K\to\CC$.
The closure of $\mathcal F$ in $C(K)$ with the norm $\norm{f}_\infty\coloneqq\sup_{x\in K}\abs{f(x)}$ is compact if and only if $\mathcal F$ is uniformly bounded and [[FD-TGBYP|uniformly equicontinuous]].

In particular, every uniformly bounded, uniformly equicontinuous sequence $(f_n)$ in $C(K)$ has a [[D-YZC3C|uniformly convergent]] subsequence.
:::
