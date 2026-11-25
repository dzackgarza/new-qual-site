---
schema: qual/card@1
id: T-OTR5M
kind: theorem
title: Borel--Cantelli lemma
slogan: 'If $\sum_k \mu(E_k)<\infty$, then almost every point lies in only finitely many of the sets $E_k$.'
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

::: {.theorem}
(a) Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space and let $(E_k)_{k\geq1}$ be a sequence in $\mcm$ with
$$
\sum_{k=1}^\infty \mu(E_k) < \infty .
$$
Then almost every $x\in X$ belongs to at most finitely many of the sets $E_k$; equivalently, the [[D-PAEDW|limit superior]] $\limsup_k E_k$ lies in $\mcm$ ([[PR-NULVE]]) and has measure zero (Royden--Fitzpatrick, *Real Analysis*, 4th ed., Chapter 17, §17.1, the Borel--Cantelli lemma).

(b) Let $(\Omega,\mcf,P)$ be a probability space and let $(E_n)_{n\geq1}$ be independent events with $\sum_{n\geq1} P(E_n) = \infty$.
Then $P\qty{\limsup_n E_n} = 1$ [@Fol99, Lemma 10.10(b)].
:::

::: {.remark}
Folland states the lemma of part (a) for a probability measure and events $E_k$, as part (a) of [@Fol99, Lemma 10.10(a)].
:::
