---
schema: qual/card@1
id: P-QZT5B
kind: problem
title: The first Borel–Cantelli lemma
classification:
  areas:
  - real-analysis
  topics:
  - Borel-Cantelli
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Show that if $\sum \mu(E_k) < \infty$ then almost every $x\in X$ is in at most finitely many $E_k$.
:::

::: {.solution}
Let $(X, \mu)$ be a measure space and $E_k$ measurable. The set of points lying in infinitely many $E_k$ is $\limsup_k E_k = \bigcap_{n\ge1}\bigcup_{k\ge n} E_k$, which is measurable.

<1>1. $\mu(\limsup_k E_k) \le \sum_{k\ge n}\mu(E_k)$ for every $n$.

::: {.proof}
$\limsup_k E_k \subseteq \bigcup_{k\ge n} E_k$, and countable subadditivity gives $\mu(\bigcup_{k\ge n} E_k) \le \sum_{k\ge n}\mu(E_k)$.
:::

<1>2. Q.E.D.

::: {.proof}
Since $\sum_k \mu(E_k) < \infty$, the tails $\sum_{k\ge n}\mu(E_k)$ tend to $0$, so step <1>1 gives $\mu(\limsup_k E_k) = 0$.
:::
:::
