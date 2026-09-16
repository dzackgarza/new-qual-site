---
schema: qual/card@1
id: FF-XZGIY
kind: fact
title: Arzelà--Ascoli theorem
prompts:
- What is the Arzela-Ascoli theorem?
- State the Arzela-Ascoli theorem.
classification:
  areas:
  - real-analysis
  topics:
  - Arzelà-Ascoli
  - Equicontinuity
  - Uniform Convergence
relations: []
review: draft
---

::: {.fact}
Let $K$ be a compact metric space, let $C(K)$ be the space of continuous functions $K\to\CC$ with the norm $\norm{f}_\infty\coloneqq\sup_{x\in K}\abs{f(x)}$, and let $\mcf\subseteq C(K)$.
Then the closure of $\mcf$ in $C(K)$ is compact if and only if $\mcf$ is uniformly bounded, that is, $\sup_{f\in\mcf}\norm{f}_\infty<\infty$, and [[FD-XVMEE|equicontinuous]] at every point of $K$.

In particular, every sequence $(f_n)$ in $C(K)$ that is uniformly bounded and equicontinuous at every point of $K$ has a subsequence that [[D-YZC3C|converges uniformly]] on $K$.
:::

::: {.remark}
Since $K$ is compact, a family $\mcf\subseteq C(K)$ that is equicontinuous at every point of $K$ is [[FD-XVMEE|uniformly equicontinuous]].
:::
