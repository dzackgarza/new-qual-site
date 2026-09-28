---
schema: qual/card@1
id: P-UCLARA18F-03
kind: problem
title: Portmanteau theorem for continuity sets
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 3. Let $(X,\rho)$ be a compact metric space and let $\mathcal P(X)$ be the set of all probability measures on the Borel sigma-algebra of $X$. Assume $\{\mu_n\}$ is a sequence in $\mathcal P(X)$ and $\mu\in\mathcal P(X)$ such that, for every continuous $f:X\to\mathbb R$,
\[
\int_X f(x)\,d\mu_n\longrightarrow\int_X f(x)\,d\mu
\qquad(n\to\infty).
\]
Prove that
\[
\mu_n(E)\to\mu(E)
\qquad(n\to\infty)
\]
whenever $E$ is a Borel subset of $X$ such that
\[
\mu(\overline E)=\mu(E^\circ),
\]
where $\overline E$ is the closure of $E$ and $E^\circ$ is the interior of $E$.
:::
