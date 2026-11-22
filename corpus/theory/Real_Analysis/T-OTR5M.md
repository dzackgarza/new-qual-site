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
(a) Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space and let $(E_k)_{k\geq1}$ be a sequence in $\mcm$.
Then the [[D-PAEDW|limit superior]] $\limsup_k E_k$ lies in $\mcm$, and for every $k\geq1$
$$
\mu\qty{\limsup_{n\to\infty} E_n} \leq \sum_{n=k}^\infty \mu(E_n) ,
$$
by monotonicity and countable subadditivity [@Fol99, Theorem 1.8(a),(b)] applied to $\limsup_n E_n=\bigcap_{k\geq1}\bigcup_{n\geq k}E_n$.
In particular, if $\sum_{k=1}^\infty \mu(E_k) < \infty$, then $\mu\qty{\limsup_{k\to\infty} E_k} = 0$, that is, almost every $x\in X$ lies in only finitely many of the sets $E_k$.

(b) Let $(\Omega,\mcf,P)$ be a probability space and let $(E_n)_{n\geq1}$ be independent events with $\sum_{n\geq1} P(E_n) = \infty$.
Then $P\qty{\limsup_n E_n} = 1$ [@Fol99, Lemma 10.10(b)].
:::

::: {.remark}
Folland states part (a) for a probability measure and events $E_k$, as [@Fol99, Lemma 10.10(a)].
:::
