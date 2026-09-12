---
schema: qual/card@1
id: P-ALZSD
kind: problem
title: Continuity from above for a finite Borel measure, and $\varepsilon$-$\delta$
  absolute continuity
classification:
  areas:
  - real-analysis
  topics:
  - Continuity of Measure
  - Measure Theory
  - Absolute Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against the UGA Spring 2019 real-analysis qualifying exam recorded by SRC-UGA-RA-SPRING-2019.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---


::: problem
Let $\mathcal B$ be the Borel sigma-algebra on $\mathbb R$, and let $\mu$ be a finite Borel measure.

1. If $F_1\supseteq F_2\supseteq\cdots$ are Borel sets, prove
\[
\mu(F_k)\longrightarrow \mu\!\left(\bigcap_{k=1}^\infty F_k\right).
\]

2. Assume $m(E)=0$ implies $\mu(E)=0$ for every Borel set $E$. Prove that for every $\varepsilon>0$ there exists $\delta>0$ such that
\[
m(E)<\delta\quad\Longrightarrow\quad \mu(E)<\varepsilon
\]
for every Borel set $E$.
:::

::: solution
<1>1. Continuity from above.
::: proof
Set
\[
F:=\bigcap_{k=1}^\infty F_k,
\qquad
E_k:=F_k\setminus F_{k+1}.
\]
Then the $E_k$ are pairwise disjoint and
\[
F_1=F\,\dot\cup\,\bigcup_{k=1}^\infty E_k.
\]
Since $\mu(F_1)<\infty$,
\[
\mu(F_1)=\mu(F)+\sum_{k=1}^\infty\mu(E_k).
\]
Also
\[
F_n=F\,\dot\cup\,\bigcup_{k=n}^\infty E_k,
\]
so
\[
\mu(F_n)=\mu(F)+\sum_{k=n}^\infty\mu(E_k).
\]
The tail of the convergent series tends to $0$, hence
\[
\mu(F_n)\to\mu(F).
\]
:::

<1>2. Absolute continuity in the epsilon--delta sense.
::: proof
Assume the conclusion fails. Then there exist $\varepsilon_0>0$ and Borel sets $E_n$ such that
\[
m(E_n)<2^{-n}
\qquad\text{and}\qquad
\mu(E_n)\ge\varepsilon_0.
\]
Define
\[
F_N:=\bigcup_{n\ge N}E_n,
\qquad
E:=\bigcap_{N=1}^\infty F_N=\limsup_{n\to\infty}E_n.
\]
Then
\[
m(F_N)\le\sum_{n\ge N}2^{-n}\to0,
\]
so
\[
m(E)=0.
\]
By hypothesis,
\[
\mu(E)=0.
\]
On the other hand, the sets $F_N$ decrease to $E$, and $\mu$ is finite, so part 1 gives
\[
\mu(E)=\lim_{N\to\infty}\mu(F_N).
\]
But $E_N\subseteq F_N$, hence
\[
\mu(F_N)\ge\mu(E_N)\ge\varepsilon_0
\]
for every $N$. Therefore
\[
\mu(E)\ge\varepsilon_0,
\]
a contradiction. Thus the desired $\delta$ exists.
:::
:::
