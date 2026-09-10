---
schema: qual/card@1
id: P-ULNGG
kind: problem
title: Almost every point of a finite-measure set lies in only finitely many of the sets $E_q=\bigcup_{0\le p\le q}\{x:|x-p/q|\le 1/q^3\}$
classification:
  areas:
  - real-analysis
  topics:
  - Borel-Cantelli
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: The preserved Arango document is solutions-only at this point, so the problem statement is reconstructed from the solution. The prior solution made an unjustified reduction to E subset [0,1] and incorrectly wrote E subset union_{q>=Q} E_q; the correct exceptional set is E intersect limsup E_q.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
[Reconstructed from solution — no problem statement page was present in this solutions-only document.] Let $E\subseteq\mathbb R$ be measurable with finite Lebesgue measure. For each positive integer $q$, let
\[
E_q=\bigcup_{0\le p\le q}\left\{x:\left|x-\frac pq\right|\le\frac1{q^3}\right\}.
\]
Show that almost every $x\in E$ lies in only finitely many of the sets $E_q$.
:::

::: solution
<1>1. Estimate the measures of the approximation sets.
::: proof
For fixed $q$, the set $E_q$ is a union of $q+1$ intervals, each of length $2/q^3$. Therefore
\[
m(E_q)\le \frac{2(q+1)}{q^3}.
\]
Hence
\[
\sum_{q=1}^\infty m(E_q)
\le 2\sum_{q=1}^\infty\left(\frac1{q^2}+\frac1{q^3}\right)<\infty.
\]
:::

<1>2. Apply the first Borel--Cantelli lemma.
::: proof
The set of points belonging to infinitely many $E_q$ is
\[
\limsup_{q\to\infty}E_q
=\bigcap_{Q=1}^\infty\bigcup_{q\ge Q}E_q.
\]
Since $\sum_qm(E_q)<\infty$, the first Borel--Cantelli lemma gives
\[
m\left(\limsup_{q\to\infty}E_q\right)=0.
\]
Consequently
\[
m\left(E\cap\limsup_{q\to\infty}E_q\right)=0.
\]
Thus for almost every $x\in E$, there is some $Q=Q(x)$ such that
\[
x\notin E_q\qquad(q\ge Q),
\]
i.e. $x$ belongs to only finitely many of the sets $E_q$.

The finite-measure hypothesis on $E$ is not actually needed for this conclusion; the exceptional limsup set is null in all of $\mathbb R$.
:::
:::
