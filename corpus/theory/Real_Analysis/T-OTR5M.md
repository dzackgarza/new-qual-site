---
schema: qual/card@1
id: T-OTR5M
kind: theorem
title: Borel--Cantelli lemma
classification:
  areas:
  - real-analysis
  topics:
  - Borel-Cantelli
  - Measure Theory
relations: []
review: draft
---

::: {.theorem}
Let $(E_k)_{k\geq1}$ be a sequence of [[D-MDJII|Lebesgue measurable]] subsets of $\RR^n$ with
$$
\sum_{k=1}^\infty m(E_k) < \infty .
$$
Then $m\qty{\limsup_{k\to\infty} E_k} = 0$, where $\limsup_k E_k$ is the [[D-PAEDW|limit superior]] of the sets $E_k$; equivalently, almost every $x\in\RR^n$ lies in only finitely many of the sets $E_k$.
:::

::: {.remark}
The same statement holds for a sequence of measurable sets in any [[D-QYLPH|measure]] space.
For a probability measure $P$ and events $E_k$ with $\sum_k P(E_k)<\infty$, it says that with probability $0$ infinitely many of the events $E_k$ occur.
:::
