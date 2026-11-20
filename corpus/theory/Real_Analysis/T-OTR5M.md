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
Then the [[D-PAEDW|limit superior]] $\limsup_k E_k$ lies in $\mcm$ and $\mu\qty{\limsup_{k\to\infty} E_k} = 0$; equivalently, almost every $x\in X$ lies in only finitely many of the sets $E_k$ [@Fol99, Theorem 10.10(a)].

(b) Let $(\Omega,\mcf,P)$ be a probability space and let $(E_n)_{n\geq1}$ be independent events with $\sum_{n\geq1} P(E_n) = \infty$.
Then $P\qty{\limsup_n E_n} = 1$ [@Fol99, Theorem 10.10(b)].
:::

::: {.proof}
For (a), $\limsup_k E_k=\bigcap_{k\geq1}\bigcup_{n\geq k}E_n$ lies in $\mcm$, and monotonicity and countable subadditivity give
$$
\mu\qty{\limsup_{n\to\infty}E_n}\leq\mu\qty{\bigcup_{n\geq k}E_n}\leq\sum_{n=k}^{\infty}\mu(E_n)
$$
for every $k$, which tends to $0$ as $k\to\infty$ when the series converges.
:::

::: {.remark}
For Lebesgue measure $m$ on $\RR^n$ and [[D-MDJII|Lebesgue measurable]] sets $E_k$ with $\sum_k m(E_k)<\infty$, almost every $x\in\RR^n$ lies in only finitely many $E_k$.
For a probability measure $P$ and events $E_k$ with $\sum_k P(E_k)<\infty$, with probability $0$ infinitely many of the events $E_k$ occur.
:::
