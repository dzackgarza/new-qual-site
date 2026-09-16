---
schema: qual/card@1
id: FF-GNU7E
kind: fact
title: Borel--Cantelli lemma
prompts:
- What is the Borel-Cantelli lemma?
classification:
  areas:
  - real-analysis
  topics:
  - Borel-Cantelli
  - Measure Theory
relations: []
review: draft
---

::: {.fact}
Let $(\Omega,\mcf,P)$ be a probability space, let $(E_n)_{n\geq 1}$ be a sequence of events, and let $\limsup_n E_n$ be its [[D-PAEDW|limit superior]].

1. If $\sum_{n\geq 1} P(E_n) < \infty$, then $P(\limsup_n E_n) = 0$.

2. If the events $E_n$ are independent and $\sum_{n\geq 1} P(E_n) = \infty$, then $P(\limsup_n E_n) = 1$.
:::

::: {.proof}
For (1), $\limsup_n E_n\subseteq\bigcup_{n\geq N}E_n$ for every $N$, so $P(\limsup_n E_n)\leq\sum_{n\geq N}P(E_n)\to 0$ as $N\to\infty$.

For (2), the complement of $\limsup_n E_n$ is $\bigcup_{N\geq 1}\bigcap_{n\geq N}E_n^c$.
For $M\geq N$, independence and $1-t\leq e^{-t}$ give
$$
P\qty{\bigcap_{n=N}^{M}E_n^c} = \prod_{n=N}^{M}(1-P(E_n))\leq\exp\qty{-\sum_{n=N}^{M}P(E_n)}\to 0 \quad (M\to\infty),
$$
so $P\qty{\bigcap_{n\geq N}E_n^c} = 0$ for every $N$, and the countable union of these null events is null.
:::
