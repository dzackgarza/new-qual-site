---
schema: qual/card@1
id: P-CFMLS
kind: problem
title: The set of reals with infinitely many rational approximations $|x-p/q|<q^{-3}$
  has measure zero
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
  date: 2026-09-08
  note: Checked against the UGA Spring 2018 real-analysis qualifying exam recorded by SRC-UGA-RA-SPRING-2018.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---


::: problem
Define
\[
E:=\left\{x\in\mathbb R:\left|x-\frac pq\right|<q^{-3}
\text{ for infinitely many }p,q\in\mathbb N\right\}.
\]
Prove that $m(E)=0$.
:::

::: solution
Fix $N\in\mathbb N$ and work on the bounded interval $[-N,N]$. For each $q\ge1$, let
\[
E_{q,N}:=\left\{x\in[-N,N]:
\left|x-\frac pq\right|<q^{-3}
\text{ for some }p\in\mathbb N\right\}.
\]
Only numerators with
\[
0\le p\le Nq+1
\]
can contribute to $E_{q,N}$, so $E_{q,N}$ is covered by at most $Nq+2$ intervals of length $2q^{-3}$. Hence
\[
m(E_{q,N})\le 2(Nq+2)q^{-3}
\le \frac{2N}{q^2}+\frac4{q^3}.
\]
Therefore
\[
\sum_{q=1}^\infty m(E_{q,N})<\infty.
\]
By the first Borel--Cantelli lemma,
\[
m\left(\limsup_{q\to\infty}E_{q,N}\right)=0.
\]
But
\[
E\cap[-N,N]\subseteq \limsup_{q\to\infty}E_{q,N},
\]
so
\[
m(E\cap[-N,N])=0.
\]
Finally,
\[
E=\bigcup_{N=1}^\infty(E\cap[-N,N]),
\]
so countable subadditivity gives
\[
\boxed{m(E)=0.}
\]
:::
