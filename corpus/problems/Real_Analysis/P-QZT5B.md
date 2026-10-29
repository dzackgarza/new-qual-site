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
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source left X, mu and E_k undeclared; the statement now declares a measure space and a sequence of measurable sets.
---

::: {.problem}

Let $(X, \mathcal{M}, \mu)$ be a measure space and $(E_k)_{k\ge1}$ a sequence of measurable sets. Show that if $\sum \mu(E_k) < \infty$ then almost every $x\in X$ is in at most finitely many $E_k$.

:::

::: {.solution}

The set of points lying in infinitely many $E_k$ is $\limsup_k E_k = \bigcap_{n\ge1}\bigcup_{k\ge n} E_k$, which is measurable.

::: pf

::: {.pf-step #s1}

$\mu(\limsup_k E_k) \le \sum_{k\ge n}\mu(E_k)$ for every $n$.

::: pf-proof

$\limsup_k E_k \subseteq \bigcup_{k\ge n} E_k$, and countable subadditivity gives $\mu(\bigcup_{k\ge n} E_k) \le \sum_{k\ge n}\mu(E_k)$.

:::

:::

::: pf-qed

Since $\sum_k \mu(E_k) < \infty$, the tails $\sum_{k\ge n}\mu(E_k)$ tend to $0$, so step [](#s1){.pf-ref} gives $\mu(\limsup_k E_k) = 0$.

:::

:::

:::
